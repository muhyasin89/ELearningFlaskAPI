from flask import url_for


def test_home(app):
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
