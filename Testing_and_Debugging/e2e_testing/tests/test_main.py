from fastapi.testclient import TestClient
from Testing_and_Debugging.e2e_testing.app.main import app

client = TestClient(app)


def test_eligibility_pass():
    response = client.post(
        '/loan-eligibility',
        json={
            'income': 60000,
            'age': 60,
            'employment_status': 'employed'
        }
    )

    assert response.status_code == 200
    assert response.json() == {'eligibility': True}


def test_eligibility_fail():
    response = client.post(
        '/loan-eligibility',
        json={
            'income': 6000,
            'age': 10,
            'employment_status': 'unemployed'
        }
    )

    assert response.status_code == 200
    assert response.json() == {'eligibility': False}