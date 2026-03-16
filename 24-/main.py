#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


with open("./Input/Names/invited_names.txt") as file:
    contents = file.readlines()



with open("./Input/Letters/starting_letter.txt") as template:
    letter_template = template.read()

for name in contents:
    clean_name = name.strip()
    saved_letter = letter_template.replace("[name]", clean_name)

    with open (f"./Output/ReadyToSend/Letter_to_{clean_name}.txt", "w") as letter_to_send:
        letter_to_send.write(saved_letter)





