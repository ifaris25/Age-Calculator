import datetime
now = datetime.date.today()
Data = []
def add_user(date):
    date=str(date).replace(' ' ,'')
    reset=date.split(',')
    myname=reset[0]
    age=reset[1]
    age=age.split('-')
    userDate=datetime.date(int(age[2]),int(age[1]),int(age[0]))
    # userAge= result = now.year - userDate.year
    userAge = now.year - userDate.year - ((now.month, now.day) < (userDate.month, userDate.day))
    if now.month < userDate.month:
        ageMonths = now.month + 12 - userDate.month
        userAge -= 1
    else:
        ageMonths = now.month - userDate.month
    if now.day < userDate.day:
        ageDays = now.day + 30 - userDate.day
        if ageMonths == 0:
            userAge -= 1
    else:
        ageDays = now.day - userDate.day

    day=userDate.strftime('%A')
    da = {
        'name': myname ,
        'year': userDate.year,
        'month': userDate.month,
        'day': userDate.day,
        'age':userAge,
        'dday': day,
        'userMonth':ageMonths,
        'userDays':ageDays
    }
    Data.append(da)
def comp(per1, per2): # if per1 bigger than per2 return True ,otherwise return False
    if per1['year'] < per2['year']:
        return True
    elif (per1['year'] == per2['year']) and (per1['month'] < per2['month']) :
        return True
    elif (per1['year'] == per2['year']) and (per1['month'] == per2['month']) and (per1['day'] < per2['day']):
        return True
    else:
        return False

def sort_users(users):
    n =len(users)
    for i in range(n):
        for j in range(0,n-i-1):
            if comp(users[j+1],users[j]):
                temp=users[j]
                users[j]=users[j+1]
                users[j+1]=temp
    return users
def output(user):
    print(user['name'],"is",user['age'],"years and",user['userMonth'],'months and ',user['userDays'],'days on',user['dday'])
add_user("Faris, 11-8-2002")
Data=sort_users(Data)
for n in Data:
    output(n)