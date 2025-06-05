import pytest
from modules.GetGoals import GetGoals
from modules.CreateGoal import CreateGoal
from modules.DeleteGoal import DeleteGoal

class TestCreateGoal:

    @pytest.fixture(autouse=True)
    def setup(self):

        self.get_goals = GetGoals()
        self.delete_goal = DeleteGoal()
        self.create_goal = CreateGoal()

    @pytest.fixture(scope="function", autouse=True)
    def teardown(self):
        yield
        self.delete_goal.delete_goal(self.delete_goal.env_response().get('id'))

    def test_create_goal_and_return_200(self):
        assert self.create_goal.create_goal_with_random_name().status_code == 200

    def test_POST_request_with_valid_body_from_file_with_correct_name(self):
        response = self.create_goal.create_goal_with_file()
        assert response.json()['goal']['name'] in self.get_goals.get_goals().text

    def test_POST_request_without_auth(self):
        assert self.create_goal.create_goal_without_auth().status_code == 400

    def test_get_goal_validate_schema(self):
        assert self.create_goal.create_goal_schema_validate()