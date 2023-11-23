import OpenAI from 'openai'

const openai = new OpenAI({
    apiKey: process.env.OPENAI_API_KEY,
});

(async () => {
    const chatCompletion =  await openai.chat.completions.create({
        model: "gpt-3.5-turbo",
        messages: [{ role: "user", content: "Is there life on Mars?" }],
    })

    // Print the answer
    console.log(chatCompletion.choices[0].message.content);
})()
