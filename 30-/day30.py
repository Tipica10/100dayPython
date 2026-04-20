#FileNotFound
from idlelib.autocomplete import FILES

# try:
#     file = open("a_file.txt")
#     dictionary = {"key": "value"}
#     print(dictionary["swdefr"])
# except FileNotFoundError:            #with just the one except (wihtout filenotfounderror specfics, the code would have ignored the keyerror in line 7
#     file = open("a_file.txt", "w")
#     file.write("Something")
# except KeyError as error_message:
#     print(f"This key {error_message} does not exist")
# else:
#     content = file.read()
#     print(content)
#     #if jas exception, else block will never be reached
# finally:
#     # file.close()
#     #this is executed regardless of everything
#     raise KeyError("This is an error that I made up")
#


height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human Height should not be over 3 meters. ")

bmi = weight / height ** 2
print(bmi)