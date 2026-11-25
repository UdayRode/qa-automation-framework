from playwright.sync_api import Page, expect
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


def test_checkout_complete(logged_in_page: Page):
    page = logged_in_page
    inventory = InventoryPage(page)
    cart = CartPage(page)
    checkout = CheckoutPage(page)

    # Step 2: add first item → badge shows 1
    inventory.add_first_item_to_cart()
    expect(inventory.cart_badge).to_have_text("1")

    # Step 3: open cart → URL is /cart.html, 1 item listed
    inventory.open_cart()
    expect(page).to_have_url("/cart.html")
    expect(cart.cart_items).to_have_count(1)

    # Step 4: checkout → step one page
    cart.go_to_checkout()
    expect(page).to_have_url("/checkout-step-one.html")

    # Step 5: fill details + continue → overview page
    checkout.fill_details("John", "Tester", "411001")
    checkout.continue_to_overview()
    expect(page).to_have_url("/checkout-step-two.html")

    # Step 6: finish → order complete 🎉
    checkout.finish()
    expect(page).to_have_url("/checkout-complete.html")
    expect(checkout.complete_header).to_have_text("Thank you for your order!")

def test_checkout_empty_form_shows_error(logged_in_page: Page):
    page = logged_in_page
    inventory = InventoryPage(page)
    cart = CartPage(page)
    checkout = CheckoutPage(page)

    # Step 2: add first item → badge shows 1
    inventory.add_first_item_to_cart()
    expect(inventory.cart_badge).to_have_text("1")

    # Step 3: open cart → URL is /cart.html, 1 item listed
    inventory.open_cart()
    expect(page).to_have_url("/cart.html")
    expect(cart.cart_items).to_have_count(1)

    # Step 4: checkout → step one page
    cart.go_to_checkout()
    expect(page).to_have_url("/checkout-step-one.html")

    #5. click Continue WITHOUT filling anything
    checkout.continue_to_overview()
    expect(page).to_have_url("/checkout-step-one.html")
    expect(checkout.error_message).to_be_visible()
    expect(checkout.error_message).to_have_text("Error: First Name is required")


    # 1. create the page objects you need
    # 2. add an item, open the cart, go to checkout
    # 3. click Continue WITHOUT filling anything
    # 4. expect the error message to be visible
    # 5. expect the error to contain "First Name is required"