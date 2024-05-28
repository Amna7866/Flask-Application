from flask import Flask 

app = Flask(__name__) 

stores = [ {

    "name": "My Store",
    "Items":[ {
        "name":"sofa", "price":"876$", 
        
    }

    ]
}

]
@app.get("/store") #endppoint
def get_stores():
    return {"stores":stores} 
