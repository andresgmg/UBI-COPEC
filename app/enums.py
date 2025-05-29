from enum import Enum


class UbicacionType(str, Enum):
    PRONTO = "pronto"
    BENCINERA = "bencinera"
    SERVICIO = "servicio"
    OTRO = "otros"
