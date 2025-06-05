import pytest
from modules.CreateGoal import CreateGoal
from modules.DeleteGoal import DeleteGoal

@pytest.fixture(scope="class")
def create_goal_with_delete():
    response = CreateGoal().create_goal_with_random_name()
    data = {
        'name': response.json()['goal']['name'],
        'id': response.json()['goal']['id']
    }
    print(f"Name: {data['name']} ID: {data['id']}")

    yield data

    DeleteGoal().delete_goal(data['id'])

@pytest.fixture(scope="class")
def create_goal():
    response = CreateGoal().create_goal_with_random_name()
    data = {
        'name': response.json()['goal']['name'],
        'id': response.json()['goal']['id']
    }
    print(f"Name: {data['name']} ID: {data['id']}")

    return data



