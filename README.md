This script sends a biomedical abstract to Claude and returns a structured JSON with the main info on the abstract.

## Fields extracted
- condition
- study_type
- sample_size
- methodology 
- key findings
- clinical relevance

## Prerequisites
- Python 3.9+
- uv
- Anthropic API key

## Setup
1. Clone the repo
2. Set ANTHROPIC_API_KEY as an environment variable in your system (that was the easiest way for me at least)
3. bash - uv sync
4. bash - uv run main.py 


