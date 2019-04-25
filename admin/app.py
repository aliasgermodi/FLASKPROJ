from flask import Flask
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from models import db, User, Role


app = Flask(__name__)

# set optional bootswatch theme
app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'

admin = Admin(app, name='microblog', template_mode='bootstrap3')
admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Post, db.session))	
# Add administrative views here

app.run()