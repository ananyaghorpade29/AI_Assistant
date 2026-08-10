from report import generate_report


title = "Introduction to Artificial Intelligence"

content = """
Artificial Intelligence is a field of computer science
that focuses on creating systems capable of performing
tasks that normally require human intelligence.

Examples include:

- Machine Learning
- Natural Language Processing
- Computer Vision
- Robotics
"""


output_path = "reports/ai_report.pdf"


generate_report(
    title,
    content,
    output_path
)

print("Report generated successfully!")
print(f"Saved to: {output_path}")
