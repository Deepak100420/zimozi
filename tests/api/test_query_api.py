from fastapi.testclient import TestClient
import sys
import os

# Ensure the project root is in sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from main import app  # Import your FastAPI app

client = TestClient(app)

def test_process_query():
    response = client.post("/query", json={"query": "What is AI?"})
    assert response.status_code == 200
    assert "response" in response.json()
    assert "What is AI?" in response.json()["response"]
