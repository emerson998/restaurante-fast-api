from pydantic import BaseModel

class RestaurantCreate(BaseModel):
    name: str
    address: str
