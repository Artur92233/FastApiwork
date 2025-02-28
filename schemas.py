from pydantic import BaseModel, Field


class PatchProduct(BaseModel):
    price: float = Field(ge=1000)
    title: str = Field(min_length=10, max_length=50)


class NewProduct(PatchProduct):
    description: str = Field(min_length=30, max_length=200)
    cover: str = Field()


class ProductId(BaseModel):
    id: str


class SavedProduct(ProductId, NewProduct):
    pass
