''' for number in range(0, 10, 2):
    print("Number is : ", number) '''

''' user1 = {"name": "Furkan", "job": "CE", "age": 25}
user2 = {"name": "Enes", "job": "EE", "age": 23}
user3 = {"name": "Mustafa", "job": "CE", "age": 24}

userList = [user1, user2, user3]


sumOfAges = 0
for user in userList:
    #print("NAME : ", user["name"], "  JOB : ", user["job"], " AGE : ", user["age"])
    
    sumOfAges = sumOfAges + user["age"]

print("AVERAGE OF AGES : ", sumOfAges / (len(userList))) '''

''' for i in range(6):
    print("Furkan") '''



#print("USER : ", user1)
#print("USER NAME : ", user1["name"], " ", user2["job"], " ", user3["age"])

from datetime import date

class User:
    todays_date = date.today()

    def __init__(self, name, job, birthyear):
        self.name = name
        self.job = job
        self.birthyear = birthyear
        
        
    def calcAge(self):
        print(todays_date.year - self.birthyear)
        
        
user1 = User("Furkan", "Software Engineer", 1997)

user1.calcAge()










user2 = User("Deniz", "Student", 1999)
user3 = User("Melih", "Student", 2005)

#print(todays_date.year - user1.birthyear)
''' userList = [user1, user2, user3]
 '''
''' for user in userList:
    print("NAME: ", user.name, " JOB: ", user.job, " AGE: ", user.age) '''




#print(userList[0].name)

#print(userList)

''' print(user1.name)
print(user2.name)
 '''