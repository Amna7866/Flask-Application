from flask import Flask, request  

app = Flask(__name__) 

stores = [ {

    "name": "My Store",
    "items":[ {   
        "name":"sofa", "price":"876$", 
        
    }   

    ]
}

]
# to create store
@app.get("/store") #endppoint
def get_stores():
    return {"stores":stores} 

@app.post("/store") 
def create_stores():
    request_data = request.get_json() 
    new_store = {"name":request_data["name"], "items":[]} 
    stores.append(new_store) 
    return new_store, 201 
#200 is the defualt status code that means everything went well 
# 201 is the status code that means i accept the data for the store.


# to create items in each store
@app.post("/store/<string:name>/item") 
def create_item(name):
    request_data = request.get_json() 
    for store in stores:
        if store["name"] == name:
            new_item = {"name":request_data["name"],"price":request_data["price"]} 
            store["items"].append(new_item) 
            return new_item,201
    return{"message": "store not found"}, 404  

# to get specific item from the store and its item 
@app.get("/store/<string:name>") 
def get_store(name): 
    for store in stores:
        if store["name"] == name:
            return store 
    return{"message": "store not found"}, 404

@app.get("/store/<string:name>/item") 
def get_item_in_store(name): 
    for store in stores:
        if store["name"] == name:
            return {"items":store["items"]} 
    return{"message": "store not found"}, 404



