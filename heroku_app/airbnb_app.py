from flask import Flask
import category_encoders as ce
import joblib
import pandas as pd
from flask import Blueprint
from flask import request
import json
import tensorflow as tf

app1 = Blueprint('app1', __name__)

encode = joblib.load('new_categorical_encoder.pkl')
scale = joblib.load('new_scaler.pkl')
nn = tf.keras.models.load_model('my_model.h5')


def create_app():
    app = Flask(__name__)

    @app.route('/', methods=['POST'])
    def root():
        var = request.get_json()
        var = pd.DataFrame.from_dict(var, orient='index').T
        var[['borough', 'property_type', 'room_type', 'cancellation_policy']] = encode.transform(
            var[['borough', 'property_type', 'room_type', 'cancellation_policy']])
        var = scale.transform(var)
        var = pd.DataFrame(var)
        p = nn.predict(var)
        return str({p})
    return app
#
#sdthtgaesgasdgr