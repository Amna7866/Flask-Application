import uuid 
from flask import request 
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from schemas import ItemSchema, ItemUpdateSchema  

blp = Blueprint("Items", __name__, description= "operation on items")  

@blp.route("/item/<string:item_id>")
class Store(MethodView):
    @blp.response(200, ItemSchema)
    def get(self, item_id):
        try:
            return items[item_id] 
        except KeyError:
            abort (404, message = "item not found.") 
    
    def delete(self, item_id):
        try:
            del items[item_id]   
            return {"message":"item deleted"}  
        except KeyError:
            abort (404, message = "item not found.")  

    @blp.arguments(ItemUpdateSchema)
    @blp.response(200, ItemSchema) 
    def put(self, item_data, item_id):
        try:
            item = items[item_id] 
            item |= item_data #to update the item, to merge items.
            return item, 200
        except KeyError:
            abort(404, message = "Item not found.") 


@blp.route("/item") 
class ItemList(MethodView):
    @blp.response(200, ItemSchema(many=True)) 
    def get(self):
        return items.values() 
    
    @blp.arguments(ItemSchema)  
    @blp.response(200, ItemSchema) 
    def post(self, item_data): #this second paramater will contain json which is the validated fields that schema requsted. 
        # item_data = request.get_json() not needed anymore 
        for item in items.values():
            if (
            item_data["name"] == item["name"] 
            and item_data["store_id"] == item["store_id"] 
        ):
                abort (400, message = f"item already exists.") 

    
        item_id =  uuid.uuid4().hex 
        item =  { **item_data, "id":item_id}
        items[item_id] = item
        return item, 201  