import re
import random
import allure
from utils.custom_logger import get_logger

logger = get_logger(__name__)

@allure.feature("Cart & Checkout")
class TestCartAndCheckout:

    @allure.story("Add to cart and expect checkout to redirect to login")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_add_to_cart_and_checkout_redirects_to_login(self, base_url, session):
        logger.info("Fetching catalog for product IDs...")
        catalog_page = session.get(f"{base_url}/catalog").text
        product_ids = re.findall(r'/catalog/product\?productId=(\d+)', catalog_page)
        assert product_ids, "No products found"
        product_id = random.choice(product_ids)
        logger.info(f"Selected product: {product_id}")

        add_cart_url = f"{base_url}/catalog/cart"
        payload = {"productId": product_id, "quantity": "1", "redir": "PRODUCT"}
        headers = {"Content-Type": "application/x-www-form-urlencoded"}

        add_cart_response = session.post(add_cart_url, data=payload, headers=headers)
        assert add_cart_response.status_code == 200

        cart_page = session.get(add_cart_url)
        assert "Your cart is currently empty" not in cart_page.text

        csrf_token = re.search(r'name="csrf" value="([^"]+)"', cart_page.text)
        assert csrf_token, "No CSRF token"
        token = csrf_token.group(1)
        logger.debug(f"CSRF: {token}")

        checkout_url = f"{base_url}/catalog/cart/checkout"
        checkout_response = session.post(checkout_url, data={"csrf": token}, allow_redirects=False)
        assert checkout_response.status_code in [302, 303]

        redirect_location = checkout_response.headers.get("Location")
        assert redirect_location == "/login?redirect=cart"
        logger.info(f"Redirected to: {redirect_location}")

        login_page = session.get(f"{base_url}{redirect_location}")
        assert login_page.status_code == 200
        assert "Login" in login_page.text
