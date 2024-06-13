#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

# Turn invited names to a list
with open("./Input/Names/invited_names.txt", "r") as file:
    invited_names = file.read().splitlines()

#Get letter info
with open ("./Input/Letters/starting_letter.txt", "r") as file:
    letters_info = file.read()

for invited_name in invited_names:
    file_name = f"./Output/ReadyToSend/{invited_name}.txt"
    with open(file_name, 'a') as file:
        new_letters = letters_info.replace("[name]",f"{invited_name}")
        file.write(new_letters)



