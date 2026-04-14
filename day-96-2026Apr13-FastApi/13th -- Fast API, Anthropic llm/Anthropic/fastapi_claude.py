# pip install fastapi uvicorn anthropic python-dotenv

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from anthropic import Anthropic
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="Anthropic Claude API")
client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

# ── Request / Response schemas ──────────────────────────────────────────────

class ChatRequest(BaseModel):
    message: str
    max_tokens: int = 1024

class ChatResponse(BaseModel):
    response: str
    model: str
    input_tokens: int
    output_tokens: int

# ── Routes ───────────────────────────────────────────────────────────────────

@app.get("/")
def root():
    return {"status": "ok", "message": "Anthropic FastAPI is running"}


@app.post("/chat", response_model=ChatResponse)
def chat(req: ChatRequest):
    if not req.message.strip():
        raise HTTPException(status_code=400, detail="Message cannot be empty")

    try:
        result = client.messages.create(
            model="claude-sonnet-4-5",
            max_tokens=req.max_tokens,
            messages=[{"role": "user", "content": req.message}],
        )

        return ChatResponse(
            response=result.content[0].text,
            model=result.model,
            input_tokens=result.usage.input_tokens,
            output_tokens=result.usage.output_tokens,
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/chat/stream")
def chat_stream(req: ChatRequest):
    """Streaming version — returns text chunks as server-sent events."""
    from fastapi.responses import StreamingResponse

    def generate():
        with client.messages.stream(
            model="claude-sonnet-4-5",
            max_tokens=req.max_tokens,
            messages=[{"role": "user", "content": req.message}],
        ) as stream:
            for text in stream.text_stream:
                yield f"data: {text}\n\n"
        yield "data: [DONE]\n\n"

    return StreamingResponse(generate(), media_type="text/event-stream")