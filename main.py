from models import person
from typing import Union
from fastapi import FastAPI, Depends
from sec import get_current_username
from config import create_db_connection


app = FastAPI()

@app.get("/api/person")
async def Featch_All_Person(username: str = Depends(get_current_username)):
        conn = create_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM dbo.person')
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        people_list=[]
    
        for row in rows:
            person_dict=person(id=row.id,name=row.name,family=row.family)
            people_list.append(person_dict)

        return people_list


@app.post("/api/person")
async def Register_Person(new_person: person, username: str = Depends(get_current_username)):
    # Create connection
    conn = create_db_connection()
    cursor = conn.cursor()
    insert_query = "INSERT INTO [dbo].[person](name,family) VALUES(?, ?)"
    values_to_insert = (new_person.name, new_person.family)
    cursor.execute(insert_query, values_to_insert)
    conn.commit()
    cursor.close()
    conn.close()


    # Reopen connection and cursor to fetch the new person's ID
    conn = create_db_connection()
    cursor = conn.cursor()
    query = "SELECT TOP 1 [id] FROM [dbo].[person] ORDER BY id DESC"
    cursor.execute(query)
    newpersonid = cursor.fetchone()  # Fetch a single result
    cursor.close()
    conn.close()

    return {"id": newpersonid[0]}  # Fetch the ID value from the tuple
