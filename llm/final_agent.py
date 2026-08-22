
import os
from tools.langchain_tools import TOOLS
from langchain.agents import create_agent
from langchain_google_genai import ChatGoogleGenerativeAI
from config import (
	GEMINI_MODEL,
	get_gemini_api_key,)
from memory.memory_manager import (
	load_memory,
	save_memory,
	add_messages,
	build_memory_context,
	)
from memory.long_term_memory import (
	add_memory,
	get_memories,
	build_long_term_context,
	)


SYSTEM_PROMPT = """
	You are an AI assistant for a BSc Data Science project.

	You have access to the following tools:

	1. Database tool:
	   Use it for student records, student counts,
	   names, courses, CGPA, and enrollment information.

	2. PDF search tool:
	   Use it when the user asks about information
	   contained in the project PDF documents.

	3. Web search tool:
	   Use it for current, recent, or up-to-date information.

	You may also receive conversation memory and
	long-term memory.

	Use memory to understand the user's context.

	However, when a tool can provide authoritative
	or current information, use the tool instead of
	relying on memory.

	Do not invent information.

	After receiving a tool result, use that result
	to formulate the final answer.
	"""


def create_final_agent():
	"""
	Create and configure the Langchain AI agent.
	"""
	api_key = get_gemini_api_key()

	if not api_key:
		raise RuntimeError("GEMINI_API_KEY evnironment variable is not set")

	model = ChatGoogleGenerativeAI(
		model = GEMINI_MODEL,
		google_api_key =get_gemini_api_key()
		)

	agent = create_agent(
		model =model,
		tools = TOOLS,
		system_prompt = SYSTEM_PROMPT,
		)

	return agent



def get_final_answer(agent, prompt:str) -> str:
	"""
	Send a prompt to the AI agent and return the final text response.
	"""
	result = agent.invoke(
		{
		"messages":[
			{
			"role":"user",
			"content":prompt,
			}
			]
		}
		)

	final_message = result["messages"][-1]
	return final_message.content




def handle_remember_command(query:str) -> None:

	memory_text = query[
		len("remember:")
		].strip()

	if not memory_text:
		print("Please provide something to remember")
		return

	add_memory(
		"user",
		memory_text,
		)
	print("Memory saved.")


def show_long_term_memory() -> None:
	"""
	display all stored long-term memories
	"""


	memories = get_memories()

	if not memories:
		print("\nNo long-term memory found")
	else:
		print("\nLong-term Memory:")

		for memory_item in memories:
			category = memory_item[1]
			content = memory_item[2]
			print(f" -[{category}] {content}")


def main():
	"""
	final AI Assistant.
	"""

	print("="*70)
	print("AI ASSISTANT")
	print("="*70)

	print("\n\nCommands: ")
	print("   remember: <text>  - save long-term memory")
	print("   memories          - show long term memories")
	print("   exit              - quit")


	memory = load_memory()
	agent = create_final_agent()

	while True:

		query = input("\nYou: ").strip()

		if not query:
			continue

		if query.lower() == "exit":
			print("\nGoodbye! See ya again:) ")
			break


#REMEMBER
		if query.lower().startswith("remember:"):
			handle_remember_command(query)
			continue

#LONG-TERM MEMORY
		if query.lower() == "memories":
			show_long_term_memory()
			continue

#MEMORY CONTEXT
		conversation_context = build_memory_context(memory)

		long_term_context = build_long_term_context()



		prompt = f"""
			{SYSTEM_PROMPT}

			know long-term information:

			{long_term_context}

			Conversation context:

			{conversation_context}

			Current user question:

			{query}
			"""

		try:
			answer = get_final_answer(
				agent,
				prompt,
				)
		except Exception as error:
			print(f"\nAgent error:{error}")
			continue

		print("\nAssistant:")
		print(answer)

		add_messages(
			memory,
			"user",
			query,)

		add_messages(
			memory,
			"assistant",
			answer,)

		save_memory(memory)


if __name__ == "__main__":
	main()







