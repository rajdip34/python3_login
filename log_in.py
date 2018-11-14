from getpass import getpass
ki = {
 'username': 'Rajdip34',
 'Age': '21',
 'password': '1610'
}
def log(u, p):
    if ki['username']in u:
      print("your user name is right")
    elif ki['password']in p:
            print("wellcome " + str(ki['username']))
    else:
        print("worng usr and password")
u = input("enter your username: ")
p = getpass("enter your password: ")
print(log(u,p))
print("your age is " + str(ki['Age']))
# other most perfact login is now you shoing
hg = {
'usr1':{
'name':'rajdip',
'usr_id':'82406',
'password':'rajdip34',
},'usr2':{
'name':'amrita',
'usr_id':'97754',
'password':'amrita34'
}
}
def log_in (id,pas):
        if hg['usr1'].get('usr_id') in id:
            print("hello wellcome " + str(hg['usr1'].get('name')))
            if hg['usr1'].get('password') in pas:
                print("accsess granted you are login " + str(hg['usr1'].get('name')))
            else:
                print("invalid password try agin")
        else:
            print("invalid input try agin")
k = (input("enter your ussr ID : "))
p = getpass("enter your password : ")
print(log_in(k,p))
