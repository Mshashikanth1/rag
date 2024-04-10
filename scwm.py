from llama_index.llms import Ollama
from llama_index import ServiceContext
from llama_index.chat_engine import SimpleChatEngine

print(" ============================ simple conversation with memory ============================")

llm = Ollama(model="mistral")

service_context = ServiceContext.from_defaults(
    llm=llm,
    embed_model="local:BAAI/bge-small-en-v1.5",
)

chat_engine = SimpleChatEngine.from_defaults(service_context=service_context)

action = "start"
while not action.__contains__("stop"):
    action = input()
    print("\033[92m")
    print(chat_engine.chat(action))
    print("\033[0m")

print("thank you!")
