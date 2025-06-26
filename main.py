from dotenv import load_dotenv
from pydantic import BaseModel
from typing import Optional
import os
from langchain_together import ChatTogether
from langchain_core.prompts import ChatPromptTemplate 
from langchain_core.output_parsers import PydanticOutputParser
from langchain.agents import create_tool_calling_agent , AgentExecutor
from tools import search_tool, wiki_tool, save_tool


class ResearchResponse(BaseModel):
    topic : str
    summary : str
    tools : list[str]
    subtasks: list[str]
    sources : Optional[list[str]]= []



load_dotenv()

llm = ChatTogether(
    model="mistralai/Mixtral-8x7B-Instruct-v0.1",
    temperature=0.7,
    openai_api_key=os.getenv("OPENAI_API_KEY"),)

parser= PydanticOutputParser(pydantic_object=ResearchResponse)

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
            "You are a task planner AI agent that breaks complex user goals into structured, actionable steps. Follow these rules strictly:
            1. Understand the user's intent.
            2. Research if needed using tools.
            3. Return the final plan in this **strict structured format**:
            - topic: Short title of the tas
            - summary: A concise overview (3-5 sentences)
            - tools: List of tools used (e.g., Wikipedia, DuckDuckGo)
            - subtasks: 5-7 clear, numbered subtasks
            - sources: Any relevant URLs
            Respond in this format only. Do not include any other explanation.
            "Do not include null values in 'sources'. If no sources are found, return an empty list: sources: []
            "\n{format_instructions}""

            """,
        ),
        ("placeholder", "{chat_history}"),
        ("human", "{query}"),
        ("placeholder", "{agent_scratchpad}"),
    ]
).partial(format_instructions=parser.get_format_instructions())

tools= [search_tool, wiki_tool, save_tool] 
agent = create_tool_calling_agent(
    llm=llm,
    prompt=prompt,
    tools=tools,
)


AE = AgentExecutor(agent=agent, tools=tools, verbose=True)
query= input("  Enter task that you want to accomplish: ") 
if not query:
    query = "Do you want me to syggest a task for you? If yes, please provide a topic or area of interest."
response = AE.invoke({"query" : query})

from tools import save_to_txt  # Import the save function

try:
    structured_response = parser.parse(response.get("output"))
    print("Topic:", structured_response.topic)

    save_status = save_to_txt(structured_response.model_dump_json())
    print(save_status)

except Exception as e:
    print("Error parsing response:", e)
    print("Raw response:", response.get("output"))

