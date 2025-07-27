import allure
from utils.custom_logger import get_logger

logger = get_logger(__name__)

@allure.feature("Homepage")
class TestHomepage:

    @allure.story("Verify homepage loads")
    @allure.severity(allure.severity_level.NORMAL)
    def test_homepage(self, base_url, session):
        logger.info("Requesting homepage...")
        response = session.get(base_url)
        logger.debug(f"Status code: {response.status_code}")
        assert response.status_code == 200
        assert "Juice Shop" in response.text
