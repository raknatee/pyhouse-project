import os
from service.ContainerService.ComposeMode import ComposeMode


BASE_PATH:str = "/manager/api"
APPLICATION_MODE:ComposeMode = ComposeMode.factory(os.environ['app_mode'])