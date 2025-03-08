from fastapi import APIRouter
from pydantic import BaseModel, Field
from app.config.logger import logger 

class QueryRequest(BaseModel):
    """
    Schema for the request body of the query endpoint.
    """
    query: str = Field(..., title="Enter your query", description="The query string to be executed")

router = APIRouter()

@router.post("/query", tags=["Query"],summary="Process a user query")
async def process_query(request: QueryRequest):
    """
    Handles user queries and logs the request.

    - **query**: The user-inputted query string.

    Returns:
    - A JSON response confirming query receipt.
    """
    
    logger.info(f"Query received: {request.query}")
    return {"response": f"Your query '{request.query}' was received successfully!"}
