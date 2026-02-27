from fastapi import APIRouter, Request
from core.storage import answer_key, template

router = APIRouter()


@router.post("/api/set-key")
async def set_key(request: Request):

    data = await request.json()

    answer_key.clear()
    answer_key.update(data)

    return {"status": "saved"}


@router.post("/api/set-template")
async def set_template(request: Request):

    data = await request.json()

    template.clear()
    template.update(data)

    return {"status": "saved"}
