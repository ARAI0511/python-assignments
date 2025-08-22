try:
    dic={"Alice":85,"Billy":91,"Dustin":100,"Mike":80}
    name=str(input("Enter the Student's Name: "))
    print(f"{name}'s marks:{(dic[name])}")
except KeyError:
    print("Student not found")