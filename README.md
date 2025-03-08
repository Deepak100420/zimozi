# FastAPI Microservice with AI Summarization Tool (Distilbart-cnn-12-6)


## 🎯 Objective
Design and develop a production-ready microservice using **FastAPI** that integrates with an open-source AI language model (e.g., Hugging Face models) to process user requests in real-time. The microservice must implement:

## 🚀 Features
- **Query Processing Endpoint**  
  Accepts a user’s query and returns a basic response, demonstrating structured API handling.
- **Text Summarization Endpoint**  
  Takes long-form text input and returns a concise summary using a free, open-source AI summarization model (**DistilBART 12-6** from Hugging Face).

## Main Dependencies
- **FastAPI** for creating endpoints and testing APIs
- **Pydantic** for data validation
- **Transformers** for downloading models locally
- **Evaluate** for evaluating output summaries using ROUGE technique
- **Pytest** for testing functionality

## Directory Structure

```
├── app/
│   ├── main.py  # FastAPI application
│   ├── services/
│   │   ├── summarization.py  # Contains generate_summary function
│   ├── routes/
│   │   ├── query_api.py  # API for processing queries
│   │   ├── summarization_api.py  # API for text summarization
│   ├── config/
│   │   ├── logger.py  # Logging configuration
│   ├── logs/
│   │   ├── app.log  # Application logs
│
├── tests/
│   ├── api/
│   │   ├── test_query_api.py  # Tests for query API
│   │   ├── test_summarization_api.py  # Tests for summarization API
│   ├── functions/
│   │   ├── test_generate_summary.py  # Unit tests for generate_summary function
│   ├── model/
│   │   ├── test_model.py  # Model testing using ROUGE scores
│
├── myenv/  # Virtual environment
├── pytest.ini  # Pytest configuration
├── requirements.txt  # Dependencies
├── README.md  # Project documentation
└── main.py  # FastAPI application entry point (outside the app folder for better separation)
```

## Installation
### 1. Clone the Repository
```sh
git clone https://github.com/your-repo/zimozi_1.git
cd zimozi_1
```

### 2. Set Up a Virtual Environment
```sh
python -m venv myenv
source myenv/bin/activate  # For Linux/macOS
myenv\Scripts\activate  # For Windows
```

### 3. Install Dependencies
```sh
pip install -r requirements.txt
```


## Download and Save DistilBART Model Locally

### Step 1: Create a Hugging Face Access Token
1. Go to the [Hugging Face website](https://huggingface.co/).
2. Sign in or create an account.
3. Navigate to [Access Tokens](https://huggingface.co/settings/tokens).
4. Generate a new token with `read` access.
5. Copy the token for later use.

### Step 2: Download and Save DistilBART Model
Use the following Python script to download the `sshleifer/distilbart-cnn-12-6` model and save it locally.

```python
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

# Define model name and access token
model_name = "sshleifer/distilbart-cnn-12-6"
token = "your_huggingface_access_token_here"  # Replace with your actual token

# Load model and tokenizer
model = AutoModelForSeq2SeqLM.from_pretrained(model_name, use_auth_token=token)
tokenizer = AutoTokenizer.from_pretrained(model_name, use_auth_token=token)

# Define save path
save_path = "D:/interview/zimozi_1/model/distilbart"  # Change to your preferred directory

# Save model and tokenizer locally
model.save_pretrained(save_path)
tokenizer.save_pretrained(save_path)

print(f"Model saved successfully in {save_path}!")
```

### Step 3: Run the Script
1. Create a `.env` file in the project root with the following content:
   ```ini
   HF_TOKEN=your_huggingface_access_token_here
   MODEL_PATH=Change to your preferred directory

   ```
2. Replace `your_huggingface_access_token_here` with the token you generated.
3. Modify `MODEL_PATH` to your desired directory.
4. Run the script in your Python environment.
5. The model and tokenizer will be saved locally for offline use.

#### Notes
- Ensure you have `transformers` and `python-dotenv` installed:
  ```sh
  pip install transformers python-dotenv
  ```
- Make sure your access token has the necessary permissions.
- The saved model can be loaded later using `from_pretrained(save_path)`. 

---

### 📜 Environment Variables (.env)
The `.env` file is used to store sensitive information such as model paths and Hugging Face access tokens.

```ini
HF_TOKEN=your_huggingface_access_token_here
MODEL_PATH=Change to your preferred directory
```

Make sure this file is not included in version control (`.gitignore`).




## Running the Application
Start the FastAPI server:
```sh
uvicorn main:app --reload
```
Access API docs at: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

## Running Tests
To run all tests:
```sh
pytest -v
```
To run function tests only:
```sh
pytest tests/functions/ -v
```
To run API tests only:
```sh
pytest tests/api/ -v
```
To run model tests only (evaluated using ROUGE score), run the following Python file:
**Optional**
```sh
python tests/model/test_model.py

```

## API Endpoints
### 1. Process Query
**Endpoint:** `POST /query`
- **Request:** `{ "query": "your query here" }`
- **Response:** `{ "response": "Your query '...' was received successfully!" }`

### 2. Summarize Text
**Endpoint:** `POST /summarize`
- **Request:** `{ "text": "long text here..." }`
- **Response:** `{ "summary": "shorter text summary..." }`

## Contributing
Feel free to submit issues or pull requests to improve the project.


