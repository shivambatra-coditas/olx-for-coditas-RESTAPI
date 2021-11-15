from db import db
from OLXApp import app , bcrypt
from itsdangerous import (
    TimedJSONWebSignatureSerializer as Serializer,
    BadSignature,
    SignatureExpired
) 



class UserModel(db.Model) :
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80) , unique=False , nullable=False)
    contact = db.Column(db.String(10), unique=False, nullable=False)
    gender = db.Column(db.String(10) , nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    advertisements = db.relationship("AdvertisementModel" , backref='user' , lazy=True)
    #profile_image = something
    password = db.Column(db.String(100) , nullable=False)
    
    def get_JSON(self) :
        return {"id" : self.id , "name" : self.name , "contact" : self.contact , "gender" : self.gender , "email" : self.email, "password" : str(self.password) }

    def get_advertisements(self) :
        return {"advertisements" : self.advertisements}

    def hash_password(self , password) :
        self.password = bcrypt.generate_password_hash(password)

    def verify_password(self , password) :
        return bcrypt.check_password_hash(self.password , password)

    # for token based authentication
    def generate_auth_token(self, expiration=60) :
        s = Serializer(app.config["SECRET_KEY"] , expires_in=expiration)
        return s.dumps({"id" : self.id}).decode("utf-8")

    @classmethod
    def verify_auth_token(cls, token) :
        s = Serializer(app.config["SECRET_KEY"])
        try :
            data = s.loads(token)
        except SignatureExpired :
            return None
        except BadSignature :
            return None
        
        user = cls.query.get(data["id"])
        return user
