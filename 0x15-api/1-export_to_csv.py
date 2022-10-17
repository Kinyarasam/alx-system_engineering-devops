#!/usr/bin/python3
""" Script that uses Rest API

Returns:
    Employee information about his/her TODO list progress.
Notes:
    Implemented Using Recursion
"""

import requests
import sys
import re


"""REST API url"""
REST_API = 'https://jsonplaceholder.typicode.com'
ID = sys.argv[1]


if __name__ == "__main__":
    if len(sys.argv) > 1:
        if re.fullmatch(r'\d+', ID):
            employee_id = int(ID)
            employee_res = requests.get('{}/users/{}'.format(
                REST_API,
                employee_id)).json()
            todos_res = requests.get('{}/todos'.format(
                REST_API)).json()
            employee_name = employee_res.get('name')
            todos = list(filter(
                lambda x: x.get('userId') == employee_id, todos_res))
            with open(
                    '{}.csv'.format(employee_id),
                    'w',
                    encoding='utf-8',
                    ) as file:
                for todo in todos:
                    file.write(
                            '"{}","{}","{}","{}"\n'.format(
                                employee_id,
                                employee_name,
                                todo.get('completed'),
                                todo.get('title')
                                )
                            )
