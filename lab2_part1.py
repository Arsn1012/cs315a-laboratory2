from fastapi import FastAPI, Query, Path
from typing import Optional

app = FastAPI()

prices_db = [15.50, 99.99, 45.00, 250.00, 12.00, 500.25, 75.10]

@app.get("/prices")
def get_prices(
    min_price: Optional[float] = Query(
        None,
        ge=0.0,
        title="Minimum Price",
        description="Lowest price to include"
    ),
    max_price: Optional[float] = Query(
        None,
        le=1000.0,
        title="Maximum Price",
        description="Highest price to include"
    )
):
    filtered = []

    for price in prices_db:
        if min_price is not None and price < min_price:
            continue
        if max_price is not None and price > max_price:
            continue
        filtered.append(price)

    return {
        "filtered_prices": filtered,
        "count": len(filtered)
    }

employee_db = {
    1001: "Alice Johnson",
    1002: "Bob Smith",
    1003: "Charlie Davis"
}

@app.get("/employees/{emp_id}")
def get_employee(
    emp_id: int = Path(
        ...,
        ge=1000,
        lt=10000,
        title="Employee ID Key",
        description="4-digit internal employee code"
    )
):
    if emp_id in employee_db:
        return {
            "emp_id": emp_id,
            "name": employee_db[emp_id]
        }

    return {
        "error": "Employee record not found"
    }