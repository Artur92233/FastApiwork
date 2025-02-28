import os
import uuid
import json
from abc import ABC, abstractmethod
from schemas import NewProduct, SavedProduct, ProductId
from fastapi import HTTPException, status
from pymongo import MongoClient
from settings import settings


class BaseStorage(ABC):
    @abstractmethod
    def create_product(self, new_product: NewProduct) -> SavedProduct:
        pass

    @abstractmethod
    def get_product(self, product_id: str) -> SavedProduct:
        pass

    @abstractmethod
    def get_products(
        self, q: str = "", limit: int = 10, skip: int = 0
    ) -> list[SavedProduct]:
        pass

    @abstractmethod
    def delete_product(self, product_id: str) -> None:
        pass


class MongoStorage(BaseStorage):
    def __init__(self, uri: str):
        print(uri)
        client = MongoClient(uri)
        db = client.products
        collection_product = db.products
        self.collection_product = collection_product

    def create_product(self, new_product: NewProduct) -> SavedProduct:

        payload = {
            "title": new_product.title,
            "price": new_product.price,
            "description": new_product.description,
            "cover": new_product.cover,
            "id": uuid.uuid4().hex,
        }
        self.collection_product.insert_one(payload)
        saved_product = SavedProduct(**payload)
        return saved_product

    def get_product(self, product_id: str) -> SavedProduct:
        query = {"id": product_id}
        car = self.collection_product.find_one(query)
        if not car:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Product not found"
            )
        return car

    def get_products(
        self, q: str = "", limit: int = 20, skip: int = 0
    ) -> list[SavedProduct]:
        query = {}
        if q:
            query = {
                "$or": [
                    {
                        "title": {
                            "$regex": q,
                            "$options": "i",
                        }
                    },
                    {
                        "description": {
                            "$regex": q,
                            "$options": "i",
                        }
                    },
                ]
            }
        cars = self.collection_product.find(query).limit(limit).skip(skip)
        return cars or []

    def delete_product(self, product_id: str) -> None:
        query = {"id": product_id}
        self.collection_product.delete_many(query)


storage: BaseStorage = MongoStorage(settings.MONGO_URI)
