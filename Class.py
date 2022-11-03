class Student:
 
    
    def __init__(self, name, srcode):
        self.name = name
        self.srcode = srcode
 
    def display(self):
        print('Name:', self.name)
        print('SR Code:', self.srcode)
        print('Section:', self.section)
        print('Subject Code:', self.subscode)
 

class Information(Student):
    def __init__(self, name, srcode, section, subscode):
        self.section = section
        self.subscode = subscode
 
        
        Student.__init__(self, name, srcode)
 
 

Info = Information('Kris Nathaniel Dimaapi', '21-00385', 'IT-2102', "CS 121")

Info.display()
