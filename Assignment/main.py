import csv
from fastapi import FastAPI, Query, HTTPException
app=FastAPI()
@app.get('/students')
def get_students(page: int = Query(1, gt=0), page_size: int = Query(10, gt=0)):
    try:
        start_index = (page - 1) * page_size
        end_index = start_index + page_size

        with open('students.csv', 'r') as file:
            reader = csv.DictReader(file)
            students = list(reader)

        paginated_students = students[start_index:end_index]

        return paginated_students
    except Exception as e:
        raise HTTPException(status_code=500,detail=str(e))
