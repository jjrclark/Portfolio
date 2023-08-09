# test_project.py
# Jadyn Renk

from project import goals, convert_bmi, convert_protein

def test_convert_bmi():
    assert convert_bmi(115,62) == 21
    assert convert_bmi(200,70) == 29
    assert convert_bmi(100.5,62) == 18


def test_convert_protein():
    assert convert_protein(115) == 172.5
    assert convert_protein(200) == 300.0
    assert convert_protein(100.5) == 150.75


def test_function_goal_correctly_outputs():
    assert goals("gain strength") == "You should be in a caloric surplus, eat 10% more calories and lean foods only"
    assert goals("loose weight") == "You should be in a calorie deficit, eat 10% less calories than you are currently"
    assert goals("gain body mass") == "You should be in a caloric surplus, eat 10% more calories than you are currently"
