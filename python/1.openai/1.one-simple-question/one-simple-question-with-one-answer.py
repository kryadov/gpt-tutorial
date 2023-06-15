import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

# Full list of models - https://platform.openai.com/docs/models/overview

# OpenAI ChatCompletion
chat_completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    # model="gpt-4" # https://openai.com/waitlist/gpt-4-api - Thank you for joining the waitlist to build with GPT-4!
    messages=[
        {"role": "user", "content": "Is there life on Mars?"}
    ]
)

print(f"GPT-3 answer:   {chat_completion.choices[0].message.content}")

# OpenAI Completion
completion = openai.Completion.create(
    model="text-davinci-003",
    prompt="Is there life on Mars?"
)
answer = completion.choices[0].text.strip("\n")
print(f"Davinci answer: {answer}")
