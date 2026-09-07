from fastapi import APIRouter
router=APIRouter(tags=["venues"])
@router.get("/venues")
def list_venues(): return []
@router.post("/venues")
def create_venue(): return {"todo":"M2 CRUD + import CSV/Excel + soft-delete"}
