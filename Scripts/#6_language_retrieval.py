import requests
import pandas as pd

# GitHub API token (to increase API limits)
GITHUB_TOKEN = "GITHUB_TOKEN"
GITHUB_API_URL = "https://api.github.com/repos"

# Function to get the main language of a GitHub repository
def get_repo_language(repo_name):
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}
    response = requests.get(f"{GITHUB_API_URL}/{repo_name}", headers=headers)
    if response.status_code == 200:
        return response.json().get("language", "Unknown")
    else:
        print(f"Error fetching data for {repo_name}: {response.status_code}")
        return "Error"

# Read input CSV
input_csv = "/home/uji657/Downloads/src/HumanAISE2025/Dataset/#5_repo_metadata+popularity_data.csv"  # Replace with your input file
output_csv = "/home/uji657/Downloads/src/HumanAISE2025/Dataset/#5_repo_metadata+popularity+language_data.csv"  # Replace with your output file

# Read the CSV into a DataFrame
df = pd.read_csv(input_csv)


# Fetch and append language data
df["language"] = df["repository"].apply(get_repo_language)

# Save the updated DataFrame to a new CSV
df.to_csv(output_csv, index=False)

print(f"Updated CSV with languages saved to {output_csv}")
