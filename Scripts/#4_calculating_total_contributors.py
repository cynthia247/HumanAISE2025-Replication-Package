import pandas as pd

def calculate_and_assign_contributors(developer_csv, target_csv, output_csv):
    """
    Calculate total developers for each repository and assign the totals to another CSV file.

    Args:
        developer_csv (str): Path to the CSV containing repository and developer information.
        target_csv (str): Path to the target CSV file to match repositories.
        output_csv (str): Path to save the resulting CSV with total contributors added.
    """
    # Load the CSV files
    dev_df = pd.read_csv(developer_csv)
    target_df = pd.read_csv(target_csv)


    # Calculate total developers for each repository
    contributor_counts = dev_df.groupby('repository')['username'].nunique().reset_index()
    contributor_counts.rename(columns={'username': 'total_contributors'}, inplace=True)

    # Merge with the target CSV
    result_df = target_df.merge(contributor_counts, on='repository', how='left')

    # Save the updated target CSV with the new column
    result_df.to_csv(output_csv, index=False)
    print(f"Results saved to {output_csv}")

# File paths
developer_csv = '/home/uji657/Downloads/src/HumanAISE2025/Dataset/MAIN_developers_name.csv'  # Replace with the path to the developer CSV
target_csv = '/home/uji657/Downloads/src/HumanAISE2025/Dataset/#3_filtering_repos_withDiversity.csv'  # Replace with the path to the target CSV
output_csv = '/home/uji657/Downloads/src/HumanAISE2025/Dataset/#4_filtering_repos_withTotalContributors.csv'  # Replace with the desired output file path

# Run the function
calculate_and_assign_contributors(developer_csv, target_csv, output_csv)
