import pandas as pd
import numpy as np
import re
from nltk.corpus import stopwords

# Class for preprocessing the transaction data. 
# This class will handle cleaning the text descriptions and managing missing values.
class DataPreprocessor:
    def __init__(self, transactions):
        """
        Initializes the DataPreprocessor with transaction data.
        
        :param transactions: DataFrame containing the transaction data.
        """
        self.transactions = transactions

    def clean_descriptions(self):
        """
        Cleans the transaction descriptions by removing special characters,
        converting to lowercase, and removing stopwords.
        """
        stop_words = set(stopwords.words('english'))
        
        def clean_text(text):
            # Remove special characters and convert to lowercase
            text = re.sub(r'[^a-zA-Z\s]', '', text)
            text = text.lower()
            # Remove stopwords
            text = ' '.join(word for word in text.split() if word not in stop_words)
            return text
        
        self.transactions['cleaned_description'] = self.transactions['description'].apply(clean_text)

    def handle_missing_values(self):
        """
        Handles missing values in the transaction data.
        """
        # Example: Fill missing amounts with 0 and drop rows with missing descriptions
        self.transactions['amount'].fillna(0, inplace=True)
        self.transactions.dropna(subset=['description'], inplace=True)

    def preprocess(self):
        """
        Executes the preprocessing steps.
        """
        self.clean_descriptions()
        self.handle_missing_values()