from fastapi import FastAPI , Form , File , UploadFile , HTTPException
from fastapi.responses import StreamingResponse , FileResponse
import sqlite3

# Connect to database
connection = sqlite3.connect('app/todo.db')
cursor = connection.cursor()

app = FastAPI()

          

@app.get("/")
def first():
    msg = "Welcome to todo list"
    return msg

@app.get("/task")
def read_tasks():
    connection = sqlite3.connect('app/todo.db')
    cursor = connection.cursor()
    query = "SELECT * FROM todo_list"
    tasks = []
    all_task = cursor.execute(query)
    connection.commit()
    for task in all_task:
            tasks.append({"id": task[0], "title": task[1], "description": task[2], "time": task[3],"status":task[4]})

    return tasks

@app.post("/task")
def add_task(id:int = Form(None),title:str = Form(None),description: str = Form(None),time:str = Form(None),status:int = Form(None)):
    if id is None:
        raise HTTPException(status_code=400, detail="You should enter id")
    if title is None:
        raise HTTPException(status_code=400, detail="You should enter title")
    if description is None:
        raise HTTPException(status_code=400, detail="You should enter description")
    if time is None:
        raise HTTPException(status_code=400, detail="You should enter time")
    if status is None:
        raise HTTPException(status_code=400, detail="You should enter status")
    
    connection = sqlite3.connect('app/todo.db')
    cursor = connection.cursor()
    cursor.execute("INSERT INTO todo_list(id, title, description, time, status) VALUES (?, ?, ?, ?,?)",(id, title, description, time, status))
    tasks = []
    all_task = cursor.execute("SELECT * FROM todo_list")
    connection.commit()
    for task in all_task:
            tasks.append({"id": task[0], "title": task[1], "description": task[2], "time": task[3],"status":task[4]})

    return tasks

@app.delete("/del_task/{id}")
def delete_task(id:int=None):
    if id is None :
        raise HTTPException(status_code=400,detail="id not found")
    print(id)
    connection = sqlite3.connect('app/todo.db')
    cursor = connection.cursor()
    cursor.execute("DELETE FROM todo_list WHERE id=?",(id,))
    query = "SELECT * FROM todo_list"
    tasks = []
    all_task = cursor.execute(query)
    connection.commit()
    for task in all_task:
            tasks.append({"id": task[0], "title": task[1], "description": task[2], "time": task[3],"status":task[4]})

    return tasks

@app.put("/update_task/{id}")
def update_task(id:int,title:str = Form(None),description: str = Form(None),time:str = Form(None),status:int = Form(None)):
    if id is None:
        raise HTTPException(status_code=400, detail="You should enter id")
    if title is None:
        raise HTTPException(status_code=400, detail="You should enter title")
    if description is None:
        raise HTTPException(status_code=400, detail="You should enter description")
    if time is None:
        raise HTTPException(status_code=400, detail="You should enter time")
    if status is None:
        raise HTTPException(status_code=400, detail="You should enter status")
    connection = sqlite3.connect('app/todo.db')
    cursor = connection.cursor()
    cursor.execute("UPDATE todo_list SET title=?, description=?, time=?, status=? WHERE id=?",(title, description, time,status,id))
    query = "SELECT * FROM todo_list"
    tasks = []
    all_task = cursor.execute(query)
    connection.commit()
    for task in all_task:
            tasks.append({"id": task[0], "title": task[1], "description": task[2], "time": task[3],"status":task[4]})

    return tasks

    