from fastapi import FastAPI, APIRouter, HTTPException, status
from fastapi.responses import JSONResponse
from requests_oauthlib import OAuth1
from fastapi.encoders import jsonable_encoder
import requests
import json
from dotenv import load_dotenv
import os

load_dotenv()

X_URL = os.getenv("X_BASE_URL")
QUOTE_URL = os.getenv("RANDOM_QUOTE_URL")
X_API_KEY = os.getenv("X_API_KEY")
X_ACCESS_TOKEN = os.getenv("X_ACCESS_TOKEN")

app = FastAPI()
router = APIRouter()


@router.post("/")
def post_tweet():
    try:
        #GET request to quotable.io
        quote_response = requests.request(
            "GET",
            QUOTE_URL,
        )
        quote_content = quote_response.json()

        payload = json.dumps({"text": quote_content.get("content", "")})

        headers = {
            "Content-Type": "application/json",
            "Authorization": f'OAuth oauth_consumer_key="{X_API_KEY}",oauth_token="{X_ACCESS_TOKEN}",oauth_signature_method="HMAC-SHA1",oauth_timestamp="1698450376",oauth_nonce="IKyeonwsItU",oauth_version="1.0",oauth_signature="feWp1pD%2BCeuHS%2BiYnBeIAR9dDTw%3D"',
            "Cookie": 'guest_id=v1%3A169844508887984404; guest_id_ads=v1%3A169844508887984404; guest_id_marketing=v1%3A169844508887984404; personalization_id="v1_oWzgkOxyMejRSts5xQtdsw=="',
        }
        print(X_URL,X_API_KEY,X_ACCESS_TOKEN)
        #POST request to Twitter X
        response = requests.request("POST", X_URL, headers=headers, data=payload)

        print(response.text)
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={
                "res": jsonable_encoder(response.json()),
            },
        )
    except Exception as e:
        print(e)
        raise HTTPException(status_code=400, detail="Something went wrong :(")


app.include_router(router, prefix="/tweet", tags=["tweets"])
