from __future__ import division
from flask import *
from math import *
import serial
app = Flask(__name__,template_folder="D:\\python")  
app.secret_key = "abc"
ser=serial.Serial('COM3',9600,timeout=1)
data=ser.readline()
import geocoder
g=geocoder.ip('me')
def euclidean(x,y,x1,y1):
    return sqrt((x-x1)*(x-x1)+(y-y1)*(y-y1))*1000
@app.route('/after',methods = ["GET","POST"])
def ind():  
    return render_template('index.html')  
@app.route('/index',methods = ["GET","POST"])
def home():  
    error = None;  
    if request.method == "POST":
        print('akshay;')
        if request.form['val'] == '':  
            error = "invalid name"  
        else:
            import pyttsx3
            engine = pyttsx3.init()
            engine.say(request.form['val']+", don't worry. We will rescue you. Currently your gas status is fine. Once detected we will send rescue team.")
            engine.runAndWait()
            flash(request.form['val'])
            flash(data)
            flash("you are successfuly sent rescued")
            flash("You are at "+str(g.latlng))
            flash("We are "+ str(euclidean(g.latlng[0],g.latlng[1],22.5436,88.2341))+" Km far from you only")
            return redirect(url_for('ind'))  
    return render_template('page.html',error=error) 
  
  
      
if __name__ == '__main__':  
    app.run(host="localhost",debug = False)  
