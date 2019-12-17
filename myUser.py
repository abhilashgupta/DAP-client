class User:
    def __init__(self, name, email):
        self._name = name
        self._email = email
    
    def get_name(self):
        return self._name
    
    def get_email(self):
        return self._email
        
    def do_something(self):
        print ("Hello, I'm " + str(self))
        
    def __str__(self):
        return self._name + ", " + self._email


users_list = [User("test1", "test1@mail.com"), User("test2", "test2@notmail.com"), User("test3", "test3@somewhatmail.com")]

for user in users_list:
    user.do_something()