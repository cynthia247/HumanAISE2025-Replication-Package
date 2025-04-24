
import pandas as pd

# Load the CSV file
data = pd.read_csv("/home/uji657/Downloads/src/HumanAISE2025/Dataset/#1_developers_names_percentage.csv")

# Function to annotate repositories
def annotate_repository(df):
    annotations = []
    for repo in df['repository'].unique():
        repo_data = df[df['repository'] == repo]
        print(repo_data)
        if 'Female' in repo_data['gender'].values:
            annotations.append((repo, "diverse")) 
        else:
            annotations.append((repo, "not-diverse"))  
    return pd.DataFrame(annotations, columns=['repository', 'annotation'])

annotations_df = annotate_repository(data)

data = data.merge(annotations_df, on='repository')

data.to_csv("/home/uji657/Downloads/src/HumanAISE2025/Dataset/#2_annotate_diversity.csv", index=False)

print("Annotations added and saved to 'annotated_file.csv'")
