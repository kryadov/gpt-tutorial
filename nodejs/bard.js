import Bard from "bard-ai";

(async () => {
    await Bard.init(process.env.BARD_API_KEY)
    const response = await Bard.askAI("Is there life on Mars?");

    // Print the answer
    console.log(response);
})()
