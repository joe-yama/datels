from pathlib import Path
import pytest

from datels import datels

TEST_ROOT_DIR: str = Path(__file__).parent

testcases = [
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
]


@pytest.mark.parametrize("start, end, expected_filename", testcases)
def __test_datels_with_pandas(start, end, expected_filename) -> None:
    with open(expected_filename) as f:
        expected = f.readlines()
    actual = datels.list_dates_with_pandas(start, end)
    assert len(expected) == len(actual)
    for exp, act in zip(expected, actual):
        assert exp == act


def __test_datels_with_numpy(start, end, expected_filename) -> None:
    with open(expected_filename) as f:
        expected = f.readlines()
    actual = datels.list_dates_with_numpy(start, end)
    assert len(expected) == len(actual)
    for exp, act in zip(expected, actual):
        assert exp == act
