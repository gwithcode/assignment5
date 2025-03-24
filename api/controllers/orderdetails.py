from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response, Depends
from ..models import models, schemas

def create_order_details(db: Session, order_details):
    db_order_details = models.OrderDetail(
        order_id = order_details.order_id,
        sandwich_id = order_details.sandwich_id,
        amount = order_details.amount
    )

    db.add(db_order_details)

    db.commit()

    db.refresh(db_order_details)

    return db_order_details

def read_all_order_details(db: Session):
    return db.query(models.OrderDetail).all()

def read_one_order_details(db: Session, order_details_id):
    return db.query(models.OrderDetail).filter(models.OrderDetail.id == order_details_id)

def update_one_order_details(db: Session, order_details_id, order_details):
    db_order_details = db.query(models.OrderDetail).filter(models.OrderDetail.id == order_details_id)

    update_order_details = order_details.model_dump(exclude_unset = True)

    db_order_details.update(update_order_details, synchronize_session = False)

    db.commit()

    return db_order_details.first()

def delete_one_order_details(db: Session, order_details_id):
    db_order_details = db.query(models.OrderDetail).filter(models.OrderDetail.id == order_details_id)

    db_order_details.delete(synchronize_session = False)

    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)