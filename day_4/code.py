import re

with open('input.txt') as f:
    text = f.read()
    passports = text.split('\n\n')
    count = 0
    for passport in passports:
        data = passport.split()
        dataDict = {}
        for entry in data:
            dataDict[entry.split(':')[0]] = entry.split(':')[1]
        fields = [entry.split(':')[0] for entry in data]
        if all(x in dataDict for x in ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']):
            if 1920 <= int(dataDict['byr']) <= 2002 and \
               2010 <= int(dataDict['iyr']) <= 2020 and \
               2020 <= int(dataDict['eyr']) <= 2030 and \
               ((dataDict['hgt'][-2:] == 'cm' and 150 <= int(dataDict['hgt'][:-2]) <= 193) or \
               (dataDict['hgt'][-2:] == 'in' and 59 <= int(dataDict['hgt'][:-2]) <= 76)) and \
               re.search("^#[0-9a-f]{6}$", dataDict['hcl']) is not None and \
               dataDict['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'] and \
               re.search("^[0-9]{9}$", dataDict['pid']) is not None:
                   count += 1
    print(count)
