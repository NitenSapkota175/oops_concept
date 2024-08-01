class Atm:
    
    def __init__(self):
        
        self.pin = ""
        self.balance = 0.0
        
     
    def check_pin(self):
            
            entered_pin = input("Entered your pin : ")
            if entered_pin == self.pin:
                return True
            else : return False 
        
            
    def create_pin(self):
        self.pin = input("Enter your pin : ")
        print("Pin is set ")     
        
    def deposit(self):
        
        if self.check_pin():
            amount = int(input("Enter the amount you want to desposite : "))
            self.balance = self.balance + amount
            print("Amount sucessfully desposited") 
        
        else:
            print("you pin is incorrect please try again! ")
        
    def withdraw(self):
        
        if self.check_pin():
            amount = int(input("Enter the amount you want to withdraw : "))
            if amount <= self.balance:
                self.balance = self.balance - amount
                print("Amount withdrawn rs : ",amount)
            else:
                print("Insufficent amount")
        else:
            print("Invalid pin")
            
    
    def check_balance(self):
        
        if self.check_pin():
            print("Your balance is : ",self.balance)
        else:
            print("Your pin is incorrect")
              
            


    def main(self):
        
            while(True):
                choice = input(
                    ''' 
                        What would you like to do ? 
                        
                        1. create pin
                        2. withdrawal 
                        3. check balance 
                        4. deposit
                        5. exit  
                        
                    '''
                ) 
            
                if choice == '1':
                
                    self.create_pin()
                
                elif choice == '2':
                    
                    self.withdraw()
                    
                elif choice == '3':
                    
                    self.check_balance()
                
                elif choice == '4':
                    
                    self.deposit()
                    
                else:
                    print("Thankyou for using our atm")
                    break
                
            
if  __name__ == "__main__": 
        print("Hello")
        kotak = Atm()
        kotak.main()
        
          