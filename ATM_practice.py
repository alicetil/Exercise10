import getpass

pin = "3241"
tries = 0
max_tries = 3

while tries < 3:
    supplied_pin = getpass.getpass("Enter your PIN: ")
    print(supplied_pin)
    if supplied_pin == pin:
        print("PIN entry is successful")
        break
    else:
        print("PIN incorrect")
        print("You have had", tries+1, "attempts of 3")
    tries =+ 1
    if max_tries == tries:
        print("You have reached your max number of tries.")