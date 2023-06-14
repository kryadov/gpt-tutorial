import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are famous science fiction writer who really believes in miracles"},
        {"role": "user", "content": "Is there life on Mars?"}
    ]
)

print(f"Role: {completion.choices[0].message.role}")
print(f"Answer: {completion.choices[0].message.content}")
