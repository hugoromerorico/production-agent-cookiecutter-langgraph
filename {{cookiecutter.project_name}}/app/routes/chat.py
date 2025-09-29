from fastapi import APIRouter, Request, HTTPException, Depends
from pydantic import BaseModel
from app.application.chat import Chat
from loguru import logger
from typing import List
from langchain_core.messages import AnyMessage

router = APIRouter(tags=["chat"])

# Request/Response models
class ChatMessageRequest(BaseModel):
    message: str
    thread_id: str

class ChatMessageResponse(BaseModel):
    message: str

class ThreadHistoryRequest(BaseModel):
    thread_id: str

class ThreadHistoryResponse(BaseModel):
    messages: List[AnyMessage]

def get_chat(request: Request) -> Chat:
    return request.app.state.chat

@router.post("/chat", response_model=ChatMessageResponse)
async def chat_message(
    chat_request: ChatMessageRequest,
    request: Request,
    chat: Chat = Depends(get_chat)
):
    """
    Send a message to the chat agent and get a response.
    """
    try:
        logger.debug(f"Request: {chat_request}")
        result = chat.execute(chat_request.message)
        
        messages = result.get("messages", [])
        
        if not messages:
            raise HTTPException(status_code=500, detail="No response generated")
        
        # Get the last message which should be the assistant's response
        last_message = messages[-1]
        response_content = last_message.text()
        
        return ChatMessageResponse(
            message=response_content
        )
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing message: {str(e)}")

@router.get("/chat/{thread_id}", response_model=ThreadHistoryResponse)
async def get_thread_history(
    thread_id: str,
    request: Request,
    chat: Chat = Depends(get_chat)
):
    """
    Get the history of a thread.
    """
    return chat.get_state(thread_id)