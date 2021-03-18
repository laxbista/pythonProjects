import pandas

data = pandas.read_csv("squirrel_data.csv")
# Get gray squirell rows
grey_squirrels = data[data["Primary Fur Color"] == "Gray"]

#Get squirrels counts
grey_squirrels_counts = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_counts = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_counts = len(data[data["Primary Fur Color"] == "Black"])

#Create a data Frame of counts and save to csv file
data_dict = {
    "Fur Colors": ["Gray","Cinnamon","Black"],
    "Count": [grey_squirrels_counts,red_squirrels_counts,black_squirrels_counts]
}
df = pandas.DataFrame(data_dict)
df.to_csv("squirrelsCounts.csv")
