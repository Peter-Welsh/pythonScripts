#periodic elements quiz

#Created January 27, 2016

import time
import random
import sys
All = {"H": "Hydrogen", "He": "Helium", "Li": "Lithium", "Be": "Beryllium", "B": "Boron", "C": "Carbon", "N": "Nitrogen", "O": "Oxygen", "F": "Fluorine", "Ne": "Neon", "Na": "Sodium", "Mg": "Magnesium",
"Al": "Aluminum", "Si": "Silicon", "P": "Phosphorus", "S": "Sulfur", "Cl": "Chlorine", "Ar": "Argon", "K": "Potassium", "Ca": "Calcium", "Sc": "Scandium", "Ti": "Titanium", "V": "Vanadium", "Cr": "Chromium", "Mn": "Manganese", "Fe": "Iron", "Co": "Cobalt",
"Ni": "Nickel", "Cu": "Copper", "Zn": "Zinc", "Ga": "Gallium", "Ge": "Germanium", "As": "Arsenic", "Se": "Selenium", "Br": "Bromine", "Kr": "Krypton", "Rb": "Rubidium", "Sr": "Strontium", "Y": "Yttrium", "Zr": "Zirconium", "Nb": "Niobium",
"Mo": "Molybdenum", "Tc": "Technetium", "Ru": "Ruthenium", "Rh": "Rhodium", "Pd": "Palladium", "Ag": "Silver", "Cd": "Cadmium", "In": "Indium", "Sn": "Tin", "Sb": "Antimony", "Te": "Tellurium", "I": "Iodine", "Xe": "Xenon", "Cs": "Cesium",
"Ba": "Barium", "La": "Lanthanum", "Ce": "Cerium", "Pr": "Praseodymium", "Nd": "Neodymium", "Pm": "Promethium", "Sm": "Samarium", "Eu": "Europium", "Gd": "Gadolinium", "Tb": "Terbium", "Dy": "Dysprosium", "Ho": "Holmium", "Er": "Erbium", "Tm": "Thulium",
"Yb": "Ytterbium", "Lu": "Lutetium", "Hf": "Hafnium", "Ta": "Tantalum", "W": "Tungsten", "Re": "Rhenium", "Os": "Osmium", "Ir": "Iridium", "Pt": "Platinum", "Au": "Gold", "Hg": "Mercury", "Tl": "Thallium", "Pb": "Lead", "Bi": "Bismuth",
"Po": "Polonium", "At": "Astatine", "Rn": "Radon", "Fr": "Francium", "Ra": "Radium", "Ac": "Actinium", "Th": "Thorium", "Pa": "Protactinium", "U": "Uranium", "Np": "Neptunium", "Pu": "Plutonium", "Am": "Americium", "Cm": "Curium", "Bk": "Berkelium",
"Cf": "Californium", "Es": "Einsteinium", "Fm": "Fermium", "Md": "Mendelevium", "No": "Nobelium", "Lr": "Lawrencium", "Rf": "Rutherfordium", "Db": "Dubnium", "Sg": "Seaborgium", "Bh": "Bohrium", "Hs": "Hassium", "Mt": "Meitnerium", "Ds": "Darmstadtium", "Rg": "Roentgenium",
"Cn": "Copernicium", "Uut": "Ununtrium", "Fl": "Flerovium", "Uup": "Ununpentium", "Lv": "Livermorium", "Uus": "Ununseptium", "Uuo": "Ununoctium"}

alkali = {"Li": "Lithium", "Na": "Sodium", "K": "Potassium", "Rb": "Rubidium", "Cs": "Cesium", "Fr": "Francium"}

alkaline = {"Be": "Beryllium", "Mg": "Magnesium", "Ca": "Calcium", "Sr": "Strontium", "Ba": "Barium", "Ra": "Radium"}

lanthanoids = {"La": "Lanthanum", "Ce": "Cerium", "Pr": "Praseodymium", "Nd": "Neodymium", "Pm": "Promethium", "Sm": "Samarium", "Eu": "Europium", "Gd": "Gadolinium", "Tb": "Terbium", "Dy": "Dysprosium", "Ho": "Holmium", "Er": "Erbium", "Tm": "Thulium",
"Yb": "Ytterbium", "Lu": "Lutetium"}

actinoids = {"Ac": "Actinium", "Th": "Thorium", "Pa": "Protactinium", "U": "Uranium", "Np": "Neptunium", "Pu": "Plutonium", "Am": "Americium", "Cm": "Curium", "Bk": "Berkelium",
"Cf": "Californium", "Es": "Einsteinium", "Fm": "Fermium", "Md": "Mendelevium", "No": "Nobelium", "Lr": "Lawrencium"}

transition = {"Sc": "Scandium", "Ti": "Titanium", "V": "Vanadium", "Cr": "Chromium", "Mn": "Manganese", "Fe": "Iron", "Co": "Cobalt",
"Ni": "Nickel", "Cu": "Copper", "Y": "Yttrium", "Zr": "Zirconium", "Nb": "Niobium", "Mo": "Molybdenum", "Tc": "Technetium", "Ru": "Ruthenium", 
"Rh": "Rhodium", "Pd": "Palladium", "Ag": "Silver", "Hf": "Hafnium", "Ta": "Tantalum", "W": "Tungsten", "Re": "Rhenium", "Os": "Osmium", "Ir": "Iridium", "Pt": "Platinum", 
"Au": "Gold", "Rf": "Rutherfordium", "Db": "Dubnium", "Sg": "Seaborgium", "Bh": "Bohrium", "Hs": "Hassium", "Mt": "Meitnerium", "Ds": "Darmstadtium", "Rg": "Roentgenium"}

poor = {"Al": "Aluminum", "Zn": "Zinc", "Ga": "Gallium", "Ge": "Germanium", "Cd": "Cadmium", "In": "Indium", "Sn": "Tin", "Sb": "Antimony", 
"Hg": "Mercury", "Tl": "Thallium", "Pb": "Lead", "Bi": "Bismuth", "Po": "Polonium", "Cn": "Copernicium", "Uut": "Ununtrium", "Fl": "Flerovium", "Uup": "Ununpentium", "Lv": "Livermorium"}

nonmetals = {"B": "Boron", "C": "Carbon", "N": "Nitrogen", "O": "Oxygen", "F": "Fluorine", "Si": "Silicon", "P": "Phosphorus", "S": "Sulfur", "Cl": "Chlorine",
"As": "Arsenic", "Se": "Selenium", "Br": "Bromine", "Te": "Tellurium", "I": "Iodine", "At": "Astatine"}

noble = {"He": "Helium", "Ne": "Neon", "Ar": "Argon", "Kr": "Krypton", "Xe": "Xenon", "Rn": "Radon"}

def quiz_me(n=10):
	quit = False
	test_mode = 0
	test_base = []
	iteration = 0
	print "Periodic elements Quiz"
	while not quit:
		if test_mode == 1:
			n = len(test_base)
		else:
			n = 10
		score = 0
		exit = 0
		picks = ['', '']
		if test_mode == 0:
			iteration = 0
			mode = str.lower(raw_input("\nSelect a subject from below:\n1. Alkali metals\n2. Alkaline earth metals\n3. Lanthanoids\n4. Actinoids\n5. Transition metals\n6. Poor metals\n7. Other nonmetals\n8. Noble gases\nor take the full, " + str(len(All)) + "-question test by entering \"test\"\n> "))
			startTime = time.time()
			if mode == "alkali" or mode == "1":
				quiz_base = list(alkali.keys())
				n = 6
			elif mode == "alkaline" or mode == "2":
				quiz_base = list(alkaline.keys())
				n = 6
			elif mode == "lanthanoids" or mode == "l" or mode == "3":
				quiz_base = list(lanthanoids.keys())
			elif mode == "actinoids" or mode == "a" or mode == "4":
				quiz_base = list(actinoids.keys())
			elif mode == "transition" or mode == "t" or mode == "5":
				quiz_base = list(transition.keys())
			elif mode == "poor" or mode == "p" or mode == "6":
				quiz_base = list(poor.keys())
			elif mode == "other" or mode == "nonmetals" or mode == "o" or mode == "7":
				quiz_base = list(nonmetals.keys())
			elif mode == "noble" or mode == "n" or mode == "8":
				quiz_base = list(noble.keys())
				n = 6
			elif mode == "test":
				mode = "all"
				if iteration == 0:
					n = len(All)
				else:
					n = len(test_base)
				test_mode = 1
				startTime = time.time() #start timer for test
				quiz_base = list(All.keys())
			else:
				mode = "all"
				quiz_base = list(All.keys())
		else:
			quiz_base = test_base

		for _ in range(n):
			key = random.choice(quiz_base)
			while key in picks:
				key = random.choice(quiz_base)
			picks.append(key)
			hint_given = 1
			while hint_given == 1:
				i = str.lower(raw_input(key + ': ')) #get input
				hint_given = 0
				hint = All[key].split()[0][0]
				
				if i == str.lower(All[key]):
					print 'Correct!'
					if test_mode == 1 and iteration != 0:
						test_base.remove(key)
					score += 1
				elif levenshtein(i, str.lower(All[key])) == 1: #for edit distances of 1
					print 'Close enough: it\'s ' + All[key] + '.'
					if test_mode == 1 and iteration != 0: #only remove elements from test_base after the first iteration
						test_base.remove(key)
					score += 1
				elif i == "":
					print 'It\'s ' + All[key] + '.'
					if test_mode == 1 and iteration == 0: #only populate the test_base on the first go-round
							test_base.append(key)
				elif i == "hint":
					hintf(hint)
					hint_given = 1
				elif i == "quit" or i == "exit" or i == "q" or i == "end":
					exit = 1
					hint_given = 0
					test_mode = 0
				else:
					print 'No, it\'s ' + All[key] + '.'
					if test_mode == 1 and iteration == 0:
						test_base.append(key)
				if _ == n / 2 and test_mode == 1 and iteration == 0:
					print 'You\'re half way through!'
				elif _ == n - 10 and test_mode == 1 and iteration == 0:
					print 'Just 10 more to go!'
			if exit == 1:
				break
		seconds = int(time.time() - startTime)
		minutes = seconds / 60
		seconds = seconds % 60
		if minutes != 0:
			print 'You got ' + str(score) + '/' + str(n) + ' elements right in ' + str(minutes) + ' minutes and ' + str(seconds) + ' seconds. '
		else:
			print 'You got ' + str(score) + '/' + str(n) + ' elements right in ' + str(seconds) + ' seconds. '
		if test_mode == 1 and len(test_base) != 0:
			quit = raw_input("Play again with the ones you missed? (Y/N) ")
		else:
			if test_mode == 1 and n == score:
				print 'Congratulations! You completed the test!'
			quit = raw_input("Again? (Y/N) ")
			test_mode = 0
		if('n' in quit or 'N' in quit):
			quit = True
		else:
			iteration += 1
			quit = False

def levenshtein(s1, s2):
    if len(s1) < len(s2):
        return levenshtein(s2, s1)
 
    # len(s1) >= len(s2)
    if len(s2) == 0:
        return len(s1)
 
    previous_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[j + 1] + 1 # j+1 instead of j since previous_row and current_row are one character longer
            deletions = current_row[j] + 1       # than s2
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row
 
    return previous_row[-1]

def hintf(hint):
	sys.stdout.write('It begins with a')
	if hint == "A" or hint == "E" or hint == "F" or hint == "H" or hint == "I" or hint == "L" or hint == "M" or hint == "N" or hint == "O" or hint == "R" or hint == "S" or hint == "X":
		sys.stdout.write('n') #'print' comes with whitespace; this just outputs the letter with nothing else
	print ' ' + str(hint) + '.'

quiz_me()