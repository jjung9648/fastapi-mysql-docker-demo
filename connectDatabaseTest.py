from fastapi import FastAPI
from databases import Database

DATABASE_URL = "mysql+aiomysql://root@localhost/testdb"
database = Database(DATABASE_URL)

app = FastAPI()

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

@app.get("/db-status")
async def db_status():
    try:
        query = "SELECT 1"
        await database.execute(query=query)
        return {"status": "Connected to Database"}
    except Exception as e:
        return {"status": "Connection Failed", "detail": str(e)}
