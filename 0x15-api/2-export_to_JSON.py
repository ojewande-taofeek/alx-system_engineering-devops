#!/usr/bin/python3
"""
    Export json file to the jsonplaceholder
"""
import json
import requests
from sys import argv


if __name__ == "__main__":
    if len(argv) > 2:
        exit(1)
    try:
        emp_id = int(argv[1])
    except Exception:
        exit(1)
    filename = "{}.json".format(emp_id)
    BASE_URL = "https://jsonplaceholder.typicode.com"
    user_response = requests.get("{}/users".format(BASE_URL))
    if user_response.status_code == 200:
        user_json = user_response.json()
        for user in user_json:
            if user.get("id") == emp_id:
                user_name = user.get("username")
                break
    todo_response = requests.get("{}/todos".format(BASE_URL))
    if todo_response.status_code == 200:
        todo_json = todo_response.json()
        dict_list = list()
        for item in todo_json:
            item_dict = dict()
            if item.get("userId") == emp_id:
                item_dict.update({"task": item.get("title")})
                item_dict.update({"completed": item.get("completed")})
                item_dict.update({"username": user_name})
                dict_list.append(item_dict)
    emp_id = str(emp_id)
    user_dict = dict()
    user_dict.update({emp_id: dict_list})
    with open(filename, "w", encoding="utf-8") as new_file:
        json.dump(user_dict, new_file)
    requests.post("{}/posts".format(BASE_URL), data=filename)
