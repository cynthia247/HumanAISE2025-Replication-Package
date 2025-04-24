import pandas as pd
# from github_token import *
repo_input_src = '/home/uji657/Downloads/src/HumanAISE2025/Dataset/repo_name.csv'
repo_output_src = '/home/uji657/Downloads/src/HumanAISE2025/Dataset/temp.csv'


# Define the GitHub instance using the token from github_token
from github import Github
import time
g = Github("GITHUB_TOKEN")


repo_set = set()

df_repo = pd.read_csv(repo_input_src)
for index, paper in df_repo.iloc[73:74].iterrows():
    df_issue = pd.DataFrame()

    print(f'[{index + 1}] {paper["Name_Repo"]}')
    repo_url = paper['Name_Repo']
    
    try:
        repo = g.get_repo(repo_url)
        if 'tree/master' in repo_url:
            print(f"Skipping repository '{repo_url}' as it contains 'tree/master'")
            continue
        if 'google-research' in repo_url:
            print(f"Skipping repository '{repo_url}' as it contains 'tree/master'")
            continue
        # print(repo.raw_data['status'])
        # if repo.raw_data['status'] != 200:
        #     print(f'Error: Status code {repo.raw_data["status"]}')
        #     print("retrying after 60 seconds")
        #     time.sleep(60)
        #     continue
        
    except:
        print(f'Could not find: {repo_url}')
        print('*' * 40)
        continue


    open_issues = repo.get_issues(state="open")
 
    closed_issues = repo.get_issues(state="closed")

    open_pulls = repo.get_pulls(state="open")

    closed_pulls = repo.get_pulls(state="closed")
 
    num_stars = repo.stargazers_count

    num_forks = repo.forks_count
 
    num_watchers = repo.subscribers_count
   
    # contributors = repo.get_contributors()
    num_issue_open = sum(issue.pull_request is None for issue in open_issues)
 
    num_issue_closed = sum(issue.pull_request is None for issue in closed_issues)
  
    issue_labels = repo.get_labels()
  
    num_pr_open = sum(1 for pull in open_pulls)

    num_pr_closed = sum(1 for pull in closed_pulls)
    


    #May need to verify
    # num_issue_open_no_assignee = sum(issue.pull_request is None and issue.assignee is None for issue in open_issues)
    # num_issue_open_no_label = sum(issue.pull_request is None and len(issue.labels) == 0 for issue in open_issues)
    # num_issue_closed_no_assignee = sum(issue.pull_request is None and issue.assignee is None for issue in closed_issues)
    # num_issue_closed_no_label = sum(issue.pull_request is None and len(issue.labels) == 0 for issue in closed_issues)


    print(f'[{repo_url}]')
    print(f'Number of stars: {num_stars}')
    df_repo.loc[index, 'Num_Star'] = num_stars

    print(f'Number of forks: {num_forks}')
    df_repo.loc[index, 'Num_Fork'] = num_forks

    print(f'Number of watchers: {num_watchers}')
    df_repo.loc[index, 'Num_Watcher'] = num_watchers

    print(f'Created at: {repo.created_at}')
    df_repo.loc[index, 'Date_Created'] = repo.created_at

    print(f'Last updated at: {repo.updated_at}')
    df_repo.loc[index, 'Date_Last_Mod'] = repo.updated_at

    print(f'Number of issues: {num_issue_open}')
    df_repo.loc[index, 'Num_Issue'] = num_issue_open + num_issue_closed

    print(f'Number of issue types: {issue_labels.totalCount}')
    df_repo.loc[index, 'Num_Issue_Type'] = issue_labels.totalCount

    print(f'Number of open issues: {num_issue_open}')
    df_repo.loc[index, 'Num_Issue_Open'] = num_issue_open

    print(f'Number of closed issues: {num_issue_closed}')
    df_repo.loc[index, 'Num_Issue_Closed'] = num_issue_closed

    print(f'Number of open PRs: {num_pr_open}')
    df_repo.loc[index, 'Num_PR_Open'] = num_pr_open

    print(f'Number of closed PRs: {num_pr_closed}')
    df_repo.loc[index, 'Num_PR_Closed'] = num_pr_closed

    # print(f'Contributors: ')
    # df_repo.loc[index, 'Contributors'] = "\n".join([_._identity for _ in contributors])

    # if num_issue_open > 0:
    #     print(
    #         f'Open issues with no assignee: {(num_issue_open_no_assignee / num_issue_open):.2%} ({num_issue_open_no_assignee})')
    #     df_repo.loc[index, 'Num_Issue_Open_No_Assignee'] = int(num_issue_open_no_assignee)
    #     print(
    #         f'Open issues with no label: {(num_issue_open_no_label / num_issue_open):.2%} ({num_issue_open_no_label})')
    #     df_repo.loc[index, 'Num_Issue_Open_No_Label'] = int(num_issue_open_no_label)

    # if num_issue_closed > 0:
    #     print(
    #         f'Closed issues with no assignee: {(num_issue_closed_no_assignee / num_issue_closed):.2%} ({num_issue_closed_no_assignee})')
    #     df_repo.loc[index, 'Num_Issue_Closed_No_Assignee'] = int(num_issue_closed_no_assignee)
    #     print(
    #         f'Closed issues with no label: {(num_issue_closed_no_label / num_issue_closed):.2%} ({num_issue_closed_no_label})')
    #     df_repo.loc[index, 'Num_Issue_Closed_No_Label'] = int(num_issue_closed_no_label)



    df_repo.to_csv(repo_output_src, index=False)
    
