from os import listdir

from fastapi import FastAPI
from fastapi import HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

from .utils import WeatherTrends


api = FastAPI(title='Weather-Trends-API',version='v1.0')
api.mount(
    "/charts",
    StaticFiles(directory='charts'),
    name='charts'
)
util = WeatherTrends()

origins = ["*"]
api.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@api.get("/", tags=["Home"])
async def welcome():
    return {
        "message": "Welcome!"
    }


@api.get(
    "/api/v1/{city}",
    tags=["Cities"],
    description="Returns all data which are related by city name",
)
async def CityDetail(city: str):
    charts:list = listdir('charts/')
    filename:str = city.title() + ".png"

    if filename in charts:
        return {
            "file": f"charts/{filename}"
        }

    try:
        util.save(city.title())

    except:
        raise HTTPException(404)

    return {
        "file":f"charts/{filename}"
    }

