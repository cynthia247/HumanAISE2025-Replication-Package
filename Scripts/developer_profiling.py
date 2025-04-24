

import requests
import pandas as pd

def get_contributors(repo, token):
    """
    Fetch all contributors for a given repository, including their detailed info.
    
    Args:
        repo (str): Repository in the format 'owner/repo'.
        token (str): GitHub personal access token.
    
    Returns:
        list: A list of dictionaries containing contributor details.
    """
    url = f"https://api.github.com/repos/{repo}/contributors"
    headers = {'Authorization': f'token {token}'}
    all_contributors = []

    # Pagination loop to fetch all contributors
    while url:
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            print(f"Error fetching contributors for {repo}: {response.json()}")
            break

        contributors = response.json()

        for contributor in contributors:
            username = contributor['login']

            # Fetch user details
            user_url = f"https://api.github.com/users/{username}"
            user_response = requests.get(user_url, headers=headers)
            if user_response.status_code != 200:
                print(f"Error fetching user details for {username}: {user_response.json()}")
                continue

            user_info = user_response.json()

            # Extract contributor details
            all_contributors.append({
                "repository": repo,
                "username": username,
                "name": user_info.get('name', 'N/A'),
                "bio": user_info.get('bio', 'N/A'),
                "location": user_info.get('location', 'N/A'),
                "contributions": contributor['contributions']
            })

        # Check for the 'next' link in pagination
        url = response.links.get('next', {}).get('url')

    return all_contributors

def process_repositories(input_csv, output_csv_dev, token):
    """
    Process repositories from a CSV file and save the output to another CSV file.
    
    Args:
        input_csv (str): Path to the input CSV file containing repository names.
        output_csv_dev (str): Path to the output CSV file for contributor data.
        token (str): GitHub personal access token.
    """
    # Read the input CSV
    repo_df = pd.read_csv(input_csv)
    all_contributors = []

    for _, row in repo_df.iloc[0:].iterrows():
        repo = row['Name_Repo']
        print(f"Processing repository: {repo}")
        try:
            contributors = get_contributors(repo, token)
            all_contributors.extend(contributors)
        except Exception as e:
            print(f"Failed to process {repo}: {e}")

    # Save the results to the output CSV
    if all_contributors:
        output_df = pd.DataFrame(all_contributors)
        output_df.to_csv(output_csv_dev, index=False)
        print(f"Contributor data saved to {output_csv_dev}")
    else:
        print("No contributor data collected.")

if __name__ == "__main__":
    # Input CSV file with repository names
    input_csv = "/home/uji657/Downloads/src/HumanAISE2025/Dataset/repo_name.csv"  # Input file with a 'Name_Repo' column (owner/repo format)
    output_csv_dev = "/home/uji657/Downloads/src/HumanAISE2025/Dataset/developers_name.csv"  # Output file to save results

    token = "GITHUB_TOKEN"

    # Process repositories and save results
    process_repositories(input_csv, output_csv_dev, token)
