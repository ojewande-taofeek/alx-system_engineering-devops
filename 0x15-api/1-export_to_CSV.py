#!/usr/bin/python3
"""
    Export data in the CSV format
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
    filename = "{}.csv".format(emp_id)
    BASE_URL = "https://jsonplaceholder.typicode.com"
    user_response = requests.get("{}/users".format(BASE_URL))
    if user_response.status_code == 200:
        user_json = user_response.json()
        for user in user_json:
            if user["id"] == emp_id:
                emp_username = user["username"]
                break
    todo_response = requests.get("{}/todos".format(BASE_URL))
    if todo_response.status_code == 200:
        todo_json = todo_response.json()
        with open(filename, 'a', encoding="utf-8") as new_file:
            for item in todo_json:
                if item["userId"] == emp_id:
                    text = '"{}","{}","{}","{}"\n'.format(emp_id, emp_username,
                                                          item["completed"],
                                                          item["title"])
                    new_file.write(text)
    requests.post("{}/posts".format(BASE_URL), data=filename)
