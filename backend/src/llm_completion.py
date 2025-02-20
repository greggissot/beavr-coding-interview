from openai import OpenAI
import ast

def completion(document):
    
    client = OpenAI()

    completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {
        "role": "user",
        "content": "Summarize the following document for me. Make it a 3 sentences long summary. You will be provided a document."
        },
        {"role": "user", "content": document},
    ]
)
    return completion.choices[0].message.content

client = OpenAI()

def extract_key_elements(document):
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are an AI specialized in extracting structured key elements from documents."},
            {
                "role": "user",
                "content": (
                    "Extract the key elements from the following document. "
                    "Each key element should have a 'title' and a 'content'. "
                    "Return only (nothing after and before) an array with this structure: [{'title': 'Title1', 'content': 'Content1'}, {'title': 'Title2', 'content': 'Content2'}]. "
                    "Here is the document:\n\n"
                    f"{document}"
                )
            }
        ]
    )

    # Convertir la réponse en objet Python (si ce n'est pas déjà au bon format)
    import json
    response_text = completion.choices[0].message.content
    try:
        print(response_text)
        key_elements = json.loads({response_text})
    except json.JSONDecodeError:
        key_elements = [{"title": "Error", "content": "Failed to parse JSON response"}]

    return key_elements
