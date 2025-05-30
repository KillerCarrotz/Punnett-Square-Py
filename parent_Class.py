#Program Name: parent_Class.py

#Programmer: Kacey Brukiewa
#Date: 5/19/2025

#Program description: This program is for a class called Parent 
# wich can instance a Parent object that holds two gene strings and 
# a boolean to represent recessiveness. 

class Parent():

    def __init__(self,gene_1: str, gene_1_dominant, gene_2:str, gene_2_dominant):

        #Assign passed values to object variables.
        self.gene_a = gene_1
        self.gene_b = gene_2
        self.gene_a_symbol = gene_1[0]
        self.gene_b_symbol = gene_2[0]
        self.gene_1_dominant = gene_1_dominant
        self.gene_2_dominant = gene_2_dominant

        #Capitalize the gene_a_symbol and gene_b_symbol strings if they are dominant.
        if self.gene_1_dominant == True:
            self.gene_a_symbol = self.gene_a_symbol.upper()
        else:
            self.gene_a_symbol = self.gene_a_symbol.lower()

        if self.gene_2_dominant == True:
            self.gene_b_symbol = self.gene_b_symbol.upper()
        else:
            self.gene_b_symbol = self.gene_b_symbol.lower()

