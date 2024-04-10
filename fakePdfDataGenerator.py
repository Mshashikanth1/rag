from faker import Faker
import random
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


def generate_people_table(num_people):
    # Create an instance of Faker
    fake = Faker()

    # Generate a table of people with random names and ages
    people_table = []

    for _ in range(num_people):
        name = fake.name()
        age = random.randint(18, 80)  # Generate a random age between 18 and 80
        people_table.append({"name": name, "age": age})

    return people_table


def create_pdf_from_people_table(people_table, output_file):
    # Create a PDF document
    c = canvas.Canvas(output_file, pagesize=letter)
    width, height = letter

    # Set up table header
    table_header = ["Name", "Age"]
    col_widths = [300, 100]
    y_start = height - 100

    # Draw table header
    for i, header in enumerate(table_header):
        c.drawString(100 + sum(col_widths[:i]), y_start, header)

    # Draw table rows
    y_offset = 20
    for person in people_table:
        c.drawString(100, y_start - y_offset, person["name"])
        c.drawString(400, y_start - y_offset, str(person["age"]))
        y_offset += 20

    # Save the PDF document
    c.save()


if __name__ == "__main__":
    num_people = 100
    people_table = generate_people_table(num_people)
    output_file = "people_table.pdf"
    create_pdf_from_people_table(people_table, output_file)
    print(f"PDF file '{output_file}' has been created with the people table.")

#
#
# # Import libraries (replace with actual import statements if needed)
# from llama_index import LLAMAIndex  # Assuming llama_index library is available
# from rag_retrieve import Retriever  # Assuming rag_retrieve library is available
#
# # Ollama client setup (replace with your Ollama API details)
# ollama_host = "localhost"
# ollama_port = 11434
# ollama_client = LLAMAIndex(host=ollama_host, port=ollama_port)
#
# # Define retrieval function using Neo4j or alternative knowledge base (replace with your implementation)
# def my_knowledge_base_retrieval(query):
#     # Implement logic to retrieve relevant entities and information from your knowledge base using the query
#     # This could involve querying Neo4j or another system
#     # ...
#     return retrieved_entities, retrieved_info  # Replace with actual data structures
#
# # Mistral LLM interaction (replace with your Ollama API calls)
# def query_mistral(prompt):
#     response = ollama_client.call(model_name="mistral", prompt=prompt)
#     return response["generated_text"]
#
# # Main loop for processing user queries
# while True:
#     user_query = input("Enter your question: ")
#
#     # Retrieval step
#     retrieved_entities, retrieved_info = my_knowledge_base_retrieval(user_query)
#
#     # RAG step (combine retrieved information with query for LLM)
#     rag_prompt = f"Here's some information I found: {retrieved_info}. Based on this, what can you tell me about {user_query}?"
#
#     # LLM generation step
#     generated_response = query_mistral(rag_prompt)
#
#     # Print the final response
#     print(f"Mistral (LLM) Response: {generated_response}")
#
# def my_knowledge_base_retrieval(query):
#     with driver.session() as session:
#         # Construct Cypher query based on specific retrieval goals and data model
#         cypher_query = """
#       MATCH (entity:MyEntity)
#       WHERE toLower(entity.name) CONTAINS toLower($query)
#       OR entity.description CONTAINS $query
#       RETURN entity, entity.name, entity.description, entity.other_relevant_properties
#     """
#         # Execute the query
#         results = session.run(cypher_query, query=query)
#
#         retrieved_entities = []
#         retrieved_info = []
#
#         for result in results:
#             entity = result["entity"]
#             entity_info = {
#                 "name": result["entity.name"],
#                 "description": result["entity.description"],
#                 # ...other properties
#             }
#             retrieved_entities.append(entity)
#             retrieved_info.append(entity_info)
#
#     return retrieved_entities, retrieved_info

