#!/usr/bin/python3
import csv
import re
#~ mods = re.compile('[\[(<{~].+[\])>}~')
with open('cty.csv', newline='') as csvfile:
	with open("all_prefixes.h", "w") as outfile:
		print("/* generated from cty.csv from https://www.country-files.com/category/big-cty/", file=outfile)
		print("   using the script generate_prefix_h.py */\n", file=outfile)
		print("char *all_prefixes[] = {", file=outfile)
		rdr = csv.reader(csvfile, delimiter=',', quotechar='|')
		count = 0
		for row in rdr:
			prefixes = row[9].split()
			for pfx in prefixes:
				if not pfx.startswith("="):
					unmod = re.split(r'\W+', pfx)
					print('\t"{0}", // {1}'.format(unmod[0], row[1]), file=outfile)
					count += 1
		print("};", file=outfile)
		print("\nconst int all_prefixes_count = {0};".format(count), file=outfile)
