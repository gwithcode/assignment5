from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response, Depends
from ..models import models, schemas

def create_recipe(db: Session, recipe):
    db_recipe = models.Recipe(
        sandwich_id = recipe.sandwich_id,
        resource_id = recipe.resource_id,
        amount = recipe.amount
    )

    db.add(db_recipe)

    db.commit()

    db.refresh(db_recipe)

    return db_recipe

def read_all_recipe(db: Session):
    return db.query(models.Recipe).all()

def read_one_recipe(db: Session, recipe_id):
    return db.query(models.Recipe).filter(models.Recipe.id == recipe_id)

def update_one_recipe(db: Session, recipe_id, recipe):
    db_recipe = db.query(models.Recipe).filter(models.Recipe.id == recipe_id)

    update_recipe = recipe.model_dump(exclude_unset = True)

    db_recipe.update(update_recipe, synchronize_session = False)

    db.commit()

    return db_recipe.first()

def delete_one_recipe(db: Session, recipe_id):
    db_recipe = db.query(models.Recipe).filter(models.Recipe.id == recipe_id)

    db_recipe.delete(synchronize_session = False)

    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)