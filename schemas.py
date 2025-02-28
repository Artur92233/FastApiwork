from pydantic import BaseModel, Field


class NewProduct(BaseModel):
    price: float = Field(ge=1000)
    title: str = Field(min_length=10, max_length=50)
    description: str = Field(min_length=30, max_length=200)
    cover: str = Field()


class ProductId(BaseModel):
    id: str


class SavedProduct(ProductId, NewProduct):
    pass
