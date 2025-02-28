from fastapi import FastAPI

from base_storage import storage

from schemas import NewProduct, SavedProduct

app = FastAPI()


@app.get("/")
def index():
    return {"status": "OK"}


@app.post("/cars/", tags=["Автомобілі"])
def create_car(new_car: NewProduct) -> SavedProduct:
    car = storage.create_product(new_car)
    return car


@app.get("/cars/{car_id}")
def get_car(car_id: str) -> SavedProduct:
    car = storage.get_product(car_id)
    return car


@app.get("/cars/")
def get_cars(query: str = "", limit: int = 10, skip: int = 0) -> list[SavedProduct]:
    cars = storage.get_products(q=query, limit=limit, skip=skip)
    return cars


@app.patch("/cars/{car_id}")
def edit_car(car_id: str, data: dict):
    pass


@app.delete("/cars/{car_id}")
def delete_car(car_id: str) -> dict:
    storage.delete_product(car_id)
    return {}
