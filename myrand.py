import random
import time
import argparse

parser = argparse.ArgumentParser(description = "This program generates a random number matrix")
parser.add_argument("num_plates", type = int, help = "Number of 24-well plates in experiment")
parser.add_argument("strains", type = str, nargs = '*', help = "List of strains you will use, " + 
	"separated by spaces. Ex: N2 CX12311 CX16904")
args = parser.parse_args()

def modified(num_plates, strains):
	# Total number of columns
	num_cols = num_plates * 6
	# Total number of wells
	num_wells = num_plates * 24
	# A total of 4 control wells per plate should be present. Control wells have no worms.
	# 12 control wells for 3 plates may end up being distributed unevenly across plates
	num_control_wells = num_plates * 4
	# Number of wells available to the worms
	available_wells = num_wells - num_control_wells
	# If the number of wells available to the worms cannot be divided evenly among the strains,
	# extra wells will be turned into control wells with no worms.
	if (available_wells % len(strains) != 0):
		change = available_wells % len(strains)
		num_control_wells += change
		available_wells -= change

	# Set up dictionary to keep track of the number of wells need for control and strains.
	counts = {'C':num_control_wells}
	starting_strain_wells = available_wells / len(strains)
	for strain in strains:
		counts[strain] = starting_strain_wells

	# Initialize random seed and the output string, which will be exported to csv format
	random.seed(time.time())
	output_str = ''
	# Plate number headers
	for i in range(num_plates):
		output_str += 'Plate ' + str(i + 1) + ',,,,,,,'
	output_str += '\n'

	# A random number will be generated for each well that corresponds to the control or one
	# of the strains in the counts dictionary. If the maximum number of wells for the control
	# or one of the strains have been filled, the random number is redone.
	for well in range(num_wells):
		x = random.randint(0, len(strains))
		strain = ''
		if x == len(strains):
			strain = 'C'
		else:
			strain = strains[x]

		while counts[strain] == 0:
			x = random.randint(0, len(strains))
			if x == len(strains):
				strain = 'C'
			else:
				strain = strains[x]

		output_str += strain + ","
		# Adjust dictionary count
		counts[strain] -= 1

		# Formatting and spacing of the csv
		if (well + 1) % num_cols == 0:
			output_str += "\n"
		elif (well + 1) % 6 == 0:
			output_str += ','

	# Write to csv file
	f = open("PlateLayoutModified.csv","w")
	f.write(output_str)
	f.close()
modified(args.num_plates, args.strains)