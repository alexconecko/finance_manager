import sys

#parent class of a finance records allows different types of 
#transactions to become child classes and inherit these attributes
class FinanceRecord():
    date = "YYYY-MM-DD"
    name = None
    amount = 0
    
    def __init__(self, date, name, amount):
        self.date = date
        self.name = name
        self.amount = amount
        
#child class of FinanceRecord allows us to create different instances
#that inherit properties and methods from the parent class
class Expense(FinanceRecord):
    #optional attribute that can be assigned to an expense object
    #when creating an expense object you must still provide all the
    #paramters required by FinanceRecords constructor method as it 
    #is also inherited by thee child class
    category = None

#child class of FinanceRecord allows us to create different instances
#that inherit properties and methods from the parent class
class Income(FinanceRecord):
    #income class has a source attribute however this is mandatory
    #as it is required by the constructor method of this class.
    source = None
    
    #super() is used to set the other paremeters without duplicating
    #the code that is in the FinanceRecord constructor method
    def __init__(self, date, name, amount, source):
        #the super() function is used to give access to methods and
        #properties of a parent or sibling class
        super().__init__(date, name, amount)
        self.source = source

class FinanceManager():
    finance_records = []
    
