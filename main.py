import random
import math
random.seed(2)


trophic_level = [200000, 1000, 100, 10]

repeats = 100

for i in range(0, repeats):
	print_str = ""
	for tl in trophic_level:
		print_str = print_str + str(tl) + ", "
	print_str = print_str[:-2]
	print(print_str)
	new_tl = [0] * len(trophic_level)
	new_tl[0] = 200000 # Comment out whichever type of food growth you want.
	#new_tl[0] = trophic_level[0] + 150 # Constant growth
	#new_tl[0] = int(trophic_level[0] + (150*(1+math.sin(i * (math.pi/40))))) # Seasons

	for p in range(1, len(trophic_level)):
		for n in range(0, trophic_level[p]):
			if (trophic_level[p] == 0):
				q_score = 0.001
			else:
				q_score = new_tl[p-1]/trophic_level[p]
			rand_score = random.randint(1, 10)

			if (q_score > 10):
				if (rand_score < 3):
					new_tl[p] = new_tl[p] + 1
					new_tl[p-1] = new_tl[p-1] - 1
				else:
					new_tl[p] = new_tl[p] + 2
					new_tl[p-1] = new_tl[p-1] - 2
			elif (q_score <= 10 and q_score > 1):
				if (rand_score < 3):
					# Dies, does not pass on.
					new_tl[0]= new_tl[0] + 0.5

				elif (rand_score > 7):
					# Reproduces
					new_tl[p] = new_tl[p] + 2
					new_tl[p-1] = new_tl[p-1] - 2
				else:
					new_tl[p] = new_tl[p] + 1
					new_tl[p-1] = new_tl[p-1] - 1
			elif (q_score <= 1 and q_score > 0):
				if (rand_score < 2):
					# Survives.
					new_tl[p] = new_tl[p] + 1
					new_tl[p-1] = new_tl[p-1] - 1
				else:
					# Dies
					new_tl[0] = new_tl[0] + 0.5

	trophic_level = new_tl
