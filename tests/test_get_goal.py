import pytest

from modules.DeleteGoal import DeleteGoal
from modules.GetGoal import GetGoal
from modules.CreateGoal import CreateGoal


class TestGetGoal:

    @pytest.fixture(autouse=True)
    def setup_and_teardown(self, create_goal_with_delete):
        self.get_goal = GetGoal()
        self.create_goal = CreateGoal()
        self.delete_goal = DeleteGoal()

        self.goal_name = create_goal_with_delete.get('name')
        self.goal_id = create_goal_with_delete.get('id')

    def test_get_goal_return_200(self):
        assert self.get_goal.get_goal(self.goal_id).status_code == 200

    def test_contain_correct_name(self):
        assert self.goal_name in self.get_goal.get_goal(self.goal_id).text

    def test_get_goal_without_auth(self):
        assert self.get_goal.get_goal_without_auth(self.goal_id).status_code == 400

    def test_get_goal_validate_schema(self):
        assert self.get_goal.get_goal_schema_validate(self.goal_id)