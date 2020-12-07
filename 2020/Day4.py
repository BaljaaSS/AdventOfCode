import json 
from re import search, match

file1 = open('AdventOfCode/2020/Input/Input4.txt', 'r') 
lines = file1.read().splitlines() 

class Passport:
    byr_uLimit = 2002
    byr_lLimit = 1920

    iyr_uLimit = 2020
    iyr_lLimit = 2010

    eyr_uLimit = 2030
    eyr_lLimit = 2020

    hgtCM_uLimit = 193
    hgtCM_lLimit = 150

    hgtIN_uLimit = 76
    hgtIN_lLimit = 59    

    hcl_rex = '^#[a-zA-Z0-9]{6}$'
    ecl_colors = 'amb blu brn gry grn hzl oth'

    pid_rex = "^[0-9]{9}$"

    def __init__(self, byr, iyr, eyr, hgt , hcl, ecl, pid, cid = 0):
        self.byr = int(byr)
        self.iyr = int(iyr)    
        self.eyr = int(eyr)
        self.hgt = hgt    
        self.hcl = hcl
        self.ecl = ecl        
        self.pid = pid
            
    def Validate(self):
        if (self.byr_lLimit > self.byr or self.byr > self.byr_uLimit):
            return False

        if (self.iyr_lLimit > self.iyr or self.iyr > self.iyr_uLimit):
            return False

        if (self.eyr_lLimit > self.eyr or self.eyr > self.eyr_uLimit):
            return False        

        if (search("cm",self.hgt)):
            hgt = int(self.hgt[:-2])
            if (self.hgtCM_lLimit > hgt or hgt > self.hgtCM_uLimit):
                return False                        
        else:
            hgt = int(self.hgt[:-2])
            if (self.hgtIN_lLimit > hgt or hgt > self.hgtIN_uLimit):
                return False                        

        if (not match(self.hcl_rex, self.hcl)):
            return False

        if (not search(self.ecl, self.ecl_colors)):
            return False

        if (not search(self.pid_rex, self.pid)):
            return False

        return True

requiredFields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

# %% Part-1
def ContainsAllFields(passportStr):
    count = 0
    for field in requiredFields:
        if (search(field, passportStr)):
            count += 1        
    
    if (count == len(requiredFields)):
        return True
    else:
        return False        

# %% Part-2
def ValidatePassport(passportStr):
    if (ContainsAllFields(passportStr)):
        passport = ParseToPassportClass(passportStr)
        return passport.Validate()
    return False    

def ParseToPassportClass(passportStr):
    passportJson = '{\"' + passportStr.strip().replace(" ", ",") + '\"}'
    passportJson = passportJson.replace(":", "\":\"").replace(",","\",\"")
    return Passport(**json.loads(passportJson))

# %% Main
passportStr = ""
count = 0
countV = 0
for line in lines:
    if (line == ''):
        if (ContainsAllFields(passportStr)):
            count += 1
        if (ValidatePassport(passportStr)):    
            countV += 1
        passportStr = ""
    else:
        passportStr = passportStr + line + " "

print("Part-1: A number of valid passports is :", count)        
print("Part-2: A number of valid passports with validation is :", countV)