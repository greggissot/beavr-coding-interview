import streamlit as st
import pdfplumber
import requests
import io
import ast
import os

# Définir l'URL du backend FastAPI
BACKEND_URL = "http://localhost:8000"

st.title("Beavr - Gestion des documents")

# Upload de fichier
uploaded_file = st.file_uploader("Uploader un document (PDF ou texte)", type=["txt", "pdf"])

if uploaded_file:
    file_bytes = uploaded_file.read()
    if uploaded_file.type == "application/pdf":
    
        with pdfplumber.open(io.BytesIO(file_bytes)) as pdf:
            document_text = "\n".join([page.extract_text() for page in pdf.pages if page.extract_text()])
    else:  # 📌 Si c'est un fichier texte
        document_text = file_bytes.decode("utf-8", errors="ignore")
    response = requests.post(f"{BACKEND_URL}/add_document", json={"title":uploaded_file.name, "content":document_text})

    if response.status_code == 200:
        st.success("Document uploadé avec succès !")
    else:
        st.error("Erreur lors de l'upload du document.")

# Récupération et affichage des documents
st.subheader("📜 Liste des documents")
response = requests.get(f"{BACKEND_URL}/documents")

if response.status_code == 200:
    documents = response.json()
    for doc in documents:
        st.write(f"- {doc['title']}")
        st.write(f"  {doc['summary']}")
        key_elements_list = ast.literal_eval(doc['key_elements'])
else:
    st.error("Impossible de récupérer la liste des documents.")
