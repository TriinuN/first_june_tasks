import pytest


@pytest.fixture
def mock_file():
    return "mock.csv"


@pytest.fixture
def test_list_48():
    return [
        {
            "id": "1",
            "first_name": "Elyse",
            "last_name": "D'Alessio",
            "email": "edalessio0@upenn.edu",
            "gender": "Female",
            "age": "48"
        }
    ]


@pytest.fixture
def test_list_13():
    return [
        {
            "id": "1",
            "first_name": "Elyse",
            "last_name": "D'Alessio",
            "email": "edalessio0@upenn.edu",
            "gender": "Female",
            "age": "13"
        }
    ]