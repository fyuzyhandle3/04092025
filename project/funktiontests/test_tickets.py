import pytest
from funktion import get_ticket_price


def test_child_free():
    assert get_ticket_price(5) == 0.0


def test_teen_discount():
    assert get_ticket_price(10) == 50.0


def test_adult_full_price():
    assert get_ticket_price(30) == 100.0


def test_senior_discount():
    assert get_ticket_price(70) == 70.0
