class Customer:
    
    def __init__(self,name,gender,address):
        self.name = name
        self.gender = gender
        self.address = address
        
   
        
       
        
        
    def edit_profile(self,new_name,new_city,new_pincode,new_state):
            self.name = new_name
            self.address.change_address(new_city,new_pincode,new_state)
        

class Address:
    def __init__(self,city,pincode,state):
        
        self.city = city
        self.pincode  = pincode 
        self.state = state
        
    def change_address(self,new_city,new_pincode,new_state):
        
        self.new_city = new_city
        self.pincode = new_pincode 
        self.state = new_state
        
    

add = Address("Kolkata", 734009 , "WB")

cus = Customer("Niten" , "Male" , add)
print(cus.address.pincode)
cus.edit_profile("Bishesh","Darjeeling","78900","BG")
print(cus.address.pincode)