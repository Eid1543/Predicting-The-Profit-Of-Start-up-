from flask import Flask, render_template, request
import pickle
import numpy as np

model = pickle.load(open('model.pkl', 'rb'))

app = Flask(__name__ , template_folder='template')



@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    data1 = request.form['a']
    data2 = request.form['b']
    data3 = request.form['c']
    data4 = request.form['d']
    
    
    if data1 == 'New York':
        x , y , z = 0.0 , 0.0 , 1.0
    elif data1 == 'California':
          x , y , z = 1.0 , 0.0 , 0.0
    else :
         x , y , z = 0.0 , 1.0 , 0.0
         
    
    arr = np.array([[x , y , z , data2, data3, data4]])
    pred = model.predict(arr)


    return render_template('index.html', prediction_text='profit should be $ {}'.format(pred))



if __name__ == "__main__":
    app.run(debug=True)
    
    
    
    