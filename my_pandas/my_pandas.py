import pandas as pd

# series

# result = pd.Series([84,91,77], index=["sara","saim","ahmed"])
# print(result["saim"])

# result2 = pd.Series({"ali": 10, "hamza": 14, "saqib": 16})
# print(result2["saqib"])

# data = {
#     "class": [1,2,3,4],
#     "total_students": [33,28,41,25],
#     "present": [30,27,37,25],
#     "absent": [3,1,4,0]
# }
# table = pd.DataFrame(data)

# inspecting dataframes

# print(table.head(2))
# print(table.info())
# print(table.describe())
# print(table.columns)
# print(table.shape)

# selecting columns and rows

# print(table["present"])
# print(table[["class","absent"]])
# first_row = table.iloc[1]
# print(first_row)
# row = table.loc[2]
# print(row)
# data = table[table["class"]<= 3][["present","absent"]]
# print(data)

# adding and removing columns

# table["pass"] = [28,28,40,21]
# print(table)
# table.drop("pass", axis=1, inplace=True)
# print(table)
# table.loc[4] = [5,50,48,2]
# table.drop(4, axis=0, inplace=True)
# print(table)
# pd.set_option("display.max_rows", 100)     # show up to 100 rows
# pd.set_option("display.max_columns", None) # show ALL columns         this function is not good

file = pd.read_csv("first_copy.csv")
# file.sort_values(by=[" Department"," Degree Title"," Year of Student"," CGPA"," HSC Percentage"], ascending=False, inplace=True)
# print(file.head()) 
# print(file.shape)
# count_selected = file.loc[file[" Status"] == "Selected"]
# print(count_selected)
count1 = file[" Department"].value_counts()["Management Sciences"]
print(count1)
count = file[(file[" Department"] == "Management Sciences") & (file[" Year of Student"] == 1) & (file[" Status"] == "Selected")].shape[0]
print(count)
count2 = file[(file[" Department"] == "Management Sciences") & (file[" Year of Student"] == 2) & (file[" Status"] == "Selected")].shape[0]
print(count2)
count3 = file[(file[" Department"] == "Management Sciences") & (file[" Year of Student"] == 3) & (file[" Status"] == "Selected")].shape[0]
print(count3)