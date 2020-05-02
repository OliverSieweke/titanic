"""
Submit
======

This module contains methods for directly uploading submissions to
`Kaggle's`_ `Titanic competition`_.

.. warning::
    In order to use the methods contained in this module, please ensure
    your Kaggle account credentials are saved to
    :code:`~/.kaggle/kaggle.json` as described in the `Kaggle API
    documentation`_.

.. _Kaggle's: https://www.kaggle.com/
.. _Titanic competition: https://www.kaggle.com/c/titanic/overview
.. _Kaggle API documentation: https://github.com/Kaggle/kaggle-api/#api-credentials
"""


# Standard Library ---------------------------------------------------------------------
import os
import re

# Third Party --------------------------------------------------------------------------
from dotenv import load_dotenv
from titanic.data import PassengersDataFrame
from titanic.paths import submissions_data_dir_path

# Data Science
import pandas as pd

from sklearn.linear_model import LogisticRegression


load_dotenv()


def model(sk_model: LogisticRegression, feature_engineer, message):
    """Submit predictions as Scikit-Learn Model with specific feature
    engineering.

    Parameters
    ----------
    sk_model
        Scikit Model
    feature_engineer
        Feature engineering function. Has to return a data frame.
    message
        Submission message.
    """
    train_df = PassengersDataFrame(kind="train")
    test_df = PassengersDataFrame(kind="test")

    y = train_df.survived_column()
    sk_model.fit(feature_engineer(train_df), y)

    test_df["Survived"] = sk_model.predict(feature_engineer(test_df))

    data(test_df, message)


def data(data_frame: pd.DataFrame, message: str):
    """Submit predictions as Pandas Data Frame.

     - The data frame should contain exactly **418** entries.
     - The data frame should include the following columns 2 columns:
        - PassengerId
            Numbered from  892 to 1309.
        - Survived
            Binary prediction for death (0) and survival (1).

    Parameters
    ----------
    data_frame
        Pandas DataFrame.
    message
        Submission message.
    """

    file_name = re.sub(r"\s", "_", message)
    file_name_with_extension = f"{file_name}.csv"
    file_path = os.path.join(submissions_data_dir_path(), file_name_with_extension)

    data_frame[["Survived"]].to_csv(file_path)
    file(file_path, message)


def file(file_path: str, message: str) -> None:
    """Submit predictions as CSV file.

    - The CSV file should contain exactly **418** entries (plus a header row).
    - The CSV file should contain exactly 2 columns:

        - PassengerId
            Numbered from  892 to 1309.
        - Survived
            Binary prediction for death (0) and survival (1).

    Parameters
    ----------
    file_path
        Absolute file path.
    message
        Submission message.
    """

    print(
        os.popen(
            f"kaggle competitions submit -f {file_path} -m {message} {os.getenv('KAGGLE_COMPETITION_ID')}"
        ).read()
    )
