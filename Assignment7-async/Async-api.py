import asyncio 
import requests
import dotenv
import os
import time
import json

dotenv = dotenv.load_dotenv()

rhyme_key = os.getenv("RHYME_API")


async def rhyme_finder(word):
    url = f"https://rhyming.ir/api/rhyme-finder?api={rhyme_key}&w={word}&sb=1&mfe=2&eq=1"
    print("******* started ******* ")
    response = requests.request("GET", url)
    data = json.loads(response.text)
    print(data)
    return data

def get_states():
    url = "https://iran-locations-api.vercel.app/api/v1/fa/states"
    response = requests.request("GET", url)
    data_states = json.loads(response.text)
    return data_states

def get_cities(state_id):
    url = f"https://iran-locations-api.vercel.app/api/v1/fa/cities?state_id={state_id}"
    response = requests.request("GET", url)
    data_cities = json.loads(response.text)
    cities_list = data_cities["cities"]
    return cities_list

def find_city(list_cities,city_name):
    for city in list_cities:
        if city["name"] == city_name:
            return city

def find_id(state_name,states_list):
    for state in states_list:
        if state["name"] == state_name:
            state_id = state["id"]
            print(state_id)
            return state_id

async def get_coordinates(state_name,city_name):
    list_states = get_states()
    state_id = find_id(state_name=state_name,states_list=list_states)

    list_cities = get_cities(state_id=state_id)
    city_data = find_city(list_cities,city_name)
    await asyncio.sleep(2)
    print("Latitude: ",city_data["latitude"])
    print("Longitude: ",city_data["longitude"])
    return city_data["latitude"] , city_data["longitude"]

async def main():
    await asyncio.gather(rhyme_finder("مادر"),get_coordinates("خراسان رضوی","مشهد"))


if __name__ == "__main__":
    start_time = time.perf_counter()
    asyncio.run(main())
    end_time = time.perf_counter()
    total_time = end_time - start_time
    print(f"Executed in {total_time} seconds")
 


        
