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


def get_recent_messages(memory:list) -> list:
#return most recent messages
	return memory["messages"][-MAX_RECENT_MESSAGES:]


def summarize_messages(
	model,
	existing_summary:str,
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
	recent_messages = messages[-MAX_RECENT_MESSAGES:]
	summary = summarize_messages(
		model,
		memory.get("summary",""),
		old_messages,
		)
	memory["summary"]= summary
	memory["messages"]= recent_messages

	return memory



def add_messages (
	memory:dict,
	role:str,
	content:str,
) -> str:

	"""
	Add a message to conversation memory.
	"""
	memory["messages"].append(
		{
		"role":role,
		"content":content,
		}
		)

def build_memory_context(memory):
	"""
	Build a text representation of memory for large language model.
	"""
	summary = memory.get(
		"summary",
		"",
		)

	messages = memory.get(
		"messages",
		[],
		)

	context_parts = []

	if summary:
		context_parts.append(
			f"Conversation summary:\n{summary}"
			)
	if messages:
		recent_text = "\n".join(
			[
			f"{message['role']}: "
			f"{message['content']}: "
			for message in messages
			]
			)

		context_parts.append(
			f"Recent conversation:\n{recent_text}"
			)
	return "\n\n".join(context_parts)

