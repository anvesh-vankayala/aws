from fastapi import FastAPI, File, HTTPException
from fastapi.responses import JSONResponse
import uvicorn

app = FastAPI(
    title="Image Classification API",
    description="FastAPI application serving an ONNX model for image classification",
    version="1.0.0",
)


@app.get("/")
async def helloworld():
    return JSONResponse(
        content={"status": "healthy", "hello_world": True}, status_code=200
    )


@app.get("/health")
async def health_check():
    return JSONResponse(
        content={"status": "healthy", "model_loaded": True}, status_code=200
    )


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)