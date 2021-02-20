import requests
from datetime import datetime

USERNAME: str = "YOUR USERNAME"
TOKEN: str = "YOUR SELF-CREATED TOKEN"
GRAPH_ID: str = "YOUR GRAPH ID"
HEADER: dict = {
    "X-USER-TOKEN": TOKEN
}

today = datetime.now()

pixela_endpoint = "https://pixe.la/v1/users"
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

# Switch for the process
# 1: Create user
# 2: Create graph
# 3: Input data
# 4: Update data
# 5: Delete data
switch: int = int(input(f"""
######## Welcome to habit tracker ########
#                                        #
#  Your choices                          #
#  1: Create user                        #
#  2: Create graph                       #
#  3: Input data                         #
#  4: Update data                        #
#  5: Delete data                        #
#										 #
##########################################

What do you want to do? (Enter a number): 
"""))


user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "kuro"
}

if switch == 1:
    response = requests.post(url=pixela_endpoint, json=user_params)
    print(response.text)
elif switch == 2:
    response = requests.post(url=graph_endpoint, json=graph_config, headers=HEADER)
    print(response.text)
elif switch == 3:
    pixel_data = {
        "date": today.strftime("%Y%m%d"),
        "quantity": input("How many kilometers did you cycle today?: "),
    }
    response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=HEADER)
    print(response.text)
elif switch == 4:
    new_pixel_data = {
        "quantity": input("What do you want to update the value as?: ")
    }
    response = requests.put(url=update_endpoint, json=new_pixel_data, headers=HEADER)
    print(response.text)
elif switch == 5:
    response = requests.delete(url=delete_endpoint, headers=HEADER)
    print(response.text)
else:
    print("Error: You have entered a wrong choice.")
