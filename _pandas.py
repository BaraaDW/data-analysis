import pandas as pd


print(f' Version : {pd.__version__}')

# __________________Introduction___________________
# data_frame = pd.read_csv('data.csv')
# print(data_frame)
# print(type(data_frame))  # DataFrame
# print(len(data_frame))  # count of rows [without column names]

# print(data_frame[:1])  # show first row + [-with column name-]

# print(data_frame.to_string())
# print(type(data_frame.to_string()))  # str

# ______________________Started_______________________
# data_set = {key : "column_name", value : [rows]}
# data_set = {
#   'cars': ["BMW", "Volvo", "Ford"],
#   'passings': [3, 7, 2]
# }

# data_frame = pd.DataFrame(data_set)

# print(data_frame['cars'])  # print column
# print(type(data_frame))  # DataFrame
# print(len(data_frame))  # count of rows [without column names]

# ______________________Series_______________________
# a = [5, 6, 7]

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
# data_set = {
#   "calories": [420, 380, 390],
#   "duration": [50, 40, 45],
#   "meta": [10, 20, 30]
# }

# data_frame = pd.DataFrame(data_set)
# print(data_frame)

# column = data_frame['calories']
# print(column)
# print(column[1])

# columns = data_frame[['calories', 'meta', 'duration']]
# print(columns)

# row = data_frame.loc[0]  # Series
# print(row)
# print(row['calories'])  # 420

# rows = data_frame.loc[0:1]  # DataFrame
# print(rows)
# print(rows['calories'])  # 420 - 380

# rows = data_frame.loc[[0, 2]]  # DataFrame
# print(rows)
# print(rows['duration'])  # 50 - 45

# --------------------

# data_frame = pd.DataFrame(data_set, index=['day1', 'day2', 'day3'])
# print(data_frame)

# column = data_frame['calories']
# print(column)
# print(column['day2'])

# row = data_frame.loc['day1']  # Series
# print(row)
# print(row['calories'])  # 420

# rows = data_frame.loc['day1':'day2']  # DataFrame
# print(rows)
# print(rows['calories'])  # 420 - 380

# rows = data_frame.loc[['day1', 'day3']]  # DataFrame
# print(rows)
# print(rows['duration'])  # 50 - 45

# ______________________Read CSV______________________

# data_frame = pd.read_csv('data_set.csv')

# pd.options.display.max_rows = 2  # max rows that system show

# print(len(data_frame))

# print(data_frame)

# print(data_frame.head())  # By default will get first 5 rows
# print(data_frame.head(10))  # first 10 rows

# print(data_frame.tail())  # By default will get last 5 rows
# print(data_frame.tail(10))  # last 10 rows

# ______________________Write CSV______________________

# data_set = {'item': ['iphone5'], 'count': [50], 'cost': [500]}

# data_frame = pd.DataFrame(data_set)
# print(data_frame)

# first time
# columns_name = ['item', 'count', 'cost']
# data_frame.to_csv("insert.csv", index=True, header=columns_name, sep=',', mode='a')

# second time
# data_frame.to_csv("insert.csv", index=True, header=False, sep=',', mode='a')

# (index) --> insert the index as a cell
# (header) --> insert the columns name (-at the first-)
# (sep) must be ',' to insert each value in cell
# (mode = a) to Append DataFrame to existing CSV File

# ______________________Read JSON______________________

