from fastapi import APIRouter
router=APIRouter(tags=["anomaly"])
@router.post("/anomaly/detect")
def detect(): return {"todo":"M6 Isolation Forest"}
