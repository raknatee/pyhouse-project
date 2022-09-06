from fastapi.testclient import TestClient
from main import app
client = TestClient(app)
def test_get_imagename():
    resp = client.get("/manager/api/images")
    images = resp.json()
    assert len(images["images"]) > 0