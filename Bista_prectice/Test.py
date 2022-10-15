from abc import ABC,abstractclassmethod

class ele(ABC):
    def des(self):
        pass
    

class device():
    def __init__(self) -> None:
        self._a = 2
    def print_type(self):
        print('I am a device')
    def genarel(self,**k):
        print(k['display'])
    def des(self):
        print('i can use electricity or fuel')

class Electric():
    def cost(self,watt):
        print("Electric cost for this week is",watt)
    def print_type(self):
        print('I am Electric')
    def des(self):
        print('i only use electricity')

class mobile(device,Electric):
    def __init__(self) -> None:
        super().__init__()
    def info(self,name,type):
        self.name = name
        self.type = type
    def des(self,battary_type):
        print('I use charging battery. Type =',battary_type)
        print('calling Electric "des" method....')
        Electric.des(self)
    
class mobile_5g(mobile):
    def __init__(self) -> None:
        print("I support 5G")



#polymorphism
Hitter=Electric()
Hitter.print_type()
Genarator=device()
Genarator.genarel(display=True)
#Inheritance
print("mobile")
Samsung=mobile()
Samsung.print_type()
Samsung.cost(30)
#override
Genarator.des()
Samsung.des('Li-ion')
#multi-level
Iphone_13=mobile_5g()
Iphone_13.cost(60)
