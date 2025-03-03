from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from app.database import get_connection

app = FastAPI()

# Pydantic model for request validation
class User(BaseModel):
    name: str

# Dependency to get a database connection
def get_db_conn():
    conn = get_connection()
    try:
        yield conn
    finally:
        conn.close()

@app.get("/user")
def get_users(db=Depends(get_db_conn)):
    with db.cursor() as cur:
        cur.execute("SELECT * FROM user_info.users;")
        users = cur.fetchall()
    return users

@app.post("/user")
def add_user(user: User, db=Depends(get_db_conn)):
    try:
        with db.cursor() as cur:
            # Insert the new user and return id and name
            cur.execute(
                "INSERT INTO user_info.users (name) VALUES (%s) RETURNING id, name;",
                (user.name,)
            )
            new_user = cur.fetchone()  # Fetch the newly created user
            db.commit()

        # Return only the user data
        if new_user:
            return {"id": new_user["id"], "name": new_user["name"]}
        else:
            raise HTTPException(status_code=500, detail="Failed to retrieve user from the database")
    except Exception as e:
        print("Error while inserting user:", e)
        raise HTTPException(status_code=500, detail="Database error")
