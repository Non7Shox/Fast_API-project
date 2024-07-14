from fastapi import APIRouter, status
from fastapi.exceptions import HTTPException
from models import User
import schemas
from database import session, engine
from utils.hashing_password import hash_password
from utils.jwt_tokens import create_access_token

router = APIRouter(
    prefix="/auth",
)

session = session(bind=engine)


@router.post('/register', status_code=status.HTTP_201_CREATED, response_model=schemas.UserOut)
async def register_user(user: schemas.RegisterUser):
    db_email = session.query(User).filter(User.email == user.email).first()
    if db_email is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email does not exist")

    db_username = session.query(User).filter(User.username == user.username).first()
    if db_username is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Username does not exist")

    hashed_password = await hash_password(user.password)
    new_user = User(username=user.username, email=user.email, password=hashed_password, first_name=user.first_name, last_name=user.last_name)

    session.add(new_user)
    session.commit()
    session.refresh(new_user)

    return new_user


@router.post('/login', status_code=status.HTTP_200_OK)
async def login_user(user: schemas.LoginUser):
    hashed_password = await hash_password(user.password)
    db_user = session.query(User).filter(User.username == user.username, User.password == hashed_password).first()

    if db_user is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email does not exist")

    response = {
        "access_token": await create_access_token(data={"username": user.username}),
    }
    return response


@router.delete('/delete', status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(user: schemas.DeleteUser):
    db_user = session.query(User).filter(User.username == user.username).first()
    if db_user is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Username does not exist")

    session.delete(db_user)
    session.commit()
    session.refresh(db_user)

    return {"message": "User deleted"}
