import subprocess
import requests
import time
import os
import shutil
import pandas as pd


SONARQUBE_URL = "http://localhost:9000"
SONARQUBE_TOKEN = "SONARQUBE_TOKEN"
BASE_DIR = "/home/uji657/Downloads/src/test"  
OUTPUT_CSV = "/home/uji657/Downloads/src/HumanAISE2025/Dataset/sonarqube_analysis_results.csv"

METRICS = "security_hotspots, code_smells, comment_lines_density, complexity, cognitive_complexity"

def clone_repository(repo_url, repo_name):
   
    repo_path = os.path.join(BASE_DIR, repo_name)
    if os.path.exists(repo_path):
        print(f"Repository {repo_name} already exists. Skipping clone.")
    else:
        print(f"Cloning repository: {repo_name}...")
        subprocess.run(["git", "clone", repo_url, repo_path], check=True)
    return repo_path

def run_sonar_scanner(repo_name,project_key, project_dir):
    """Run SonarScanner to analyze the project."""
    owner, repo = repo_name.split("/")
    try:
        print(f"Running SonarScanner for {project_key}...")
        command = f"cd {project_dir} && git clone https://github.com/{repo_name} && cd {repo} && sonar-scanner -Dsonar.projectKey=Test_project -Dsonar.host.url={SONARQUBE_URL} -Dsonar.login={SONARQUBE_TOKEN}"
        subprocess.run( command, check=True, shell=True)
        print("SonarScanner completed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"SonarScanner failed for {project_key}: {e}")
        return False
    return True

def fetch_analysis_results(project_key):
    """Fetch analysis results from SonarQube."""
    url = f"{SONARQUBE_URL}/api/measures/component"
    params = {"component": project_key, "metricKeys": METRICS}
    response = requests.get(url, params=params, auth=(SONARQUBE_TOKEN, ""))
    if response.status_code == 200:
        data = response.json()
        metrics = {metric["metric"]: metric["value"] for metric in data["component"]["measures"]}
        return metrics
    else:
        print(f"Failed to fetch results for {project_key}: {response.status_code} - {response.text}")
        return {}

def delete_repository(repo_name):
    """Delete the repository directory after analysis."""
    owner, repo = repo_name.split("/")
    if os.path.exists(repo):
        print(f"Deleting repository: {repo}...")
        shutil.rmtree(f"/home/uji657/Downloads/src/test/{repo}/")
        print(f"Repository {repo} deleted.")
    else:
        print(f"Repository {repo} does not exist, skipping deletion.")

def main():
    input_csv = "/home/uji657/Downloads/src/HumanAISE2025/Dataset/sonar_analysis.csv"  
    df = pd.read_csv(input_csv)

    results = []

    for _, row in df.iterrows():
        repo_name = row["repository"]
        
        repo_url = f"https://github.com/{repo_name}"
        project_key = "Test_project"  
        
        if run_sonar_scanner(repo_name,project_key, BASE_DIR):
            time.sleep(20)
            metrics = fetch_analysis_results(project_key)
            print('metrics: ', metrics)
            metrics["repository"] = repo_name
            results.append(metrics)
        else:
            print(f"Skipping metrics fetch for {repo_name} due to scanner failure.")
        time.sleep(10)
        delete_repository(repo_name)
        

    # Save results to CSV
    output_df = pd.DataFrame(results)
    output_df.to_csv(OUTPUT_CSV, index=False)
    print(f"Analysis results saved to {OUTPUT_CSV}")

if __name__ == "__main__":
    main()
