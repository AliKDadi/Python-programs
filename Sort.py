#BSCIT-05-0836/2022
#Sort list of Dictionary by given key
def list_in_dict():
#prompt user to enter list of dictionaries
    num_people=int(input("Enter the number of dictionaries: "))
    people=[]
    for i in range(num_people):
        name=input(f"Enter name for person{i+1}: ")
        age=int(input(f"Enter the age for person{i+1}: "))
        people.append({"name": name, "age": age})

    sort=input("Enter the key to sort by: ")
    sorted_people=sorted(people, key=lambda x: x[sort])
    return sorted_people
print("Sorted list: ",list_in_dict())
