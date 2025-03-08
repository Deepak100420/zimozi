from fastapi import FastAPI,Request
import time
from app.config.logger import logger 

from app.routes.query import router as query_router
from app.routes.summary import router_0 as summary_router


# Initialize FastAPI app
app = FastAPI(title="AI-Powered Microservice", version="1.0")
# Log server start



# Log application startup
logger.info("FastAPI server is starting...")


# Include routers
app.include_router(query_router, tags=["Query"])
app.include_router(summary_router, tags=["Summarization"])





# Root endpoint
@app.get("/")
async def root():
    return {"message": "Welcome to the AI-powered FastAPI Microservice!"}


# Middleware to log HTTP requests
@app.middleware("http")
async def log_requests(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time

    logger.info(f"{request.method} {request.url} - {response.status_code} - {process_time:.2f}s")
    return response

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
