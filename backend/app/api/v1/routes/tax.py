from fastapi import APIRouter
router=APIRouter(tags=["tax"])
@router.post("/tax/pbjt")
def pbjt(): return {"todo":"M5 pbjt = omzet * tarif"}
