from llm.memory import(
	add_user_message,
	add_assistant_message,
	get_history,
	clear_history,)

add_user_message("Explain Transformers.")
add_assistant_message("Transformers use attention mechanisms.")
add_user_message("What is self-attention?")

history = get_history()
for message in history:
	print(message)

