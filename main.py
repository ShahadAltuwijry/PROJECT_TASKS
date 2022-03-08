from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import engine, localsession, Base
import models, schemas
import tasks_crud

Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = localsession()
    
    try:
        yield db
    finally:
        db.close()
        

# gets all tasks
@app.get("/tasks/all")
def getAllTasks(db: Session = Depends(get_db)):
    return tasks_crud.get_all_tasks(db)

# gets tasks sorted by date
""" this is not working, will ask on it
@app.get("/tasks/bydate")
def getTasksByDate(db: Session = Depends(get_db)):
    return tasks_crud.get_sorted_tasks(db)
"""

# search tasks by id
@app.get("/tasks/search/{id}")
def searchTask(id: int, db: Session = Depends(get_db)):
    return tasks_crud.search_tasks(id, db)


# add new task
@app.post("/tasks/new")
def new_task(task: schemas.Tasks, db: Session = Depends(get_db)):
    tasks_crud.create_task(task, db)
    return {"msg": "new task is added"}


# delete task by id
@app.delete("/tasks/delete/{id}")
def deleteTask(id: int, db: Session = Depends(get_db)):
    tasks_crud.delete_task(id, db)
    return {"msg": f"the task with id: {id}, id delete succesfuly"}


# update task
@app.put("/tasks/update")
def updateTask( task: schemas.Tasks, db: Session = Depends(get_db)):
    tasks_crud.update_task(task, db)
    return {"msg": "post is updated succesfully!"}
  
  
# sets task as Completed = true 
@app.put("/tasks/completed/{id}")
def completeTask(id: int, db: Session = Depends(get_db)):
    tasks_crud.complete_task(id, db)
    return {"msg": "post is checked succesfully!"}
