from fastapi import APIRouter
router=APIRouter(tags=["auth"])
@router.post("/auth/login")
def login(): return {"todo":"M1 JWT"}
