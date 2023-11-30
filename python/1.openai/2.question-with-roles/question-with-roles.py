import os
from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

chat_completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are famous science fiction writer who really believes in miracles"},
        {"role": "user", "content": "Is there life on Mars?"}
    ]
)

print(f"Role: {chat_completion.choices[0].message.role}")
print(f"Answer: {chat_completion.choices[0].message.content}")
