from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import jwt
from gateway_service.main import verify_token
app = FastAPI()
security = HTTPBearer()

SECRET_KEY = "mysecret"

def verify_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return payload
    except:
        raise HTTPException(status_code=401, details = "Invalid User")

@app.get("/")
def health():
    return {"status": "gateway running"}

@app.get("/secure")
def secure_endpoint(user=Depends(verify_token)):
    return {"message":"Authorized","user":user}