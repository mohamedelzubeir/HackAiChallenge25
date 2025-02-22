# HackAiChallenge25

# Team Members: Mohamed, Amir, Yunus, Omar

## Project Overview
This project aims to develop an AI-based Personal Finance Tracker that automatically categorizes financial transactions based on their descriptions and amounts. The application will provide insights into spending patterns and help users manage their finances effectively.

## Step-by-Step Plan

### Step 1: Data Collection
- Obtain sample transaction data (CSV files from real or mock bank statements).
- Structure should include:
  - **Date**: The date of the transaction.
  - **Description**: A brief description of the transaction (e.g., "Walmart Grocery").
  - **Amount**: The amount spent or received.
  - **Type**: Credit/Debit.

### Step 2: Preprocessing
- Clean text descriptions:
  - Remove special characters and punctuation.
  - Convert text to lowercase.
  - Remove stopwords.
- Handle missing values.
- Convert categorical values to numerical if needed.

### Step 3: AI Model for Categorization
- **Baseline Approach**: Use simple rule-based mapping (e.g., "Walmart" → "Groceries").
- **Machine Learning Approach**: Train an ML classifier (e.g., Logistic Regression, Random Forest) to categorize transactions.
- **Deep Learning Approach (Advanced)**: Use NLP models like BERT to classify transaction descriptions.

### Step 4: Visualizing Data
- Generate spending charts:
  - Pie charts for category breakdown.
  - Line graphs for spending trends.
  - Bar charts for monthly expenses.

### Step 5: Deployment
- Use Streamlit to create an interactive web-based dashboard.
- Deploy on Hugging Face Spaces or Heroku.

## Algorithm Breakdown
1. **Data Input**: Load transaction data from a CSV or JSON file.
2. **Data Cleaning**: 
   - Remove unnecessary characters from descriptions.
   - Normalize text (lowercase).
   - Handle missing values appropriately.
3. **Feature Extraction**: 
   - Convert transaction descriptions into a format suitable for model training (e.g., using CountVectorizer or TF-IDF).
4. **Model Training**:
   - Split data into training and testing sets.
   - Train the chosen model (e.g., Random Forest) on the training set.
5. **Prediction**:
   - Use the trained model to predict categories for new transactions.
6. **Visualization**:
   - Generate visualizations to represent spending patterns and insights.
7. **User Interface**:
   - Create a Streamlit dashboard for user interaction.
8. **Deployment**:
   - Deploy the application to a cloud platform for public access.

## Conclusion
This project will provide users with a comprehensive tool to track and analyze their financial transactions, helping them make informed decisions about their spending habits.