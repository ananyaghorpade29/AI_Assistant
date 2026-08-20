from langchain_core.messages import HumanMessage, AIMessage, ToolMessage

conversation =[]

conversation.append(
	HumanMessage(
		content=(
			"Explain Transformers."
			)
		)
	)

conversation.append(
	AIMessage(
		content =(
			"Transformers are nueral network"
			"architectures based heavily on attention"
			)
		)
	)

conversation.append(
	HumanMessage(
		content =(
			"What is attention?"
			)
		)
	)


for message in conversation:
	print(type(message).__name__, ":", message.content,)
