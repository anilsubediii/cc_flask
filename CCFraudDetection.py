
from flask import Flask, render_template, request
import pickle


app = Flask(__name__,template_folder='templates')



@app.route('/',methods=['POST','GET'])
def predict():
    result=''
   
    if request.method=='POST':
        pickled_model=pickle.load(open('./model.pkl','rb'))
        Time=request.form['Time']
        Amount=request.form['Amount']

        print('test test ')

        result_arr=pickled_model.predict([[float(Time),-1.3598071336738,-0.0727811733098497,2.53634673796914,1.37815522427443,-0.338320769942518,0.462387777762292,0.239598554061257,0.0986979012610507,0.363786969611213,0.0907941719789316,-0.551599533260813,-0.617800855762348,-0.991389847235408,-0.311169353699879,1.46817697209427,-0.470400525259478,0.207971241929242,0.0257905801985591,0.403992960255733,0.251412098239705,-0.018306777944153,0.277837575558899,-0.110473910188767,0.0669280749146731,0.128539358273528,-0.189114843888824,0.133558376740387,-0.0210530534538215,float(Amount)]])

        if result_arr[0]==1:
            result= "fraud"
        else:
            result="legit"
        return render_template('index1.html',result=result)
    else:
        return render_template('index1.html')

if __name__ == '__main__':
    app.run(debug=True)
    