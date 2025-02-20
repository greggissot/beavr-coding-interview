# Beavr Coding interview

## The assignment : Full-Stack Document Processing App

### **Objective**

Build a minimal full-stack web application that allows users to:

1. **Upload documents** (e.g., text or PDF files).
2. **Summarize documents and extract key elements**.
3. **Bonus : Ask questions based on the document content** and receive AI-generated responses.

### **Expectations & Time Limit**

- The assignment should take no more than **2 hours** to complete.
- Focus on **functionality over polish**—the goal is to demonstrate problem-solving and full-stack development.
- Keep the solution **simple and maintainable**.

### **Requirements**

### **Backend**

- Implement a **REST API** (Node.js/Express, Flask, FastAPI, or similar) that supports:
  - File upload and storage.
  - Document summarization and key element extraction
  - **Bonus :** Answering questions based on the document content.
- Use **SQLite, PostgreSQL, or MongoDB** (or an in-memory solution) to store data

### **Frontend**

- Create a **simple web UI** that allows users to:
  - Upload documents.
  - View the extracted summaries and key points.
- **Bonus:** Ask questions and see AI-generated answers.
- Minimal but **functional UI** is sufficient

### **Submission Guidelines**

1. Provide a **GitHub repository link** with clear instructions to run your app.
2. Include a **README** explaining:
   - Tech stack choices.
   - How to install and run the application.
   - Any trade-offs made due to time constraints.
3. Ensure the code is **well-structured and documented**.

### **Evaluation Criteria**

- **Completeness**: Does the app cover all the core functionalities?
- **Code Quality**: Is the code clean, readable, and well-organized?
- **Technical Choices**: Are the selected tools/libraries appropriate for the task?
- **Efficiency**: Does the app process documents effectively?
- **User Experience**: Is the UI intuitive and functional?

Good luck! 🚀

## Run the app

This repository contains a full stack app template you can use for this assignment.

### Backend

Dependencies :

```
python3 -m venv venv
source venv/bin/activate
python3 -m pip install "fastapi[all]" "uvicorn[standard]" sqlalchemy
```

Run the app :

```
python3 -m uvicorn backend.main:app --reload
```

### Frontend

If necessary, install node : https://docs.npmjs.com/downloading-and-installing-node-js-and-npm

```
cd frontend
npm install
npm run dev
```

To run the frontend (streamlit), you should install the package and run

```
python3 -m streamlit run app.py

```


### Choice of Streamlit

The choice of streamlit is based on the fact that it gives access to component that does exactly what we want (for the uploading files aspect) and is easy to manipulate with the fastAPI backend. Moreover, I already used it to summarize document in my previous projects at Theodo.

### Choice of OpenAI 

For the key element extraction and summary, a LLM calling looks an easy way to do this. Due to a lack of time, the key element extraction is not fully functional (as I was unware of the possibility to constraint the output of a LLM with the OpenAI package itself).

### Dependencies 

Other packages are required : streamlit, requests, pdfplumber, openai.
