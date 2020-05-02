"""
Data
=====

This module provides the :class:`.PassengersDataFrame` class, which
exposes methods for manipulating the `Titanic data`_.

.. _Titanic data: https://www.kaggle.com/c/titanic/data

"""

from __future__ import annotations

# Third Party --------------------------------------------------------------------------
from dotenv import load_dotenv
from titanic.paths import original_test_data_path, original_train_data_path

# Data Science
import pandas as pd


load_dotenv()


def read() -> pd.DataFrame:
    """Return pandas data frame with training data.

    Returns
    -------
    DataFrame
        Pandas data frame with training data
    """
    return pd.read_csv(original_train_data_path(), index_col=0)


class PassengersDataFrame(pd.DataFrame):
    """Passengers Data Frame."""

    def __init__(self, kind: str = "train") -> None:
        if kind == "test":
            super().__init__(pd.read_csv(original_test_data_path(), index_col=0))
        else:
            super().__init__(pd.read_csv(original_train_data_path(), index_col=0))

    def create_male_dummies(self) -> PassengersDataFrame:
        """Create a new "Male" dummy column from the original "Sex" column."""
        self["Male"] = pd.get_dummies(self["Sex"], drop_first=True)
        return self

    def impute_fare(self) -> PassengersDataFrame:
        """Impute missing fare values with the mean."""
        self["Fare"].fillna((self["Fare"].mean()), inplace=True)
        return self

    def survived_column(self) -> PassengersDataFrame:
        return self["Survived"]

    @property
    def _constructor_expanddim(self) -> NotImplementedError:
        return super()._constructor_expanddim()
