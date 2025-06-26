# Task-Planner-AI-Agent
AI Task Planner & Research Agent
This project is an intelligent, interactive AI agent designed to help users break down complex tasks into structured, research-backed plans. It uses LangChain, Pydantic, and modern LLMs like Mixtral (via Together API) or Claude 3.5 (via Anthropic) to combine reasoning, research, and local storage in one seamless pipeline.

What It Does
Accepts natural language queries such as "I want to learn guitar"
Breaks down the query into a clear, structured set of subtasks
Uses web tools like DuckDuckGo Search and Wikipedia for accurate information

Outputs a structured response including:
Topic
Summary
Tools used
Numbered subtasks
Sources (URLs, if applicable)
Saves the output to a local .txt file with a timestamp

Example
User Input:


How do I get started with playing the guitar?

Agent Output:

{
  "topic": "Guitar Playing for Beginners",
  
  "summary": "This plan introduces you to the basics of playing the guitar...",
  
  "tools": ["Wikipedia", "Justin Guitar"],
  
  "subtasks": [
    "1. Learn how to tune your guitar...",
    "2. Familiarize yourself with the basic parts of the guitar...",
    ...
  ],
  
  "sources": ["https://en.wikipedia.org/wiki/Guitar"]
}
This structured response is also saved to research_output.txt.

Tech Stack:

LangChain for agent orchestration and tool execution.
Pydantic for data validation and structured outputs.
Together API / Anthropic Claude as LLM backends.
DuckDuckGo and Wikipedia for live research tools.
Python for file handling and custom utility tools.

Tools Included:

search_tool: Queries the web via DuckDuckGo

wiki_tool: Extracts information from Wikipedia

save_tool: Stores structured research plans in a local file

Use Cases:
Educational planning (e.g., "Learn about quantum computing")

Research summaries (e.g., "Summarize the Industrial Revolution")

Personal goal breakdowns (e.g., "Train for a half marathon")

Content scaffolding (e.g., "Create a blog plan about AI tools")

