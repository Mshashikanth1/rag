# Import libraries (replace with your preferred LLM library)
import transformers

# Define LLM model and tokenizer (replace with desired model names)
# llm = Ollama(model="phi3")

model_name = "facebook/llama-base"
tokenizer = transformers.AutoTokenizer.from_pretrained(model_name)
model = transformers.AutoModelForSequenceClassification.from_pretrained(model_name)


# Function to analyze article and user preferences with LLM
def analyze_with_llm(article_text, user_preferences):
    # Preprocess article text
    article_input = tokenizer(article_text, return_tensors="pt")

    # Prompt for LLM (replace with your specific prompt)
    prompt = f"This article is about {article_text}. How relevant is this to user preferences: {user_preferences}?"

    # Combine prompt and article for LLM input
    combined_input = tokenizer(prompt + article_input["input_ids"], return_tensors="pt")

    # Get LLM output (logits)
    output = model(**combined_input)
    logits = output.logits.squeeze(0)

    # Interpret logits (higher value indicates more relevance)
    relevance_score = logits[1]  # Assuming logits[0] is not relevant score
    return relevance_score


# Example usage
article_text = "This is a fascinating article about the applications of machine learning."
user_preferences = "I enjoy articles about technology advancements."

relevance_score = analyze_with_llm(article_text, user_preferences)

print(f"Relevance score for article: {relevance_score}")
