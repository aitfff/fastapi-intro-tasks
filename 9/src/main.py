from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field, condecimal
from typing import List, Optional


app = FastAPI()

# Временная база данных
product_list = []
product_id_counter = 1

# BEGIN (write your solution here)
class Specifications(BaseModel):
    size: str
    color: str
    material: str

class Product(BaseModel):
    name: str
    price: condecimal(gt=0) 
    specifications: Specifications

class ProductResponse(BaseModel):
    id: int
    name: str
    price: float

class ProductDetailResponse(BaseModel):
    id: int
    name: str
    price: float
    specifications: Specifications

@app.post("/product", response_model=ProductResponse)
async def create_product(product: Product):
    global product_id_counter
    product_id_counter += 1
    new_product = {**product.dict(), "id": product_id_counter - 1}
    product_list.append(new_product)
    return new_product

@app.get("/products", response_model=List[ProductResponse])
async def get_products():
    return [{"id": p["id"], "name": p["name"], "price": p["price"]} for p in product_list]

@app.get("/product/{product_id}", response_model=ProductDetailResponse)
async def get_product(product_id: int):
    for product in product_list:
        if product["id"] == product_id:
            return product
    raise HTTPException(status_code=404, detail="Product not found")
# END