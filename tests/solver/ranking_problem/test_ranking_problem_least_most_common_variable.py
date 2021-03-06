import pytest
from solver.ranking_problem import RankingProblem


def test_ranking_problem_variable_constraints_count():
    expected_results = {
        "Blue": 3,
        "Green": 3,
        "Red": 1,
        "Yellow": 1,
    }

    r = RankingProblem()
    r.set_items(["Red", "Blue", "Green", "Yellow"])
    r.not_directly_before_or_after("Blue", "Green")

    result = r.variable_constraints_count()

    try:
        assert(result == expected_results)
    except AssertionError:
        pytest.fail("Failed to get expected variable_constraints_count from RankingProblem")


def test_ranking_problem_least_most_common_variable():
    expected_results = ("Red", "Blue")

    r = RankingProblem()
    r.set_items(["Red", "Blue", "Green", "Yellow"])
    r.not_directly_before_or_after("Blue", "Green")

    result = r.least_most_common_variable()

    try:
        assert(result == expected_results)
    except AssertionError:
        pytest.fail("Failed to get expected variable_constraints_count from RankingProblem")
