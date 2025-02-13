Want_instructions = input("Do you want to see the instructions").lower()

# check the user says yes / no
if Want_instructions == "yes" or Want_instructions == "y":
    print("you said yes")
elif Want_instructions == "no" or Want_instructions == "n":
    print("you said no")
else:
    print("please enter yes / no")
