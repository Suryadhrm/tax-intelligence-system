from fastapi import APIRouter
router=APIRouter(tags=["dashboard"])
@router.get("/dashboard/summary")
def summary(): return {"total_venue":0,"total_omzet_potensial":0,"total_pbjt_potensial":0,"anomali":0}
