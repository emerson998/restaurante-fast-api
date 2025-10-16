from sqlalchemy.orm import Session
from app.domain.models import Restaurant, Dish

class RestaurantRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return self.db.query(Restaurant).all()

    def get(self, restaurant_id: int):
        return self.db.query(Restaurant).filter(Restaurant.id == restaurant_id).first()

    def create(self, name: str, address: str):
        restaurant = Restaurant(name=name, address=address)
        self.db.add(restaurant)
        self.db.commit()
        self.db.refresh(restaurant)
        return restaurant
    

    def add_dish(self, restaurant_id: int, name: str, price: float):
        dish = Dish(name=name, price=price, restaurant_id=restaurant_id)
        self.db.add(dish)
        self.db.commit()
        self.db.refresh(dish)
        return dish

    def get_dishes(self, restaurant_id: int):
        return self.db.query(Dish).filter(Dish.restaurant_id == restaurant_id).all()
