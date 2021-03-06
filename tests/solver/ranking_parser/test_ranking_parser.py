from solver import RankingParser
from test_data import programmer_riddle


def test_can_create_rule_parser():
    rp = RankingParser()
    assert(isinstance(rp, RankingParser))


def test_ranking_parser_multi_line_input():
    multi_line_input = """
    [Green] before [Red]
    [Yellow] before [Green]
    """

    expected_result = [
        ("Yellow", "Green", "Red")
    ]

    rp = RankingParser()
    rp.build()
    rp.parse(multi_line_input)

    assert(rp.solve() == expected_result)


def test_ranking_parser_parse_statements():
    expected_result = ("Sarah", "John", "Jessie", "Evan", "Matt",)

    rp = RankingParser()
    result = rp.parse_statements(programmer_riddle)
    print(result)
    assert(result == expected_result)


def test_ranking_parser_parse_whitespace_in_brackets():
    expected_result = ("Captain_Blackbeard", "Long_John_Silver")
    rp = RankingParser()
    result = rp.parse_statements([
        "[Captain Blackbeard] is not last",
        "[Long John Silver] is not first"
    ])
    assert(result == expected_result)


def test_ranking_parser_parse_whitespace_no_brackets():
    expected_result = ("Captain_Blackbeard", "Long_John_Silver")
    rp = RankingParser()
    result = rp.parse_statements([
        "Captain Blackbeard is not last",
        "Long John Silver is not first"
    ])
    assert(result == expected_result)


def test_ranking_parser_parse_whitespace_no_brackets_multiline():
    expected_result = [("Walk_the_dog", "Feed_the_cat")]
    rp = RankingParser()
    rp.build()
    rp.parse(
        """Walk the dog is not last
        Feed the cat is not first"""
    )
    result = rp.solve()
    assert(result == expected_result)


def test_ranking_parser_whitespace_partial_token_matches():
    expected_result = ("The_orange_cat", "The_grey_cat")
    rp = RankingParser()
    result = rp.parse_statements([
        "The orange cat before The grey cat",
    ])
    assert(result == expected_result)


def test_ranking_parser_whitespace_partial_token_matches_missed_capital():
    expected_result = ("The_orange_cat", "Grey_cat")
    rp = RankingParser()
    result = rp.parse_statements([
        "The orange cat is before the Grey cat",
    ])
    assert(result == expected_result)


def test_ranking_parser_parse_statements_no_statements():
    rp = RankingParser()
    result = rp.parse_statements([])

    assert(result is None)

