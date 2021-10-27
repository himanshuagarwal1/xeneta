from flask import Flask, render_template, request
import json
import requests



app = Flask(__name__)



listen = ['default']

def Get_API(z, y):   
    url1 ="https://685rp9jkj1.execute-api.eu-west-1.amazonaws.com/prod/rates?origin="+z+"&destination="+y
    x = requests.get( url =url1, headers={"x-api-key":"OFn3YmyhnH4GS4lGq5Vs634BcAeHxufXax7kWuD4"})   
    gi = x.content   
    gi = gi.decode('utf-8')
    y1 = json.loads(gi)
    
    dic= {"NOOSL": "Oslo","CNSGH": "Shanghai" ,"CNSTG": "Shantou","NLRTM": "Rotterdam","DEHAM": "Hamburg","GBFXT": "Felixstowe","USNYC": "New York"}
    z = dic[z]
    y = dic[y]
    return y1,z,y


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method =="POST":
        con = request.form.to_dict()
        z = con['select1']
        y = con['select2']    
        
        y1 ,z,y = Get_API(z, y)
        z = "Showing results for ports from "+z+" to " +y
        
        
        
        if type(y1) == list and len(y1) > 2:
            return render_template("dashboard.html", fi = y1, z =z)
        
        else:
            z1 ="Data not avaliable for these ports please select some different ports" 
            return render_template("index.html", x=z1, z=z)
            
            
    else:
        
        return render_template("index.html")


if __name__ == "__main__":

    app.run(debug=True)

