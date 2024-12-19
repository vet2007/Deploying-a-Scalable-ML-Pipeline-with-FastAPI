# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details
Used RandomForestClassifer for modeling with a hyperparameter of random_state=42
## Intended Use
This model is designed to predict a person's salary based on employment information.

## Training Data
The data used was census.csv containing the following categories: workclass, education, martial-status, occupation, relationship, race, sex, and native country.
## Evaluation Data
OneHotEncoder was used for categorical features.
## Metrics
_Please include the metrics used and your model's performance on those metrics._
Precision, Recall and F-Score was used.
## Ethical Considerations
Data outcomes can contain social biases that affect the data.
## Caveats and Recommendations
Model should not be solely used to determine data outcomes due to biases.