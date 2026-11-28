from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
import pytest

@pytest.mark.parametrize("username", [
    "standard_user",
    "problem_user",
    "performance_glitch_user",
    "visual_user",
])
def test_valid_users_can_login(page: Page, username):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login(username, "secret_sauce")
    # expect(page).to_have_url("/inventory.html") #expect waits up to 5 seconds. This user takes about 4–5 seconds to log in, so it's just barely passing. 😬 On a busy day, like 15 tests in parallel, it could cross 5 seconds and fail randomly: another flaky test waiting to happen.
    expect(page).to_have_url("/inventory.html", timeout=10_000)
    # 1. create LoginPage
    # 2. open it
    # 3. login with username + "secret_sauce"
    # 4. expect URL /inventory.html

# def test_login_success(page: Page):
#     login_page = LoginPage(page)
#     login_page.open()
#     login_page.login("standard_user", "secret_sauce")

#     expect(page).to_have_url("/inventory.html")

def test_login_locked_out_user(page: Page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login("locked_out_user", "secret_sauce")

    expect(page).to_have_url("/")
    expect(login_page.error_message).to_be_visible()
    expect(login_page.error_message).to_contain_text("locked out")#imp message to validate

    