<!--suppress HtmlDeprecatedAttribute | JetBrains Inspection -->
<p align="center">
    <a title="MIT License" href="https://choosealicense.com/licenses/mit">
      <img alt="License: MIT" src="https://img.shields.io/github/license/OliverSieweke/titanic" />
    </a>
    <a title="Releases" href="https://github.com/OliverSieweke/titanic/releases">
        <img alt="Version" src="https://img.shields.io/github/v/tag/OliverSieweke/titanic" />
    </a>
    <a>
      <img alt="Python 3.7" src="https://img.shields.io/badge/python-3.7-blue.svg"/>
    </a>
    <a href="https://github.com/psf/black">
      <img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"/>
    </a>
    <a href="https://dependabot.com/">
        <img alt="Dependabot" src="https://badgen.net/dependabot/OliverSieweke/titanic/?icon=dependabot"/>
    </a>
    <a title="Documentation Status" href="https://os-titanic.readthedocs.io/en/latest/?badge=latest">
        <img alt="Documentation Status" src="https://readthedocs.org/projects/os-titanic/badge/?version=latest" />
    </a>
    <a title="MyBinder" href="https://mybinder.org/v2/gh/OliverSieweke/titanic/master?filepath=notebooks">
        <img alt="Binder" src="https://mybinder.org/badge_logo.svg" />
    </a>
</p>


<p align="center">
    <img alt="Iceberg Logo" align="center" src="iceberg-logo.svg" />
</p>


<h1 align="center">Titanic</h1> 

Welcome to *Titanic*! This project proposes a machine learning model to predict passenger survival on the *RMS Titanic* and was submitted to the Kaggle competition *[Titanic: Machine Learning from Disaster](https://www.kaggle.com/c/titanic)*.

- [Data](#data)
- [User Guide](#user-guide)
- [Developer Guide](#developer-guide)

## Data

The data was downloaded from [Kaggle](https://www.kaggle.com/c/titanic/data) on the *26.04.20* and includes:

- `data/original/train.csv` which contain the details of a subset of 891 passengers on board, including their survival status.
- `data/original/test.csv` which contains the data for 418 additional passangers for which the survival is unknown.

## User Guide

### Viewing the Project

The various notebooks used in this project for exploratory data anlysis, visualizations and predictive modeling can be viewed on [MyBinder](https://mybinder.org/) (this may take some time in case no container is currently deployed):

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/OliverSieweke/master?filepath=notebooks)

### Running the Project

If you have [Python 3](https://www.python.org/downloads/) installed, you may run the project on your local machine by executing the following commands from your terminal:

```bash
$ git clone https://github.com/OliverSieweke/titanic.git
$ cd titanic
$ pip install -r requirements.txt
$ jupyter notebook notebooks
```

### Documentation

Documentation for the project can be viewed on [Read the Docs](https://readthedocs.org/):

[![Documentation Status](https://readthedocs.org/projects/os-titanic/badge/?version=latest)](https://os-titanic.readthedocs.io/en/latest/?badge=latest)

## Developer Guide

Contributions are welcome! Please fork the project, make sure you have [Python 3.7](https://www.python.org/downloads/) installed and set up your local repository as follows:

```bash
$ git clone https://github.com/<path_to_your_fork>
$ cd <your_local_repository>
$ python3.7 -m pip install -r requirements-dev.txt
$ pre-commit install
```

This will install required dependencies and set up git hooks to ensure that your commits conform to the project's standards and code style.
