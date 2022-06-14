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

The code is compatible with python >=3.10, additinal dependencies
are listed in `requrements.txt`, to install them run:

    pip install -r requrements.txt
   
in the root folder of this project.

## Workflow

I'm well aware of sklearn's [pipelines](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html) and would use them virtually everytime, I find them not to be ideal for demonstrating puposes, so in this project they will only enter into play in the hyperparameter tuning part at the very end.

The notebooks should be run in the following order:

- [Intro.ipynb](./Intro.ipynb)
- [Processing_and_Cleaning.ipynb](Processing_and_Cleaning.ipynb)
- [Feature_Engineering.ipynb](Feature_Engineering.ipynb)
- [Model_Selection.ipynb](Model_Selection.ipynb)