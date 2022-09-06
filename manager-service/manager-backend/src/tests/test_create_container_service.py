from fastapi.testclient import TestClient
from main import app
client = TestClient(app)


def test_create_container():
    resp = client.post("/manager/api/create_container",json={
        "docker_compose_mode":"DEV",
        "docker_image_name":"pyhouse-image-global-base-cpu:version1",
        "attach_gpu":False
    })
    