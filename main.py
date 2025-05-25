#Program Name: main.py

#Programmer: Kacey Brukiewa
#Date: 5/19/2025

#Program description: This program takes user input for two parent objects. Then it 
# displays a punnett square in a text file depicting likely hood of an ofspring gene 
# result. It then prompts user to run a simulation which will give a possible distribution
# of genes given an amount of ofspring.

#TODO: In simulateOffspring; Use MatPlotLib to generate a graph of offspring results.
#TODO: Add functionality to cleanInputInt, cleanInputYN, cleanInputStr. Clean user input so only a 30 char maximum for gene names and y/n for dominance and ints between 1 and 5000 are accepted.
#TODO: Use loops in main so that new punnett squares can be generated back to back.

import random
from parent_Class import *

def main():
    #Default parent1 and parent2 used for testing
    parent1 = Parent("A", True, "b", False)
    parent2 = Parent("A", True, "b", False)
    continue_yn = "y"

    #Create two parent objects with the genes assigned from the get genes funtion.
    gene_1_parent_1, gene_1_parent_1_dominant, gene_2_parent_1, gene_2_parent_1_dominant = getGenes("1")
    parent1 = Parent(gene_1_parent_1, gene_1_parent_1_dominant, gene_2_parent_1, gene_2_parent_1_dominant)
    gene_1_parent_2, gene_1_parent_2_dominant, gene_2_parent_2, gene_2_parent_2_dominant = getGenes("2")
    parent2 = Parent(gene_1_parent_2, gene_1_parent_2_dominant, gene_2_parent_2, gene_2_parent_2_dominant)
    
    #createSquare will create the punnett square and write it to punnett_py.txt
    createSquare(parent1, parent2)
    
    #Run simulation until user chooses to exit.
    while continue_yn == "y":
        #simulateOffspring will randomly determine each offspring's genes and display a total amount of offspring with each gene combo.
        simulateOffspring(parent1, parent2)
        continue_yn = input("Would you like to simulate again? y/n :")

    else:
        return


def getGenes(number_of_parent):#number_of_parrent is used to acurately prompt the user.
    #Taking user input and saving them to temporary variables.
    gene_1 = input("Enter parent " + number_of_parent + " first gene: ")

    #todo: create a loop for gene_1_is_dominant and gene_2_is_dominant so that only y or n are accepted outputs.
    gene_1_is_dominant = input("Is this trait dominant? y/n ")
    gene_1_is_dominant = gene_1_is_dominant.lower()

    gene_2 = input("Enter parent " + number_of_parent + " second gene: ")

    gene_2_is_dominant = input("Is this trait dominant? y/n ")
    gene_2_is_dominant = gene_2_is_dominant.lower()

    #Creating a boolean value for whether a gene is dominant.
    if gene_1_is_dominant == "n":
        gene_1_dominant = False
    else:
        gene_1_dominant = True


    if gene_2_is_dominant == "n":
        gene_2_dominant = False
    else:
        gene_2_dominant = True

    return gene_1, gene_1_dominant, gene_2, gene_2_dominant

def createSquare(parent1, parent2):
    #createSquare function takes two parent objects, creates a punnet square using their genes, and prints it to the terminal and writes it to punnett_py.txt.
    punnet_square_lines = [
        " ____________________ \n",
        "|        Parent 1    |\n",
        "|P        ", parent1.gene_a_symbol, "      ", parent1.gene_b_symbol, "   |\n",
        "|a     ______ ______ |\n",
        "|r  ", parent2.gene_a_symbol," |  ", parent1.gene_a_symbol, parent2.gene_a_symbol, "  |  ", parent1.gene_b_symbol, parent2.gene_a_symbol, "  ||\n",
        "|e    |______|______||\n",
        "|n  ", parent2.gene_b_symbol, " |  ", parent1.gene_a_symbol, parent2.gene_b_symbol, "  |  ", parent1.gene_b_symbol, parent2.gene_b_symbol, "  ||\n",
        "|t    |______|______||\n",
        "|2                   |\n",
        "|____________________|\n"
    ]

    #Print punnet square to terminal
    for line in punnet_square_lines:
        print(line, end='')

    #Create and output to a text file.
    punnett_file_path = "punnett_py.txt"
    with open(punnett_file_path, 'a') as file:
        file.writelines(punnet_square_lines)
    
    #Informs user of file write.
    print(f"This square has been written to {punnett_file_path} (the file is now closed automatically).") 

    return

def simulateOffspring(parent_object_1, parent_object_2):
    #simulateOffspring function takes two parent objects and determines based on the dominance of the genes passed how many offspring will have 
    #different genes.

    #todo: After determining how many offspring are in each category using random from math, it will display a graph using matplotlib.

    #Get user input for how many offspring will be generated
    number_of_offspring = input("How many offspring would you like to simulate? (1-5,000)")
    number_of_offspring = int(number_of_offspring)

    #instanciate variables for gene total calculations.
    gene_list = [0, 0, 0, 0]
    number_dominant_expressed = 0
    number_recessive_expressed = 0

    #For each offspring we want to determine which of 4 gene combos they have, and if dominant or recessive genes are expressed.
    for offspring in range(number_of_offspring):

        random_gene = random.randint(0,3) #determine random genes of offspring

        gene_list[random_gene]+=1 #increase proper counter in gene_list

        #Determine which gene combo this offspring has, and add to total dominant or recessive values depending on which it expresses.
        if random_gene == 0:
            if parent_object_1.gene_1_dominant == False and parent_object_2.gene_1_dominant == False:
                number_recessive_expressed+=1
            else:
                number_dominant_expressed+=1

        elif random_gene == 1:
            if parent_object_1.gene_1_dominant == False and parent_object_2.gene_2_dominant == False:
                number_recessive_expressed+=1
            else:
                number_dominant_expressed+=1

        elif random_gene == 2:
            if parent_object_1.gene_2_dominant == False and parent_object_2.gene_1_dominant == False:
                number_recessive_expressed+=1
            else:
                number_dominant_expressed+=1
        
        elif random_gene ==3:
            if parent_object_1.gene_2_dominant == False and parent_object_2.gene_2_dominant == False:
                number_recessive_expressed+=1
            else:
                number_dominant_expressed+=1

        offspring +=1 #increase counter

    #Print totals at the end.
    else:
        print(f"{parent_object_1.gene_a_symbol}{parent_object_2.gene_a_symbol}: {gene_list[0]}")
        print(f"{parent_object_1.gene_a_symbol}{parent_object_2.gene_b_symbol}: {gene_list[1]}")
        print(f"{parent_object_1.gene_b_symbol}{parent_object_2.gene_a_symbol}: {gene_list[2]}")
        print(f"{parent_object_1.gene_b_symbol}{parent_object_2.gene_b_symbol}: {gene_list[3]}")
        print(f"Total dominant genes expressed: {number_dominant_expressed}\nTotal recessive genes expressed: {number_recessive_expressed}")

    return

def cleanInputInt():
    #Called on a user input Int value to clean it for only int values. Returns with boolean value, True if clean, False if new input is needed.

    return

def cleanInputYN():
    #Called on a user input String value to clean it for only "y" or "n" values. Returns with boolean value, True if clean, False if new input is needed.

    return

def cleanInputStr():
    #Called on a user input Str value to clean it for only str values. Returns with boolean value, True if clean, False if new input is needed.

    return

if __name__ == "__main__":
    main()
