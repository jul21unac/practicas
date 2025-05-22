class User:

    _max_leng = 8

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self,value):
        if self.validLeng(value):
            self._password = value
        else:
            raise ValueError("The len should be more than 7")




    @property
    def ultimo_login(self):
        return self._ultimo_login

    @ultimo_login.setter
    def ultimo_login(self,value):
        self._ultimo_login = value

    def __init__(self,value, ultimo_login):
        self.password = value
        self._ultimo_login = ultimo_login



    def validLeng(self,value):
        if len(str(value))>= self._max_leng :
            return True

    def __str__(self):
        return f'[User{self.ultimo_login}_{self.password}]'

