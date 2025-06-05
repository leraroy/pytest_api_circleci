from typing import Tuple

import requests
import json
from pathlib import Path
from jsonschema import validate
from jsonschema.exceptions import ValidationError
from helper.config import *
from helper.GeneratorData import GeneratorData


generator = GeneratorData()


class BasePage:

    def __init__(self):
        self.API_URL = str(API_URL),
        self.TOKEN = str(TOKEN),
        self.TEAM_ID = str(TEAM_ID)
        self.FOLDER_ID = str(FOLDER_ID)

    def env_response(self):
        data = {
            "name": "",
            "id": ""
        }

        return data

    def sent_request(self, method, uri, body=None):
        return requests.request(method=method,
                                url=f"{API_URL}{uri}",
                                json=body,
                                headers={
                                    'Authorization': TOKEN,
                                    'Content-Type': 'application/json'
                                })


    def sent_request_without_auth(self, method, uri, body=""):
        return requests.request(method=method,
                                url=f"{API_URL}{uri}",
                                data=body,
                                headers={
                                    'Authorization': '',
                                    'Content-Type': 'application/json'
                                })

    def load_schema(self, filename):
        project_root = Path(__file__).resolve().parent.parent
        path_body = project_root / 'schemas' / filename

        with open(path_body, 'r') as file:
            return json.load(file)

    def validate_schema(self, func, path):
        schema = self.load_schema(path)
        print(schema)
        response = func

        try:
            validate(instance=response, schema=schema)
            print("OK validate")
            return True
        except ValidationError as error:
            return False, f'Error: {error.message}'

    def read_path_body_with_random_fields(self, filename):
        project_root = Path(__file__).resolve().parent.parent
        path_body = project_root / 'helper' / filename

        with open(path_body, 'r') as json_file:
            data = json.load(json_file)
            data["name"] = generator.name
            data["due_date"] = generator.due_date
            data["description"] = generator.description
            data["multiple_owners"] = generator.multiple_owners
            data["color"] = generator.color
            return data

