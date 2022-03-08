from sqlalchemy.orm import Session
import models, schemas


def get_all_tasks(db : Session):
    return db.query(models.Tasks).all()

''' not working, will ask 
def get_sorted_tasks(db : Session):
    return db.query(models.Tasks).order_by(models.Tasks.deadline.asc())
'''

def search_tasks(id: int, db: Session):
   return db.query(models.Tasks).get(id)
     

def create_task(task : schemas.Tasks, db : Session):
    newTask = models.Tasks(title = task.title, description = task.description, isComplete = task.isComplete, deadline = task.deadline )

    db.add(newTask)
    db.commit()
    db.refresh(newTask)


def delete_task(id:int, db: Session):
    task = db.query(models.Tasks).get(id)
    db.delete(task)
    db.commit()
    
def update_task(task: schemas.Tasks, db: Session):
    db.query(models.Tasks).filter(models.Tasks.id == task.id).update({models.Tasks.title: task.title, models.Tasks.description: task.description,  models.Tasks.isComplete: task.isComplete,  models.Tasks.deadline: task.deadline})
    db.commit()
    
def complete_task(id: int, db: Session):
    db.query(models.Tasks).filter(models.Tasks.id == id).update({models.Tasks.isComplete: True})
    db.commit()