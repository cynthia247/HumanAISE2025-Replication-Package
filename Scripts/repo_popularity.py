import requests
import re
import pandas as pd
import time

# GitHub personal access token (optional for higher rate limits)
TOKEN = "GITHUB_TOKEN"
HEADERS = {"Authorization": f"token {TOKEN}"}

def fetch_repo_contents(repo, path=""):
    """
    Fetch the contents of a repository or directory.
    """
    url = f"https://api.github.com/repos/{repo}/contents/{path}"
    while True:
        response = requests.get(url, headers=HEADERS)
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 403:  # Rate limit exceeded
            print("Rate limit exceeded. Sleeping for 60 seconds...")
            time.sleep(60)
        else:
            raise Exception(f"Failed to fetch contents for {repo} at {path}: {response.status_code}")

def count_code_files(repo,path=""):
    """
    Count the number of code files in a repository.
    """
    try:
        # Fetch contents of the current directory
        contents = fetch_repo_contents(repo, path)
        file_count = 0

        for item in contents:
            if item['type'] == 'file' and item['name'].endswith(('.py', '.js', '.java', '.c', '.cpp', '.h', '.cs', '.html', '.css')):
                # Match common pre-trained model file extensions
                file_count += 1
            elif item['type'] == 'dir':
                # Recursively check subdirectories
                file_count += count_code_files(repo, item['path'])

        return file_count
    except Exception as e:
        print(f"Error fetching pre-trained models in {repo}/{path}: {e}")
        return 0


TARGET_EXTENSIONS = {".py", ".js", ".java", ".c", ".cpp", ".h", ".cs", ".html", ".css"}

def count_lines_in_file(url):
    """Fetch file content and count lines."""
    while True:
        response = requests.get(url, headers=HEADERS)
        if response.status_code == 200:
            content = response.text
            return content.count('\n') + 1  # Count lines in the file
        elif response.status_code == 403:  # Rate limit exceeded
            print("Rate limit exceeded. Sleeping for 60 seconds...")
            time.sleep(60)
        else:
            return 0
        
def calculate_lines_of_code_by_extension(repo, path=""):
    """Calculate lines of code in specific file extensions."""
    try:
        contents = fetch_repo_contents(repo, path)
        total_lines = 0
        file_type_counts = {ext: 0 for ext in TARGET_EXTENSIONS}

        for item in contents:
            if item['type'] == 'file':
                # Check file extension
                file_extension = item['name'].split('.')[-1]
                if f".{file_extension}" in TARGET_EXTENSIONS:
                    lines = count_lines_in_file(item['download_url'])
                    total_lines += lines
                    file_type_counts[f".{file_extension}"] += lines
            elif item['type'] == 'dir':
                # Recurse into subdirectories
                subdir_lines, subdir_counts = calculate_lines_of_code_by_extension(repo, item['path'])
                total_lines += subdir_lines
                for ext, count in subdir_counts.items():
                    file_type_counts[ext] += count
        return total_lines, file_type_counts
    except Exception as e:
        print(f"Error processing repository {repo}: {e}")
        raise

def count_subdirectories(repo):
    """
    Count the number of subdirectories in the root directory of a GitHub repository.
    
    :param repo: str - Repository in the format "owner/repo"
    :return: int - Number of subdirectories in the root directory
    """
    try:
        contents = fetch_repo_contents(repo,)
        
        # Count items of type 'dir'
        subdirectories = [item for item in contents if item['type'] == 'dir']
        return len(subdirectories)
    
    except Exception as e:
        print(f"Error processing repository {repo}: {e}")
        return 0

def count_shell_scripts(repo):
    """
    Count the number of shell scripts in a repository.
    """
    try:
        contents = fetch_repo_contents(repo)
        shell_scripts = [item for item in contents if item['type'] == 'file' and item['name'].endswith('.sh')]
        return len(shell_scripts)
    except Exception as e:
        print(f"Error fetching shell scripts: {e}")
        return 0
    

def count_pretrained_models(repo, path=""):
    """
    Count the number of pre-trained model files in a repository (e.g., .tar.gz, .pt, .h5, .onnx).
    This function recursively traverses all directories in the repository.
    """
    try:
        # Fetch contents of the current directory
        contents = fetch_repo_contents(repo, path)
        pretrained_model_count = 0

        for item in contents:
            if item['type'] == 'file' and re.search(r"\.(tar\.gz|pt|h5|onnx|ckpt|weights)$", item['name'], re.IGNORECASE):
                # Match common pre-trained model file extensions
                pretrained_model_count += 1
            elif item['type'] == 'dir':
                # Recursively check subdirectories
                pretrained_model_count += count_pretrained_models(repo, item['path'])

        # print(pretrained_model_count)
        return pretrained_model_count
    except Exception as e:
        print(f"Error fetching pre-trained models in {repo}/{path}: {e}")
        return 0
    

def analyze_readme(repo):
    """
    Analyze the README file for lists, code blocks, inline code, and GitHub links.
    """
    try:
        # Fetch the README file
        url = f"https://api.github.com/repos/{repo}/readme"
        response = requests.get(url, headers=HEADERS)
        if response.status_code != 200:
            raise Exception(f"Failed to fetch README for {repo}: {response.status_code}")
        
        readme_content = requests.get(response.json()['download_url']).text
        
        # Count lists
        list_count = len(re.findall(r"^\s*[-*+]\s", readme_content, re.MULTILINE))
        
        # Count code blocks (triple backticks)
        
        code_block_count = readme_content.count("```")
        
        # Count inline code elements (single backticks)
        inline_code_matches = re.findall(r"(?<!`)`(?!`).+?`(?!`)", readme_content)
        inline_code_count = len(inline_code_matches)
        
        # Count GitHub links
        github_links = re.findall(
        r"(https?://github\.com/[^\s)<>\"']+)",  # Matches GitHub URLs 
        readme_content
    )
        # Count images
        image_links = re.findall(r"!\[.*?\]\((.*?)\)", readme_content)
        image_count = len(image_links)

        
        return list_count, code_block_count // 2, inline_code_count, len(set(github_links)), image_count
    except Exception as e:
        print(f"Error analyzing README: {e}")
        return 0, 0, 0, 0, 0
       

def check_license(repo):
    """
    Check whether the repository has a license.
    """
    try:
        contents = fetch_repo_contents(repo)
        for item in contents:
            if item['type'] == 'file' and item['name'].lower() == 'license':
                return True
        return False
    except Exception as e:
        print(f"Error checking license: {e}")
        return False

def analyze_repository(repo):
    """
    Perform all analyses on the repository.
    """
    print(f"Analyzing repository: {repo}")
    try:
        num_code_files = count_code_files(repo, path="")
        total_lines, extension_counts = calculate_lines_of_code_by_extension(repo)
        num_modules = count_subdirectories(repo)
        shell_script_count = count_shell_scripts(repo)
        list_count, code_block_count, inline_code_count, github_links, image_count = analyze_readme(repo)
        has_license = check_license(repo)
        pretrained_model_count = count_pretrained_models(repo)
        
        print(f"Analysis complete for {repo}")
        print(f"Code files: {num_code_files}")
        print(f"Total lines of code: {total_lines}")
        print(f"Modules: {num_modules}")
        print (f"Pretrained models: {pretrained_model_count}")  
        print(f"Shell scripts: {shell_script_count}")
        print(f"Lists in README: {list_count}") 
        print(f"Code blocks in README: {code_block_count}")
        print(f"Inline code in README: {inline_code_count}")
        print(f"GitHub links in README: {github_links}")
        print(f"Images in README: {image_count}")
        print(f"License: {'Yes' if has_license else 'No'}")
        print("\n")

        return {
            "repository": repo,
            "num_code_files": num_code_files,
            "total_lines_of_code": total_lines,
            "num_modules": num_modules,
            "pretrained_models": pretrained_model_count,
            "shell_scripts": shell_script_count,
            "lists_in_readme": list_count,
            "code_blocks_in_readme": code_block_count,
            "inline_code_in_readme": inline_code_count,
            "images_in_readme": image_count,
            "github_links_in_readme": github_links,
            "has_license": "Yes" if has_license else "No",   
        }
    except Exception as e:
        print(f"Error analyzing repository {repo}: {e}")
        return {
            "repository": repo,
            "num_code_files": num_code_files,
            "total_lines_of_code": total_lines,
            "num_modules": 0,
            "pretrained_models": 0,
            "shell_scripts": 0,
            "lists_in_readme": 0,
            "code_blocks_in_readme": 0,
            "inline_code_in_readme": 0,
            "images_in_readme": 0,
            "github_links_in_readme": 0,
            "has_license": "Error",            
        }

def process_repositories(input_csv, output_csv):
    """
    Process repositories from a CSV file and save the output to another CSV file.
    """
    # Read the input CSV
    repo_df = pd.read_csv(input_csv)
    results = []

    for _, row in repo_df.iloc[0:].iterrows():
        repo = row['Name_Repo']
        print(f"Processing repository: {repo}")
        try:
            result = analyze_repository(repo)
            results.append(result)
            print(f"Finished processing {repo}")
        except Exception as e:
            print(f"Failed to process {repo}: {e}")

    # Save the results to the output CSV
    output_df = pd.DataFrame(results)
    output_df.to_csv(output_csv, index=False)
    print(f"Results saved to {output_csv}")


# Input and output CSV files
input_csv = "/home/uji657/Downloads/src/HumanAISE2025/Dataset/repo_name.csv"  # Input file with a 'repository' column (owner/repo format)
output_csv = "/home/uji657/Downloads/src/HumanAISE2025/Dataset/repo_analysis.csv"  # Output file to save results

# Process repositories
process_repositories(input_csv, output_csv)
