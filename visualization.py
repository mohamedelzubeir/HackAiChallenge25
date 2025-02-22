import matplotlib.pyplot as plt

def plot_spending_summary(transactions):
    """
    Plots a pie chart of spending by category.
    
    :param transactions: DataFrame containing the transaction data with categories.
    """
    spending_summary = transactions.groupby('category')['Amount'].sum()
    
    plt.figure(figsize=(10, 6))
    plt.pie(spending_summary, labels=spending_summary.index, autopct='%1.1f%%', startangle=140)
    plt.title('Spending by Category')
    plt.axis('equal')  # Equal aspect ratio ensures that pie chart is circular.
    plt.show()