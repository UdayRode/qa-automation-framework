import pytest

@pytest.fixture(scope="session") #scope = how long the fixture lives:
def user():
    print("\n🔧 Creating user...")
    return {"name": "Uday", "age": 25}

@pytest.fixture
def browser():
    print("\n🟢 Opening browser")     # setup (before the test)
    yield "chrome"                    # ⏸️ test runs here
    print("\n🔴 Closing browser")     # cleanup (after the test)

def test_user_from_conftest(user):
    assert user["name"] == "Uday"