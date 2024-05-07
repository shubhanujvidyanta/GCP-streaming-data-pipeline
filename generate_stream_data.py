with open("utils/setup.py") as file:
    exec(file.read())


# read from car prices csv file and push to pub sub service every 5 minutes data for each year.
import pandas as pd
import time
import json
from poc_prj_001.src.utils import pub_sub
from poc_prj_001 import data

sales_data = pd.read_csv('../data/car_prices.csv')
year_list = (sorted(sales_data['year'].unique()))

for year in year_list:
    mask = sales_data['year'] == year
    yearly_sales_data = sales_data[mask]
    for i in yearly_sales_data.index:
        row_json = yearly_sales_data.loc[i].to_json()
        print(row_json)
        print(f'Total records:{i}')
        print(f'message_id:{pub_sub.push_message("new_sales_data", row_json)}')
    # yearly_sales_data.to_csv(f'../data/temp/yearly_sales_data-{year}.csv')
    # pub_sub.push_message('new_sales_data', json.dumps(yearly_sales_data.to_json(orient='records', lines=True)))
    # result = yearly_sales_data.to_json(orient='records')
    # result_json = json.loads(result)
    # print(type(result))
    # print(type(result_json[0]))
    # print(result_json)
    # print(f'message_id:{pub_sub.push_message("new_sales_data", json.dumps(result_json))}')
    time.sleep(30)

# print(sales_data.head())