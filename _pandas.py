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

# data_set = {
#   "item": {'a': 'iphone', 'b': 'nokia', 'c': 'samsung'},
#   "count": {'a': '50', 'b': '75', 'c': '100'},
#   "price": {'a': '800', 'b': '200', 'c': '500'}
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
# data_frame = pd.read_json('data.json')
# print(data_frame)

# ______________________Write JSON______________________
# data_set = {
#   "calories": [420, 380, 390],
#   "duration": [50, 40, 45],
#   "meta": [10, 20, 30]
# }

# data_frame = pd.DataFrame(data_set)
# data_frame = pd.DataFrame(data_set, index=['a', 'b', 'c'])
# print(data_frame)

# data_frame.to_json("insert.json")

# ______________________Data Cleaning______________________

data_frame = pd.read_csv('dirtydata.csv')
print(data_frame)  # 32 rows

# __________________________
# (0) Math

# mean = data_frame["Calories"].mean()  # the average value
# print(f'mean is {mean}')

# median = data_frame["Calories"].median()  # the value in the middle, after you have sorted
# print(f'median is {median}')

# mode = data_frame["Calories"].mode()  # the value that appears most frequently.
# print(f'mode is {mode}')

# __________________________
# (1) Empty Value:

# new_data_frame = data_frame.dropna()  # remove all rows that have a value NAN
# print(new_data_frame)  # 29 rows

# data_frame.dropna(inplace=True)
# print(data_frame)  # 29 rows

# data_frame.dropna(subset=['Calories'], inplace=True)
# print(data_frame)

# -----------------------
# data_frame.fillna(130, inplace=True)  # replace empty cell with value
# print(data_frame)

# data_frame["Calories"].fillna(300, inplace=True)
# print(data_frame)

# __________________________
# (2) Wrong Format:

# data_frame['Date'] = pd.to_datetime(data_frame['Date'])
# print(data_frame)

# data_frame.dropna(subset=['Date'], inplace=True)  # dropna (remove row have NAN)
# print(data_frame)

# __________________________
# (3) Wrong Data:

# print(data_frame.loc[7, 'Duration'])    # [ - - DW - - ]

# data_frame.loc[7, 'Duration'] = 45
# print(data_frame)

# for index in data_frame.index:
#     if data_frame.loc[index, "Duration"] > 60:
#         data_frame.loc[index, "Duration"] = 60
# print(data_frame)

# for index in data_frame.index:
#     if data_frame.loc[index, "Duration"] > 120:
#         data_frame.drop(index, inplace=True)      # dropna (remove row have NAN) , drop (remove any row)
# print(data_frame)

# __________________________
# (3) Wrong Data:

# print(data_frame.duplicated())

# data_frame.drop_duplicates(inplace=True)

# ______________________(Data Correlations) Finding Relationships______________________

