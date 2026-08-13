
conversation_history = []

def add_user_message(message:str):
#add users message to convo_history

	conversation_history.append({
		"role" :"user",
		"content" : message,
		})



def add_assistant_message(message:str):
#add assistant message to convo_history

	conversation_history.append({
		"role" : "assistant",
		"content" : message,
		})

def get_history():
#Return current convo_history
	return conversation_history

def clear_history():
#delete history
	conversation_history.clear()
