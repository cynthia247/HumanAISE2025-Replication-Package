import pandas as pd

def filter_repositories_by_percentage(csv1_path, csv2_path, output_csv):

    
    df1 = pd.read_csv(csv1_path)
    df2 = pd.read_csv(csv2_path)

    
    if 'repository' not in df1.columns or 'repository' not in df2.columns or 'percentage_with_name' not in df2.columns:
        raise ValueError("Both CSV files must contain the 'repository' column, and the second CSV must have 'percentage_with_name'.")

   
    filtered_repos = df2[df2['percentage_with_name'] > 25]['repository']
    print(len(filtered_repos))
    
    filtered_df = df1[df1['repository'].isin(filtered_repos)]
    

    
    filtered_df.to_csv(output_csv, index=False)
    print(f"Filtered data saved to {output_csv}")


csv1_path = '/home/uji657/Downloads/src/HumanAISE2025/Dataset/MAIN_developers_name.csv'  
csv2_path = '/home/uji657/Downloads/src/HumanAISE2025/Dataset/temp.csv'  
output_csv = '/home/uji657/Downloads/src/HumanAISE2025/Dataset/#1_developers_names_percentage.csv'  

filter_repositories_by_percentage(csv1_path, csv2_path, output_csv)
