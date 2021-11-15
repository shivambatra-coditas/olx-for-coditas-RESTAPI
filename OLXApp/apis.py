from flask_restful  import Api 
from OLXApp.resources.advertisement import Advertisements , Advertisement 
from OLXApp.resources.user import Users , User , AuthUser
from OLXApp import app
# api object
api = Api(app)

api.add_resource(Advertisements, '/ads')
api.add_resource(Advertisement, '/ad/<int:ad_id>')
api.add_resource(Users, '/users')
api.add_resource(User, '/user/<int:user_id>')
api.add_resource(AuthUser , '/auth')