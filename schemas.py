from marshmallow import Schema, fields 

# marshamallow schemas are used to validate incoming data, to check the data the client sends us


class PlainItemSchema(Schema):
    id = fields.Str(dump_only= True) 
    name = fields.Str(required = True)   
    price = fields.Float(required = True) 

class PlainStoreSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required = True)

class ItemUpdateSchema(Schema):
    name = fields.Str() 
    price = fields.Float() 

class StoreSchema(PlainStoreSchema):
    items = fields.List(fields.Nested(lambda: ItemSchema()), dump_only=True) 

class ItemSchema(PlainItemSchema):
    store_id = fields.Int(required=True, load_only= True) 
    store = fields.Nested(lambda: StoreSchema(), dump_only=True)  



