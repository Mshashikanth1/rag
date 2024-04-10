#!/bin/bash

# Build the Docker image
docker build -t ollama-local .

# Run the Docker container
docker run -d \
  -v ollama:/root/.ollama \
  -p 11434:11434 \
  --name ollama \
  ollama-local

# Enter the container's shell
docker exec -it ollama bash

# Pull the desired model within the container
ollama pull mistral  # Replace "mistral" with the desired model name

# Exit the container's shell
exit
