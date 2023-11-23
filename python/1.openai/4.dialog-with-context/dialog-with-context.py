import os
from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

first_question = "Is there life on Mars?"
second_question = "When last research was performed?"

chat_completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    # model="gpt-4" # https://openai.com/waitlist/gpt-4-api - Thank you for joining the waitlist to build with GPT-4!
    messages=[
        {"role": "system", "content": "You are the scientist."},
        {"role": "user", "content": first_question},
        {"role": "assistant",
         "content": "I don't have a definitive answer to this question yet. However, over the years, prominent space agencies around the world have conducted several missions aimed at finding signs of life on Mars. Although there is no conclusive evidence to support the idea of life on Mars, several findings suggest the possibility of microbial organisms on the planet's subsurface and in ancient times when the planet had a thicker atmosphere and flowing water. Future missions to Mars will likely continue to investigate this exciting question and expand our understanding of the planet."},
        {"role": "user", "content": second_question}
        # also for understanding last available knowledge date
    ]
)

print(f"Question: {second_question}")
print(f"Answer: {chat_completion.choices[0].message.content}")
