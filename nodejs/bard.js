import Bard from "bard-ai";

(async () => {
    await Bard.init(process.env.BARD_API_KEY)
    const response = await Bard.askAI("Hello world");

    // Print the answer
    console.log(response);
})()
