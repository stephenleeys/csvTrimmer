import os
import pandas as pd

def trim_and_sort(input_file):
    """
    Trim the rows of a CSV file so that all integers in the 'coln' column
    have the same number of occurrences, and save the trimmed data to a new
    CSV file.
    """
    
    # Read the CSV data from the file
    df = pd.read_csv(input_file)
    
    # Sort the DataFrame by the 'coln' column
    df = df.sort_values(by=['coln','row'])
    # Reset index after sorting
    df.reset_index(drop=True, inplace=True)
    
    # Count occurrences of each integer in the 'coln' column
    occurrences = df['coln'].value_counts()
    
    # Find the minimum occurrence
    min_occurrence = occurrences.min()
    print(f'Minimum occurrence: {min_occurrence}')
    
    # Identify integers with occurrences greater than the minimum
    to_trim = occurrences[occurrences > min_occurrence].index
    
    # Create a DataFrame to store the trimmed data
    trimmed_df = pd.DataFrame()
    
    # Trim the rows for each integer that exceeds the minimum occurrence
    for integer in to_trim:
        # Get the rows corresponding to the integer
        rows = df[df['coln'] == integer]
        
        # Select only the number of rows equal to the minimum occurrence
        trimmed_rows = rows.head(min_occurrence)
        
        # Append to the new DataFrame
        trimmed_df = pd.concat([trimmed_df, trimmed_rows], ignore_index=True)
    
    # Include rows that do not exceed the minimum occurrence
    for integer in occurrences[occurrences == min_occurrence].index:
        rows = df[df['coln'] == integer]
        trimmed_df = pd.concat([trimmed_df, rows], ignore_index=True)
    
    # Sort the trimmed DataFrame by the 'coln' column
    trimmed_df = trimmed_df.sort_values(by=['coln','row'])
    # Reset index after sorting
    trimmed_df.reset_index(drop=True, inplace=True)
    
    # Display the trimmed and sorted DataFrame
    print("Trimmed and Sorted DataFrame:")
    print(trimmed_df)
    
    # Save the trimmed and sorted DataFrame to a CSV file
    output_file = f'output/{os.path.basename(input_file)}'
    trimmed_df.to_csv(output_file, index=False)
    print(f'Truncated and sorted data saved to {output_file}')

# Define the input folder
input_folder = 'input'
# List all files in the input folder
files = os.listdir(input_folder)
# Filter for CSV files
csv_files = [f for f in files if f.endswith('.csv')]

# Check if there are any CSV files
if csv_files:
    # Loop through all the CSV files
    for file_name in csv_files:
        # Construct the full path
        file_path = os.path.join(input_folder, file_name)
        
        # Read the CSV file
        data = pd.read_csv(file_path)

        print(f"File name: {file_name}")
        print("Data loaded from the CSV file:")
        print(data)
        
        # Trim and sort the data
        trim_and_sort(file_path)
else:
    print("No CSV files found in the input folder.")


