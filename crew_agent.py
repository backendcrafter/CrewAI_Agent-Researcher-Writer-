from crewai import Agent
from crewai import Task
from crewai import Crew
import os
from dotenv import load_dotenv
load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("GROQ_API")
os.environ["OPENAI_API_BASE"] = "https://api.groq.com/openai/v1"
os.environ["OPENAI_MODEL_NAME"] = "llama-3.3-70b-versatile"

researcher = Agent(role="researcher", goal="Find accurate information about a given topic", backstory="You are an expert researcher with years of experience.")
research_task = Task(description="Research the topic: {topic}. Find key facts and summarize.", expected_output="A bullet point summary of key facts", agent=researcher)
writer= Agent(role="writer", goal="Write a clear and concise article based on the research findings", backstory="You are a skilled writer who can turn complex information into engaging articles.")
writer_task = Task(description="Write an article about {topic} based on the research findings.", expected_output="A well-structured article with an introduction, body, and conclusion", agent=writer)

crew = Crew(agents=[researcher, writer], tasks=[research_task, writer_task])

topic = input("Enter a topic to research and write about: ")
result=crew.kickoff(inputs={"topic": topic})
print("Researcher Output:")
print(result)