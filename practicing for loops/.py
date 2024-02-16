class Student:
    def __init__(self,name,years_UM,knowledge=0):
        self.name = name
        self.years_UM = years_UM
        self.knowledge = knowledge
        
    def study(self):
        self.knowledge += 1
        return None
    def getKnowledge(self):
        return self.knowledge
    def year_at_umich(self):
        return self.years_UM

s = Student('Ali',1,0)

assert s.name == 'Ali'
assert s.years_UM == 1
assert s.knowledge == 0
assert s.study() == None
assert s.getKnowledge() == 0
assert s.year_at_umich == 1