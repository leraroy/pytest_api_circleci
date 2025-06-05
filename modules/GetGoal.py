import pytest

from modules.base_page import BasePage
from helper.config import *


class GetGoal(BasePage):

    def __init__(self):
        super().__init__()
        self.URI = f"/goal"

    def get_goal(self, id):
        return self.sent_request("GET", f"{self.URI}/{id}")

    def get_goal_without_auth(self, id):
        return self.sent_request_without_auth("GET", f"{self.URI}/{id}")

    def get_goal_schema_validate(self, id):
        return self.validate_schema(func=self.get_goal(id).json(), path="get_goal_schema.json")


