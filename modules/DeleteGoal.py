from modules.base_page import BasePage


class DeleteGoal(BasePage):

    def __init__(self):
        super().__init__()
        self.URI = f"/goal"

    def delete_goal(self, goal_id):
        return self.sent_request("DELETE", f"{self.URI}/{goal_id}")

    def delete_goal_with_invalid_ID(self):
        return self.sent_request("DELETE", f"{self.URI}/b63b8dbe-8556-4147-dc22-d32a405a66bd")

    def delete_goal_without_auth(self, goal_id):
        return self.sent_request_without_auth('DELETE', f"{self.URI}/{goal_id}")

