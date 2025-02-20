from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from .src.model import Document
from .src.schema import DocumentBase
from .src.database import SessionLocal, engine, Base
from .src.llm_completion import completion, extract_key_elements
from sqlalchemy.orm import Session

Base.metadata.create_all(bind=engine)

app = FastAPI()


origins = [
    "http://http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
 return {"message": "Welcome to Beavr"}


@app.post("/add_document")
def add_document(document: DocumentBase, db: Session = Depends(get_db)):
    db_doc = Document(title=document.title, content=document.content, summary=completion(document.content), key_elements=extract_key_elements(document.content))
    db.add(db_doc)
    db.commit()
    db.refresh(db_doc)
    return db_doc

@app.get("/documents")
def get_documents(db: Session = Depends(get_db)):
    docs = db.query(Document).all()
    return docs




