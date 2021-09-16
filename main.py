import databases
import sqlalchemy
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from sqlalchemy import ForeignKey
from starlette.requests import Request

metadata = sqlalchemy.MetaData()
Database_url = "postgresql://postgres:sports@localhost:5432/phonebook"

database = databases.Database(Database_url)
engine = sqlalchemy.create_engine(
    Database_url, connect_args={}
)

metadata.create_all(engine)

users = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.INTEGER, primary_key=True),
    sqlalchemy.Column("user_name", sqlalchemy.String),
    sqlalchemy.Column("email", sqlalchemy.String),
    sqlalchemy.Column("phone", sqlalchemy.String),
    sqlalchemy.Column("city_id", sqlalchemy.INTEGER, ForeignKey("cities.id"))
)

city = sqlalchemy.Table(
    "city",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.INTEGER, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String)
)


class User(BaseModel):
    id: int
    user_name: str
    email: str
    phone: str
    city_id: int


class City(BaseModel):
    id: int
    name: str


app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@app.post("/new_user/")
async def add_new_user(request: Request):
    request_data = await request.json()

    city_name = request_data.get('city')
    temp_city = await database.execute(city.select().where(city.c.name == city_name))

    if not temp_city:
        await database.execute(city.insert().values(name=city_name))

    city_id = await database.execute(city.select().where(city.c.name == city_name))

    query = users.insert().values(user_name=request_data.get("user_name"), email=request_data.get("email"),
                                  phone=request_data.get("phone"),
                                  city_id=city_id)
    id = await database.execute(query)
    return id


@app.get("/get_user/{id}", response_model=User)
async def get_user_by_id(id: int):
    query = users.select().where(users.c.id == id)
    print(query)
    return await database.fetch_one(query)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
