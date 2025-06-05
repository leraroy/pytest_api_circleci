import pytest

from modules.DeleteGoal import DeleteGoal
from modules.GetGoals import GetGoals
from modules.CreateGoal import CreateGoal


class TestGetGoal:

    @pytest.fixture(autouse=True)
    def setup_and_teardown(self, create_goal):
        self.get_goals = GetGoals()
        self.create_goal = CreateGoal()
        self.delete_goal = DeleteGoal()

        self.goal_name = create_goal.get('name')
        self.goal_id = create_goal.get('id')


    def test_delete_goal_return_200(self):
        assert self.delete_goal.delete_goal(self.goal_id).status_code == 200

    def test_contain_correct_name_and_id(self, create_goal):
        self.delete_goal.delete_goal(create_goal.get('id'))
        assert create_goal.get('name') not in self.get_goals.get_goals().text

    def test_delete_goal_without_auth(self):
        assert self.delete_goal.delete_goal_without_auth(self.goal_id).status_code == 400

    def test_delete_with_invalid_ID(self):
        assert self.delete_goal.delete_goal_with_invalid_ID().status_code == 404