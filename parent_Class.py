#Program Name: parent_Class.py

#Programmer: Kacey Brukiewa
#Date: 5/19/2025

#Program description: This program is for a class called Parent 
# wich can instance a Parent object that holds two gene strings and 
# a boolean to represent recessiveness. 

class Parent():

    def __init__(self,gene_1, gene_1_dominant, gene_2, gene_2_dominant):
        #Capitalize the gene_1 and gene_2 strings if they are dominant
        self.gene_a = gene_1
        self.gene_b = gene_2
        self.gene_1_dominant = gene_1_dominant
        self.gene_2_dominant = gene_2_dominant

        if self.gene_1_dominant == True:
            self.gene_a = gene_1.upper()
        else:
            self.gene_a = gene_1.lower()

        if self.gene_2_dominant == True:
            self.gene_b = gene_2.upper()
        else:
            self.gene_b = gene_2.lower()

