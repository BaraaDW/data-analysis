import pandas as pd


print(f' Version : {pd.__version__}')

# __________________Introduction___________________
# info = pd.read_csv('data.csv')
# print(info)
# print(type(info))  # DataFrame
# print(len(info))  # count of rows [without column names]

# print(info[:1])  # show first row + [-with column name-]

# print(info.to_string())
# print(type(info.to_string()))  # str

# ______________________Started_______________________
# data_set = {key : "column_name", value : [rows]}
# data_set = {
#   'cars': ["BMW", "Volvo", "Ford"],
#   'passings': [3, 7, 2]
# }

# data_frame = pd.DataFrame(data_set)

# print(data_frame)
# print(type(data_frame))  # DataFrame
# print(len(data_frame))  # count of rows [without column names]

# ______________________Series_______________________
# a = [1, 7, 2]

# series = pd.Series(a)

# print(series)  # Series
# print(series[1])  # like list

# series = pd.Series(a, index=["x", "y", "z"])  # [[change index]]

# print(series)  # type is Series
# print(series['y'])  # get value by new index


# ------------------
# calories = {"day1": 420, "day2": 380, "day3": 390}

# series = pd.Series(calories)

# print(series)  # type is Series
# print(series['day2'])  # like dictionary

# series = pd.Series(calories, index=["day1", "day3"])  # [[filter]] --> delete 'day2'

# print(series)
# print(series['day1'])

# ______________________DataFrames______________________
