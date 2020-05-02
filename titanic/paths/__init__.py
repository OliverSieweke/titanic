"""
Paths
=====

This module provides utility methods for retrieving project paths,
mostly concatenated from environment variables.
"""
# Standard Library ---------------------------------------------------------------------
from os import getenv, path

# Third Party --------------------------------------------------------------------------
from dotenv import load_dotenv


load_dotenv()


def project_root_path() -> str:
    """Return absolute project root path.

    Returns
    -------
    str
        Absolute project root path.
    """
    return path.abspath(path.join(__file__, "..", "..", ".."))


def original_train_data_path() -> str:
    """Return absolute original training data file path.

    Returns
    -------
    str
        Absolute original training data file path.
    """
    return path.join(original_data_dir_path(), getenv("TRAIN_DATA_FILE"))


def original_test_data_path():
    return path.join(original_data_dir_path(), getenv("TEST_DATA_FILE"))


def original_data_dir_path() -> str:
    """Return absolute original data directory path.

    Returns
    -------
    str
        Absolute original data directory path.
    """
    return path.abspath(
        path.join(project_root_path(), getenv("DATA_DIR"), getenv("ORIGINAL_DATA_DIR"))
    )


def submissions_data_dir_path() -> str:
    """Return absolute submissions data directory path.

    Returns
    -------
    str
        Absolute submissions data directory path.
    """
    return path.abspath(
        path.join(
            project_root_path(), getenv("DATA_DIR"), getenv("SUBMISSIONS_DATA_DIR")
        )
    )
