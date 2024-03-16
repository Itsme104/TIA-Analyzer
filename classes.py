# Author: Ryan Stone
# Project: TIA Analyzer - Classes
# Date: 3/7/2024

class Group:
    def __init__(self, name):
        self.name = name
        self.schools = []
        self.divisions = []
        self.names = []

    def __str__(self):
        return self.getName()
    

    def getName(self):
        return self.name
    def getSchools(self):
        return self.schools
    def getDivisions(self):
        return self.divisions
    def getNames(self):
        return self.names
    
    
    def addSchool(self, school):
        self.names.append(school.getName())
        self.schools.append(school)
        self.addDivision(school.getDivision())
    def addDivision(self, division):
        if division not in self.getDivisions():
            self.divisions.append(division)

    def rankSchools(self, category):
        ranked = reversed(sorted(self.getSchools()[:], key=lambda school: school.getTotal())) #Get Info for modularity
        ranked = [school for school in ranked]
        for (i, school) in enumerate(ranked):
            school.setRank(i+1)
        return ranked



class School:
    def __init__(self, groupDiv, name, total, date, cat1, s1, cat2, s2, cat3=None, s3=None, cat4=None, s4=None, cat5=None, s5=None):
        group, division = groupDiv.split(":")
        self.group = group.strip(" ")
        self.division = division.strip(" ")
        self.name = name
        self.rank = None
        self.total = total
        self.date = date
        self.cat1, self.cat2, self.cat3, self.cat4, self.cat5 = cat1, cat2, cat3, cat4, cat5
        self.score1, self.score2, self.score3, self.score4, self.score5 = s1, s2, s3, s4, s5
        

    def __str__(self):
        outStr = "~~~~~" * 8 + '\n'
        outStr += f"Name: {self.getName()}\n"
        if self.rank != None:
            outStr += f"Rank: {self.getRank()}\n"
        outStr += f"Date: {self.getDate()}\n"
        outStr += f"Group: {self.getGroup()}\n"
        outStr += f"Division: {self.getDivision()}\n\n"

        outStr += f"{self.getCategory1()}: {self.getScore1()}\n"
        outStr += f"{self.getCategory2()}: {self.getScore2()}\n"

        if self.getCategory3() != None:
            outStr += f"{self.getCategory3()}: {self.getScore3()}\n"
            if self.getCategory4() != None:
                outStr += f"{self.getCategory4()}: {self.getScore4()}\n"
                if self.getCategory5() != None:
                    outStr += f"{self.getCategory5()}: {self.getScore5()}\n"

        outStr += f"\nTotal: {self.getTotal()}\n"
        return outStr + "~~~~~" * 8 + '\n'
    

    def getGroup(self):
        return self.group
    def getDivision(self):
        return self.division
    def getName(self):
        return self.name
    def getTotal(self):
        return self.total
    def getDate(self):
        return self.date
    def getRank(self):
        return self.rank
    
    def getCategory1(self):
        return self.cat1
    def getCategory2(self):
        return self.cat2
    def getCategory3(self):
        return self.cat3
    def getCategory4(self):
        return self.cat4
    def getCategory5(self):
        return self.cat5
    
    def getScore1(self):
        return self.score1
    def getScore2(self):
        return self.score2
    def getScore3(self):
        return self.score3
    def getScore4(self):
        return self.score4
    def getScore5(self):
        return self.score5

    #Here
    def getInfo(self, category):
        ...

    
    def setRank(self, rank):
        self.rank = rank

    def resetRank(self):
        self.rank = None
    
    
    def update(self, school):
        self.date = school.getDate()
        self.total = school.getTotal()
        self.cat1 = school.getCategory1()
        self.score1 = school.getScore2()
        self.cat2 = school.getCategory2()
        self.score2 = school.getScore2()

        if self.getCategory3() != None:
            self.cat3 = school.getCategory3()
            self.score3 = school.getScore3()
            if self.getCategory4() != None:
                self.cat4 = school.getCategory4()
                self.score4 = school.getScore4()
                if self.getCategory5() != None:
                    self.cat5 = school.getCategory5()
                    self.score5 = school.getScore5()
