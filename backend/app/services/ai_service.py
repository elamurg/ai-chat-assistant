"""Building context from conversation history and user input."""
import google.generativeai as genai
from config.settings import settings
from app.models.chat import ChatRequest, ChatMessage, ChatResponse
from typing import List
import logging
from datetime import datetime

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class AIService:
    def __init__(self):
        genai.configure(api_key = settings.GEMINI_API_KEY)
        self.model = genai.GenerativeModel('gemini-pro')
    
    def generate_response(self, user_message: str, conversation_history: List[ChatMessage] = []) -> str:
        try:
            #build the context from conversation history
            context = self._build_context(conversation_history)
            full_prompt = f"{context}\n User: {user_message}\n Assistant: "
            logger.info(f"Generating AI response for: {user_message[:50]}...")
            response = self.model.generate_content(full_prompt)

            if response and response.text:
                return response.text.strip()
            else:
                return "I appologise, but I couldn't generate a response at this time."
        except Exception as e:
            logger.error(f"Error generating AI response: {e}")
            return f"I am experiencing technical difficulties: {str(e)}"
    
    def _build_context(self, conversation_history: List[ChatMessage]) -> str:
        if not conversation_history:
            return "You are a helpful AI assistant. Provide consise and accurate response to user queries."
        context = "You are a helpful AI assistant. Here is the conversation so far: \n"
        for message in conversation_history[-5:]: #limit to 5 messages for context
            context += f"{message.role.title()}: {message.content}\n"
        return context
    
ai_service = AIService()