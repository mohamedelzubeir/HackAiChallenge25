import pandas as pd

# Class to handle the loading of transaction data from a CSV file. 
# This will be the foundation for our data collection step.
class TransactionParser:
    def __init__(self, file_path):
        """
        Initializes the TransactionParser with the path to the transaction file.
        
        :param file_path: Path to the CSV file containing transaction data.
        """
        self.file_path = file_path

    def load_transactions(self):
        """
        Loads transactions from the specified CSV file.
        
        :return: DataFrame containing the transaction data.
        """
        try:
            transactions = pd.read_csv(self.file_path)
            return transactions
        except FileNotFoundError:
            print(f"Error: The file {self.file_path} was not found.")
            return None
        except pd.errors.EmptyDataError:
            print("Error: The file is empty.")
            return None
        except Exception as e:
            print(f"An error occurred: {e}")
            return None