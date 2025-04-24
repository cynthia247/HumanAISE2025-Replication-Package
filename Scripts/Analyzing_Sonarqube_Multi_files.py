import subprocess
import requests
import time
import os
import pandas as pd

# SonarQube Configuration
SONARQUBE_URL = "http://localhost:9000"
SONARQUBE_TOKEN = "SONARQUBE_TOKEN"

# Paths to local directories containing Python files
MALE_DIR = "/home/uji657/Downloads/src/HumanAISE2025/multi-authored-files/small/Male"
FEMALE_DIR = "/home/uji657/Downloads/src/HumanAISE2025/multi-authored-files/small/Female"

# Output CSV file for results (store results in a single CSV)
OUTPUT_CSV = "/home/uji657/Downloads/src/HumanAISE2025/Dataset/sonarqube_results_Small.csv"

# SonarQube metrics to collect
METRICS = "security_hotspots, code_smells, complexity, cognitive_complexity, comment_lines_density, ncloc"

def run_sonar_scanner(project_key, project_dir, group_name):
    """Run SonarScanner on a local directory containing Python files."""
    try:
        print(f"Running SonarScanner for {project_key} in {project_dir}...")
        command = f"cd {project_dir} && sonar-scanner -Dsonar.projectKey={project_key} -Dsonar.sources=. -Dsonar.host.url={SONARQUBE_URL} -Dsonar.login={SONARQUBE_TOKEN}"
        subprocess.run(command, check=True, shell=True)
        print(f"SonarScanner completed successfully for {group_name}.")
        return True
    except subprocess.CalledProcessError as e:
        print(f"SonarScanner failed for {project_key}: {e}")
        return False

def fetch_analysis_results(project_key):
    """Fetch SonarQube analysis results."""
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

def process_subdirectories(group_name, base_dir):
    """Iterate through subdirectories and run SonarQube analysis."""
    results = []

    for subdir in sorted(os.listdir(base_dir)):
        project_dir = os.path.join(base_dir, subdir)
        if os.path.isdir(project_dir):  # Ensure it's a directory
            group_name=subdir
            project_key = f"Test_result"
            print(f"\nProcessing {group_name} repository: {subdir}\n")

            if run_sonar_scanner(project_key, project_dir, group_name):
                time.sleep(20)  # Allow SonarQube to process results
                metrics = fetch_analysis_results(project_key)

                if metrics:
                    print(f"Metrics collected for {subdir}: {metrics}")
                    metrics["group"] = group_name
                    metrics["repository"] = subdir
                    results.append(metrics)
                else:
                    print(f"No metrics collected for {subdir}.")
            else:
                print(f"Skipping metrics fetch due to SonarScanner failure for {subdir}.")
    
    return results

def main():
    """Main function to analyze all subdirectories under Male and Female directories."""
    male_results = process_subdirectories("Male", MALE_DIR)
    female_results = process_subdirectories("Female", FEMALE_DIR)

    # Combine results and store in a single CSV file
    all_results = male_results + female_results
    if all_results:
        output_df = pd.DataFrame(all_results)
        output_df.to_csv(OUTPUT_CSV, index=False)
        print(f"\nAll analysis results saved to {OUTPUT_CSV}\n")
    else:
        print("\nNo results to save.")

if __name__ == "__main__":
    main()
