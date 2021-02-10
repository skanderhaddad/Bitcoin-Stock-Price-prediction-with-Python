import os
from flask import Flask, request, render_template
from deployment.predict import Predict


PEOPLE_FOLDER = os.path.join('static', 'pics')

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = PEOPLE_FOLDER
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def prediction():

    variable_form=[x for x in request.form.values()]
    type = variable_form[0]
    days = int(variable_form[1])
    price,graph=Predict(type, days)
    graph.savefig('static/pics/curve.png')
    pic = os.path.join(app.config['UPLOAD_FOLDER'], 'curve.png')

    return render_template('index.html', prediction_text=price, figure=pic)


if __name__ == "__main__":
    app.run(debug=True)