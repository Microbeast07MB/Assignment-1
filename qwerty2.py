Names_marks={"Alice": 85 ,"Okarun": 67 , "Videl": 88 , "Luffy": 34 , "Robin": 98 }

a=input("What is the student name: ").title()

if a in Names_marks:
    print("Marks obtained by",a,"is" ,Names_marks[a])

else:
    print("Student not found")


#------------------------------------------------------------------

natural_numbers=[1,2,3,4,5,6,7,8,9,10]
print("Original list: ",natural_numbers)

a=natural_numbers[:5]
print("Extracted first five elements: ",a )

a.reverse()
print("Reversed extracted elements: ",a)
