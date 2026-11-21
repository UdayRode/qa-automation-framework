import pytest

# @pytest.fixture
# def user():
#     print("\n🔧 Creating user...")
#     return {"name": "Uday", "age": 25} #it printed 3 times, once for each test

# @pytest.fixture(scope="session") #scope = how long the fixture lives:
# def user():
#     print("\n🔧 Creating user...")
#     return {"name": "Uday", "age": 25}

# @pytest.fixture
# def browser():
#     print("\n🟢 Opening browser")     # setup (before the test)
#     yield "chrome"                    # ⏸️ test runs here
#     print("\n🔴 Closing browser")     # cleanup (after the test)

def test_open_site(browser):
    print(f"\n🌐 Using {browser}")
    assert browser == "chrome"

def test_user_name(user):
    assert user["name"] == "Uday"

def test_user_age(user):
    assert user["age"] == 25

def test_user_age_over18(user):
    assert user["age"] > 18