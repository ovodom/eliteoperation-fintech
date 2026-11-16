from app.main import app

client = app.test_client()


def test_home_endpoint():
    response = client.get("/")

    assert response.status_code == 200
    assert response.get_json() == {
        "message": "Welcome to EliteOperation Fintech API",
        "status": "running"
    }


def test_health_endpoint():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.get_json() == {
        "status": "healthy"
    }