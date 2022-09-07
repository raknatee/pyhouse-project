from fastapi.testclient import TestClient
from main import app
client = TestClient(app)


def test_create_container():
    assert False
    resp = client.post("/manager/api/create_container",json={
        "docker_image_name":"pyhouse-image-global-base-cpu:version1",
        "attach_gpu":False
    })
def test_get_containers():
    resp = client.get("/manager/api/containers")
    assert False