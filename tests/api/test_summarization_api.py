from fastapi.testclient import TestClient
import sys
import os

# Ensure the project root is in sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from main import app  # Import your FastAPI app

client = TestClient(app)

def test_process_summarization():
    text = "Artificial intelligence is transforming the world by automating tasks, improving efficiency, and enabling new capabilities."
    response = client.post("/summarize", json={"text": text})
    assert response.status_code == 200
    assert "summary" in response.json()
