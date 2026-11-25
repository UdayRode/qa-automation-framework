from playwright.sync_api import Page


class InventoryPage:
    def __init__(self, page: Page):
        self.page = page
        self.add_to_cart_buttons = page.get_by_role("button", name="Add to cart")
        self.cart_badge = page.locator('[data-test="shopping-cart-badge"]')

    def add_first_item_to_cart(self):
        self.add_to_cart_buttons.first.click()