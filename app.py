import pickle
# from urllib import request

import numpy as np
from flask import Flask, render_template, request

app = Flask(__name__)


# prediction function
def ValuePredictor(to_predict_list):
    to_predict = np.array(to_predict_list).reshape(1, 25)
    loaded_model = pickle.load(open("finalized_model.sav", "rb"))
    result = loaded_model.predict(to_predict)
    return result[0]
@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('form.html')

@app.route('/result', methods=['POST'])
def result():
    if request.method == 'POST':
        to_predict_list = request.form.to_dict()
        to_predict_list = list(to_predict_list.values())
        to_predict_list = list(map(int, to_predict_list))
        result = ValuePredictor(to_predict_list)
        if int(result) == 1:
            prediction = 'The patient should be readmitted'
        else:
            prediction = 'The patient should be readmited'
        return render_template("result.html", prediction=prediction)


if __name__ == '__main__':
    app.run()
