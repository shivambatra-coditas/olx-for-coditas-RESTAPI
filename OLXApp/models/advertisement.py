from db import db
from datetime import datetime

class AdvertisementModel(db.Model) :
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(70) , unique=False, nullable=False)
    category = db.Column(db.String(70) , unique=False, nullable=False)
    description = db.Column(db.Text , unique=False, nullable=False)
    price = db.Column(db.Float , unique=False , nullable=False)
    user_id = db.Column(db.Integer , db.ForeignKey('user_model.id'))
    # for image later
    date_added = db.Column(db.DateTime , nullable=False , default=datetime.utcnow )

    def get_JSON(self) :
        return {"id" : self.id , "name" : self.name , "category" : self.category , "description" : self.description , "price" : self.price}