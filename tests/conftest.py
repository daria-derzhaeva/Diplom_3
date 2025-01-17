import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from config import MAIN_PAGE, CREATE_USER_ENDPOINT, DELETE_USER_ENDPOINT
from helper import generate_user_data
import requests

@pytest.fixture(params=['chrome', 'firefox'])
def driver(request):
    if request.param == 'chrome':
        options = webdriver.ChromeOptions()
        options.add_argument("--window-size=1920,1080")
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    elif request.param == 'firefox':
        driver = webdriver.Firefox()
    else:
        raise ValueError(f"Unsupported browser: {request.param}")

    driver.get(MAIN_PAGE)
    yield driver
    driver.quit()


@pytest.fixture
def create_user_and_get_creds():
    payload = generate_user_data()
    created_response = requests.post(CREATE_USER_ENDPOINT, json=payload)

    if created_response.status_code == 200:
        access_token = created_response.json().get('accessToken')
        if not access_token:
            raise ValueError("Access token not found in response")
        yield payload, access_token
        headers = {'Authorization': access_token}
        requests.delete(DELETE_USER_ENDPOINT, headers=headers)
    else:
        yield payload
