from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.domain.schemas import RestaurantCreate
from app.infra.database import SessionLocal
from app.use_case.restaurante_use_case import RestaurantUseCase

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/restaurants")
def get_restaurants(db: Session = Depends(get_db)):
    use_case = RestaurantUseCase(db)
    return use_case.list_restaurants()

@router.get("/restaurants-native/{restaurant_id}")
def get_restaurant_native(restaurant_id: int, db: Session = Depends(get_db)):
    use_case = RestaurantUseCase(db)
    try:
        return use_case.get_restaurant_native(restaurant_id, db)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.post("/restaurants")
def create_restaurant(restaurant: RestaurantCreate, db: Session = Depends(get_db)):
    use_case = RestaurantUseCase(db)
    try:
        return use_case.create_restaurant(restaurant)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/restaurants/{restaurant_id}")
def get_restaurant(restaurant_id: int, db: Session = Depends(get_db)):
    use_case = RestaurantUseCase(db)
    try:
        return use_case.get_restaurant(restaurant_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.post("/restaurants/{restaurant_id}/dishes")
def add_dish(restaurant_id: int, name: str, price: float, db: Session = Depends(get_db)):
    use_case = RestaurantUseCase(db)
    try:
        return use_case.add_dish(restaurant_id, name, price)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/restaurants/{restaurant_id}/dishes")
def get_dishes(restaurant_id: int, db: Session = Depends(get_db)):
    use_case = RestaurantUseCase(db)
    return use_case.list_dishes(restaurant_id)
