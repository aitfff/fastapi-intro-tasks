from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field, condecimal
from typing import List


app = FastAPI()

# Временная база данных
product_list = []
product_id_counter = 1

# BEGIN (write your solution here)
class ProductSpecifications(BaseModel):
    size: str
    color: str
    material: str

class Product(BaseModel):
    name: str
    price: condecimal(gt=0)
    specifications: ProductSpecifications

@app.post("/product")
def create_product(product: Product):
    global product_id_counter
    product_dict = product.dict()
    product_dict["id"] = product_id_counter
    product_list.append(product_dict)
    product_id_counter += 1
    return {"message": "Product added successfully", "product": product_dict}

@app.get("/products", response_model=List[Product])
def get_products():
    return product_list
# END
