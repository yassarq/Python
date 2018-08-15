
from system.core.controller import *

class Users(Controller):
    def __init__(self, action):
        super(Users, self).__init__(action) 
        self.load_model('User')
       

    def index(self):
        return self.load_view('index.html')

    


    def create_user(self):
        user_details = {
        'name': request.form['name'],
        'alias': request.form['alias'],
        'date_of_birth':request.form['dob'],
        'email': request.form['email'],
        'password':request.form['password'],
        'comfirmpw':request.form['comfirmpw']
        }
        create_status = self.models['User'].add_user(user_details)
        if create_status['status'] == True :
            session['id'] = create_status['user']['id']
            session['alias'] = create_status['user']['alias']
            return redirect('/pokes')
        else:
            for message in create_status['errors']:
                flash(message,'regis_errors')
            return redirect('/pokes')

    def login_user(self):
        user_details = {
            'email': request.form['email'],
            'password': request.form['password']
        }
        login_status = self.models['User'].login_user(user_details)
        if login_status['status'] == True:
            session['id'] = login_status['user']['id']
            session['alias'] = login_status['user']['alias']
            return redirect('/pokes')
        else:
            for message in login_status['errors']:
                flash(message,'regis_errors')
                return redirect('/')
        print session['id']    
  
    def make_poke(self):
        info = {
            'user_id': request.form['poker'],
            'poke': request.form['poked']
        }
        self.models['User'].make_poke(info)
        return redirect('/pokes')

    def pokes(self):
        info = {
            'id': session['id']
        }
        users = self.models['User'].select_users(info)
        x_pokes = self.models['User'].count_pokes(info)
        return self.load_view('pokes.html', users = users, x_pokes = x_pokes)


    def logout(self):
        session.clear()
        return redirect('/')
