from flask import Flask
import category_encoders as ce
import joblib
import pandas as pd
from flask import Blueprint
from flask import request
import json
app1 = Blueprint('app1', __name__)

encode = joblib.load("heroku_app/encoder1.pkl")
nlp = joblib.load("heroku_app/baseline1.pkl")
rfr = joblib.load("heroku_app/baseline2.pkl")

request_pred = {"description": "Ugly, yet pretty in a weird way",
                "neighborhood": "Queens",
                "property_type": "Apartment",
                "room_type": "private room",
                "zipcode": "11105",
                "beds": "1",
                "number_of_reviews": "0"
                }

var = request.get_json()
text = var["description"]
prediction = nlp.predict([text])
var.update(nlp_pred=prediction)
del var['description']
var = pd.DataFrame.from_dict(var, orient='index').T
encoder = ce.OrdinalEncoder()
var[['neighborhood', 'property_type', 'room_type']] = encoder.fit_transform(
    var[['neighborhood', 'property_type', 'room_type']])
price = rfr.predict(var)
return {price}  # .json()
