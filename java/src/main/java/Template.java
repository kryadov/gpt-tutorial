import com.theokanning.openai.OpenAiService;
import com.theokanning.openai.completion.CompletionRequest;

public class Template {
    public static void main(String[] args) {
        OpenAiService service = new OpenAiService("...");
        CompletionRequest completionRequest = CompletionRequest.builder()
                .prompt("Create new word and meaning")
                .model("ada")
//                .temperature(...)
//                .presencePenalty(...)
//                .frequencyPenalty(...)
                .echo(true)
                .build();
        service.createCompletion(completionRequest).getChoices().forEach(System.out::println);
    }
}
