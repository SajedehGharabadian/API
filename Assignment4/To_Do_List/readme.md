# To-Do List 

◻️Connect a sqlite database to an API

## How to run

```
uvicorn main:app --reload
```

## GET

◻️Read Database
```
http://127.0.0.1:8000/task
```
## POST

◻️Add a new data
```
http://127.0.0.1:8000/task
```
## DELETE

◻️Delete from from database
◻️You must enter the id of data
```
http://127.0.0.1:8000/del_task/{id}
```
## PUT

◻️Update data in database
◻️You must enter the id of data
```
http://127.0.0.1:8000/update_task/{id}
```
