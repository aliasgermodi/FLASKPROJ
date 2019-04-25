from flask import Flask, render_template, render_template, redirect, url_for, request,g, session
import pymongo
import os
import flask
from bson.objectid import ObjectId
from flask import Flask
import flask_admin as admin
from wtforms import form, fields
from flask_admin.form import Select2Widget
from flask_admin.contrib.pymongo import ModelView, filters
from flask_admin.model.fields import InlineFormField, InlineFieldList

# Create application
app = Flask(__name__)

# Create dummy secrey key so we can use sessions
app.secret_key = os.urandom(24)

# Create models
conn = pymongo.Connection()
db = conn.test

#session

@app.route('/', methods=['GET', 'POST'])
def sess():

    error = None
      if request.method == 'POST':
        session.pop('user',None)
        if request.form['username'] =='admin' or request.form['password'] =='admin':
            session['user'] = request.form['username']
            return redirect(url_for('index'))

    return render_template('login.html', error=error)

@app.route('/protected')
def protected():
    if g.user:
        return redirect(url_for('index'))

    return render_template('login.html')    


@app.before_request
def before_request():
    g.user = None
    if 'user' in session:
        g.user = session['user']

@app.route('/getsession')
def getsession():
    if 'user' in session:
        return session['user']

    return 'User not logged in'

@app.route('/dropsession', methods = ['GET'])
def dropsession():
    session.pop('user', None)
    return redirect(url_for('sess'))

# User admin
class InnerForm(form.Form):
    name = fields.StringField('Name')
    test = fields.StringField('Test')


class UserForm(form.Form):
    name = fields.StringField('Name')
    email = fields.StringField('Email')
    password = fields.StringField('Password')

    # Inner form
    inner = InlineFormField(InnerForm)

    # Form list
    form_list = InlineFieldList(InlineFormField(InnerForm))


class UserView(ModelView):
    column_list = ('name', 'email', 'password')
    column_sortable_list = ('name', 'email', 'password')

    form = UserForm

# Project admin
class ProjectForm(form.Form):
    name = fields.StringField('Name')
    test = fields.StringField('Test')


class User_ProjectForm(form.Form):
    name = fields.StringField('Name')
    email = fields.StringField('Email')
    password = fields.StringField('Password')

    # Inner form
    inner = InlineFormField(ProjectForm)

    # Form list
    form_list = InlineFieldList(InlineFormField(ProjectForm))


class proj(ModelView):
    column_list = ('name', 'email', 'password')
    column_sortable_list = ('name', 'email', 'password')

    form = User_ProjectForm

# Country admin
class CountryForm(form.Form):
    name = fields.StringField('Name')
    test = fields.StringField('Test')


class User_CountryForm(form.Form):
    name = fields.StringField('Name')
    email = fields.StringField('Email')
    password = fields.StringField('Password')

    # Inner form
    inner = InlineFormField(CountryForm)

    # Form list
    form_list = InlineFieldList(InlineFormField(CountryForm))


class country(ModelView):
    column_list = ('name', 'email', 'password')
    column_sortable_list = ('name', 'email', 'password')

    form = User_ProjectForm

# Area admin
class AreaForm(form.Form):
    name = fields.StringField('Name')
    test = fields.StringField('Test')


class User_AreaForm(form.Form):
    name = fields.StringField('Name')
    email = fields.StringField('Email')
    password = fields.StringField('Password')

    # Inner form
    inner = InlineFormField(AreaForm)

    # Form list
    form_list = InlineFieldList(InlineFormField(AreaForm))


class area(ModelView):
    column_list = ('name', 'email', 'password')
    column_sortable_list = ('name', 'email', 'password')

    form = User_AreaForm

# Zone admin
class ZoneForm(form.Form):
    name = fields.StringField('Name')
    test = fields.StringField('Test')


class User_ZoneForm(form.Form):
    name = fields.StringField('Name')
    email = fields.StringField('Email')
    password = fields.StringField('Password')

    # Inner form
    inner = InlineFormField(ZoneForm)

    # Form list
    form_list = InlineFieldList(InlineFormField(ZoneForm))


class zone(ModelView):
    column_list = ('name', 'email', 'password')
    column_sortable_list = ('name', 'email', 'password')

    form = User_ZoneForm


# Device admin
class DeviceForm(form.Form):
    name = fields.StringField('Name')
    test = fields.StringField('Test')


class User_DeviceForm(form.Form):
    name = fields.StringField('Name')
    email = fields.StringField('Email')
    password = fields.StringField('Password')

    # Inner form
    inner = InlineFormField(DeviceForm)

    # Form list
    form_list = InlineFieldList(InlineFormField(DeviceForm))


class dev(ModelView):
    column_list = ('name', 'email', 'password')
    column_sortable_list = ('name', 'email', 'password')

    form = User_DeviceForm


    #def get_list(self, *args, **kwargs):
        #count, data = super(TweetView, self).get_list(*args, **kwargs)

        # Grab user names
        #query = {'_id': {'$in': [x['user_id'] for x in data]}}
        #users = db.user.find(query, fields=('name',))

        # Contribute user names to the models
        #users_map = dict((x['_id'], x['name']) for x in users)

        #for item in data:
        #    item['user_name'] = users_map.get(item['user_id'])

        #return count, data

    # Contribute list of user choices to the forms
    def _feed_user_choices(self, form):
        users = db.user.find(fields=('name',))
        form.user_id.choices = [(str(x['_id']), x['name']) for x in users]
        return form

    def create_form(self):
        form = super(TweetView, self).create_form()
        return self._feed_user_choices(form)

    def edit_form(self, obj):
        form = super(TweetView, self).edit_form(obj)
        return self._feed_user_choices(form)

    # Correct user_id reference before saving
    def on_model_change(self, form, model):
        user_id = model.get('user_id')
        model['user_id'] = ObjectId(user_id)

        return model


# Flask views
@app.route('/index')
def index():
    if g.user:
        return redirect(url_for('admin.index'))
    return render_template('login.html')    
    


if __name__ == '__main__':
    
    # Create admin
    admin = admin.Admin(app ,template_mode='bootstrap3')

    # Add views
    admin.add_view(UserView(db.user, 'User'))
    admin.add_view(proj(db.proj,'Project'))
    admin.add_view(country(db.country,'Country'))
    admin.add_view(area(db.area,'Area'))
    admin.add_view(zone(db.zone,'Zone'))
    admin.add_view(dev(db.dev,'Device'))

    # Start app
    app.run(debug=True)
