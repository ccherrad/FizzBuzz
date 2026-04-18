from fizzbuzz.service import generate_fizzbuzz


def test_divisible_by_int1():
    assert generate_fizzbuzz(3, 5, 3, "Fizz", "Buzz")[2] == "Fizz"


def test_divisible_by_int2():
    assert generate_fizzbuzz(3, 5, 5, "Fizz", "Buzz")[4] == "Buzz"


def test_divisible_by_both():
    assert generate_fizzbuzz(3, 5, 15, "Fizz", "Buzz")[14] == "FizzBuzz"


def test_not_divisible():
    assert generate_fizzbuzz(3, 5, 1, "Fizz", "Buzz")[0] == "1"


def test_limit_length():
    result = generate_fizzbuzz(3, 5, 10, "Fizz", "Buzz")
    assert len(result) == 10


def test_custom_strings():
    result = generate_fizzbuzz(2, 3, 6, "Foo", "Bar")
    assert result == ["1", "Foo", "Bar", "Foo", "5", "FooBar"]


def test_limit_one():
    assert generate_fizzbuzz(3, 5, 1, "Fizz", "Buzz") == ["1"]


def test_same_divisor():
    result = generate_fizzbuzz(2, 2, 4, "A", "B")
    assert result == ["1", "AB", "3", "AB"]
