from inventory_report.product import Product
import pytest

# Dados de exemplo para o teste
product_id = "123"
company_name = "Example Company"
product_name = "Example Product"
manufacturing_date = "2023-01-30"
expiration_date = "2024-01-30"
serial_number = "ABC123"
storage_instructions = "Store in a cool and dry place."


def test_product_report() -> None:
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

    # Testar o método __str__
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

    # Testar cada trecho individualmente
    assert product_id in str(product)
    assert product_name in str(product)
    assert serial_number in str(product)
    assert manufacturing_date in str(product)
    assert company_name in str(product)
    assert expiration_date in str(product)
    assert storage_instructions in str(product)


if __name__ == "__main__":
    pytest.main(["-v", "--color=yes", "test_product_report.py"])
