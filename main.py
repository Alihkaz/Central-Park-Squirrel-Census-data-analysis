#imports
import pandas

data=pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv") #reading the CSV

gray=(data[data["Primary Fur Color"]=="Gray"]) #extracting all the elements having gray color from the fur color column 
gnumber=(len(gray)) #counting them

cinnamon=(data[data["Primary Fur Color"]=="Cinnamon"])
cnumber=(len(cinnamon))

black=(data[data["Primary Fur Color"]=="Black"])
bnumber=(len(black))


color_dict={

  "furcolor":["gray","cinnamon","black"] ,
  "count":[gnumber,cnumber,bnumber]

} #adding the data about the colors to a dictionary , having the color as a key , and the number of squirrel having that color


table=pandas.DataFrame(color_dict) #converting the dictionary to a  new csv 
table.to_csv("color data.csv")
print(table)


