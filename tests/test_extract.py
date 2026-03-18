import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_submit_and_get_task(monkeypatch):
    # Mock Celery task
    class MockTask:
        id = "123"
        status = "SUCCESS"
        result = "Mock result"

    monkeypatch.setattr("app.api.endpoints.extract.extract_task.delay", lambda url: MockTask())

    # Submit task
    response = client.post("/api/extract", json={"url": "https://example.com"})
    assert response.status_code == 200
    assert response.json()["task_id"] == "123"

    # Get task
    response_get = client.get("/api/task/123")
    assert response_get.status_code == 200
    data = response_get.json()
    assert data["status"] == "SUCCESS"
    assert data["result"] == "Mock result"
