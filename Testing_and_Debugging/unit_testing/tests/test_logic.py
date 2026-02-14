import pytest
from Testing_and_Debugging.unit_testing.app.logic import is_eligible_for_loan


def test_eligible_user():
    assert is_eligible_for_loan(60000, 25, 'employed') == True


def test_underage_user():
    assert is_eligible_for_loan(70000, 20, 'employed') == False 


def test_low_income():
    assert is_eligible_for_loan(15000, 25, 'employed') == False 


def test_unemployed_user():
    assert is_eligible_for_loan(80000, 35, 'unemployed') == False


def test_boundary_case():
    assert is_eligible_for_loan(50000, 21, 'employed') == True 

