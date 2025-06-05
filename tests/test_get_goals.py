# import pytest
#
# from modules.DeleteGoal import DeleteGoal
# from modules.GetGoals import GetGoals
# from modules.CreateGoal import CreateGoal
#
# class TestGetGoals:
#
#     @pytest.fixture(autouse=True)
#     def setup_and_teardown(self, create_goal_with_delete):
#         self.get_goals = GetGoals()
#         self.create_goal = CreateGoal()
#         self.delete_goal = DeleteGoal()
#
#         self.goal_name = create_goal_with_delete.get('name')
#         self.goal_id = create_goal_with_delete.get('id')
#
#
#     def test_get_goals_return_200(self):
#         response = self.get_goals.get_goals()
#         assert response.status_code == 200
#
#     def test_contain_correct_name_and_id(self):
#         response = self.get_goals.get_goals()
#         assert self.goal_name in response.text
#
#     def test_get_goals_without_auth(self):
#         assert self.get_goals.get_goals_without_auth().status_code == 400
#
#     def test_get_goals_validate_schema(self):
#         assert self.get_goals.get_goals_schema_validate()