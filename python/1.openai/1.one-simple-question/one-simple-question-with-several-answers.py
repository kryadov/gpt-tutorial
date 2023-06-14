import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": "Give me a random name please."}
    ],
    n=5
)
print(f"Answers: {len(completion.choices)}")

for i, c in enumerate(completion.choices):
    print(f"Answer {i + 1}: {c.message.content}")

# Capitan Obviously question: how to get 5 names in 1 answer?
