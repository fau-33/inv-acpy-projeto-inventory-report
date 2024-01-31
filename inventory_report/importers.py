import json
from typing import Dict, List, Type
from inventory_report.product import Product
from abc import ABC, abstractmethod


class Importer(ABC):
    def __init__(self, path: str):
        self.path = path

    @abstractmethod
    def import_data(self) -> List[Product]:
        pass


class JsonImporter(Importer):
    def import_data(self) -> List[Product]:
        with open(self.path, "r") as file:
            data = json.load(file)

        products = []
        for item in data:
            product = Product(
                id=str(item.get("id")),
                product_name=str(item.get("product_name")),
                company_name=str(item.get("company_name")),
                manufacturing_date=str(item.get("manufacturing_date")),
                expiration_date=str(item.get("expiration_date")),
                serial_number=str(item.get("serial_number")),
                storage_instructions=str(item.get("storage_instructions")),
            )
            products.append(product)

        return products


class CsvImporter:
    pass


# Não altere a variável abaixo

IMPORTERS: Dict[str, Type[Importer]] = {
    "json": JsonImporter,
    "csv": CsvImporter,
}
