from abc import ABC, abstractmethod
from typing import Dict, Type


class Importer(ABC):
    def __init__(self, path: str):
        self.path = path

    @abstractmethod
    def import_data(self) -> list:
        pass


class JsonImporter:
    def import_data(self) -> list:
        return []


class CsvImporter:
    def import_data(self) -> list:
        return []


# Não altere a variável abaixo

IMPORTERS: Dict[str, Type[Importer]] = {
    "json": JsonImporter,
    "csv": CsvImporter,
}
