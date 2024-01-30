import pytest
from inventory_report.product import Product


def test_create_product() -> None:
    # Dados de exemplo para o teste
    product_id = "123"
    company_name = "Example Company"
    product_name = "Example Product"
    manufacturing_date = "2023-01-30"
    expiration_date = "2024-01-30"
    serial_number = "ABC123"
    storage_instructions = "Store in a cool and dry place."

    # Criar um objeto Product usando o construtor
    product = Product(
        id=product_id,
        company_name=company_name,
        product_name=product_name,
        manufacturing_date=manufacturing_date,
        expiration_date=expiration_date,
        serial_number=serial_number,
        storage_instructions=storage_instructions
    )

    # Testar cada atributo individualmente
    assert product.id == product_id
    assert product.company_name == company_name
    assert product.product_name == product_name
    assert product.manufacturing_date == manufacturing_date
    assert product.expiration_date == expiration_date
    assert product.serial_number == serial_number
    assert product.storage_instructions == storage_instructions

    # Testar a função __str__
    expected_output = (
        f"The product {product_id} - {product_name} "
        f"with serial number {serial_number} "
        f"manufactured on {manufacturing_date} "
        f"by the company {company_name} "
        f"valid until {expiration_date} "
        f"must be stored according to the following instructions: "
        f"{storage_instructions}."
    )
    assert str(product) == expected_output


if __name__ == "__main__":
    pytest.main(["-v", "--color=yes", "test_product.py"])
