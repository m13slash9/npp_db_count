from Npp import *

#Specify characters that separate the name from the key
key_separator = ' - '
top_to_show = 5

#Read all data and separate names
all_text = editor.getText()
all_entries = all_text.split('\n')
all_names_and_keys = [cntr.split(key_separator) for cntr in all_entries]
all_names = [cntr[0] for cntr in all_names_and_keys]

#Find unique names
unique_names = set(all_names)

#Count titles
number_of_titles = [{'title':cntr, 'quantity': all_names.count(cntr)} for cntr in unique_names]
number_of_titles.sort(reverse=True)

#Create message text
out_string = ''
for cntr in range(top_to_show):
	out_string += number_of_titles[cntr]['title'] + ": " + str(number_of_titles[cntr]['quantity']) + "\n" + "\n"
out_string = out_string[:-2]

#Display results
notepad.messageBox(out_string,"Top " + str(top_to_show) + " entries") 
