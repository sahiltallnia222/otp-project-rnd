from fastapi import APIRouter

router = APIRouter()

@router.get("/items")
async def read_items():
    return [{"name": "Item 1 v1"}, {"name": "Item 2 v1"}]

@router.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"name": f"Item {item_id} v1", "version": "v1"}