import pandas as pd
import numpy as np
from datetime import datetime, timedelta


def list_dates_with_pandas(start, end, freq="D", format=None, sep=None):
    if format is None:
        if sep is None:
            sep = "/"
        format = sep.join(("%Y", "%m", "%d"))

    return [
        date.strftime(format) for date in pd.date_range(start=start, end=end, freq=freq)
    ]


def list_dates_with_numpy(
    start, end, inclusive="both", freq="D", format=None, sep=None
):
    if freq != "D":
        raise NotImplementedError("datels only support date-based frequency.")

    start = datetime.strptime(start, "%Y-%m-%d")
    end = datetime.strptime(end, "%Y-%m-%d")

    if inclusive == "both":
        end = end + timedelta(days=1)
    elif inclusive == "left":
        pass
    elif inclusive == "right":
        start = start + timedelta(days=1)
        end = end + timedelta(days=1)

    if format is None:
        if sep is None:
            sep = "/"
        format = sep.join(("%Y", "%m", "%d"))

    arr = np.arange(start, end, timedelta(days=1)).astype(datetime)
    return np.vectorize(lambda d: d.strftime(format))(arr).tolist()
