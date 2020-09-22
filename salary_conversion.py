import json
import requests

currencyConverter = requests.get(
    "https://free.currconv.com/api/v7/convert?q=IDR_USD&compact=ultra&apiKey=0df8d46877741711d91a").json()
IDRtoUSD = currencyConverter["IDR_USD"]
data_users = requests.get("http://jsonplaceholder.typicode.com/users").json()

f = open('salary_data.json', 'r')
data_salary = json.load(f)


# function to merge data by id
def join(data_1, data_2):
    join_data = data_1
    for i in range(len(data_1)):
        del (join_data[i]['website'])
        del (join_data[i]['company'])
        for j in range(len(data_2["array"])):
            if data_1[i]["id"] == data_2["array"][j]["id"]:
                join_data[i]["salaryInIDR"] = data_2["array"][j]["salaryInIDR"]
        join_data[i]["salaryInUSD"] = join_data[i]["salaryInIDR"] * IDRtoUSD  # convert IDR to USD
    return join_data


result_data = join(data_users, data_salary)
f.close()
print(result_data)

out_file = open("output_salary_conversion.json", "w")
json.dump(result_data, out_file, indent=6)
out_file.close()
