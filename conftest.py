import pytest
from playwright.sync_api import expect
from pages.login_page import LoginPage
import os
from dotenv import load_dotenv

load_dotenv()

@pytest.fixture(scope="session") #scope = how long the fixture lives:
def user():
    print("\n🔧 Creating user...")
    return {"name": "Uday", "age": 25}

@pytest.fixture
def fake_browser():
    print("\n🟢 Opening browser")     # setup (before the test)
    yield "chrome"                    # ⏸️ test runs here
    print("\n🔴 Closing browser")     # cleanup (after the test)




# @pytest.fixture
# def logged_in_page(page):
#     # 1. go to "/"
#     # 2. fill username
#     # 3. fill password
#     # 4. click Login
#     # 5. return page
#     page.goto("/")
#     page.get_by_placeholder("Username").fill("standard_user")
#     page.get_by_placeholder("Password").fill("secret_sauce")
#     page.get_by_role("button", name="Login").click()
#     expect(page).to_have_url("/inventory.html")
#     expect(page.get_by_text("Products")).to_be_visible()
#     return page

@pytest.fixture
def logged_in_page(page):
    login_page = LoginPage(page)                                                    # 1. call the chef
    login_page.open()                                                               # 2. open the login page
    # login_page.login("standard_user", "secret_sauce")                             # 3. log in
    login_page.login(os.getenv("SAUCE_USERNAME"), os.getenv("SAUCE_PASSWORD"))  
    expect(page).to_have_url("/inventory.html")                                     # 4. make sure it worked
    return page                                                                     # 5. serve the dish 🍽️
