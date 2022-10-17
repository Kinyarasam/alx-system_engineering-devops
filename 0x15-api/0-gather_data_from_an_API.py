#!/usr/bin/python3
""" Script that uses Rest API

Returns:
    Employee information about his/her TODO list progress.
"""

import requests
import sys
import re


# REST API url
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
            todos_done = list(filter(lambda x: x.get('completed'), todos))
            print(
                    'Employee {} is done with tasks({}/{}):'.format(
                        employee_name,
                        len(todos_done),
                        len(todos)
                        )
                    )
            for todos in todos_done:
                print('\t{}'.format(todos.get('title')))
