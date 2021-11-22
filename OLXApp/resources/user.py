from flask import request
from flask_restful import Resource
from OLXApp.models.user import UserModel

from db import db

# for authentication purpose

class Users(Resource) :
    def get(self) :
        users = UserModel.query.all()
        for index in range(len(users)) :
            users[index] = users[index].get_JSON()
        return {"users" : users}
    def post(self) :
        user_data = request.get_json()
        user = UserModel(
            name = user_data['name'],
            gender = user_data['gender'],
            contact = user_data['contact'],
            email = user_data['email'],
        )
        # # saves password hash
        user.hash_password(user_data["password"])
        if user.is_user_exists() :
            return {"message" : "User Already Exists"}
        db.session.add(user)
        db.session.commit()
        return {"user" : user.get_JSON() ,"message" : "User Registered Successfully"}



class User(Resource) :
    def get(self, user_id) :
        user = UserModel.query.get(user_id)
        if not user :
            return {"message" : "No user Found"}
        return {"user" : user.get_JSON() , "message" : "success"} , 200

class AuthUser(Resource) :
    def post(self) :
        user_data = request.get_json()
        try :
            user = UserModel.query.filter_by(email=user_data["email"]).first()

            if user and user.verify_password(user_data["password"]) :
            
                token = user.generate_auth_token()
                return {"user" : user.get_JSON() , "token" : token ,"status" : "Success"}
            return {"message" : "Invalid Username or Password" , "status" : "failed"}
        except TypeError :
            return {"message" : "No Credentials"}
        

    def get(self) :
        data = request.get_json()
        try :
            token = data["token"]
            user = UserModel.verify_auth_token(token)
            if user :
                return {"user" : user.get_JSON() }
            return {"user" : "Invalid or Expired Token"}

        except TypeError :
            return {"message" : "No token Found"}