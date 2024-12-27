from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field, condecimal, conint
from typing import List


app = FastAPI()

# Временная база данных
product_list = []
product_id_counter = 1

# BEGIN (write your solution here)
class Product(BaseModel):
    id: int = Field(default_factory=lambda: next(product_id_counter))
    name: str
    price: condecimal(gt=0)  # цена должна быть больше нуля
    quantity: conint(ge=0)    # количество должно быть больше или равно нулю

# Эндпоинт для добавления продукта
@app.post("/product")
async def add_product(product: Product):
    global product_id_counter
    product.id = product_id_counter  # Устанавливаем уникальный идентификатор
    product_list.append(product)      # Добавляем продукт в список
    product_id_counter += 1           # Увеличиваем счетчик идентификаторов
    return {"message": "Product added successfully"}

# Эндпоинт для получения списка продуктов
@app.get("/products", response_model=List[Product])
async def get_products():
    return product_list
# END
