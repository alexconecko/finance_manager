import sys

#parent class of a finance records allows different types of 
#transactions to become child classes and inherit these attributes
class FinanceRecord():
    __date = "YYYY-MM-DD"
    __name = None
    __amount = 0
    
    def __init__(self, date, name, amount):
        self.__date = date
        self.__name = name
        self.__amount = amount
    
    #property tags are used for getter methods, using this tag we can call
    #the methods without the use of () at the end providing the illusion
    #of an actual attribute/property. Using this in combination with private
    #members within the FinanceRecord class keeps certain class members 
    #from being mutable    
    @property
    def date(self):
        return self.__date
    
    @property
    def name(self):
        return self.__name

    @property
    def amount(self):
        return self.__amount
        
#child class of FinanceRecord allows us to create different instances
#that inherit properties and methods from the parent class
class Expense(FinanceRecord):
    #optional attribute that can be assigned to an expense object
    #when creating an expense object you must still provide all the
    #paramters required by FinanceRecords constructor method as it 
    #is also inherited by thee child class
    __category = None
    
    @property
    def category(self):
        return self.__category

#child class of FinanceRecord allows us to create different instances
#that inherit properties and methods from the parent class
class Income(FinanceRecord):
    #income class has a source attribute however this is mandatory
    #as it is required by the constructor method of this class.
    __source = None
    
    #super() is used to set the other paremeters without duplicating
    #the code that is in the FinanceRecord constructor method
    def __init__(self, date, name, amount, source):
        #the super() function is used to give access to methods and
        #properties of a parent or sibling class
        super().__init__(date, name, amount)
        self.source = source
        
    def source(self):
        return self.__source

class FinanceManager():
    finance_records = []
    
