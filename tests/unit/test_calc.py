from calc import add , multiply, subs , divide
import pytest

@pytest.mark.smoke
def test_add():
    assert add(2, 3) == 5

def test_add_decimals():
    assert add(1.5 , 1.5) == 3

def test_add_withzero():
    assert add(0 , 1.5) == 1.5

def test_add_positivewithnegative():
    assert add(5 , (-3)) == 2

def test_addnegativenumber():
    assert add(-5,-1) == -6

def test_add_small_decimals(): #first bug : very imp - 
    assert add(0.1, 0.2) == pytest.approx(0.3)

# Computers store numbers in binary (0s and 1s), and some decimals can’t be stored exactly in binary.

# It’s like writing 1 ÷ 3 as a decimal: 0.3333… goes on forever, so you have to cut it off somewhere, and that leaves a tiny error.

# 0.1 has the same problem inside a computer, so 0.1 + 0.2 comes out as 0.30000000000000004.



#multiply

def test_multiply_2_numbers():
    assert multiply(5,4) == 20

#divide
def test_divide():
    assert divide(6,2) == 3

# def test_divide_by_zero():
#     divide(10, 0) # ZeroDivisionError

# next step is to make it an expected error : 

def test_divide_by_zero():
    with pytest.raises(ValueError): # pytest handles it and not let the testcase fail
        divide(10, 0)


# def test_divide_by_negative():
#     divide(10,-2)

# def test_divide_with_bigger_number():
#     divide(1,3)

# 🧠 Why they “passed”

# A test only fails if something goes wrong. Your tests run divide but never check the answer, so they’d pass even if divide returned 999. 😱

# This is a fake pass, and it’s one of the most dangerous mistakes in testing. Senior testers look for it in code reviews.

def test_divide_by_negative():
    assert divide(10, -2) == -5

def test_divide_with_bigger_number():
    assert divide(1, 3) == pytest.approx(0.3333, rel=1e-3)


# @pytest.mark.parametrize("a, b, expected", [
#     (2, 3, 5),
#     (0, 5, 5),
#     (-2, -3, -5),
#     (0, -3, -3),
#     (0, 0, 0)
# ])

@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 5),
    (0, 5, 5),
    (-2, -3, -5),
], ids=["positive", "zero", "negative"])
def test_add_many(a, b, expected):
    assert add(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (5, 3, 2),
    (5, 0, 5),
    (-5, -3, -2),
    (3, 5, -2),
], ids=["positive", "minus_zero", "negative_numbers", "result_below_zero"])
def test_subs_many(a, b, expected):
    assert subs(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 6),
    (0, 5, 0),
    (-2, -3, 6),
    (-2, 3, -6),
    (0.1, 3, pytest.approx(0.3)),
], ids=["positive", "zero", "negative", "negative_positive", "small_decimal"])

def test_multiply_many(a, b, expected):
    assert multiply(a, b) == expected

