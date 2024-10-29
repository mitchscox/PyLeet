import pandas as pd

# Load the uploaded CSV file
file_path = 'parsed_messages.csv'
df = pd.read_csv(file_path)

# Group by 'Stock Symbol' and sum the 'Quantity' column for each symbol
grouped_data = df.groupby('Stock Symbol')['Quantity'].sum().reset_index()

# Show the grouped data
print(grouped_data)

output_file_path = 'grouped.csv'
grouped_data.to_csv(output_file_path, index=False)

output_file_path
