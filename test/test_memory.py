from memory.memory_manager import (
	load_memory,
	save_memory)

history = load_memory()
print("Existing memory:")
print(history)

history.append(
	{
	"role":"user",
	"content":"Hellow from my AI assistant.",
	}
	)
save_memory(history)
print("\nMemory saved successfully!")

