import pandas as pd
from transaction_parser import TransactionParser
from data_preprocessor import DataPreprocessor
from model import TransactionClassifier
from visualization import plot_spending_summary

# Main application file that integrates all the components 
# Such as loading the data, preprocessing it, and training the model.
def main():
    # Step 1: Load transaction data
    file_path = 'sample_transactions.csv'  # Update with your actual file path
    parser = TransactionParser(file_path)
    transactions = parser.load_transactions()

    if transactions is not None:
        # Add a default category column
        transactions['category'] = 'Uncategorized'  # Add this line

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

        # Step 4: Visualize spending summary
        plot_spending_summary(preprocessor.transactions)

if __name__ == "__main__":
    main()