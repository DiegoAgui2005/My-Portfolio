class BaseClass:
    def __init__(self):
        self._protected_variable = "Protected"
        self.__private_variable = "Private"
        
    def _protected_method(self):
        print("Protected method")
    
    def __private_method(self):
        print("Private method")
        
    def public_method(self):
        self.__private_method()
        
base = BaseClass()
base.public_method()