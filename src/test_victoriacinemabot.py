import pytest
from movie import Film
import os

# Mocking requests module and its methods
class MockResponse:
    def __init__(self, content):
        self.content = content

def mock_get(url):
    if "https://www.victoriacinema.it/victoria_cinema/index.php" in url:
        with open("website.html", "rb") as f:
            return MockResponse(f.read())
    else:
        return MockResponse(b"")

@pytest.fixture
def mock_requests(monkeypatch):
    monkeypatch.setattr("requests.get", mock_get)

def test_web_scraping(mock_requests):
    # Call the web_scraping method
    Film.web_scraping()
    # Check if website.html file is created
    assert "website.html" in os.listdir()

def test_odd_movie(mock_requests):
   # Call the Odd_Movie method
   messageOdd = Film.Odd_Movie()
   # Check if messageOdd is a list and not empty
   assert isinstance(messageOdd, list)
   assert messageOdd

def test_even_movie(mock_requests):
   # Call the Even_Movie method
   messageEven = Film.Even_Movie()
   # Check if messageEven is a list and not empty
   assert isinstance(messageEven, list)
   assert messageEven
