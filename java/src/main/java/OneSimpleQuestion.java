import com.theokanning.openai.completion.chat.ChatCompletionRequest;
import com.theokanning.openai.completion.chat.ChatMessage;
import com.theokanning.openai.service.OpenAiService;

import java.util.Arrays;

public class OneSimpleQuestion {
    public static void main(String[] args) {
        OpenAiService service = new OpenAiService(System.getenv("OPENAI_API_KEY"));
        //
        String question = "Is there life on Mars?";
        ChatCompletionRequest request = ChatCompletionRequest.builder()
                .model("gpt-3.5-turbo")
                .messages(Arrays.asList(new ChatMessage("user", question)))
                .temperature(0.1)
                .presencePenalty(1.0)
                .frequencyPenalty(1.0)
                .build();
        //
        service.createChatCompletion(request).getChoices().
                stream().map(c -> c.getMessage().getContent()).
                forEach(System.out::println);
    }
}
