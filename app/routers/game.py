from fastapi import APIRouter

router = APIRouter()

@router.get("/users/{username}", tags=["users"])
async def read_user(username: str):
    return {"username": username}