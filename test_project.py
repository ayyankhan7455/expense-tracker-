import csv

import pytest

import project


def test_add_expense():
    expenses = []
    project.add_expense(expenses, "2026-10-18", "Food", "250", "Lunch")


    assert len(expenses) == 1
    assert expenses[0]["category"] == "Food"
    assert expenses[0]["amount"] == 250.0




def test_bad_amount():
    with pytest.raises(ValueError):
        project.add_expense([], "2026-10-18", "Food", "abc", "Lunch")




def test_zero_amount():
    with pytest.raises(ValueError):
        project.add_expense([], "2026-10-18", "Food", "0", "Lunch")




def test_calculate_total():
    expenses = [
        {"amount": 100},
        {"amount": 250.50},
    ]


    assert project.calculate_total(expenses) == 350.50




def test_load_save_expenses(tmp_path, monkeypatch):
    file_path = tmp_path / "expenses.csv"
    monkeypatch.setattr(project, "FILE_NAME", file_path)


    expenses = []
    project.add_expense(expenses, "2026-10-18", "Travel", "100", "Bus")
    project.save_expenses(expenses)


    loaded = project.load_expenses()


    assert len(loaded) == 1
    assert loaded[0]["category"] == "Travel"
    assert loaded[0]["amount"] == 100.0
