import ROOT
import re

def cut_to_branches(cut): #it accepts a tcut or a string
	if (type(cut) is ROOT.TCut):
		cut = cut.GetTitle()
	elif (type(cut) is not str):
		print "ERROR: cut_to_branches; wrong input type. Input cut has to be string or TCut!"
		raise
	#print cut
	#parts = re.split('[&&|\|\||\*|\+|\-|\/|\,|\.|>|<|=+| +|\(|\)|[min]|[max]|[sqrt]|[log]]+',cut) #split different cuts by && or || or math operators
	parts = re.split('[&&|\|\||\*|\+|\-|\/|,|>|<|=]+',cut) #split different cuts by && or || or math operators
	#parts = [branch.replace(',', '').replace('.', '').replace('>', '').replace('<', '').replace('=', '').replace(' +', '').replace('(|)', '').replace('min|max|sqrt|log','').replace('(','').replace(')','') for branch in parts] #remove other carachters and strings that are not branches
	substrings_to_remove = ['>', '<', '=', 'min(', 'max(', 'sqrt(', 'log(', '(', ')', ' ']
	for string in substrings_to_remove:
		parts = [branch.replace(string, '') for branch in parts]
	branches = []
	#now let's remove numbers
	for i, part in enumerate(parts):
		try:
			float(part)
		except:
			branches.append(part)
	#print ''
	#print branches
	#print ''
	#print ''
	return branches