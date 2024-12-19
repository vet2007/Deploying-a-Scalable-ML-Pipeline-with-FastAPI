import pytest
# TODO: add necessary import
import pandas as pd

# TODO: implement the first test. Change the function name and input as needed
def test_empty():
    """
    # Check if Dataset Contains Data
    """
    data_path = "/home/factsnotfeelings/Deploying-a-Scalable-ML-Pipeline-with-FastAPI-1/data/census.csv"
    data = pd.read_csv(data_path)
    assert not data.empty, "Dataset is empty. Please ensure the data file exists and is correctly loaded."
    


# TODO: implement the second test. Change the function name and input as needed
def test_rows():
    """
    # Check if Dataset Contains Rows
    """
    data_path = "/home/factsnotfeelings/Deploying-a-Scalable-ML-Pipeline-with-FastAPI-1/data/census.csv"
    data = pd.read_csv(data_path)
    assert data.shape[0] > 0, "Dataset has no rows. Please ensure the dataset is correctly populated."
    
    pass


# TODO: implement the third test. Change the function name and input as needed
def test_columns():
    """
    # Check if Dataset Contains Columns
    """
    data_path = "/home/factsnotfeelings/Deploying-a-Scalable-ML-Pipeline-with-FastAPI-1/data/census.csv"
    data = pd.read_csv(data_path)
    assert data.shape[1] > 0, "Dataset has no rows. Please ensure the dataset is correctly populated."
    pass
