from fastapi import APIRouter
from ..db import get_db

router = APIRouter()

@router.get("/health")
async def health():
    db = get_db()
    # simple ping-like query
    names = await db.list_collection_names()
    return {"status": "ok", "collections": names}
