from app.infra.repository import RestaurantRepository
from app.domain.schemas import RestaurantCreate
from sqlalchemy.orm import Session

class RestaurantUseCase:
    def __init__(self, db: Session):
        self.repo = RestaurantRepository(db)

    def create_restaurant(self, restaurant_create: RestaurantCreate):
        if not restaurant_create.name.strip():
            raise ValueError("O nome do restaurante não pode estar vazio")
        return self.repo.create(restaurant_create.name, restaurant_create.address)

    def get_restaurant(self, restaurant_id: int):
        restaurant = self.repo.get(restaurant_id)
        if not restaurant:
            raise ValueError("Restaurante não encontrado")
        return restaurant

    def list_restaurants(self):
        return self.repo.get_all()

    def get_restaurant_native(self, restaurant_id: int, db: Session):
        sql = "SELECT * FROM restaurants WHERE id = :id"
        result = db.execute(sql, {"id": restaurant_id}).mappings().first()
        if not result:
            raise ValueError("Restaurante não encontrado")
        return result

    def add_dish(self, restaurant_id: int, name: str, price: float):
        if price <= 0:
            raise ValueError("O preço do prato deve ser positivo")
        return self.repo.add_dish(restaurant_id, name, price)

    def list_dishes(self, restaurant_id: int):
        return self.repo.get_dishes(restaurant_id)
