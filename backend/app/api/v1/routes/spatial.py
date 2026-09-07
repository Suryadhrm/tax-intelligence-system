from fastapi import APIRouter
router=APIRouter(tags=["spatial"])
@router.get("/spatial/znt")
def znt(): return {"todo":"M3 spatial join PostGIS"}
