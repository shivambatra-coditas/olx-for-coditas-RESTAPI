from OLXApp import app
from db import db

db.init_app(app)
if __name__ == '__main__' :
    
    app.run(port=9000 , debug=True)