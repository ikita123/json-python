import re
import json 
import os
file_exist=os.path.exists("signup.json")
print(file_exist)
if file_exist==False:
    dic3={}
    list3=[]
    dic4={}
    user=input("enter a singup/login")
    if user=="s":
        NAME=input("ente the name")
        PASSWORD=input("enter the password")
        if re.search("[A-Z]", PASSWORD) and re.search("[a-z]", PASSWORD) and re.search("[0-9]", PASSWORD) and re.search("[@#$%^&]", PASSWORD):
            C_PASSWORD=input("conform password")
            if PASSWORD==C_PASSWORD:
                print("password is correct")
                DESCRIPTION=input("ente the discription")
                BIRTH=input("enter a birth date")
                HOBBY=input("enter your hobby")
                GENDER=input("enter your gander f/m")
                list1=["NAME","PASSWORD","DESCRIPTION","BIRTH OF DATE","HOBBY","GANDER"]
                list2=[NAME,PASSWORD,DESCRIPTION,BIRTH,HOBBY,GENDER]
                for i in range(0,len(list1)):
                    dic3.update({list1[i]:list2[i]})
                list3.append(dic3)
                dic4.update({PASSWORD:list3})
                with open("signup.json","w") as h:
                    json.dump(dic4,h,indent=4)
        else:
            print("enter capital latter,special character(#@$%),small latter,numbers")
elif file_exist==True:
    dic3={}
    list3=[]
    dic4={}
    user=input("enter a singup/login")
    if user=="s":
        NAME=input("ente the name")
        PASSWORD=input("enter the password")
        with open("signup.json","r") as a:
                data=json.load(a)
        if re.search("[A-Z]", PASSWORD) and re.search("[a-z]", PASSWORD) and re.search("[0-9]", PASSWORD) and re.search("[@#$%^&]", PASSWORD):
            C_PASSWORD=input("conform password")
            if PASSWORD==C_PASSWORD:
                print("password is correct")
                DESCRIPTION=input("ente the discription")
                BIRTH=input("enter a birth date")
                HOBBY=input("enter your hobby")
                GENDER=input("enter your gander f/m")
                list1=["NAME","PASSWORD","DESCRIPTION","BIRTH OF DATE","HOBBY","GANDER"]
                list2=[NAME,PASSWORD,DESCRIPTION,BIRTH,HOBBY,GENDER]

                for i in range(0,len(list1)):
                    dic3.update({list1[i]:list2[i]})
                list3.append(dic3)
                data.update({C_PASSWORD:list3})
                with open("signup.json","w") as h:
                    json.dump(data,h,indent=4)
        else:
            print("enter capital latter,special character(#@$%),small latter,numbers")
    elif user=="l":
        NAME_1=input("enter your name")
        PASSWORD_1=input("enter the user password")
        with open("signup.json","r") as a:
            data=json.load(a)

        for i in data:
            if i==PASSWORD_1:
                print("you login is successfully")
                print(data[i])
            else:
                print("password is invalid")
import re
import json 
import os
file_exist=os.path.exists("signup.json")
print(file_exist)
if file_exist==False:
    dic3={}
    list3=[]
    dic4={}
    user=input("enter a singup/login")
    if user=="s":
        NAME=input("ente the name")
        PASSWORD=input("enter the password")
        if re.search("[A-Z]", PASSWORD) and re.search("[a-z]", PASSWORD) and re.search("[0-9]", PASSWORD) and re.search("[@#$%^&]", PASSWORD):
            C_PASSWORD=input("conform password")
            if PASSWORD==C_PASSWORD:
                print("password is correct")
                DESCRIPTION=input("ente the discription")
                BIRTH=input("enter a birth date")
                HOBBY=input("enter your hobby")
                GENDER=input("enter your gander f/m")
                list1=["NAME","PASSWORD","DESCRIPTION","BIRTH OF DATE","HOBBY","GANDER"]
                list2=[NAME,PASSWORD,DESCRIPTION,BIRTH,HOBBY,GENDER]
                for i in range(0,len(list1)):
                    dic3.update({list1[i]:list2[i]})
                list3.append(dic3)
                dic4.update({PASSWORD:list3})
                with open("signup.json","w") as h:
                    json.dump(dic4,h,indent=4)
        else:
            print("enter capital latter,special character(#@$%),small latter,numbers")
elif file_exist==True:
    dic3={}
    list3=[]
    dic4={}
    user=input("enter a singup/login")
    if user=="s":
        NAME=input("ente the name")
        PASSWORD=input("enter the password")
        with open("signup.json","r") as a:
                data=json.load(a)
        if re.search("[A-Z]", PASSWORD) and re.search("[a-z]", PASSWORD) and re.search("[0-9]", PASSWORD) and re.search("[@#$%^&]", PASSWORD):
            C_PASSWORD=input("conform password")
            if PASSWORD==C_PASSWORD:
                print("password is correct")
                DESCRIPTION=input("ente the discription")
                BIRTH=input("enter a birth date")
                HOBBY=input("enter your hobby")
                GENDER=input("enter your gander f/m")
                list1=["NAME","PASSWORD","DESCRIPTION","BIRTH OF DATE","HOBBY","GANDER"]
                list2=[NAME,PASSWORD,DESCRIPTION,BIRTH,HOBBY,GENDER]

                for i in range(0,len(list1)):
                    dic3.update({list1[i]:list2[i]})
                list3.append(dic3)
                data.update({C_PASSWORD:list3})
                with open("signup.json","w") as h:
                    json.dump(data,h,indent=4)
        else:
            print("enter capital latter,special character(#@$%),small latter,numbers")
    elif user=="l":
        NAME_1=input("enter your name")
        PASSWORD_1=input("enter the user password")
        with open("signup.json","r") as a:
            data=json.load(a)

        for i in data:
            if i==PASSWORD_1:
                print("you login is successfully")
                print(data[i])
            else:
                print("password is invalid")

