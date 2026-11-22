class users:
    def __init__(self):
        self._username = ''
        self._password = ''
        self.personagens = []
    
    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, dado):
        self._username = dado

    @property
    def password(self):
        return self._password
    
    @password.setter
    def password(self, dado):
        self._password = dado

    def criar_user(self, a, b):
        self._username = a
        self._password = b