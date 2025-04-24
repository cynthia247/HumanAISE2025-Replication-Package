import os
import subprocess
import pandas as pd
import shutil
import time

PROJECT_DIR="/home/uji657/Downloads/src/test/"
AUTHOR_CSV = "/home/uji657/Downloads/src/HumanAISE2025/Dataset/MAIN_developers_name.csv"  # CSV with author and gender info
MALE_OUTPUT_DIR = "/home/uji657/Downloads/src/test/male_files"  # Male-authored files
FEMALE_OUTPUT_DIR = "/home/uji657/Downloads/src/test/female_files"  # Female-authored files
CODE_EXTENSIONS = {".py", ".java", ".js", ".cpp", ".c", ".h", ".html", ".css", ".ts", ".rb", ".php", ".ipynb"}  # Add code file extensions here

# Read author-gender mapping from CSV
def load_author_gender_mapping(csv_path):
    """Load author-to-gender mapping from CSV."""
    df = pd.read_csv(csv_path)
    return dict(zip(df["name"], df["gender"]))  # CSV should have columns: name, gender

# Run `git blame` and get authors for a file
def get_file_authors(file_path, repo_dir):
    """Run `git blame` on a file and extract authors."""
    try:
        result = subprocess.run(
            ["git", "blame", "--line-porcelain", file_path],
            cwd=repo_dir,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        if result.returncode != 0:
            print(f"Error running git blame on {file_path}: {result.stderr}")
            return set()

        authors = set()
        for line in result.stdout.splitlines():
            if line.startswith("author "):
                author = line[len("author "):].strip()
                authors.add(author)
        return authors
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return set()

# Copy files to their respective directories
def copy_file(file_path, output_dir, repo_dir):
    """Copy a file to the specified output directory."""
    try:
        relative_path = os.path.relpath(file_path, repo_dir)
        dest_path = os.path.join(output_dir, relative_path)
        os.makedirs(os.path.dirname(dest_path), exist_ok=True)
        shutil.copy2(file_path, dest_path)
    except Exception as e:
        print(f"Error copying file {file_path} to {output_dir}: {e}")

# Main function to process the repository
def analyze_repository(repo_dir, author_gender_map):
    """Analyze all code files in the repository."""
    for root, _, files in os.walk(repo_dir):
        for file in files:
            # Skip non-code files
            if not any(file.endswith(ext) for ext in CODE_EXTENSIONS):
                continue

            file_path = os.path.join(root, file)
            relative_file_path = os.path.relpath(file_path, repo_dir)

            # Get authors of the file
            authors = get_file_authors(relative_file_path, repo_dir)

            # Skip files with multiple authors
            if len(authors) != 1:
                print(f"Skipping file with multiple authors: {relative_file_path}")
                continue

            # Get gender of the sole author
            author = list(authors)[0]
            gender = author_gender_map.get(author)

            if gender == "Male":
                print(f"Copying male-authored file: {relative_file_path}")
                copy_file(file_path, MALE_OUTPUT_DIR, repo_dir)
            elif gender == "Female":
                print(f"Copying female-authored file: {relative_file_path}")
                copy_file(file_path, FEMALE_OUTPUT_DIR, repo_dir)
            else:
                print(f"Unknown author or gender for file: {relative_file_path}. Skipping.")

if __name__ == "__main__":
    # Load author-gender mapping
    df = pd.read_csv("/home/uji657/Downloads/src/HumanAISE2025/Dataset/sonar_analysis.csv")
    for _, row in df.iterrows():
        name = row["repository"]

        command = f"cd {PROJECT_DIR} && git clone https://github.com/{name}"
        subprocess.run(command, check=True, shell=True)

        owner,repo = name.split("/")
        REPO_DIR = f"/home/uji657/Downloads/src/test/{repo}"
        author_gender_map = load_author_gender_mapping(AUTHOR_CSV)

        # Analyze the repository
        analyze_repository(REPO_DIR, author_gender_map)

        print("File categorization completed.")
        time.sleep(10)