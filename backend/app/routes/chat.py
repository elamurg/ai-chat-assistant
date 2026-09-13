"""API endpoints for chat functionality."""
from fastapi import APIRouter, HTTPException
from app.services.ai_service import ai_service
from app.models.chat import ChatRequest, ChatResponse, ChatMessage
from datetime import datetime
import logging

logger = logging.getLogger(__name__)
router = APIRouter()

@router.post("/chat", response_model=ChatResponse)
async def chat_endpoint(request: ChatRequest):
    """Endpoint to handle chat requests and generate AI responses."""
    try:
        if not request.message.strip():
            return HTTPException(status_code=400, detail="Message cannot be empty.")
        logger.info(f"Processing chat request: {request.message[:50]}...")
        ai_response = ai_service.generate_response(
            request.message,
            request.conversation_history or []
        )

        return ChatResponse(
            response=ai_response,
            timestamp=datetime.now(),
            success=True
        )
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        return ChatResponse(
            response="I appologise for the technical difficulties. Please try again.",
            success=False,
            timestamp=datetime.now(),
            error_message=str(e),
        )

@router.get("/health")
async def health_check():
    return {"status": "healthy", "service": "AI Chat Assistant"}
