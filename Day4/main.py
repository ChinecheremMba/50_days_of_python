Name=input("name please ")
print( "Hi  "  +  Name   +  "  welcome to the mere friuts market")


fruits = ('apple', 'pineapple', 'watermelon', 'mango', 'avocado', 'pears')
nuts = ('almond nuts', 'cashew nuts',  'groundnut')

print( "we have fruits and nuts " )

wants =input("Which one do you want (fruits/nuts)? ").lower()

if wants == 'fruits':
    print(fruits)
elif wants == 'nuts':
    print(nuts)
else:
    print("These are the available items")
    
print("Thank you. See ya next time")
