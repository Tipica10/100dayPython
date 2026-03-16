#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


with open("./Input/Names/invited_names.txt", mode = 'r') as file:
    contents = file.readlines()

print(contents)


for name in contents:
    with open("./Input/Letters/starting_letter.txt", mode='a') as template:
        txt = "[name]"
        saved_letter = template.write(txt.replace("[name]",name))


print(saved_letter)

