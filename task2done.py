casino_blacklist = ["alla black", "anna white", "alla blue", "anna red", "alla red", "anna sydor", "anna pekar"]
poker_blacklist = ["anna white", "alla black", "alla blue", "anna pekar", "aja red", "alla red"]
alcohol_blacklist = ["anna white", "alla blue", "anna red", "anna black", "inna red", "anna pekar"]

counter = 0
while counter <= len(casino_blacklist) - 1:
    if casino_blacklist[counter] in poker_blacklist and casino_blacklist[counter] in alcohol_blacklist:
        print(casino_blacklist[counter])
    counter += 1
