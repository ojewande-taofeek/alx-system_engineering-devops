#!/usr/bin/python3
"""
    Uses the JSONplaceholder
    Returns the list progress for an employee
"""
import json
import requests
from sys import argv


if __name__ == "__main__":
    if (len(argv) > 2):  # checks excess args
        exit()
    try:
        emp_id = int(argv[1])  # raise error if not int
    except Exception as e:
        exit(1)
    BASE_URL = "https://jsonplaceholder.typicode.com"
    todo_response = requests.get("{}/todos".format(BASE_URL))
    if todo_response.status_code == 200:
        todo_json = todo_response.json()
        task_com = list()  # list of all completed tasks
        count_com = 0  # count the number of tasks completed
        count_task = 0  # count the total number of tasks
        for item in todo_json:  # todo_json is a list and item is dict
            if item["userId"] == emp_id:
                count_task += 1
                if item["completed"]:
                    task_com.append(item["title"])
                    count_com += 1
    emp_response = requests.get("{}/users".format(BASE_URL))
    if emp_response.status_code == 200:
        emp_json = emp_response.json()
        for user in emp_json:
            if user["id"] == emp_id:
                emp_name = user["name"]
                break
    print("Employee {} is done with tasks({}/{}):".format(emp_name, count_com,
                                                          count_task))
    for compl_task in task_com:
        print("\t{}".format(compl_task))
