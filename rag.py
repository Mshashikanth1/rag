from llama_index import (
    ServiceContext,
    SimpleDirectoryReader,
    StorageContext,
    VectorStoreIndex,
    set_global_service_context,
)
from llama_index.llms import Ollama

print(" ============================ simple RAG (retrieve augmented generation) ============================")
print("reading the pdfs present in current directory")
# llm = Ollama(model="mistral")
# llm = Ollama(model="llama3")
# llm = Ollama(model="phi3")
llm=Ollama(model="mixtral:8x22b")

# Reads pdfs at "./" path
documents = (
    SimpleDirectoryReader(
        input_dir='./',
        required_exts=[".pdf",".csv"])
    .load_data()
)

# ServiceContext is a bundle of commonly used
# resources used during the indexing and
# querying stage
service_context = (
    ServiceContext
    .from_defaults(
        llm=llm,
        embed_model="local:BAAI/bge-small-en-v1.5",
        chunk_size=300
    )
)
set_global_service_context(service_context)

# Node represents a “chunk” of a source Document
nodes = (
    service_context
    .node_parser
    .get_nodes_from_documents(documents)
)

# offers core abstractions around storage of Nodes,
# indices, and vectors
storage_context = StorageContext.from_defaults()
storage_context.docstore.add_documents(nodes)

# Create the vectorstore index
index = (
    VectorStoreIndex
    .from_documents(
        documents,
        storage_context=storage_context,
        llm=llm
    )
)
query_engine = index.as_query_engine()


print("i have read the pdfs in this directory have any queries")

action = "start"
while not action.__contains__("stop"):
    query = input()

    print("\033[92m")
    # Query the index
    response = query_engine.query(query)
    print(response)
    print("\033[0m")

print("thank you!")


