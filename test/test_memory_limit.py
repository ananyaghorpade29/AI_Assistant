from memory.memory_manager import (get_recent_messages)

history = []
for number in range(1-31):
	history.append({
		"role":"user",
		"content": f"Message {number}"
		})
recent = get_recent_messages(history)
print("Total messages:", len(history))
print("Recent messages:", len(recent))
print("\nRecent Messages:")

for message in recent:
	print(message["content"])

