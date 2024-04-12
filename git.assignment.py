#Created a simple console that takes in member info and writes it to a file
#please feel free to append, modify, delete as you please :))

# Opening the txt the file in append mode


with open('members_info.txt', 'a') as file:

    # Ask each member of the group for their information
    name = input("Enter your name: ")
    file.write(f"Name: {name}\n")

    age = input("Enter your age: ")
    file.write(f"Age: {age}\n")

    hobby = input("Whats your current hobby? ")
    file.write(f"Current hobby: {hobby}\n")

    food = input("What is your favourte dish? ")
    file.write(f"Faviourte dish: {food}\n")
    
    destination = input("Enter your favorite traveling destination: ")
    file.write(f"Favorite Traveling Destination: {destination}\n")

    have_pet = input("Do you have a pet? (yes/no) ")
    if have_pet.lower() == 'yes':
        pet_name = input("Enter your pet's name: ")
        file.write(f"Pet Name: {pet_name}\n")
    
    character = input("Who is your favourite fictional character? ")
    file.write(f"Favourite Fictional Character: {character}\n")

    # Add a newline to separate each member's information
    file.write('\n')

print("Member information has been stored to members_info.txt.")

<<<<<<< HEAD
#Salma
=======
#Deena: added a character variable in dictionary
>>>>>>> main
