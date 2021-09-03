import json

shopping={
    "shopping_list":
        { 
            "chaco":"15",
            "Biscuits":"50",
            "Diary_milk":"30",
            "ice_cream":"20",
        } 
}

item=input("enter the iteam name")
quantity=int(input("enter the quantity of iteam"))
# del shopping["shopping_list"][str(item)]
shopping["shopping_list"].update({item:quantity})
# print(shopping)
a=open("myfile.json","w")
json.dump(shopping,a,indent=6)
a.close()
