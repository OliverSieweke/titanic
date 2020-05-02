"""
Submissions
===========

This module contains methods for viewing current submissions to
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

# Third Party --------------------------------------------------------------------------
from dotenv import load_dotenv


load_dotenv()


def show() -> None:
    """Print the list of current submissions_ to the `Titanic competition`_.

    .. _submission: https://www.kaggle.com/c/titanic/submissions
    .. _Titanic competition: https://www.kaggle.com/c/titanic/overview
    .. _Reference: https://github.com/Kaggle/kaggle-api/#list-competition-submissions
    """
    print(
        os.popen(
            f"kaggle competitions submissions {os.getenv('KAGGLE_COMPETITION_ID')}"
        ).read()
    )
