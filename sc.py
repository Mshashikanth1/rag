from llama_index.llms import Ollama

import wikipedia

# llm = Ollama(model="mistral")
llm = Ollama(model="llama3")


print(" ============================ simple conversation  ============================")


action = "start"
while not action.__contains__("stop"):

    action = """give me the article sore by considering the following parameters: 
Readability,
Coherence,
Informativeness,
Language complexity,
Formatting,
Plagiarism. 

       for the article : 
    """+ wikipedia.get_random_article_content()

    print("\033[92m")
    resp = llm.complete(action)
    print(resp)
    print("\033[0m")

print("thank you!")
