import fire

from datels.datels import list_dates_with_pandas, list_dates_with_numpy


def main():
    fire.Fire(list_dates_with_numpy)
    # fire.Fire(list_dates_with_pandas)


main()
