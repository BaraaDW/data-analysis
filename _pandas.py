import pandas as pd


print(pd.__version__)

# __________________Introduction___________________
# info = pd.read_csv('data.csv')
# print(info)
# print(type(info))  # DataFrame

# print(info[:1])  # show first row + [-with column name-]

# print(info.to_string())
# print(type(info.to_string()))  # str

# ______________________Started_______________________
# data_set = {key : "column_name", value : [rows]}
data_set = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}

data_frame = pd.DataFrame(data_set)

print(data_frame)
print(type(data_frame))  # DataFrame

# ______________________Series_______________________

