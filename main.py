from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
import httpx
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_APIKEY = os.getenv("SUPABASE_APIKEY")
SUPABASE_BEARER = os.getenv("SUPABASE_BEARER")

@app.post("/guardar_memoria")
async def guardar_memoria(request: Request):
    try:
        data = await request.json()
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{SUPABASE_URL}/rest/v1/memoriagpt",
                headers={
                    "apikey": SUPABASE_APIKEY,
                    "Authorization": f"Bearer {SUPABASE_BEARER}",
                    "Content-Type": "application/json"
                },
                json=data
            )
        return JSONResponse(status_code=response.status_code, content=response.json())
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
