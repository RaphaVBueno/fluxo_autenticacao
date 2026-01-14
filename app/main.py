from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from jose import JWTError, jwt
import os
import bcrypt
from dotenv import load_dotenv
from .schemas import UserSchema

from .database import SessionLocal, UserTable, create_db
#configurar logica para expirar o token
load_dotenv()
create_db()
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/register")
async def register(user: UserSchema, db: Session = Depends(get_db)):
    email = user.email.lower()
    password = user.password
    
    user_exists = db.query(UserTable).filter(UserTable.email == email).first()
    if user_exists:
        raise HTTPException(status_code=400, detail="Email já cadastrado")
    
    password_bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password_bytes, salt)
    
    new_user = UserTable(email=email, password=hashed_password.decode('utf-8'))
    db.add(new_user)
    db.commit()
    
    return {"message": "Usuário cadastrado com sucesso!"}

@app.post("/login")
async def login(user_data: UserSchema, db: Session = Depends(get_db)):
    email = user_data.email.lower()
    password = user_data.password
    user = db.query(UserTable).filter(UserTable.email == email).first()
    
    if not user:
        raise HTTPException(status_code=401, detail="Email ou senha incorretos")

    password_bytes = password.encode('utf-8')
    hashed_bytes = user.password.encode('utf-8')
    
    if not bcrypt.checkpw(password_bytes, hashed_bytes):
        raise HTTPException(status_code=401, detail="Email ou senha incorretos")

    token = jwt.encode({"sub": email}, SECRET_KEY, algorithm=ALGORITHM)
    return {"access_token": token}

@app.get("/auth")
async def auth(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email = payload.get("sub")
        if email is None:
            raise HTTPException(status_code=401, detail="Token inválido")
        return {"message": f"Autenticado como {email}"}
    except JWTError:
        raise HTTPException(status_code=401, detail="Token inválido ou expirado")