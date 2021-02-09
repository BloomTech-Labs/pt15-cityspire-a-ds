from sqlalchemy.orm import Session

from . import models, schemas


def get_pop_predict_model(db: Session, year: int, city_state: str):
    return db.query(models.Pop_Table).filter(models.Pop_Table.city_state == city_state).filter(models.Pop_Table.year == year).first()

def pop_predict_model_all(db: Session, city_state: str):
    return db.query(models.Pop_Table).filter(models.Pop_Table.city_state == city_state).all()

