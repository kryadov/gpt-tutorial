import os
from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

chat_completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": "Give me 5 solar system planet names."}
    ],
    n=5
)
print(f"Answers: {len(chat_completion.choices)}")

for i, c in enumerate(chat_completion.choices):
    print(f"Answer {i + 1}: {c.message.content}")

# Capitan Obviously question: how to get 5 names in 1 answer?
