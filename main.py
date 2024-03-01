# Author: Ryan Stone
# Project: TIA Analyzer
# Date: 3/1/2024

from classes import Group, School       

twirlers, dancers, guards, stationaryPerc, marchingPerc, winds, jazz = Group("Twirlers"), Group("Dance"), Group("Guard"), Group("Stationary Percussion"), Group("Marching Percussion"), Group("Winds"), Group("Jazz")
groups = twirlers, dancers, guards, stationaryPerc, marchingPerc, winds, jazz


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
    if school.getGroup() == "Twirlers":
        for matchSchool in twirlers.getSchools():
            if matchSchool.getName() == school.getName() and matchSchool.getDivision() == school.getDivision():
                matchSchool.update(school)
                append = False
        if append == True:
            twirlers.addSchool(school)

    elif school.getGroup() == "Dance":
        for matchSchool in dancers.getSchools():
            if matchSchool.getName() == school.getName() and matchSchool.getDivision() == school.getDivision():
                matchSchool.update(school)
                append = False
        if append == True:
            dancers.addSchool(school)

    elif school.getGroup() == "Guard":
        for matchSchool in guards.getSchools():
            if matchSchool.getName() == school.getName() and matchSchool.getDivision() == school.getDivision():
                matchSchool.update(school)
                append = False
        if append == True:
            guards.addSchool(school)

    elif school.getGroup() == "Stationary Percussion":
        for matchSchool in stationaryPerc.getSchools():
            if matchSchool.getName() == school.getName() and matchSchool.getDivision() == school.getDivision():
                matchSchool.update(school)
                append = False
        if append == True:
            stationaryPerc.addSchool(school)

    elif school.getGroup() == "Marching Percussion":
        for matchSchool in marchingPerc.getSchools():
            if matchSchool.getName() == school.getName() and matchSchool.getDivision() == school.getDivision():
                matchSchool.update(school)
                append = False
        if append == True:
            marchingPerc.addSchool(school)

    elif school.getGroup() == "Winds":
        for matchSchool in winds.getSchools():
            if matchSchool.getName() == school.getName() and matchSchool.getDivision() == school.getDivision():
                matchSchool.update(school)
                append = False
        if append == True:
            winds.addSchool(school)

    elif school.getGroup() == "Jazz":
        for matchSchool in jazz.getSchools():
            if matchSchool.getName() == school.getName() and matchSchool.getDivision() == school.getDivision():
                matchSchool.update(school)
                append = False
        if append == True:
            jazz.addSchool(school)

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



def getSelection(names, question, index=False, mult=False):
    if question[-1] != " ":
        question += " "

    indexes = [str(i+1) for i in range(len(names))]
    for i, name in enumerate(names):
        print(f"{i+1}: {name}")
    
    if mult == False:
        user = None
        while user not in indexes:
            user = input(question)
    else:
        print("Note: Enter Nothing To Continue.")
        done, userList = False, []
        while done == False:
            user = input(question)
            if user in indexes:
                if index == False:
                    print("Added", names[int(user)-1])
                    userList.append(names[int(user)-1])
                else:
                    print("Added", names[int(user)-1])
                    userList.append(int(user)-1)
            elif user == "":
                done = True
    print()

    if mult == False:
        if index == False:
            return names[int(user)-1]
        else:
            return int(user)-1
    else:
        return userList



def selectData():
    selection = getSelection(["Twirlers", "Dancers", "Guards", "Stationary Percussion", "Marching Percussion", "Winds", "Jazz"], "Which Database Would You Like To View?", index=True)
    group = groups[selection]
    selection = getSelection(["Name", "Division"], "What Would You Like To Search By?")
    
    selectionGroup = []
    if selection == "Name":
        schools = group.getSchools()
        schoolNames = group.getNames()
        schoolNames.sort()

        for name in schoolNames:
            for school in schools:
                if name == school.getName():
                    print(school)


    elif selection == "Division":
        for division in group.getDivisions():
            selectionGroup.append(division)
        selectedDivisions = getSelection(selectionGroup, "What Division(s) Would You Like To Look At?", mult=True)
        for school in group.getSchools():
            if school.getDivision() in selectedDivisions:
                print(school)

    #elif selection == "Total":
    #    for school in group.getSchools():
    #        print(school.getTotal())



def main():
    data = readFile('WINDI Data Time.csv')
    convertData(data)
    selectData()



if __name__ == "__main__":
    try:
        main()
    except:
        print("An Error Occured.")

    from time import sleep
    sleep(360)
