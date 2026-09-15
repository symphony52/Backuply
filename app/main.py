from fastapi import FastAPI
from app.config import get_user_settings
app = FastAPI()

settings = get_user_settings()

@app.get("/")
async def root():
   return {"message": "Hello World"}

@app.get("/status")
async def status(): 
   return {
   "app": "MishaCloud",
   "device_id": settings["device_id"],
   "sync_folder": settings["sync_folder"],
   "listen_host": settings["listen_host"],
   "listen_port": settings["listen_port"],
   "peer_url": settings["peer_url"],
   "database_path": settings["database_path"],
   }