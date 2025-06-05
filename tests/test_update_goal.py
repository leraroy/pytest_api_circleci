# import pytest
# from modules.GetGoal import GetGoal
# from modules.UpdateGoal import UpdateGoal
# from modules.DeleteGoal import DeleteGoal
#
# class TestUpdateGoal:
#
#     @pytest.fixture(autouse=True)
#     def setup_and_teardown(self, create_goal_with_delete):
#         self.get_goal = GetGoal()
#         self.update_goal = UpdateGoal()
#         self.delete_goal = DeleteGoal()
#
#         self.goal_name = create_goal_with_delete.get('name')
#         self.goal_id = create_goal_with_delete.get('id')
#
#
#     def test_UPDATE_request_and_return_200(self):
#         assert self.update_goal.update_random_name_goal(self.goal_id).status_code == 200
#
#     def test_UPDATE_request_contain_correct_name(self):
#         response = self.update_goal.update_random_name_goal(self.goal_id)
#         assert response.json()['goal']['name'] in self.get_goal.get_goal(self.goal_id).text
#
#     def test_UPDATE_request_without_auth(self):
#         assert self.update_goal.update_without_auth(self.goal_id).status_code == 400
