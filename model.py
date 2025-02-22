import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import classification_report

# Model for categorizing the transactions. 
# This will involve creating a class that trains a machine learning model on the cleaned transaction data.
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import classification_report

class TransactionClassifier:
    def __init__(self, data):
        """
        Initializes the TransactionClassifier with transaction data.
        
        :param data: DataFrame containing the transaction data with cleaned descriptions and categories.
        """
        self.data = data
        self.vectorizer = CountVectorizer()
        self.model = RandomForestClassifier()

    def train(self):
        """
        Trains the Random Forest model on the transaction data.
        """
        X = self.vectorizer.fit_transform(self.data['cleaned_description'])
        y = self.data['category']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        # Fit the model
        self.model.fit(X_train, y_train)
        
        # Evaluate the model
        y_pred = self.model.predict(X_test)
        print(classification_report(y_test, y_pred))

    def predict(self, new_descriptions):
        """
        Predicts categories for new transaction descriptions.
        
        :param new_descriptions: List of new transaction descriptions to classify.
        :return: List of predicted categories.
        """
        X_new = self.vectorizer.transform(new_descriptions)
        return self.model.predict(X_new)