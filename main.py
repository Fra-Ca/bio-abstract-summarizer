import sys
import json
from anthropic import Anthropic
import os

client = Anthropic()

system_prompt = """You are a biomedical research assistant. Given a paper abstract, extract and return ONLY a valid JSON object with the following fields:
- condition: the disease or condition being studied
- study_type: the type of study
- sample_size: number of patients or subjects as an integer
- methodology: brief description of how the study was conducted
- key_findings: a list of the main findings
- clinical_relevance: why these findings matter clinically

Return only raw JSON, no other text, no markdown, no backticks. Start your response with { and end with }.
"""
file_path = sys.argv[1]
with open(file_path, "r") as f:
    abstract = f.read()

message = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=1024,
    system=system_prompt,
    messages=[{"role": "user", "content": abstract}]
)
raw = message.content[0].text
result = json.loads(raw)
print(json.dumps(result, indent=2))
