from http import client

# from fastapi import FastAPI
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Wikipedia API. Call /search or /wiki"}


def test_read_search():
    response = client.get("/search/obama")
    assert response.status_code == 200
    assert response.json() == {
        "Result": [
            "Barack Obama",
            "Michelle Obama",
            "Presidency of Barack Obama",
            "Barack Obama Sr.",
            "Family of Barack Obama",
            "Barack Obama citizenship conspiracy theories",
            "Obama (surname)",
            "Obama (disambiguation)",
            "Barack Obama 2008 presidential campaign",
            "2008 United States presidential election",
        ]
    }
