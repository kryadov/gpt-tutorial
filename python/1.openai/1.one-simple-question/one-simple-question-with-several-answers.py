import os
from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

chat_completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": "Give me a solar system planet name."}
    ],
    n=5
)
print(f"Answers: {len(completion.choices)}")

for i, c in enumerate(completion.choices):
    print(f"Answer {i + 1}: {c.message.content}")

# Capitan Obviously question: how to get 5 names in 1 answer?
