# Transcription factor binding prediction

## Preparation

### Data location

The notebooks assume the presence of two files:

- `./data/peak_data.txt`
- `./data/shuffled_data.txt`

Further the folder `./data` should contain the subfolders

- `./data/interim/`
- `./data/engineered/`

### Installation

The code is compatible with python >=3.10, additional dependencies
are listed in `requrements.txt`, to install them run:

    pip install -r requrements.txt
   
in the root folder of this project.

## Workflow

sklearn's [pipelines](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html) are a great tool to condense an analysis and I would use them in most cases.
However, I find them not to be ideal for demonstrating purposes, so in this project they will only come into play in the hyper-parameter tuning part in [Hyperparam_Tuning.ipynb](Hyperparam_Tuning.ipynb).

The notebooks should be run in the following order:

- [Intro.ipynb](./Intro.ipynb): This is **optional** as it only provides some info about the problem at hand
- [Processing_and_Cleaning.ipynb](Processing_and_Cleaning.ipynb): Creates pandas DataFrame's from the raw data (see #data-location)
- [Feature_Engineering.ipynb](Feature_Engineering.ipynb): Performs some feature engineering steps to convert the DNA sequences into usable feature vectors
- [Model_Selection.ipynb](Model_Selection.ipynb): Performs a basic screening over the potential classifiers
- [Hyperparam_Tuning.ipynb](Hyperparam_Tuning.ipynb): Performs hyper-parameter tuning, including some feature-engineering parameter, by cross-validating ml pipelines

**Note:** The [Hyperparam_Tuning.ipynb](Hyperparam_Tuning.ipynb) includes feature engineering into a pipeline so it can work directly with the cleaned data generated in [Feature_Engineering.ipynb](Feature_Engineering.ipynb).
