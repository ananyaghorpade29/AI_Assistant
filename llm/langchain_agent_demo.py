from langchain.agents import create_agent
from langchain_google_genai import ChatGoogleGenerativeAI

from config import GEMINI_MODEL
from tools.langchain_registry import LANGCHAIN_TOOLS

from memory.memory_manager import (
	load_memory,
	save_memory,
	)
from memory.long_term_memory import (
	add_memory,
	get_memories,
	)


def main():

	model = ChatGoogleGenerativeAI(
		model = GEMINI_MODEL,)

	agent = create_agent(
		model = model,
		tools = LANGCHAIN_TOOLS,
		)

	query = (
		"Search my PDF documents for information about "
		"transformer architecture. Then create a PDF report "
		"using the information you found. After creating the "
		"report, tell me where it was saved."
		)

	conversation_history = load_memory()
	print("=" *70)
	print("AI ASSISTANT")
	print("="*70)
	print("Type 'exit' to quit.")

	while True:

		query = input("\nYou: ").strip()
		if query.lower() == "exit":
			print("Goodbye!! See you again:)")
			break

#save long-term memory
		if query.lower().startswith("remember:"):
			memory_text = query[len("remember:")].strip()

			add_memory = (
				"user",
				memory_text,
				)

			print("Memory Saved.")
			continue

#display long-term memories
		if query.lower() == "memories":
			memories = get_memories()

			if not memories:
				print("No memories found.")
			else:
				print("\nLong-term memories: ")

				for memory in memories:
					print(
						f"-[{memory[0]}]"
						f"{memory[1]}"
						)
			continue

		conversation_history.append(
			{
			"role":"user",
			"content":query,
			}
			)

		result = agent.invoke(
			{
			"messages":conversation_history
			}
			)

		conversation_history = result["messages"]
		save_memory(conversation_history)
		final_message = result["messages"][-1]

		print("\nAssistant:")
		print(final_message.content)

if __name__ == "__main__":
	main()
