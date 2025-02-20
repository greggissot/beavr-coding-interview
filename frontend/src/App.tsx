import { useEffect, useState } from "react";
import "./App.css";

interface Document {
  id: string;
  name: string;
}

function App() {
  const [documents, setDocuments] = useState<Document[]>([]);
  const [newName, setNewName] = useState<string>("");

  const fetchDocuments = () => {
    fetch("http://localhost:8000/documents").then((res) => {
      res.json().then((data) => {
        setDocuments(data);
      });
    });
  };

  useEffect(() => {
    fetchDocuments();
  }, []);

  const handleAddDocument = () => {
    fetch("http://localhost:8000/add_document", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ name: newName }),
    }).then(() => {
      fetchDocuments();
    });
  };

  return (
    <>
      <div>
        <h1>Beavr</h1>
      </div>
      <div>
        <h2>Documents</h2>
        <ul>
          {documents.map((document) => (
            <li key={document.id}>{document.name}</li>
          ))}
        </ul>
      </div>
      <div>
        <h2>Add Document</h2>
        <div style={{ display: "flex", flexDirection: "column", gap: "10px" }}>
          <input
            type="text"
            placeholder="Document Name"
            value={newName}
            onChange={(e) => setNewName(e.target.value)}
          />
          <button onClick={handleAddDocument}>Add Document</button>
        </div>
      </div>
    </>
  );
}

export default App;
