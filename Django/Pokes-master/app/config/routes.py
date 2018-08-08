
from system.core.router import routes


routes['default_controller'] = 'Users'
routes['POST']['/create'] = 'Users#create_user'
routes['POST']['/login'] = 'Users#login_user'
routes['/logout'] = 'Users#logout'


# pokes routes
routes['/pokes'] = 'Users#pokes'
routes['POST']['/pokes/make'] = 'Users#make_poke'

