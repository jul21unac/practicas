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


    @password.getter
    def password(self):
        return self._password

    def __init__(self,value):
        self.password = value



    def validLeng(self,value):
        if len(str(value))> self._max_leng :
            return True



