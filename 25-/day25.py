# csv stands for comma seperated values

# with open("weather_data.csv") as data:
#     contents = data.readlines()
#
# print(contents)

# import csv
#
# with open("weather_data.csv") as data:
#     data = csv.reader(data)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
# print(temperatures)

import pandas

#dataframe is like any excel sheet table or csv
#series represents a columns or list

# data = pandas.read_csv("weather_data.csv")
# print(data["temp"])

# data_dict = data.to_dict()
# print(data_dict)
#
# data["temp"].mean()
#
# maxx = data["temp"].max()
# print(maxx)

#Get data in rows
# print(data[data.day == "Monday"])

# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# print(monday.condition)

#create dataframe from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76,56,65]
# }
# data = pandas.DataFrame(data_dict)
# print(data)
# data.to_csv("new_data.csv")
#

squirrel = pandas.read_csv("squirrel_Data.csv")
fur_colour = squirrel["Primary Fur Color"]

fur_list = fur_colour.to_list()

grey_count = 0
red_count = 0
black_count = 0

for fur in fur_list:
    if fur == "Gray":
        grey_count += 1
    if fur == "Cinnamon":
        red_count += 1
    if fur == "Black":
        black_count += 1

# grey_squirrels = len(squirrel[squirrel["Primary Fur Color"] == "Gray"])
# black_squirrels = len(squirrel[squirrel["Primary Fur Color"] == "Black"])
# red_squirrels = len(squirrel[squirrel["Primary Fur Color"] == "Cinnamon"])

data_dict = {
    "Fur Color": ["grey", "red", "black"],
    "Count": [grey_count, red_count, black_count]
}

data = pandas.DataFrame(data_dict)
print(data)
data.to_csv("squirrel_count.csv")


