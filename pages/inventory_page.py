from playwright.sync_api import Page


class InventoryPage:
    def __init__(self, page: Page):
        self.page = page
        self.add_to_cart_buttons = page.get_by_role("button", name="Add to cart")
        self.cart_badge = page.locator('[data-test="shopping-cart-badge"]')
        self.cart_link = page.locator('[data-test="shopping-cart-link"]')   # 👈 in __init__

    def open_cart(self):                                                    # 👈 new action
        self.cart_link.click()

    def add_first_item_to_cart(self):
        self.add_to_cart_buttons.first.click()