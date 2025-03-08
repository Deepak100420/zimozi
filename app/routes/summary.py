from fastapi import APIRouter,HTTPException
from pydantic import BaseModel ,Field,field_validator
from app.config.logger import logger 
from app.services.summarization import generate_summary

router_0 = APIRouter()

#Request Model for Summary
class SummarizationRequest(BaseModel):
    """
    Schema for the request body of the summarization endpoint.
    """
    text: str = Field(
        ...,
        min_length=50,
        max_length=5000,
        description='Input text for summarization (50 to 5000 characters).'
    )

    @field_validator('text')
    @classmethod
    def validate_text(cls, value: str) -> str:
        """Ensure the text is properly formatted and meets length requirements."""
        value = value.strip()  # Keep double quotes as is
        if len(value) < 50:
            raise ValueError("Text must be at least 50 characters long.")
        return value
    
@router_0.post("/summarize", tags=["Summarization"],summary="Summarize a given text")
async def process_summarization(request: SummarizationRequest):
    
    """
    Handles text summarization requests.

    - **text**: The input text (50-5000 characters) to be summarized.
    
    Returns:
    - A JSON object containing the summarized text.
    """
    
    # Log application startup
    logger.info("Summary route accessed.")
    try:
        return {"summary":generate_summary(text=request.text)}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

   

