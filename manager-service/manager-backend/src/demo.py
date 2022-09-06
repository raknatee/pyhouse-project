import docker # type:ignore
from docker import DockerClient

client:DockerClient = docker.from_env()
for container in client.containers.list():
    print(container.name)

print(client.images.list()[0].attrs['RepoTags'])
images = [image for image in client.images.list() if "pyhouse-image" in image.attrs["RepoTags"]]



my_network = [n for n in client.networks.list() if "pyhouse" in n.name][0]
print(f"{my_network.name=} {my_network.id}")

print("Hi")