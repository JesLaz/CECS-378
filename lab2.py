#Jessie Lazo 
#CECS 378 

#Personal filePath of Ultima5\SAVED.GAM
#filePath = "C:\Users\JeLaz\OneDrive\Desktop\GAMES\Ultima5\SAVED.GAM"

#Order in which user can choose which character to edit
characterOrder = {1: "AVATAR", 2: "SHAMINO", 3: "IOLO", 4: "MARIAH", 5: "GEOFFREY", 6: "JAANA", 7: "JULIA", 8: "DUPRE",
                  9: "KATRINA", 10: "SENTRI", 11: "GWENNO",  12: "JOHNE", 13: "GORN", 14: "MAXWELL", 15: "TOSHI", 16: "SADUJ"}

#Required offsets for editing the player's main character
charOffset = {"AVATAR": int('0x02', 16), "SHAMINO": int('0x22', 16), "IOLO": int('0x42', 16), "MARIAH": int('0x62', 16),
            "GEOFFREY": int('0x82', 16), "JAANA": int('0xA2', 16), "JULIA": int('0xC2', 16), "DUPRE": int('0xE2', 16),
            "KATRINA": int('0x102', 16), "SENTRI": int('0x122', 16), "GWENNO": int('0x142', 16), "JOHNE": int('0x162', 16),
            "GORN": int('0x182', 16), "MAXWELL": int('0x1A2', 16), "TOSHI": int('0x1C2', 16), "SADUJ": int('0x1E2', 16)}

#Order in which character stats are listed
statOrder = {1: "STRENGTH", 2: "INTELLIGENCE", 3: "DEXTERITY", 4: "HP", 5: "MAXHP", 6: "EXPERIENCE", 7: "MAGIC"}

#Required offsets for editing certaim stat
statOffset = {"STRENGTH": int('0x0C', 16), "INTELLIGENCE": int('0x0E', 16), "DEXTERITY": int('0x0D', 16),
            "HP": int('0x10', 16), "MAXHP": int('0x12', 16), "EXPERIENCE": int('0x14', 16), "MAGIC": int('0x0F', 16)}

#Max allowable values for character's stats
statMaxes = {"STRENGTH": 255, "INTELLIGENCE": 255, "DEXTERITY": 255, "HP": 65535, "MAXHP": 65535, "EXPERIENCE": 65535,
           "MAGIC": 255}

#Order in which character items are listed
itemOrder = {1: "GOLD", 2: "KEYS", 3: "SKULL KEYS", 4: "GEMS", 5: "BLACK BADGE", 6: "MAGIC CARPET", 7: "MAGIC AXE"}

#Max allowable values for certain items
itemMax = {"GOLD": 65535, "KEYS": 255, "SKULL KEYS": 255, "GEMS": 255, "BLACK BADGE": 255, "MAGIC CARPET": 255,
           "MAGIC AXE": 255}

#Required offset for editing certain item count
itemOffset = {"GOLD": int('0x204', 16), "KEYS": int('0x206', 16), "SKULL KEYS": int('0x20B', 16), "GEMS": int('0x207', 16),
            "BLACK BADGE": int('0x218', 16), "MAGIC CARPET": int('0x20A', 16), "MAGIC AXE": int('0x240', 16)}

#Function that takes in the SAVED.GAM data and uses the offset dictionary to edit the hex values of the stats within the file
def editStats(characterChoice, filedata):
    print("what stat would you like to edit?")
    print("1.", statOrder[1], "\n2.", statOrder[2], "\n3.", statOrder[3], "\n4.", statOrder[4], "\n5.", statOrder[5],
          "\n6.", statOrder[6], "\n7.", statOrder[7])
    choice = 0
    while(not(0 < choice < 7)):
        choice = int(input("Enter value from 1 to 7\n"))
    stat = statOrder[choice]
    print("Editing", characterOrder[characterChoice], stat)
    l = statOffset[stat] + charOffset[characterOrder[characterChoice]]
    sMax = statMaxes[stat]
    print("Stat Max" , sMax)
    value = 0
    if(sMax < 256):
        value = filedata[l]
    else:
        value = 0

    newValue = int(input("Enter new value from 0 to {}".format(sMax)))
    while(not(0 < newValue < sMax)):
        newValue = int(input("Enter value from 0 to {}\n".format(sMax)))

    counter = 0
    byteArr = list(bytearray((newValue).to_bytes(2, byteorder="little")))
    if(len(byteArr) == 1):
        byteArr.insert(0, 0)
    for b in byteArr:
        filedata[l + counter] = b
        counter += 1
    print("New Value of {} = {}".format(stat, newValue))

    choice = input("Edit another stat? Enter 'y' or 'n'\n")
    if(choice == 'y'):
        editStats(filedata)

#Helper function for editStats which will prompt with user with the character names
#@return - int: user choice of character
def chooseCharacter(filedata):
    print("which character would you like to edit?")
    print("1.", characterOrder[1], "2.", characterOrder[2], "3.", characterOrder[3], "4.", characterOrder[4],
          "5.", characterOrder[5], "6.", characterOrder[6], "7.", characterOrder[7], "8.", characterOrder[8],
          "9.", characterOrder[9], "10.", characterOrder[10], "11.", characterOrder[11], "12.", characterOrder[12],
          "13.", characterOrder[13], "14.", characterOrder[14], "15.", characterOrder[15], "16.", characterOrder[16])
    choice = 0
    while(not(0 < choice < 17)):
        choice = int(input("Enter value from 1 to 16\n"))
    print("Character chosen:", characterOrder[choice])
    editStats(choice, filedata)

#Helper function for editItems which will prompt the user with the options of what are available to edit
#@return - int: user choice mirroring the itemOrder dictionary
def chooseItem(filedata):
    print("What item would you like to edit?")
    print("1.", itemOrder[1], "\n2.", itemOrder[2], "\n3.", itemOrder[3], "\n4.", itemOrder[4], "\n5.", itemOrder[5],
          "\n6.", itemOrder[6], "\n7.", itemOrder[7])
    choice = 0
    while(not(0 < choice < 8)):
        choice = int(input("Enter value from 1 to 7\n"))
    print("Item number chosen: ", choice)
    editItems(choice, filedata)

#Function that takes in the SAVED.GAM data and uses the offset dictionary to edit the hex values of the given items within
#the file
def editItems(itemChoice, filedata):
    print("itemChoice in editItems: ", itemChoice)
    item = itemOrder[itemChoice]
    print(item)
    l = itemOffset[item]
    iMax = itemMax[item]
    value = 0
    if(iMax > 255 and filedata[l] > 0):
        value = int(hex(filedata[l])[2:] + hex(filedata[l + 1])[2:], 16)
    elif(iMax > 255 and filedata[l] == 0):
        value = filedata[l + 1]
    else:
        value = filedata[l]

    newValue = 0
    print("Current value of {} = {}".format(item, value))
    while(not(0 < newValue <= iMax)):
        newValue = int(input("Enter value from 0 to {}\n".format(iMax)))

    counter = 0

    byteArr = list(bytearray((newValue).to_bytes(2, byteorder="little")))
    if(len(byteArr) == 1):
        byteArr.insert(0, 0)
    for b in byteArr:
        filedata[l + counter] = b
        counter += 1
    print("New number of {} chanegd to {}".format(item, newValue))
    choice = input("Edit another item count? Enter 'y' or 'n'\n")
    if(choice == 'y'):
        chooseItem(filedata)

#Function that opens the given filePath (SAVED.GAM) and returns it as a list of the bytes
def readData(filePath):
    print(filePath)
    with open(filePath, "rb") as file:
        gameData = list(bytearray(file.read()))
        file.close()
        return gameData

#Function that saved the modified values of the bytes back to SAVED.GAM
def writeData(filePath, filedata):
    with open(filePath, "wb") as file:
        file.write(bytearray(filedata))
        file.close()

def main():
    filePath = input("Please enter the file path of SAVED.GAM on your device")
    data = readData(filePath)
    choice = 0
    print("Which aspect would you like to edit?\n1.Character Stats\n2.Item Inventory\n3.Quit (Saves Changes Upon Termination")
    while(not(0 < choice < 3)):
        choice = int(input("Enter a value from 1 to 3\n"))
    while(choice != 3):
        if (choice == 1):
            chooseCharacter(data)
            choice = int(input("Edit another option?\n     1.Edit Character Stats\n     2.Edit Inventory"
                               "\n     3.Quit\nEnter a value from 1 to 3\n"))
        elif (choice == 2):
            chooseItem(data)
            choice = int(input("Edit another option?\n     1.Edit Character Stats\n     2.Edit Inventory"
                               "\n     3.Quit\nEnter a value from 1 to 3\n"))
        if (choice == 3):
            print("Writing to file")
            writeData(filePath, data)
            print("File saved, now terminating")


main()
