
https://github.com/Mshashikanth1/rag/blob/main/Screenshot%202024-04-10%20at%205.20.26%20PM.png

# TO automatically capture all the depencies from you py env use the below cmd
```
pip freeze > requirements.txt
```

# to setup ollama ( LLMS runing infra locally) 
```
docker pull ollama/ollama
docker run -d -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama
```

# to pull the desired open source llm  in ollama docker cli user this
```
ollama pull mistral
```

# RAG Retrival augmented generation design pattern

```
    we start with an existing llm
    we feed our custum data
    we ask queries on the custom data
    in this we are using llam-indexes
```


# rag
# rag
