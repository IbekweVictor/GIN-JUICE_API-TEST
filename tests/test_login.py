import re
import allure
from utils.custom_logger import get_logger

logger = get_logger(__name__)

@allure.feature("Authentication")
class TestLogin:

    @allure.story("Login page should work and redirect after login")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_login_page(self, base_url, session):
        logger.info("Fetching login page...")
        login_url = f"{base_url}/login"
        response = session.get(login_url)
        assert response.status_code == 200

        csrf_token = re.search(r'name="csrf" value="([^"]+)"', response.text)
        assert csrf_token, "CSRF token missing"
        token = csrf_token.group(1)
        logger.info(f"CSRF token: {token}")

        payload = {
            "csrf": token,
            "username": "carlos",
            "password": "hunter2"
        }
        headers = {"Content-Type": "application/x-www-form-urlencoded"}

        response = session.post(login_url, data=payload, headers=headers, allow_redirects=False)
        assert response.status_code == 302
        assert response.headers.get("Location") == "/my-account"
