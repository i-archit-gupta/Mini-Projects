import getpass
db = {"iarchitgupta": "abcd1234", "gupta.archit": "123456"}  # You can add your username and password in this dictionary
userid = input("Enter Your Username : ")
passw = getpass.getpass("Enter Your Password : ")
if userid not in db.keys():
    print("Username Not Found")
    exit(0)
for i in db.keys():
    if userid == i:
        while passw != db.get(i):
            passw = getpass.getpass("Enter Your Password Again : ")
        break
print("Verified")
