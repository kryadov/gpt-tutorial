import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

completion_not_strict = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": "Is there life on Mars?."}
    ],
    temperature=1,
    presence_penalty=2,
    frequency_penalty=2
)

completion_strict = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": "Is there life on Mars?."}
    ],
    temperature=0
)

print(f"Strict     answer: {completion_strict.choices[0].message.content}")
print(f"Not strict answer: {completion_not_strict.choices[0].message.content}")

# TODO: read about max_token and limiting answer - remember long answer of one-simple-question
