import argparse
import requests
import cv2
import matplotlib.pyplot as plt
import os 
import dotenv

parser = argparse.ArgumentParser()
dotenv = dotenv.load_dotenv()

parser.add_argument('--image_name',type=str)
opt = parser.parse_args()

ILLUSIONDIFFUSION_API = os.getenv("ILLUSIONDIFFUSION_API")
PLANT_API = os.getenv("PLANT_API")


url = 'https://fal.run/fal-ai/illusion-diffusion'
headers = {
    "Authorization" : ILLUSIONDIFFUSION_API,
    "Content-Type": "application/json"
}
payload = {
    "image_url": "https://storage.googleapis.com/falserverless/illusion-examples/checkers.png",
    "prompt": f"(masterpiece:1.4), (best quality), (detailed),landscape,{opt.image_name}",
    "Negative Prompt":"(worst quality, poor details:1.4), lowres, (artist name, signature, watermark:1.4), bad-artist-anime, bad_prompt_version2, bad-hands-5, ng_deepnegative_v1_75t"
}
url_plant = "https://my-api.plantnet.org/v2/identify/all"

headers_plant = {}

payload_plant = {
    "api-key":PLANT_API
}

try:
    response = requests.post(url,headers=headers,json=payload)
    data = response.json()
    image_link = data['image']['url']
    # print(response.status_code)
    # print(image_link)
    r = requests.get(image_link, allow_redirects=True)
    open('/content/images/pic.png', 'wb').write(r.content)
    files = {
    "images":open('/content/images/pic.png',"rb")
    }
    response_plant = requests.post(url_plant, headers=headers_plant,params=payload_plant,files=files)
    flower_data = response_plant.json()
    #print(response_plant.status_code)
    print("Name of flower is:",flower_data['results'][0]['species']['scientificNameWithoutAuthor'])
    image = cv2.imread('/content/images/pic.png')
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    plt.imshow(image)
    plt.show()
except requests.exceptions.HTTPError as errh:
    print ("Http Error:",errh)
except requests.exceptions.ConnectionError as errc:
    print ("Error Connecting:",errc)