
from system.core.model import Model
import re
# from datetime import datetime, date


class User(Model):
    def __init__(self):
        super(User, self).__init__()

    def add_user(self, user):
        EMAIL_REGEX = re.compile(r'^[a-za-z0-9\.\+_-]+@[a-za-z0-9\._-]+\.[a-za-z]*$')
        errors = []
        if not user['name']:
            errors.append('Name cannot be blank')
        if not user['alias']:
            errors.append('Alias cannot be blank')
        if not user['date_of_birth']:
            errors.append('date of birth cannot be blank')
            # errors.append('day of birth must be in past')
        if not user['email']:
            errors.append('Email cannot be blank')
        elif not EMAIL_REGEX.match(user['email']):
            errors.append('Must be real email')
        if not user['password']:
            errors.append('password cannot be blank')
        if not user['comfirmpw']:
            errors.append('Name cannot be blank')
        if user['password'] != user['comfirmpw']:
            errors.append('password does not macth comfirm')
        if errors:
            return {"status": False, "errors": errors}
        else:
            password = user['password']
            hashed_pw = self.bcrypt.generate_password_hash(password)
            query = "INSERT INTO users(name, alias, date_of_birth, email, pw_hash, created_at, updated_at) VALUES (%s, %s, %s, %s, %s, NOW(), NOW())"
            data  =[user['name'], user['alias'],user['date_of_birth'], user['email'], hashed_pw]
            user = self.db.query_db(query, data)
            get_user_query = "SELECT * FROM users ORDER BY id DESC LIMIT 1" 
            get_user = self.db.query_db(get_user_query)
            return {"status": True, "user": get_user[0]}

    def login_user(self, user):
        errors = []
        if not user['email']:
            errors.append('Email cannot be blank')
            return {"status": False, "errors": errors}
        else:
            password = user['password']
            query = "SELECT * FROM users WHERE email = %s LIMIT 1"
            data = [user['email']]
            users = self.db.query_db(query, data)
            if users:
                if self.bcrypt.check_password_hash(users[0]['pw_hash'], password):
                    return {"status": True, "user": users[0]}
            else: 
                errors.append('Password and email do not match')
                return {"status": False, "errors": errors}

    def select_users(self,info):
        query = "SELECT users.id, users.name, users. alias, users.email, pokes.user_id, count(poke) FROM users LEFT JOIN pokes on users.id = pokes.user_id WHERE users.id <> %s GROUP BY users.id "
        data = [info['id']]
        return self.db.query_db(query,data)

    def make_poke(self, info):
        query = "INSERT INTO pokes(poke, user_id) VALUES (%s, %s)"
        data = [info['user_id'], info['poke']]
        pokes = self.db.query_db(query, data)
        return pokes

    def count_pokes(self, info):
        query = "SELECT count(poke) FROM pokes WHERE user_id = %s "
        data = [info['id']]
        x_pokes = self.db.query_db(query,data)
        return x_pokes[0].values()
