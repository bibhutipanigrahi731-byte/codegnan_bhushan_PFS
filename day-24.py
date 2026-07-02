#day-24
'''
project based on regex
----------------------
validation
----------
1.mobil number
--------------
-->10 disit init...
2.password
-----------
-->cap,small,digit,spacial char, atlest 8
3.mail
------
-->@gmail.com

'''
import re
class validator:
    def validate_mobile(self, mobile):
            pattren = r'^\d{10}$'
            if re.match(pattren, mobil):
               print("valid mobile number")
            else:
                print("invalid mobile number")
    def validata_password(self, password):
                pattern = r'^(?=.[A-Z])(?=.[a-z])(?=.\d)(?=.[@#$%^&+=!]).{8,}$'
                if re.match(pattren, password):
                    print("valid password")
                else:
                    print("invalid password")
    def validata_email(self, email):
              pattern = r'^[a-zA-Z0-9._%+-]+@gmail\.com$'
              if re.match(pattren, email):
                  return "valid gmail"
              return "invalid gamil"
while True:
    print("\n-------validation project--------")
    print("1.mobile number validation")
    print("2.password validation")
    print("3.email validation")
    print("4.exit")
    choice = input("enter your choice:")
    if choice == '1':
        mobile = input("6302322032")
        self.validator.validata_mobile(mobile)
    elif choice == '2':
        password = input("7645")
        self.validator.validata_password(password)
    elif choice == '3':
        email = input("bhushan@gmail.com")
        self.validator.validata_email(email)
    elif choice == '4':
        print("thank you")
    else:
        print("invalid choice")
obj = validationapp()
obj.menu()
    

    
                
            










