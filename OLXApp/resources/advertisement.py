from flask import request
from flask_restful import Resource
from OLXApp.models.advertisement import AdvertisementModel


class Advertisements(Resource) :
    
    def get(self) :
        advertisements = AdvertisementModel.query.all()
        for i in range(len(advertisements)) :
            advertisements[i] = advertisements[i].get_JSON()
        return { "advertisements" : advertisements } , 200
    def post(self) :
        data = request.get_json()
        if data :
            print(data)
        else :
            print("Got nothing")
        return { "message" : "done"}

        
        # ad = AdvertisementModel(
        #     name=data['name'],
        #     category=data['category'],
        #     price=data['price'],
        #     description=data['description'],
            
        # )
        # db.session.add(ad)
        # db.session.commit()

class Advertisement(Resource) :
    def get(self, ad_id) :
        advertisement = AdvertisementModel.query.get(ad_id)
        if not advertisement :
            return {"message" : "Advertisement not found"} , 404
        return {"Advertisement" : advertisement.get_JSON()}