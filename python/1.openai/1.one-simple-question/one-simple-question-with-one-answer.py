import os

import openai
from openai import OpenAI

# openai.base_url = "http://localhost..."
client = OpenAI(
    # defaults to os.environ.get("OPENAI_API_KEY")
    api_key=os.getenv("OPENAI_API_KEY")
)

# Full list of models - https://platform.openai.com/docs/models/overview

# OpenAI ChatCompletion
model = "gpt-3.5-turbo"

# There is currently no conclusive evidence to support the existence of life on Mars. However, scientists have discovered evidence of past liquid...

# model = "gpt-4-1106-preview"

# First run:
# As of my knowledge cutoff in 2023, there is no confirmed evidence of life on Mars. While the planet has conditions t...

# Second run with the same model (different with default api call):
# As of my last update in 2023, scientists have not found definitive evidence of current or past life on Mars. The search for life on Mars has

chat_completion = client.chat.completions.create(
    model=model,
    messages=[
        {"role": "user", "content": "Is there life on Mars?"}
    ]
)

print(f"{model} answer:   {chat_completion.choices[0].message.content}")

# OpenAI Completion
completion = client.completions.create(
    model="text-davinci-003",
    prompt="Is there life on Mars?"
)
answer = completion.choices[0].text.strip("\n")
print(f"Davinci answer: {answer}")
