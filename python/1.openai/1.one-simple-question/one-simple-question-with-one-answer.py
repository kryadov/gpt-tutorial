import os
from openai import OpenAI

client = OpenAI(
    # defaults to os.environ.get("OPENAI_API_KEY")
    api_key=os.getenv("OPENAI_API_KEY")
)

# Full list of models - https://platform.openai.com/docs/models/overview

# OpenAI ChatCompletion
chat_completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    # model="gpt-4-1106-preview"
    messages=[
        {"role": "user", "content": "Is there life on Mars?"}
    ]
)

print(f"GPT-3 answer:   {chat_completion.choices[0].message.content}")

# OpenAI Completion
completion = client.completions.create(
    model="text-davinci-003",
    prompt="Is there life on Mars?"
)
answer = completion.choices[0].text.strip("\n")
print(f"Davinci answer: {answer}")
