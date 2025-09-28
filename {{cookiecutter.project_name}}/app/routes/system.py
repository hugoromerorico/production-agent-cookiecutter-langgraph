from fastapi import APIRouter

router = APIRouter(tags=["system"])

@router.get("/health")
async def health_check():
    return {"status": "{{cookiecutter.project_name}} is healthy"}


@router.get("/ready")
async def readiness_check():
    return {"status": "{{cookiecutter.project_name}} is ready"}
