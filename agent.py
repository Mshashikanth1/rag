from llama_index.llms import Ollama
from llama_index.agent import ReActAgent
from llama_index.tools import FunctionTool

print("========== agent will execute the tasks tools we have provided him ==========")


def add_numbers_three_fn(a: int, b: int) -> int:
    """Adds two numbers and a constant 3 and returns the result"""
    return a + b + 3


tools = [
    FunctionTool.from_defaults(fn=add_numbers_three_fn)
]

llm = Ollama(model="mistral")
agent = ReActAgent.from_tools(tools, llm=llm, verbose=True)

action = "start"
while not action.__contains__("stop"):
    action = input()
    print("\033[92m")

    response = agent.chat(action)
    print(str(response))

    print("\033[0m")

print("thank you!")


# example : "Add the numbers 3 and 2"