import simplejson

list1=["neelam","programer","24,2400"]
list2=["komal","trainer","24","20000"]
list3=["anuradha","hr","29,40000"]
list4=["abhishek","manager","29","63000"]
key=["name","designation","age","salary"]
emp1={}
emp2={}
emp3={}
emp4={}
for i in range(len(list1)):
    emp1.update({key[i]:list1[i]})
for j in range (len(list2)):
    emp2.update({key[j]:list2[j]})
for k in range (len(list3)):
    emp3.update({key[k]:list3[k]})
for s in range (len(list4)):
    emp4.update({key[s]:list4[s]})
dict1={"emp1":emp1,"emp2":emp2,"emp3":emp3,"emp4":emp4}

with open("go.json","w") as file:
    simplejson.dump(dict1,file,indent=3)
file.close()
