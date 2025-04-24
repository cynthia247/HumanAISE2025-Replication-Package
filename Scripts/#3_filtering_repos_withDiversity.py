import pandas as pd

def filter_and_merge_repositories(csv1_path, csv2_path, output_csv):
    # Load the CSV files
    df1 = pd.read_csv(csv1_path)
    df2 = pd.read_csv(csv2_path)


    # Drop duplicate repositories in the first CSV
    df1_unique = df1[['repository', 'diversity']].drop_duplicates()
    print(len(df1_unique))
    # Merge the second CSV with the unique repositories and their diversity column
    merged_df = df2.merge(df1_unique, on='repository', how='inner')

    # Save the filtered and merged DataFrame to a new CSV file
    merged_df.to_csv(output_csv, index=False)
    print(f"Filtered and merged data saved to {output_csv}")

# File paths
csv1_path = '/home/uji657/Downloads/src/HumanAISE2025/Dataset/temp.csv'  # Replace with the actual path to your first CSV
csv2_path = '/home/uji657/Downloads/src/HumanAISE2025/Dataset/MAIN_Repositories_popularity_metrics.csv'  # Replace with the actual path to your second CSV
output_csv = '/home/uji657/Downloads/src/HumanAISE2025/Dataset/#3_filtering_repos_withDiversity.csv'  # Replace with the desired output file path

# Run the function
filter_and_merge_repositories(csv1_path, csv2_path, output_csv)
