from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

assistant = client.beta.assistants.create(
    name="Doc Assistant",
    instructions="You are a helpful assistant. Answer questions based on the provided documents.",
    model="gpt-4-1106-preview",  # or gpt-4-turbo if you want streaming
    tools=[{"type": "file_search"}]
)

print("Assistant ID:", assistant.id)