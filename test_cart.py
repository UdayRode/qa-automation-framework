from playwright.sync_api import Page, expect

def test_add_to_cart(page: Page):
    page.goto("https://www.saucedemo.com")
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_role("button", name="Login").click()
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    expect(page.get_by_text("Products")).to_be_visible()
    page.get_by_role("button", name="Add to cart").first.click()
    # 1. log in as standard_user
    # 2. click "Add to cart" on the FIRST product
    # 3. expect the cart icon (top right) to show "1"
    expect(page.locator('[data-test="shopping-cart-badge"]')).to_have_text("1")