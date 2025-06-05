from modules.base_page import BasePage
from helper.config import *


class GetGoals(BasePage):

    def __init__(self):
        super().__init__()
        self.URI = f"/team/{TEAM_ID}/goal"

    def get_goals(self):
        return self.sent_request("GET", self.URI)

    def get_goals_without_auth(self):
        return self.sent_request_without_auth("GET", self.URI)

    def get_goals_schema_validate(self):
        return self.validate_schema(func=self.get_goals().json(), path="get_goals_schema.json")


