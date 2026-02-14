import numpy as np
from fastapi.testclient import TestClient
from unittest.mock import patch
from main import app 

client = TestClient(app)


def test_predict_with_mock():
    with patch('model.model.predict') as mock_predict:
        mock_predict.return_value = [99]
        response = client.post(
            '/predict',
            json={
                "sepal_length": 3.4,
                "sepal_width": 2.6,
                "petal_length": 6.4,
                "petal_width": 1.9
            }
        )

        assert response.status_code == 200 
        assert response.json() == {'prediction': 99}
        # mock_predict.assert_called_once_with(np.array([[5.5, 2.1, 4.3, 1.25]]))
    