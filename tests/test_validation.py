import pandas as pd
import pytest

from report_tools.validation import validate_clean_data

def test_negative_sessions_raise_error():
    data = pd.DataFrame({
        "sessions": [-1],
        "users": [50],
        "conversions": [5]
    })

    with pytest.raises(ValueError, match="Sessions kan inte vara negativt."):
        validate_clean_data(data)


def test_valid_data_does_not_raise_error():
    data = pd.DataFrame({
        "sessions": [100],
        "users": [80],
        "conversions": [5]
    })

    validate_clean_data(data)