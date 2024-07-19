"""
Description:
 Prints the name and age of all people in the Social Network database
 who are age 50 or older, and saves the information to a CSV file.

Usage:
 python old_people.py
"""
import os
from create_db import db_path, script_dir
import sqlite3
import csv
import pandas as pd 
 






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
    c.execute ("SELECT name, age FROM people WHERE age >= 50")
    old_people_list = c.fetchball()
    conn.close()
    return old_people_list

    
    
# Hint: See example code in lab instructions entitled "Getting People Data from the Database"
    return

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
    with open (csv_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer. writerow(["Name, Age"]) # header
        writer.writerow(name_and_age_list)

   
    return

if __name__ == '__main__':
   main()