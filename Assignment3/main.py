from typing import Union
from fastapi import FastAPI,HTTPException,status
import cv2
import numpy as np
import io
from fastapi.responses import StreamingResponse,FileResponse
import os


information_of_plants = {
    "sun":{
        "radius":696340000,
        "age":"4.5 billion years",
        "didyouknow":"a hot glowing ball of hydrogen and helium and it is our solar systems only star"
    },
    "mercury":{
        "radius":2439700,
        "age":"4.503 billion years",
        "distance_from_sun":46332000000,
        "didyouknow":" It makes one trip around the Sun once every 87.969 days"
    },
    "venus":{
        "radius":6051800,
        "age":"4.503 billion years",
        "distance_from_sun":108940000000,
        "didyouknow":"Venus is the only planet in the Solar System that has a day longer than a year, the year length of Venus is 225 Earth days"
    },
    "earth":{
        "radius":6371000,
        "age":"4.543 billion years",
        "distance_from_sun":148990000000,
        "didyouknow":"Earth also turns around in space, so that different parts face the Sun at different times",
        "moon":{
            "count":1,
            "the moon":{
                "radius":1740000,
                "distancefromplanet":384400000
            }
        }
    },
    "mars":{
        "radius":3389500,
        "age":"4.56 billion years",
        "distance_from_sun":210420000000,
        "didyouknow":"Mars is a terrestrial planet with caps of water and carbon dioxide.It has the largest volcano in the Solar System, and some very large impact craters" ,
        "moon":{
            "count":2,
            "phobos":{
                "radius":11267,
                "didyouknow":"Phobos is the larger of Mars two moons,It orbits Mars three times a day"
            },
            "deimos":{
                "radius":6200,
                "didyouknow":"It takes 30.3 hours to orbit Mars"
            }
        }
    },
    "jupiter":{
        "radius":69911000,
        "age":"4.603 billion years",
        "distance_from_sun":747940000000,
        "didyouknow":"Jupiter is a gas giant because it is so large, and made mostly of gas,Jupiter was discovered by Galileo Galilei in 1610 with a small telescope",
        "moon":{
            "count":95,
            "didyouknow":"Jupiter has 95 moons that have been officially recognized by the International Astronomical Union"
        }
    },
    "saturn":{
        "radius":58232000,
        "age":"4.503 billion years",
        "distance_from_sun":1452100000000,
        "didyouknow":"Inside Saturn is probably a core of iron, nickel, silicon and oxygen compounds, surrounded by a deep layer of metallic hydrogen, then a layer of liquid hydrogen and liquid helium and finally, an outer gaseous layer.",
        "moon":{
            "count":146,
            "didyouknow":"The moons range in size from larger than the planet Mercury, the giant moon Titan, to as small as a sports arena"
        }
    },
    "uranus":{
        "radius":25362000,
        "age":"4.503 billion years",
        "distance_from_sun":2931100000,
        "didyouknow":"The planet is made of ice, gases and liquid metal. Its atmosphere contains hydrogen (1H), helium (2He) and methane",
        "moon":{
            "count":28,
            "didyouknow":"The moons are sometimes called the literary moons because they are named for Shakespearean characters, along with a couple of the moons being named for characters from the works of Alexander Pope."
        }
    },
    "neptune":{
        "radius":24622100,
        "age":"4.503 billion years",
        "distance_from_sun":4472200000000,
        "didyouknow":"Neptune's mass is 17 times Earth's mass and a little bit more than Uranus' mass. Neptune is denser and smaller than Uranus",
        "moon":{
            "count":16,
            "didyouknow":"using telescopes and spacecraft have since discovered more moons bringing the total to 16 moons orbiting the distant world."
        }
    }
}

app = FastAPI()


@app.get("/")
def read_root():
    mes = 'Hi! Welcome to my API.The Solar System API provides information for thousands of all solar system planets and their moons.'
    return mes

@app.get('/plants') 
def inf_plants():
    return information_of_plants

@app.get('/plants/{plant_name}')
def inf_plant_name(plant_name:str):
    if plant_name in information_of_plants:
        return information_of_plants[plant_name]
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Plant not found,please try again")
    
@app.get("/plants/{plant_name}/image")
def image_plants(plant_name:str):
    if plant_name in information_of_plants:
        image = cv2.imread('images/'+plant_name+'.jpg')
        _, encode_img= cv2.imencode('.jpg',image)
        return StreamingResponse(io.BytesIO(encode_img.tobytes()),media_type='image/jpg')
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST
                             ,detail="Plant not found,please try again")
