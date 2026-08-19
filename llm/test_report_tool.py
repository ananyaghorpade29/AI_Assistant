from tools.report_tool import generate_report

content = """
Transformer Architecture

Transformers are neural network architectures
that use attention mechanisms to process
sequential information.
"""

result = generate_report(content)
print(result)

