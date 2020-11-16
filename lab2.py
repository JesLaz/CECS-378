charOffset = {"PLAYER": int('0x02', 16), "SHAMINO": int('0x22', 16), "IOLO": int('0x42', 16), "MARIAH": int('0x62', 16),
            "GEOFFREY": int('0x82', 16), "JAANA": int('0xA2', 16), "JULIA": int('0xC2', 16), "DUPRE": int('0xE2', 16),
            "KATRINA": int('0x102', 16), "SENTRI": int('0x122', 16), "GWENNO": int('0x142', 16), "JOHNE": int('0x162', 16),
            "GORN": int('0x182', 16), "MAXWELL": int('0x1A2', 16), "TOSHI": int('0x1C2', 16), "SADUJ": int('0x1E2', 16)}

statOffset = {"STRENGTH": int('0x0C', 16), "INTELLIGENCE": int('0x0E', 16), "DEXTERITY": int('0x0D', 16),
            "HP": int('0x10', 16), "MAXHP": int('0x12', 16), "EXPERIENCE": int('0x14', 16), "MAGIC": int('0x0F', 16)}

itemOffset = {"GOLD": int('0x204', 16), "KEYS": int('0x206', 16), "SKULL KEYS": int('0x20B', 16), "GEMS": int('0x207', 16),
            "BLACK BADGE": int('0x218', 16), "MAGIC CARPET": int('0x20A', 16), "MAGIC AXE": int('0x240', 16)}

def readData():
    filePath = input("Please enter the file path of SAVED.GAM on your device")
    with open(filePath, "rb") as file:
        gameData = list(bytearray(file.read()))
        file.close()
        return gameData
    

def main():
    print("That works")

main()
