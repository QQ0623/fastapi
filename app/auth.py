from jose import JWTError, jwt  
from datetime import datetime, timedelta
from fastapi import APIRouter, HTTPException, status

SECERT_KEY = "your_secret_key"
ALGOTITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

#Create JWT token
def create_access_token(
        data:dict,
        expires_delta: timedelta = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)):
    to_encode = data.copy()
    expire = datetime.utcnow() + expire_delta
    to_encode.update({"exp" : expire})
    encode_jwt = jwt.encode(to_encode, SECERT_KEY, algorithm=ALGOTITHM)
    return encode_jwt
# Verify the JWT
def verify_token(token:str):
        try:
            payload = jwt.decode(token, SECERT_KEY, algorithm=[ALGOTITHM])
        except:
              return None
router = APIRouter()

#Login route to issue JWT
@router.post("/token")
async def login_for_access_token(user:User):
      #todo:check user if exist and vaildate password
      access_token = create_access_token(data={"sub":username})
      return {"access_token": access_token, "token_type":"bearer"}
def git_current_user(token:str):
      user = verify_token(token)
      if user is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invaild")
      return user
