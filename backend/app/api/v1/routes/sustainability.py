from fastapi import APIRouter
router=APIRouter(tags=["sustainability"])
@router.get("/sustainability/{venue_id}")
def get(venue_id:str): return {"todo":"M7 weighted score if history sufficient"}
