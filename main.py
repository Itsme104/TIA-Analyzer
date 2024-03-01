# Author: Ryan Stone
# Project: TIA Analyzer
# Date: 3/XX/2024

twirlers, dancers, guards, stationaryPerc, marchingPerc, winds, jazz = [], [], [], [], [], [], []
groups = twirlers, dancers, guards, stationaryPerc, marchingPerc, winds, jazz

class School:
    def __init__(self, groupDiv, name, total, date, cat1, s1, cat2, s2, cat3=None, s3=None, cat4=None, s4=None, cat5=None, s5=None):
        group, division = groupDiv.split(":")
        self.group = group.strip(" ")
        self.division = division.strip(" ")
        self.name = name
        self.total = total
        self.date = date
        self.cat1, self.cat2, self.cat3, self.cat4, self.cat5 = cat1, cat2, cat3, cat4, cat5
        self.score1, self.score2, self.score3, self.score4, self.score5 = s1, s2, s3, s4, s5
        
    def __str__(self):
        outStr = "~~~~~" * 8 + '\n'
        outStr += f"Name: {self.getName()}\n"
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
            


def readFile(fileName):
    lines, skip = [], True
    infile = open(fileName, 'r')
    for line in infile:
        if skip == False:
            if line[:2].lower() not in ['st', 'nd', 'rd', 'th']:
                line = line.rstrip().split(',')
                if line[-1] == "":
                    del line[-1]
                if len(line) == 6:
                    del line[4]
                line[-1] = line[-1].strip('"').split(" ")[0]
                if line[-1] != '' and line[-1] != "--":
                    lines.append(line)
        else:
            skip = False
    return lines



def addSchool(school):
    append = True
    # Check For Pre-existing
    if school.getGroup() == "Twirlers":
        for matchSchool in twirlers:
            if matchSchool.getName() == school.getName() and matchSchool.getDivision() == school.getDivision():
                matchSchool.update(school)
                append = False
        if append == True:
            twirlers.append(school)

    elif school.getGroup() == "Dance":
        for matchSchool in dancers:
            if matchSchool.getName() == school.getName() and matchSchool.getDivision() == school.getDivision():
                matchSchool.update(school)
                append = False
        if append == True:
            dancers.append(school)

    elif school.getGroup() == "Guard":
        for matchSchool in guards:
            if matchSchool.getName() == school.getName() and matchSchool.getDivision() == school.getDivision():
                matchSchool.update(school)
                append = False
        if append == True:
            guards.append(school)

    elif school.getGroup() == "Stationary Percussion":
        for matchSchool in stationaryPerc:
            if matchSchool.getName() == school.getName() and matchSchool.getDivision() == school.getDivision():
                matchSchool.update(school)
                append = False
        if append == True:
            stationaryPerc.append(school)

    elif school.getGroup() == "Marching Percussion":
        for matchSchool in marchingPerc:
            if matchSchool.getName() == school.getName() and matchSchool.getDivision() == school.getDivision():
                matchSchool.update(school)
                append = False
        if append == True:
            marchingPerc.append(school)

    elif school.getGroup() == "Winds":
        for matchSchool in winds:
            if matchSchool.getName() == school.getName() and matchSchool.getDivision() == school.getDivision():
                matchSchool.update(school)
                append = False
        if append == True:
            winds.append(school)

    elif school.getGroup() == "Jazz":
        for matchSchool in jazz:
            if matchSchool.getName() == school.getName() and matchSchool.getDivision() == school.getDivision():
                matchSchool.update(school)
                append = False
        if append == True:
            jazz.append(school)

    else:
        print("????? time")
        input()



def convertData(data):
    i = 0
    while i < len(data):
        mainLine = data[i]

        x = 1
        while i+x < len(data) and data[i+x][2] == mainLine[2] and data[i+x][1] == mainLine[1]:
            x += 1

        if x == 6:
            school = School(mainLine[1], mainLine[2], data[i+5][4], mainLine[0], mainLine[3], mainLine[4], data[i+1][3], data[i+1][4], data[i+2][3], data[i+2][4], data[i+3][3], data[i+3][4], data[i+4][3], data[i+4][4])
            i += 6
        elif x == 5:
            school = School(mainLine[1], mainLine[2], data[i+4][4], mainLine[0], mainLine[3], mainLine[4], data[i+1][3], data[i+1][4], data[i+2][3], data[i+2][4], data[i+3][3], data[i+3][4])
            i += 5

        elif x == 4:
            school = School(mainLine[1], mainLine[2], data[i+3][4], mainLine[0], mainLine[3], mainLine[4], data[i+1][3], data[i+1][4], data[i+2][3], data[i+2][4])
            i += 4

        elif x == 3:
            school = School(mainLine[1], mainLine[2], data[i+2][4], mainLine[0], mainLine[3], mainLine[4], data[i+1][3], data[i+1][4])
            i += 3
        else:
            print("Weve Got A New One")
            input()

        addSchool(school)


#twirlers, dancers, guards, stationaryPerc, marchingPerc, winds, jazz
def selectData():
    options = '''Databases:
1: Twirlers
2: Dancers
3: Guards
4: Stationary Percussion
5: Marching Percussion
6: Winds
7: Jazz'''
    print(options)
    user = None
    while user == None:
        user = input("Which Database Would You Like To View? ")
        if user in ['1', '2', '3', '4', '5', '6', '7']:
            user = int(user)-1
    group = groups[user]
    
    for school in group:
        if school.getDivision() == "SAP" or school.getName() == "Northern York HS":
            print(school)


def main():
    data = readFile('WINDI Data Time.csv')
    convertData(data)
    selectData()



if __name__ == "__main__":
    print("\n\n")
    main()