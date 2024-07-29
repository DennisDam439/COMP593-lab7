"""
Description:
 Prints the name and age of all people in the Social Network database
 who are age 50 or older, and saves the information to a CSV file.

Usage:
 python old_people.py
"""
import sqlite3
import os
import pandas as pd 
from create_db import db_path, script_dir

def main():
    old_people_list = get_old_people()
    print_name_and_age(old_people_list)

    old_people_csv = os.path.join(script_dir, 'old_people.csv')
    save_name_and_age_to_csv(old_people_list, old_people_csv)

def get_old_people():
    """Queries the Social Network database for all people who are at least 50 years old.

    Returns:
        list: (name, age) of old people 
    """
    # TODO: Create function body
    conn = sqlite3.connect(db_path)
    c = conn.cursor()

    old_people_query = """ 
        SELECT name, age FROM people WHERE age >= 50; """

    c.execute (old_people_query)
    old_people_list = c.fetchall()
    conn.close()
    return old_people_list

    
    
# Hint: See example code in lab instructions entitled "Getting People Data from the Database"

def print_name_and_age(name_and_age_list):
    for name, age in name_and_age_list:
        print (f"{name} is {age} years old")


    """Prints name and age of all people in provided list

    Args:
        name_and_age_list (list): (name, age) of people
    """
    # TODO: Create function body

    # Hint: Use a for loop to iterate the list of tuples to print a sentence for each old person
    return

def save_name_and_age_to_csv(name_and_age_list, csv_path):
    """Saves name and age of all people in provided list

    Args:
        name_and_age_list (list): (name, age) of people
        csv_path (str): Path of CSV file
    """
    # TODO: Create function body
    ##with open (csv_path, 'w', newline='') as file:##
    writer = pd.DataFrame(name_and_age_list)
    header =('Name', 'Age') # header
    writer.to_csv(csv_path, header=header, index=False)

if __name__ == '__main__':
   main()