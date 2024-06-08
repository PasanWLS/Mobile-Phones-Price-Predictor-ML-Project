from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

def prediction(lst):
    filename= 'model/predictor.pickle'
    with open(filename,'rb') as file:
        model = pickle.load(file)
    pred_value = model.predict([lst])
    return pred_value


@app.route('/', methods=['POST','GET'])
def index():
    pred = 0
    if request.method == 'POST':
        brand = request.form['brand']
        storage = request.form['storage']
        ram = request.form['ram']
        camera = request.form['camera']
        screensize = request.form['screensize']
        battery = request.form['battery']
        
        feature_list = []
        
        feature_list.append(int(storage))
        feature_list.append(int(ram))
        feature_list.append(float(screensize))
        feature_list.append(int(battery))
        
        brand_list = ['apple','huawei','motorola','nokia','oneplus','oppo','realme','samsung','vivo','xiaomi','other']
        camera_list = ['12mp','13mp','48mp','50mp','64mp','other']
        
        for item in brand_list:
            if item == brand:
                feature_list.append(1)
            else:
                feature_list.append(0)
                
        for item in camera_list:
            if item == camera:
                feature_list.append(1)
            else:
                feature_list.append(0)
                
        #--------- without using for loop ---------
        #def traverse(lst, value):
            #for item in lst:
                #if item == value:
                    #feature_list.append(1)
               # else:
                    #feature_list.append(0)
        
        #traverse(brand_list, brand)
        #traverse(camera_list, camera)
        # --------------------------------------
        
        pred = prediction(feature_list)*304.70
        pred = np.round(pred[0])
        
        
    return render_template("index.html", pred = pred)

if __name__ == '__main__':
    app.run(debug=True)
    
    