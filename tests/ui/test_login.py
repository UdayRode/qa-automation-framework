from playwright.sync_api import Page, expect
from pages.login_page import LoginPage


def test_login_success(page: Page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    expect(page).to_have_url("/inventory.html")

def test_login_locked_out_user(page: Page):
    page.goto("/")
    page.get_by_placeholder("Username").fill("locked_out_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_role("button", name="Login").click()

    expect(page).to_have_url("/") 
    # expect(page.get_by_text("Products")).to_be_visible()

    