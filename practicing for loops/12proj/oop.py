class PythonForm:
    formType = 'PythonForm'
    def printForm(self):
        print(f'name is {self.name}')
        print(f'age is {self.age}')
        


myApplication = PythonForm
myApplication.name = 'Ali'
myApplication.age = '19'
        
myApplication.printForm()