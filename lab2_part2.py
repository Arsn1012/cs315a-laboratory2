from fastapi import FastAPI, Query, Path

app = FastAPI()

tasks_db: list[str] = [
    "Setup environment",
    "Write unit tests",
    "Deploy application"
]

@app.get("/tasks")
def read_tasks():
    return {
        "tasks": tasks_db,
        "count": len(tasks_db)
    }

@app.post("/tasks")
def create_task(
    task_name: str = Query(
        ...,
        min_length=3,
        max_length=50
    )
):
    tasks_db.append(task_name)

    return {
        "message": "Task added",
        "tasks": tasks_db
    }

@app.delete("/tasks/{task_index}")
def delete_task(
    task_index: int = Path(..., ge=0)
):
    if 0 <= task_index < len(tasks_db):
        deleted = tasks_db.pop(task_index)
        return {
            "message": "Task removed",
            "deleted": deleted
        }

    return {
        "error": "Index out of range"
    }

inventory_db: dict[int, str] = {
    501: "Mechanical Keyboard",
    502: "Ergonomic Mouse",
    503: "USB-C Hub"
}

@app.get("/inventory")
def get_inventory():
    return inventory_db


@app.get("/inventory/{item_id}")
def get_item(
    item_id: int = Path(..., gt=0)
):
    if item_id in inventory_db:
        return {
            "item_id": item_id,
            "item_name": inventory_db[item_id]
        }

    return {
        "error": "Item not found"
    }

@app.post("/inventory/{item_id}")
def add_item(
    item_id: int = Path(..., gt=0),
    item_name: str = Query(
        ...,
        min_length=2,
        max_length=30
    )
):
    inventory_db[item_id] = item_name

    return {
        "message": "Item added",
        "inventory": inventory_db
    }


@app.delete("/inventory/{item_id}")
def delete_item(
    item_id: int = Path(..., gt=0)
):
    if item_id in inventory_db:
        deleted = inventory_db.pop(item_id)
        return {
            "message": "Item removed",
            "deleted": deleted
        }

    return {
        "error": "Item not found"
    }