from fastapi import FastAPI

app = FastAPI(
    title="ApprovalFlow API",
    description="A configurable multi-step approval workflow backend",
    version="0.1.0",
)


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }