from llama_index.llms import Ollama

llm = Ollama(model="mistral")

print(" ============================ simple conversation  ============================")


action = "start"
while not action.__contains__("stop"):
    action = input()
    print("\033[92m")
    resp = llm.complete(action)
    print(resp)
    print("\033[0m")

print("thank you!")
