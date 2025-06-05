from modules.base_page import BasePage
from helper.config import *
from helper.GeneratorData import GeneratorData

data = GeneratorData()


class UpdateGoal(BasePage):

    def __init__(self):
        super().__init__()
        self.URI = f"/goal"

    def update_goal(self, id, body):
        return self.sent_request("PUT", f"{self.URI}/{id}", body)

    def update_random_name_goal(self, id):
        return self.update_goal(id, {"name": data.name})

    def update_color_goal(self, id):
        return self.update_goal(id, {"color": data.color})

    def update_goal_with_invalid_ID(self):
        return self.update_goal("/goal/1111131", {"name": data.name})

    def update_without_auth(self, id):
        return self.sent_request_without_auth("PUT", f"{self.URI}/{id}", {"name": data.name})
