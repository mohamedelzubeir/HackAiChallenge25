import pandas as pd
from transaction_parser import TransactionParser
from data_preprocessor import DataPreprocessor
from model import TransactionClassifier

# Main application file that integrates all the components 
# Such as loading the data, preprocessing it, and training the model.
def main():
    # Step 1: Load transaction data
    file_path = 'data/transactions.csv'  # Update with your actual file path
    parser = TransactionParser(file_path)
    transactions = parser.load_transactions()

    if transactions is not None:
        # Step 2: Preprocess the data
        preprocessor = DataPreprocessor(transactions)
        preprocessor.preprocess()

        # Step 3: Train the model
        classifier = TransactionClassifier(preprocessor.transactions)
        classifier.train()

        # Example prediction
        new_descriptions = ["Walmart Grocery", "Rent Payment", "Starbucks Coffee"]
        predictions = classifier.predict(new_descriptions)
        print("Predictions for new transactions:", predictions)

if __name__ == "__main__":
    main()