# SI 201 Project 1
# Your name: Amani Aggour
# Your student id: 26964097
# Your email: aaggour@umich.edu 
# Who or what you worked with on this homework (including generative AI like ChatGPT):
# If you worked with generative AI also add a statement for how you used it. 
# Asked Chatgpt to help debug and help guide me on writing the stucture of my function.
# I did the function calculate_body_flipper_to_mass_ratio and it's test cases
# Isa did the functions load_penguin(csv_file) and calculate_average_body_mass_species(penguins) and their corresponding test cases
# Rahma did the fuction analyze_bill_ratio_mass_relation and it's corresponding test cases
# And we all worked on the write_results function together 

# Topic question: Is there a correlation between sex and penguin body mass?
# Description: Understand the relation of penguin part size (flipper and beak) to rest of the penguin mass and how it related to sex

import os
import csv 

def load_penguin(csv_file): 
    '''
    Reads the penguin csv file and returns it as a list of dictionaries - coverts keys that have numbered outputs into integers utilizing float to account for decimals
    Input: csv_file(string)
    Output: penguins(list of dictionaries)
    '''
    base_path = os.path.abspath(os.path.dirname(__file__))
    full_path = os.path.join(base_path, csv_file)

    penguins = [] 
    numbered_keys = ['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g']

    #opens the file and turns columns that are numbers into integers
    with open(full_path, newline='') as csv_file: 
        reader = csv.DictReader(csv_file)
        for row in reader: 
            for key in numbered_keys: 
                value = row.get(key, '')
                if value.strip() != '': 
                    try: 
                        row[key] = int(float(value))
                    except ValueError: 
                        row[key] = None
                else: 
                    row[key] = None
            penguins.append(row)
    return penguins


def calculate_average_body_mass_species(penguins): 
    '''
    Grouping the body masses by species and island and finding the averages of each (island, species)
    Input: csv_file(string)
    Output: avg_body_mass_dict(dictionary)
    '''
    
    data = {}
    for row in penguins: 
        island = row['island']
        species = row['species']
        body_mass = row['body_mass_g']
        
        if body_mass is None: 
            continue 
        if island not in data: 
            data[island] = {}
        if species not in data[island]: 
            data[island][species] = [] 

        data[island][species].append(body_mass)

    avg_body_mass_dict = {}
    highest_avg_mass = 0
    heaviest_species_island = None
    for island, species_dict in data.items(): 
        for species, masses in species_dict.items(): 
            avg_mass = sum(masses) / len(masses)
            avg_body_mass_dict[(island, species)] = avg_mass #calculation 1 - calculating the average mass for each species 

            if avg_mass > highest_avg_mass:
                highest_avg_mass = avg_mass #calculation 2 - calculating the highest average mass with associated species 
                heaviest_species_island = (island, species) 
    print(f"The average mass for (island, species) is: {avg_body_mass_dict}")
    print(f"The species with the highest average mass is: {heaviest_species_island} with a mass of {highest_avg_mass:.2f}g") 
    return avg_body_mass_dict, heaviest_species_island, highest_avg_mass
