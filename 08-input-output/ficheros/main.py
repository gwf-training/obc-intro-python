from os import path

directoryPath = path.dirname(path.realpath(__file__))

def getUsers():
    file = open(directoryPath + "\\email.csv", "r")
    lines = file.readlines()
    file.close()

    users = []
    for index, line in enumerate(lines):
        if index == 0: 
            continue
        fields = line.split(";")
        users.append(fields[0])
    return users

def saveUsers(users) -> None:
    file = open(directoryPath + "\\users.csv", "w")
    for index, user in enumerate(users, start=1):
        file.write(user+"\n")
    file.close()

def main():
    print ("aprendiendo ficheros ...")
    users = getUsers()
    for user in users:
        print(f"User Name: {user}")
    saveUsers(users)    


if __name__ == "__main__":
    main()