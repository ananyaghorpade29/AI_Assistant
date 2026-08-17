from  google import genai
from llm.llm_router import choose_tool
from llm.memory import (
	add_user_message,
	add_assistant_message,
	get_history,
	clear_history,)
from tools.tool_registry import TOOLS
from config import GEMINI_MODEL


class AIAssistant:
#main AI Assistant agent.

	def __init__(self,client):
	#initailize AI-Assistant
		self.client = client

	def execute_tool(
		self,
		tool_name,
		arguments,
		query:str,
		max_retries:int=2):

		if tool_name not in  TOOLS:
			print(f"Unknown tool: {tool_name}")
			return None

		tool = TOOLS[tool_name]
		for attempt in range(max_retries+1):

			try:
				print(
				f"Executing {tool_name}"
				f"(attempt {attempt+1})..."
				)

				if arguments:
					return tool["function"](**arguments)
				return tool["function"](query)

			except Exception as error:
				print(
				f"Tool execution failed: {error}"
				)

		print("Tool failed after all retries.")
		return None


	def generate_final_answer(
		self,
		query:str,
		tool_name:str,
		tool_result,
		):
	#generate Natural language answer
			history= get_history()
			conversation= []

			for message in history:
				conversation.append(
					f"{message['role']}"
					f"{message['content']}"
					)
			prompt = f"""
			you are the final response generator for an AI assistant.

			Conversaton History:
			{chr(10).join(conversation)}

			Current user question:
			{query}

			Tool used:
			{tool_name}

			Tool_result:
			{tool_result}

			Answer the user's query using the tool result.
			Do not mention internal tool names unless necessary.
			If the tool result does not contain enough information, clearly say so.

			give a helpful a concise answer.
			"""

			response = self.client.models.generate_content(
				model = GEMINI_MODEL,
				contents=prompt,
				)
			return response.text.strip()

	def run(self, query:str):
	#process one uers query
		tool_name, arguments = choose_tool(query)

		print("\nTool selected: ", tool_name)
		print("Arguments: ", arguments)

		if tool_name is None:
			return ("I could not determine which tool to use.")

		tool_result = self.execute_tool(
			tool_name,
			arguments,
			query,
			)

		if tool_result is None:
			return ("I couldnt return the result because the selected tool failed.")

		final_answer = self.generate_final_answer(
			query,
			tool_name,
			tool_result,
			)

		add_user_message(query)
		add_assistant_message(final_answer)

		return final_answer
