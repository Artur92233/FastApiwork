from fastapi import FastAPI, status, Request, Form
from fastapi.templating import Jinja2Templates

from base_storage import storage

from schemas import NewProduct, SavedProduct, PatchProduct

app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/")
@app.post("/")
def index(request: Request, q: str = Form(default="")):
    cars = storage.get_products()
    cars = storage.get_products(q=q)
    context = {"request": request, "cars": cars}
    return templates.TemplateResponse(
        "index.html",
        context=context,
    )


@app.get("/map_route")
def map_route_2(request: Request):

    context = {"request": request}
    return templates.TemplateResponse(
        "map.html",
        context=context,
    )


@app.get("/video")
def video(request: Request):

    context = {"request": request}
    return templates.TemplateResponse(
        "video.html",
        context=context,
    )


@app.get("/{product_id}")
def get_car_info(request: Request, product_id: str):
    car = storage.get_product(product_id=product_id)
    if not car:
        return templates.TemplateResponse(
            "404.html",
            context={"request": request, "car": car},
        )

    context = {"request": request, "car": car}
    return templates.TemplateResponse(
        "details.html",
        context=context,
    )


@app.post("/cars/", tags=["Автомобілі"], status_code=status.HTTP_201_CREATED)
def create_car(new_car: NewProduct) -> SavedProduct:
    product = storage.create_product(new_car)
    return product


@app.get("/cars/{car_id}")
def get_car(car_id: str) -> SavedProduct:
    car = storage.get_product(car_id)
    return car


@app.get("/cars/")
def get_cars(query: str = "", limit: int = 10, skip: int = 0) -> list[SavedProduct]:
    cars = storage.get_products(q=query, limit=limit, skip=skip)
    return cars


@app.patch("/cars/{car_id}")
def edit_car(car_id: str, data: PatchProduct) -> SavedProduct:
    product = storage.patch_product(car_id, data)
    return product


@app.delete("/cars/{car_id}")
def delete_car(car_id: str) -> dict:
    storage.delete_product(car_id)
    return {}
