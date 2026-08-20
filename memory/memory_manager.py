import json
from pathlib import Path
from langchain_core.messages import HumanMessage,AIMessage, ToolMessage


MEMORY_FILE = Path("memory/conversation.json")
MAX_RECENT_MESSAGES = 20


def load_memory() -> list:
#load conversation

	if not MEMORY_FILE.exists():
		return {
			"summary":"",
			"messages": [],
			}

	with open(
		MEMORY_FILE,
		"r",
		encoding="utf-8",
	) as file:

		return json.load(file)


def save_memory(history:list) -> None:
#save converstion history json

	serializable_history =[]

	for message in history:
		if isinstance(message, HumanMessage):
			serializable_history.append({
				"role":"user",
				"content":message.content,
				})

		elif isinstance(message, AIMessage):
			serializable_history.append({
				"role":"assistant",
				"content":message.content,
				})

		elif isinstance(message, ToolMessage):
			serializable_history.append({
				"role":"tool",
				"content":message.content,
				})

	with open(
		MEMORY_FILE,
		"w",
		encoding="utf-8",
	) as file:

		json.dump(
			history,
			file,
			indent=4,
			ensure_ascii=False,
			 )


def get_recent_messages(history:list) -> list:
#return most recent messages
	return history[-MAX_RECENT_MESSAGES:]


def summarize_messages(
	model,
	exicting_summary:str,
	messages:list,
) -> str:
#gemini summarize old convo

	conversation_text ="\n".join(
		[
		f"{message['role']}:"
		f"{message['content']}:"
		for message in messages
		]
		)
	prompt = f"""
	Update the conversation summary.

	Existing summary:
	{existing_summary}

	New conversation messages:
	{conversation_text}

	Create a concise summary that preserves
	important information from both the existing
	summary and the new messages.

	Preserve:
	- user goals
	- important topics
	- decisions
	- relevant project information
	- important facts

	Remove unnecessary details.
	"""
	response = model.invoke(prompt)
	return response.content


def manage_memory(model, memory:dict,) -> dict:
	"""
	Summarize old messages when the history becomes too large.
	"""
	messages= memory["messages"]

	if len(messages) <= MAX_RECENT_MESSAGES:
		return memory

	old_messages = messages[:-MAX_RECENT_MESSAGES]
	recent_messages = messages[-MAX_RECENT_MESSAGES]

	summary = summarize_messages(model,old_messages)
	memory["summary"]= summary
	memory["messages"]= recent_messages

	return memory



