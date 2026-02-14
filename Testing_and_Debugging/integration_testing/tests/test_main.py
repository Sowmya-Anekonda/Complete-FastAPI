from fastapi.testclient import TestClient
from Testing_and_Debugging.integration_testing.app.main import app

client = TestClient(app)


def test_eligibility_pass():
    payload = {
        'income': 60000,
        'age': 25,
        'employment_status': 'employed'
    }
    response = client.post('/loan-eligibility', json=payload)
    assert response.status_code == 200 
    assert response.json() == {'eligible': True}


def test_eligibility_fail():
    payload = {
        'income': 6000,
        'age': 25,
        'employment_status': 'employed'
    }
    response = client.post('/loan-eligibility', json=payload)
    assert response.status_code == 200 
    assert response.json() == {'eligible': False}