from fastapi import APIRouter, Request, HTTPException, Depends
from pydantic import BaseModel
from app.application.use_case import UseCase
from loguru import logger
from app.application.workflows.wf1.state import CustomState

router = APIRouter(tags=["wf1"])

# Request/Response models
class UseCaseRequest(BaseModel):
    pass

class UseCaseResponse(BaseModel):
    state: CustomState

def get_use_case(request: Request) -> UseCase:
    return request.app.state.use_case

@router.post("/wf1", response_model=UseCaseResponse)
async def wf1(
    use_case_request: UseCaseRequest,
    request: Request,
    use_case: UseCase = Depends(get_use_case)
):
    """
    Execute the wf1 use case.
    """
    try:
        final_state = await use_case.execute()
        return UseCaseResponse(
            state=final_state
        )
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing request: {str(e)}")
