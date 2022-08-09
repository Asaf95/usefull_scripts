"""
This script can be used as a "db connection" for scripts who need to import files from other directories then were there local script is running.
The issue that the script solve is changing the absolute directory path each time from the local directory, and to create a single path to were files can
be import / export for security and access monitoring / control to the db
"""


import pandas as pd

full_path = "C:\\Users\\system_data\\" # Full Path to the file directory 


def get_local_file(file_name):
  """
  this function returns the file from the directory as a panadas dataframe using the absolute directory path
  """
    with open(full_path + file_name + '.csv', 'r') as f:
        return pd.read_csv(f)
