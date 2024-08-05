from fastapi import APIRouter

router = APIRouter()

@router.get("/items")
async def read_items():
    return [{"name": "Item 1 v2"}, {"name": "Item 2 v2"}]

@router.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"name": f"Item {item_id} v2", "version": "v2"}

@router.post("/items")
async def create_item(item: dict):
    return {"name": f"{item['name']} v2", "version": "v2"}