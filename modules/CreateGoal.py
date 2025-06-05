from modules.base_page import BasePage
from helper.config import *
from helper.GeneratorData import GeneratorData

class CreateGoal(BasePage):

    def __init__(self):
        super().__init__()
        self.URI = f"/team/{TEAM_ID}/goal"

    def create_goal(self, body):
        response = self.sent_request("POST", self.URI, body)
        self.env_response()['id'] = response.json()['goal']['id']
        self.env_response()['name'] = response.json()['goal']['name']
        return response

    def create_goal_with_random_name(self):
        response = self.create_goal({"name": GeneratorData().name})
        self.env_response()['id'] = response.json()['goal']['id']
        self.env_response()['name'] = response.json()['goal']['name']
        return response

    def create_goal_with_file(self):
        data = self.read_path_body_with_random_fields("example.json")
        response = self.create_goal(data)
        self.env_response()['id'] = response.json()['goal']['id']
        self.env_response()['name'] = response.json()['goal']['name']
        return response

    def create_goal_without_auth(self):
        return self.sent_request_without_auth("POST", self.URI)

    def create_goal_schema_validate(self):
        return self.validate_schema(func=self.create_goal_with_random_name().json(), path="create_goal_schema.json")
