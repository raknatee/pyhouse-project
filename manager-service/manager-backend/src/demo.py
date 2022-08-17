import docker # type:ignore
from docker import DockerClient

client:DockerClient = docker.DockerClient(base_url='unix://var/run/docker.sock')
for container in client.containers.list():
    print(container.name)

my_network = [n for n in client.networks.list() if "pyhouse" in n.name][0]
print(f"{my_network.name=} {my_network.id}")

print("Hi")