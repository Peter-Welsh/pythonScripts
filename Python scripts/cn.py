#Capitals quiz
#by Peter Welsh

#Created December 18, 2014
#edit December 21, 2014: case insensitivity
#edit December 28, 2014: levenshtein from Rosetta Code
#edit December 30, 2014: no duplicates
#edit April 6, 2015: gamebreaking glitch when asked for South Africa's capital fixed
#edit April 7, 2015: "St George's" -> "St. George's"
#edit April 7, 2015: softcoded score report: "/10 capitals" -> "/' + str(n) + ' capitals"
#edit April 7, 2015: more parentheticals: official/administrative/legislative capitals added
#edit April 9, 2015: full test added, "Washington DC" -> "Washington D.C."
#edit April 13, 2015: added option to retake missed questions in test mode
#edit April 14, 2015: made congratulations only appear in test mode
#edit April 14, 2015: added hints
#edit April 14, 2015: allowing user to quit by typing Q or quit, etc.
#edit April 16, 2015: Territories added; 'an'/'a' before letter hint
#edit May 19, 2015: numbered menu choices; all -> all countries; capital of taiwan -> taipei
#edit May 21, 2015: timer added to test mode
#edit May 28, 2015: timer's not resetting fixed; removed "minutes: 0" when time taken is under 60s
#edit June 11, 2015: period after close enough
#edit Sept 3, 2015: ". You took ' seconds" -> " in ' seconds" (more fluid, concise)
#edit Sept 3, 2015: test_mode = 0 after quitting (no "play again with the ones you missed?" after quitting)
#edit Sept 3, 2015: "halfway through" and "10 more to go" for test mode
#edit Sept 11, 2015: accepting "Luxembourg" (no "city") for the capital of Luxembourg
#edit Sept 15, 2015: accepting "st." for "saint" for Territories capitals
#edit Oct 22, 2015: "and iteration == 0" for halfway and 10 left markers
#edit Dec 12, 2015: melekeok->Ngerulmud

import time
import random
import sys
All = {"Afghanistan": "Kabul", "Albania": "Tirana", "Algeria": "Algiers", "Andorra": "Andorra la Vella", "Angola": "Luanda", 
	"Antigua and Barbuda": "St. John's", "Argentina": "Buenos Aires", "Armenia": "Yerevan", "Australia": "Canberra", 
	"Austria": "Vienna", "Azerbaijan": "Baku", "Bahamas": "Nassau", "Bahrain": "Manama", "Bangladesh": "Dhaka", 
	"Barbados": "Bridgetown", "Belarus": "Minsk", "Belgium": "Brussels", "Belize": "Belmopan", "Benin (official)": "Porto Novo", 
	"Bhutan": "Thimphu", "Bolivia (official)": "Sucre", "Bosnia and Herzegovina": "Sarajevo", "Botswana": "Gaborone", 
	"Brazil": "Brasilia", "Brunei": "Bandar Seri Begawan", "Bulgaria": "Sofia", "Burkina Faso": "Ouagadougou", 
	"Burundi": "Bujumbura", "Cambodia": "Phnom Penh", "Cameroon": "Yaounde", "Canada": "Ottawa", "Cape Verde": "Praia", 
	"Central African Republic": "Bangui", "Chad": "N'Djamena", "Chile (official)": "Santiago", "China": "Beijing", 
	"Colombia": "Bogota", "Comoros": "Moroni", "Costa Rica": "San Jose", "Cote d'Ivoire (official)": "Yamoussoukro", 
	"Croatia": "Zagreb", "Cuba": "Havana", "Cyprus": "Nicosia", "Czech Republic": "Prague", "Democratic Republic of the Congo": "Kinshasa", 
	"Denmark": "Copenhagen", "Djibouti": "Djibouti", "Dominica": "Roseau", "Dominican Republic": "Santo Domingo",
	"East Timor": "Dili", "Ecuador": "Quito", "Egypt": "Cairo", "El Salvador": "San Salvador", "Equatorial Guinea": "Malabo", 
	"Eritrea": "Asmara", "Estonia": "Tallinn", "Ethiopia": "Addis Ababa", "Fiji": "Suva", "Finland": "Helsinki", 
	"France": "Paris", "Gabon": "Libreville", "Georgia (official)": "Tbilisi", "Georgia (legislative)": "Kutaisi",
	"Germany": "Berlin", "Ghana": "Accra", "Greece": "Athens", "Grenada": "St. George's", "Guatemala": "Guatemala City",
	"Guinea": "Conakry", "Guinea-Bissau": "Bissau", "Guyana": "Georgetown", "Haiti": "Port-au-Prince", "Honduras": "Tegucigalpa",
	"Hungary": "Budapest", "Iceland": "Reykjavik", "India": "New Delhi", "Indonesia": "Jakarta", "Iran": "Tehran",
	"Iraq": "Baghdad", "Israel": "Jerusalem", "Italy": "Rome", "Jamaica": "Kingston", "Japan": "Tokyo", "Jordan": "Amman",
	"Kazakhstan": "Astana", "Kenya": "Nairobi", "Kiribati": "Tarawa", "Kosovo": "Pristina", "Kuwait": "Kuwait City",
	"Kyrgyzstan": "Bishkek", "Laos": "Vientiane", "Latvia": "Riga", "Lebanon": "Beirut", "Lesotho": "Maseru", "Liberia": "Monrovia",
	"Libya": "Tripoli", "Liechtenstein": "Vaduz", "Lithuania": "Vilnius", "Luxembourg": "Luxembourg City", "Madagascar": "Antananarivo",
	"Malawi": "Lilongwe", "Malaysia (official)": "Kuala Lumpur", "Malaysia (administrative)": "Putrajaya","Macedonia": "Skopje",
	"Maldives": "Male", "Mali": "Bamako", "Malta": "Valletta", "Marshall Islands": "Majuro", "Mauritania": "Nouakchott",
	"Mauritius": "Port Louis", "Mexico": "Mexico City", "Micronesia": "Palikir", "Moldova": "Chisinau", "Monaco": "Monaco",
	"Mongolia": "Ulaanbaatar", "Montenegro (official)": "Podgorica", "Morocco": "Rabat", "Mozambique": "Maputo",
	"Myanmar": "Naypyidaw", "Namibia": "Windhoek", "Nauru": "Yaren", "Nepal": "Kathmandu", "Netherlands (official)": "Amsterdam",
	"Netherlands (administrative)": "The Hague", "New Zealand": "Wellington", "Nicaragua": "Managua", "Niger": "Niamey",
	"Nigeria": "Abuja", "North Korea": "Pyongyang", "Norway": "Oslo", "Oman": "Muscat", "Pakistan": "Islamabad", "Palau": "Ngerulmud",
	"Palestine": "Jerusalem", "Panama": "Panama City", "Papua New Guinea": "Port Moresby", "Paraguay": "Asuncion", "Peru": "Lima",
	"Philippines": "Manila", "Poland": "Warsaw", "Portugal": "Lisbon", "Qatar": "Doha", "Ireland": "Dublin",
	"Republic of the Congo": "Brazzaville", "Romania": "Bucharest", "Russia": "Moscow", "Rwanda": "Kigali",
	"Saint Kitts and Nevis": "Basseterre", "Saint Lucia": "Castries", "Saint Vincent and the Grenadines": "Kingstown", "Samoa": "Apia",
	"San Marino": "San Marino", "Sao Tome and Principe": "Sao Tome", "Saudi Arabia": "Riyadh", "Senegal": "Dakar", "Serbia": "Belgrade",
	"Seychelles": "Victoria", "Sierra Leone": "Freetown", "Singapore": "Singapore", "Slovakia": "Bratislava", "Slovenia": "Ljubljana",
	"Solomon Islands": "Honiara", "Somalia": "Mogadishu", "South Africa (executive & administrative)": "Pretoria",
	"South Africa (legislative)": "Cape Town", "South Africa (judicial)": "Bloemfontein", "South Korea": "Seoul", "South Sudan": "Juba",
	"Spain": "Madrid", "Sri Lanka (commercial)": "Colombo", "Sri Lanka (administrative)": "Sri Jayawardenepura Kotte", "Sudan": "Khartoum", 
	"Suriname": "Paramaribo", "Swaziland (administrative)": "Mbabane", "Swaziland (legislative)": "Lobamba", "Sweden": "Stockholm",
	"Switzerland": "Bern", "Syria": "Damascus", "Tajikistan": "Dushanbe", "Tanzania (official)": "Dodoma", "Thailand": "Bangkok",
	"The Gambia": "Banjul", "Togo": "Lome", "Tonga": "Nuku'alofa", "Trinidad and Tobago": "Port of Spain", "Tunisia": "Tunis",
	"Turkey": "Ankara", "Turkmenistan": "Ashgabat", "Tuvalu": "Funafuti", "Uganda": "Kampala", "Ukraine": "Kiev", 
	"United Arab Emirates": "Abu Dhabi", "United Kingdom": "London", "United States": "Washington D.C.", "Uruguay": "Montevideo", 
	"Uzbekistan": "Tashkent", "Vanuatu": "Port Vila", "Vatican City": "Vatican City", "Venezuela": "Caracas", "Vietnam": "Hanoi", 
	"Yemen": "Sana'a", "Zambia": "Lusaka", "Zimbabwe": "Harare"}

Americas = {"Argentina": "Buenos Aires", "Bolivia (official)": "Sucre", "Brazil": "Brasilia", "Canada": "Ottawa", 
	"Chile (official)": "Santiago", "Colombia": "Bogota", "Costa Rica": "San Jose", "Cuba": "Havana", "Dominica": "Roseau", 
	"Dominican Republic": "Santo Domingo", "Ecuador": "Quito", "El Salvador": "San Salvador", "Grenada": "St. George's", 
	"Guatemala": "Guatemala City", "Haiti": "Port-au-Prince",	"Honduras": "Tegucigalpa", "Mexico": "Mexico City", 
	"Nicaragua": "Managua", "Panama": "Panama City", "Paraguay": "Asuncion", "Peru": "Lima", "Saint Kitts and Nevis": "Basseterre", 
	"Saint Lucia": "Castries", "Saint Vincent and the Grenadines": "Kingstown", "Suriname": "Paramaribo", 
	"Trinidad and Tobago": "Port of Spain", "United States": "Washington DC", "Uruguay": "Montevideo", "Venezuela": "Caracas"}

Europe = {"Albania": "Tirana", "Andorra": "Andorra la Vella", "Armenia": "Yerevan", "Austria": "Vienna", "Azerbaijan": "Baku", 
	"Belarus": "Minsk", "Belgium": "Brussels", "Bosnia and Herzegovina": "Sarajevo", "Bulgaria": "Sofia", "Croatia": "Zagreb", 
	"Cyprus": "Nicosia", "Czech Republic": "Prague", "Denmark": "Copenhagen", "Estonia": "Tallinn", "Finland": "Helsinki", 
	"France": "Paris", "Georgia (official)": "Tbilisi", "Georgia (legislative)": "Kutaisi", "Germany": "Berlin", 
	"Greece": "Athens", "Hungary": "Budapest", "Iceland": "Reykjavik", "Ireland": "Dublin", "Italy": "Rome", 
	"Kosovo": "Pristina", "Latvia": "Riga", "Liechtenstein": "Vaduz", "Lithuania": "Vilnius", "Luxembourg": "Luxembourg City", 
	"Macedonia": "Skopje", "Malta": "Valletta", "Moldova": "Chisinau", "Monaco": "Monaco", "Montenegro (official)": "Podgorica", 
	"Netherlands (official)": "Amsterdam", "Netherlands (administrative)": "The Hague", "Norway": "Oslo", "Poland": "Warsaw",
	"Portugal": "Lisbon", "Romania": "Bucharest", "Russia": "Moscow", "San Marino": "San Marino", "Serbia": "Belgrade", 
	"Slovakia": "Bratislava", "Slovenia": "Ljubljana", "Spain": "Madrid", "Sweden": "Stockholm", "Switzerland": "Bern",
	"Turkey": "Ankara", "Ukraine": "Kiev", "United Kingdom": "London", "Vatican City": "Vatican City"}

Africa = {"Algeria": "Algiers", "Angola": "Luanda", "Benin (official)": "Porto Novo", "Botswana": "Gaborone", "Burkina Faso": "Ouagadougou", 
	"Burundi": "Bujumbura", "Cameroon": "Yaounde", "Cape Verde": "Praia", "Central African Republic": "Bangui", 
	"Chad": "N'Djamena", "Comoros": "Moroni", "Cote d'Ivoire (official)": "Yamoussoukro", 
	"Democratic Republic of the Congo": "Kinshasa",	"Djibouti": "Djibouti", "Egypt": "Cairo", "Equatorial Guinea": "Malabo", 
	"Eritrea": "Asmara", "Ethiopia": "Addis Ababa", "Gabon": "Libreville", "Ghana": "Accra", "Guinea": "Conakry", 
	"Guinea-Bissau": "Bissau", "Kenya": "Nairobi", "Lesotho": "Maseru", "Liberia": "Monrovia", "Libya": "Tripoli", 
	"Madagascar": "Antananarivo", "Malawi": "Lilongwe", "Mali": "Bamako", "Mauritania": "Nouakchott", "Mauritius": "Port Louis", 
	"Morocco": "Rabat", "Mozambique": "Maputo", "Namibia": "Windhoek", "Niger": "Niamey", "Nigeria": "Abuja", "Rwanda": "Kigali", 
	"Sao Tome and Principe": "Sao Tome", "Senegal": "Dakar", "Seychelles": "Victoria", "Sierra Leone": "Freetown", 
	"Somalia": "Mogadishu", "South Africa (executive & administrative)": "Pretoria", "South Africa (legislative)": "Cape Town", 
	"South Africa (judicial)": "Bloemfontein", "South Sudan": "Juba", "Sudan": "Khartoum", "Swaziland (administrative)": "Mbabane", 
	"Swaziland (legislative)": "Lobamba", "Tanzania (official)": "Dodoma", "Togo": "Lome", "Tunisia": "Tunis", "Uganda": "Kampala", 
	"Zambia": "Lusaka", "Zimbabwe": "Harare"}

Asia = {"Afghanistan": "Kabul", "Armenia": "Yerevan", "Azerbaijan": "Baku", "Bahrain": "Manama", "Bangladesh": "Dhaka", 
	"Bhutan": "Thimphu", "Brunei": "Bandar Seri Begawan", "Cambodia": "Phnom Penh", "China": "Beijing", "Cyprus": "Nicosia", 
	"East Timor": "Dili", "Georgia (official)": "Tbilisi", "Georgia (legislative)": "Kutaisi", "India": "New Delhi", 
	"Indonesia": "Jakarta", "Iran": "Tehran", "Iraq": "Baghdad", "Israel": "Jerusalem", "Japan": "Tokyo", "Jordan": "Amman", 
	"Kazakhstan": "Astana",	"Kuwait": "Kuwait City", "Kyrgyzstan": "Bishkek", "Laos": "Vientiane", "Lebanon": "Beirut", 
	"Malaysia (official)": "Kuala Lumpur", "Malaysia (administrative)": "Putrajaya", "Maldives": "Male", "Mongolia": "Ulaanbaatar", 
	"Nepal": "Kathmandu", "North Korea": "Pyongyang", "Oman": "Muscat", "Pakistan": "Islamabad", "Philippines": "Manila", 
	"Qatar": "Doha", "Saudi Arabia": "Riyadh", "Singapore": "Singapore", "South Korea": "Seoul", "Sri Lanka (commercial)": "Colombo", 
	"Sri Lanka (administrative)": "Sri Jayawardenepura Kotte", "Syria": "Damascus", "Tajikistan": "Dushanbe", "Thailand": "Bangkok", 
	"Turkey": "Ankara", "Turkmenistan": "Ashgabat", "United Arab Emirates": "Abu Dhabi", "Uzbekistan": "Tashkent", "Vietnam": "Hanoi", 
	"Yemen": "Sana'a"}

States = {"Alabama": "Montgomery", "Alaska": "Juneau", "Arizona": "Phoenix", "Arkansas": "Little Rock", "California": "Sacramento", 
	"Colorado": "Denver", "Connecticut": "Hartford", "Delaware": "Dover", "Florida": "Tallahassee", "Georgia": "Atlanta", 
	"Hawaii": "Honolulu", "Idaho": "Boise", "Illinois": "Springfield", "Indiana": "Indianapolis", "Iowa": "Des Moines", 
	"Kansas": "Topeka", "Kentucky": "Frankfort", "Louisiana": "Baton Rouge", "Maine": "Augusta", "Maryland": "Annapolis", 
	"Massachusetts": "Boston", "Michigan": "Lansing", "Minnesota": "St. Paul", "Mississippi": "Jackson", "Missouri": "Jefferson City", 
	"Montana": "Helena", "Nebraska": "Lincoln", "Nevada": "Carson City", "New Hampshire": "Concord", "New Jersey": "Trenton", 
	"New Mexico": "Santa Fe", "New York": "Albany", "North Carolina": "Raleigh", "North Dakota": "Bismarck", "Ohio": "Columbus", 
	"Oklahoma": "Oklahoma City", "Oregon": "Salem", "Pennsylvania": "Harrisburg", "Rhode Island": "Providence", 
	"South Carolina": "Columbia", "South Dakota": "Pierre", "Tennessee": "Nashville", "Texas": "Austin", "Utah": "Salt Lake City", 
	"Vermont": "Montpelier", "Virginia": "Richmond", "Washington": "Olympia", "West Virginia": "Charleston", "Wisconsin": "Madison", 
	"Wyoming": "Cheyenne"}

Islands = {"Antigua and Barbuda": "St. John's", "Bahamas": "Nassau", "Barbados": "Bridgetown", "Cape Verde": "Praia", "Comoros": "Moroni", 
	"Cuba": "Havana", "Cyprus": "Nicosia", "Dominica": "Roseau", "Fiji": "Suva", "Grenada": "St. George's", "Haiti": "Port-au-Prince", 
	"Jamaica": "Kingston", "Kiribati": "Tarawa", "Maldives": "Male", "Malta": "Valletta", "Marshall Islands": "Majuro", 
	"Mauritius": "Port Louis", "Micronesia": "Palikir", "Nauru": "Yaren", "Palau": "Ngerulmud", "Saint Kitts and Nevis": "Basseterre", 
	"Saint Lucia": "Castries", "Saint Vincent and the Grenadines": "Kingstown", "Samoa": "Apia", "Sao Tome and Principe": "Sao Tome", 
	"Seychelles": "Victoria", "Solomon Islands": "Honiara", "Sri Lanka (commercial)": "Colombo", 
	"Sri Lanka (administrative)": "Sri Jayawardenepura Kotte",	"Tonga": "Nuku'alofa", "Trinidad and Tobago": "Port of Spain", 
	"Tuvalu": "Funafuti", "Vanuatu": "Port Vila"}

Territories = {"Akrotiri and Dhekelia": "Episkopi Cantonment", "American Samoa": "Pago Pago", "Anguilla": "The Valley",
	"Aruba": "Oranjestad", "Bermuda": "Hamilton", "British Virgin Islands": "Road Town", "Cayman Islands": "George Town", 
	"Christmas Island": "Flying Fish Cove", "Cocos (Keeling) Islands": "West Island", "Cook Islands": "Avarua", "Curacao": "Willemstad",
	"Falkland Islands": "Stanley", "Faroe Islands": "Torshavn", "French Guiana": "Cayenne", "French Polynesia": "Pape'ete",
	"French Southern and Antarctic Lands": "Port-aux-Francais", "Gibraltar": "Gibraltar", "Greenland": "Nuuk", "Guam": "Hagatna", 
	"Guernsey": "St. Peter Port", "Isle of Man": "Douglas", "Jersey": "Saint Helier", "Montserrat (official)": "Plymouth", 
	"New Caledonia": "Noumea", "Niue": "Alofi", "Norfolk Island": "Kingston", "Northern Mariana Islands": "Capitol Hill", 
	"Pitcairn Islands": "Adamstown", "Puerto Rico": "San Juan", "Saint Barthelemy": "Gustavia", "Saint Helena": "Jamestown",
	"Ascension Island": "Georgetown", "Tristan da Cunha": "Edinburgh of the Seven Seas", "Saint Martin": "Marigot", 
	"Saint Pierre and Miquelon": "Saint-Pierre", "Sint Maarten": "Philipsburg",
	"South Georgia and the South Sandwich Islands": "King Edward Point", "Svalbard": "Longyearbyen", "Taiwan": "Taipei",
	"Tokelau (official)": "Fakaofo", "Turks and Caicos Islands": "Cockburn Town", "U.S. Virgin Islands": "Charlotte Amalie",
	"Wallis and Futuna": "Mata-Utu", "Western Sahara": "El Aaiun"}

def quiz_me(n=10):
	quit = False
	test_mode = 0
	test_base = []
	iteration = 0
	print "GeoBee Capitals Quiz"
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
			mode = str.lower(raw_input("\nSelect a subject from below:\n1. Americas\n2. Europe\n3. Africa\n4. Asia\n5. Islands\n6. US states\n7. Territories\n8. All countries\nor take the full, " + str(len(All)) + "-question test by entering \"test\"\n> "))
			startTime = time.time()
			if mode == "americas" or mode == "am" or mode == "1":
				quiz_base = list(Americas.keys())
			elif mode == "europe" or mode == "eu" or mode == "2":
				quiz_base = list(Europe.keys())
			elif mode == "africa" or mode == "af" or mode == "3":
				quiz_base = list(Africa.keys())
			elif mode == "asia" or mode == "as" or mode == "4":
				quiz_base = list(Asia.keys())
			elif mode == "islands" or mode == "is" or mode == "5":
				quiz_base = list(Islands.keys())
			elif mode == "us" or mode == "states" or mode == "us states" or mode == "6":
				quiz_base = list(States.keys())
			elif mode == "te" or mode == "territories" or mode == "ter" or mode == "7":
				quiz_base = list(Territories.keys())
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
				if mode == "us" or mode == "states" or mode == "us states" or mode == "6": #separate from the rest because not included in "All"
					hint = States[key].split()[0][0] #first character of answer
					if i == str.lower(States[key]):
						print 'Correct!'
						score += 1
					elif levenshtein(i, str.lower(States[key])) == 1: #for edit distances of 1
						print 'Close enough: it\'s ' + States[key] + '.'
						score += 1
					elif i == "":
						print 'It\'s ' + States[key] + '.'
					elif i == "hint":
						hintf(hint) #calls hintf function, which displays the first letter of the capital
						hint_given = 1
					elif i == "quit" or i == "exit" or i == "q" or i == "end":
						exit = 1
						hint_given = 0
					else:
						print 'No, it\'s ' + States[key] + '.'
				elif mode == "te" or mode == "territories" or mode == "ter" or mode == "7": #separate from the rest because not included in "All"
					hint = Territories[key].split()[0][0] #first character of answer
					if i == str.lower(Territories[key]) or (i == "laayoune" and Territories[key] == "El Aaiun") or (i == "saint peter port" and Territories[key] == "St. Peter Port") or (i == "st. helier" and Territories[key] == "Saint Helier"):
						print 'Correct!'
						score += 1
					elif levenshtein(i, str.lower(Territories[key])) == 1: #for edit distances of 1
						print 'Close enough: it\'s ' + Territories[key] + '.'
						score += 1
					elif i == "":
						print 'It\'s ' + Territories[key] + '.'
					elif i == "hint":
						hintf(hint)
						hint_given = 1
					elif i == "quit" or i == "exit" or i == "q" or i == "end":
						exit = 1
						hint_given = 0
					else:
						print 'No, it\'s ' + Territories[key] + '.'
				else:
					hint = All[key].split()[0][0]
					#exceptions: accounting for other acceptable spellings/alternative names
					if i == str.lower(All[key]) or (i == "washington dc" and All[key] == "Washington D.C.") or (i == "nay pyi taw" and All[key] == "Naypyidaw") or ((i == "st john's" or i == "saint john's") and All[key] == "St. John's") or ((i == "st george's" or i == "saint george's") and All[key] == "St. George's") or (i == "luxembourg" and All[key] == "Luxembourg City"):
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
			print 'You got ' + str(score) + '/' + str(n) + ' capitals right in ' + str(minutes) + ' minutes and ' + str(seconds) + ' seconds. '
		else:
			print 'You got ' + str(score) + '/' + str(n) + ' capitals right in ' + str(seconds) + ' seconds. '
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