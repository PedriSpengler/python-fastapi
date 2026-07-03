from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import database
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    database.create_table()
    yield

app = FastAPI(
    lifespan=lifespan,
    title="API CRUD Python and PostgreSQL",
    description="API to CRUD with FastAPI and PostgreSQL",
    version="1.0.0"
)

# DEFINING THE USER SCHEMA FOR REQUEST BODY VALIDATION
class UserSchema(BaseModel):
    username: str
    email: str

# API ENDPOINTS
@app.post("/users/")
def create_user(user: UserSchema):
    try:
        user_id = database.insert_user(user.username, user.email)
        return {"message": "Usuário criado com sucesso", "id": user_id}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/users/")
def get_users():
    try:
        users = database.read_users()
        return {"users": users}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
class UpdateEmailSchema(BaseModel):
    new_email: str

@app.put("/users/{username}")
def update_user(username: str, data: UpdateEmailSchema):
    try:
        rows_affected = database.update_user_email(username, data.new_email)
        if rows_affected == 0:
            raise HTTPException(status_code=404, detail="Usuário não encontrado")
        return {"message": f"Email do usuário '{username}' atualizado com sucesso"}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.delete("/users/{username}")
def remove_user(username: str):
    try:
        rows_affected = database.delete_user(username)
        if rows_affected == 0:
            raise HTTPException(status_code=404, detail="Usuário não encontrado")
        return {"message": f"Usuário '{username}' deletado com sucesso"}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))