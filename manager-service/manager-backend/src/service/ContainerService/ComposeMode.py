from __future__ import annotations
from enum import Enum


class ComposeMode(Enum):
    DEV = "DEV"
    PROD = "PROD"

    @staticmethod
    def factory(data:str)->ComposeMode:
        data = data.upper()
        for mode in ComposeMode:
            if data == mode.value:
                return mode
        raise ValueError
