from pathlib import Path

import pytest
from datels import datels

TEST_ROOT_DIR: Path = Path(__file__).parent

basic_testcases = [
    (
        "2021-01-01",
        "2021-01-02",
        str(TEST_ROOT_DIR / "data" / "expected_20210101_20210102.txt"),
    ),
    (
        "2021-12-30",
        "2022-01-02",
        str(TEST_ROOT_DIR / "data" / "expected_20211230_20220102.txt"),
    ),
    (
        "2000-12-30",
        "2022-01-02",
        str(TEST_ROOT_DIR / "data" / "expected_20001230_20220102.txt"),
    ),
]


@pytest.mark.parametrize("start, end, expected_filename", basic_testcases)
def test_basic_testcases(start: str, end: str, expected_filename: str) -> None:
    with open(expected_filename) as f:
        expected = f.readlines()
    actual = datels.list_dates(start, end)
    assert len(expected) == len(actual)
    for exp, act in zip(expected, actual):
        assert exp.strip() == act


boundary_testcases = [
    (
        "2021-01-01",
        "2021-01-01",
        "both",
        str(TEST_ROOT_DIR / "data" / "expected_20210101_20210101.txt"),
    ),
    (
        "2021-01-01",
        "2021-01-01",
        "left",
        str(TEST_ROOT_DIR / "data" / "expected_20210101_20210101_left.txt"),
    ),
    (
        "2021-01-01",
        "2021-01-01",
        "right",
        str(TEST_ROOT_DIR / "data" / "expected_20210101_20210101_right.txt"),
    ),
    (
        "2021-01-01",
        "2021-01-05",
        "both",
        str(TEST_ROOT_DIR / "data" / "expected_20210101_20210105.txt"),
    ),
    (
        "2021-01-01",
        "2021-01-05",
        "left",
        str(TEST_ROOT_DIR / "data" / "expected_20210101_20210105_left.txt"),
    ),
    (
        "2021-01-01",
        "2021-01-05",
        "right",
        str(TEST_ROOT_DIR / "data" / "expected_20210101_20210105_right.txt"),
    ),
]


@pytest.mark.parametrize("start, end, inclusive, expected_filename", boundary_testcases)
def test_boundary_testcases(
    start: str, end: str, inclusive: str, expected_filename: str
) -> None:
    with open(expected_filename) as f:
        expected = f.readlines()
    actual = datels.list_dates(start, end, inclusive)
    assert len(expected) == len(actual)
    for exp, act in zip(expected, actual):
        assert exp.strip() == act


sep_testcases = [
    (
        "2021-01-01",
        "2021-01-02",
        "-",
        str(TEST_ROOT_DIR / "data" / "expected_20210101_20210102_sep.txt"),
    ),
]


@pytest.mark.parametrize("start, end, sep, expected_filename", sep_testcases)
def test_sep_testcases(start: str, end: str, sep: str, expected_filename: str) -> None:
    with open(expected_filename) as f:
        expected = f.readlines()
    actual = datels.list_dates(start, end, sep=sep)
    assert len(expected) == len(actual)
    for exp, act in zip(expected, actual):
        assert exp.strip() == act
