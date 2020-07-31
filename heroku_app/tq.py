import requests


url = "https://tylerrobichaux-airbnb.herokuapp.com/"

request_pred = {"description": "Ugly, yet pretty in a weird way",
                "neighborhood": "Queens",
                "property_type": "Apartment",
                "room_type": "private room",
                "zipcode": "11105",
                "beds": "1",
                "number_of_reviews": "0"
                }

x = requests.post(url, data=request_pred)
print(x)
