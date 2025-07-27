import random
import re
import allure
from utils.custom_logger import get_logger

logger = get_logger(__name__)

@allure.feature("Products")
class TestProducts:

    @allure.story("View products page")
    def test_products_page(self, base_url, session):
        url = f"{base_url}/catalog"
        logger.info("Fetching products page...")
        response = session.get(url)
        assert response.status_code == 200
        assert "Products" in response.text

    @allure.story("Search for a product")
    def test_search_product(self, base_url, session):
        products = ["pineapple", "cocktail", "fruit", "juice"]
        search_item = random.choice(products)
        logger.info(f"Searching for product: {search_item}")
        url = f"{base_url}/catalog?searchTerm={search_item}"
        response = session.get(url)
        assert response.status_code == 200
        assert search_item in response.text

    @allure.story("View individual product")
    def test_view_product(self, base_url, session):
        catalog = session.get(f"{base_url}/catalog").text
        product_ids = re.findall(r'/catalog/product\?productId=(\d+)', catalog)
        assert product_ids, "No product IDs found"
        product_id = random.choice(product_ids)
        logger.info(f"Viewing product ID: {product_id}")

        response = session.get(f"{base_url}/catalog/product?productId={product_id}")
        assert response.status_code == 200
        assert product_id in response.text
