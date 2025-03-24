from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response, Depends
from ..models import models, schemas

def create_sandwich(db: Session, sandwich):
    db_sandwich = models.Sandwich(
        sandwich_name = sandwich.sandwich_name,
        price = sandwich.price
    )

    db.add(db_sandwich)

    db.commit()

    db.refresh(db_sandwich)

    return db_sandwich

def read_all_sandwich(db: Session):
    return db.query(models.Sandwich).all()

def read_one_sandwich(db: Session, sandwich_id):
    return db.query(models.Sandwich).filter(models.Sandwich.id == sandwich_id)

def update_one_sandwich(db: Session, sandwich_id, sandwich):
    db_sandwich = db.query(models.Sandwich).filter(models.Sandwich.id == sandwich_id)

    update_sandwich = sandwich.model_dump(exclude_unset = True)

    db_sandwich.update(update_sandwich, synchronize_session = False)

    db.commit()

    return db_sandwich.first()

def delete_one_sandwich(db: Session, sandwich_id):
    db_sandwich = db.query(models.Sandwich).filter(models.Sandwich.id == sandwich_id)

    db_sandwich.delete(synchronize_session = False)

    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)