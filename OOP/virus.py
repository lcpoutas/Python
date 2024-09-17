#! /usr/bin/env python3

class Virus():
    
    '''
    The Virus class represents a virus with a name, a genetic sequence (list of nucleotides), and a strain.
    It also contains a mutation map (strain_map) used to identify different strains based on genetic changes
    in specific positions of the sequence.
    '''

    strain_map = {
            "alpha": (0,"a","t"),
            "gamma": (1, "t", "c"),
            "delta": (2, "c", "a"),
            "epsilon": (4, "t", "c"),
            "dseta": (5, "g", "a"),
            "ita": (6, "c", "g"),
            "zeta":(7, "g", "a"),
            "iota": (7, "g", "a"),
            "kappa":(9, "t", "g")
            }

    def __init__(self, name, seq, strain):
        self. name = name
        self.seq = seq
        self.strain = strain

    def print_info(self):
        print("--------------- Información ----------------")
        print(f"Name : {self.name}\nSeq : {self.seq}\nStrain : {self.strain}")

    def compare_seq(self, VirusMut):

        '''
        Compares the genetic sequence of this virus with another virus and detects the positions
        where the sequences differ.

        Args:
        - virus_mut (Virus): Another instance of the Virus class to compare the genetic sequence with.

        Returns:
        - LisPosMut (list): A list of tuples containing the position of the difference, the nucleotide
          in the original virus, and the nucleotide in the mutated virus.
        '''
        
        LisPosMut = [] #Lista para almacenar la posicion distinta y las bases wt y mut en esa posicion
        
        for i, nucleotide in enumerate(self.seq):
            if nucleotide != VirusMut.seq[i]:
                LisPosMut.append((i, nucleotide, VirusMut.seq[i]))
        return LisPosMut

    def identify_strain(self, LisPosMut):

        '''
        Identifies the virus strain based on the genetic changes detected in the sequence.

        Args:
        - LisPosMut (list): A list of tuples that contain the positions and the bases that differ 
          between the sequences.

        Returns:
        - IDstrains (list or str): A list of identified strains if matches are found in the mutation map (strain_map),
          or the string "New Strain" if no match is found.
        '''

        IDstrains=[]

        for change in LisPosMut:
            found_strain = False
            for strain, changes in self.strain_map.items():
                if change == changes:
                    IDstrains.append(strain)
                    found_strain = True
                    break
            if not found_strain:
                return "Nueva Cepa"
        return IDstrains

# ------------ Instancias -------------

virusWt = Virus("COVID", ["a","t","g","c","t","g","c","g","c","t"]," WT") #almacena la seq del virus
virusWt.print_info()

virusMut = Virus("COVID", ["t", "t", "g", "c", "t", "g", "c", "g", "c", "g"], "MUT")
virusMut.print_info()

# Compare the sequences and store the positions of differences
Res_LisPosMut = virusWt.compare_seq(virusMut) #Almacena la posción diferente en una lista denominada Res_LisPosMut

print("---------- Resultados ----------")

print(f"Posicion deferente: {Res_LisPosMut}")

# Identify the strains based on detected mutations
IDstrains = virusWt.identify_strain(Res_LisPosMut)
print(f"Strain Identificada: {IDstrains}")




