from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# sample in memory database
users = [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]

# Data Model for user
class User(BaseModel):
	id: int
	name: str

# Get all users
@app.get("/users")
def get_users():
	return users 

# Add a new user
@app.post("/users")
def add_user(user: User):
	users.append(user.dict())
	return user 