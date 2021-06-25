# Drawings are based on lines and points in this version
from letters import *
import sys
import copy 
import math
import os
import datetime
from args import *
args = make_args()


if __name__ == "__main__":
	plt.ion()
	# # d = Drawing(pts = 4, coords = [(0,0), (1,0), (1,2), (-1,2)], lines = [(0,1),(1,2), (1,3)])
	# # d = Drawing(pts = 4, coords = [(-1,2), (0,1),(0,0), (1,2)], lines = [(0,1),(1,2), (1,3)])
	# time.sleep(10)
	# d = Drawing(pts = 6, coords = [(0,0), (0,1), (0,2), (1,0), (1,1), (1,2)], lines = [(0,1), (1,2), (1,3), (1,4),(2,4), (3,4), (4,5)])
	# d.show(mark_points = d.coords)
	# for letter in [letter_p, letter_r, letter_a, letter_k, letter_h, letter_y]:
	# # for letter in [letter_a]:
	# 	d.check_letter(letter, find_all = True)
	# 	d.check_letter_2(letter, find_all = True)
	# 	time.sleep(2)
	# # letter = letter_a
	# # d.check_letter(letter, find_all = True)
	# # d.check_letter_2(letter, find_all = True)
	# graph_drawing = nx.Graph()
	# # graph_drawing.add_edges_from(d.lines + [(y,x) for x,y in d.lines()])
	# graph_drawing.add_edges_from(d.lines)
	# graph_letter = nx.Graph()
	# graph_letter.add_edges_from(letter.lines)
	# 	# print("\n"*2)
	# print("sleeping")
	# time.sleep(500)
	# sys.exit()

	# name = input("Enter a name: ")
	name = args.name
	name = name.lower().strip()
	print(f"the name you entered was {name}")
	# sys.exit()
	try:
		string_letters = []
		all_string_letters = []
		for x in name:
			all_string_letters.append(x)
			if x not in string_letters:
				string_letters.append(x)
		template_letters = [globals()["letter_" + x] for x in string_letters]
		template_letters_for_display = [globals()["letter_" + x] for x in all_string_letters]	
	except:
		cprint("Sorry all letters of your name have not been implemented as of now", "magenta")
		sys.exit()

	try:
		os.mkdir(f"junk/{name}")
		print("Created a folder for this person/object")
	except Exception as e:
		print("Folder already exists")
		print(e)

	# sys.exit()
	num_fig_columns = math.ceil((len(name) + 1)**0.5)
	cprint(f"Looking for {string_letters}", "cyan")
	cprint(f"respective toughness is {[letter_toughness(letter.pts, len(letter.lines)) for letter in template_letters]}")
	cprint(f"num columns is {num_fig_columns}", "cyan")
	time.sleep(3)

	# plt.tight_layout()
	# plt.show()
	# test the config and interations
	# template_letters = [letter_j, letter_a]
	# template_letters = [letter_j_minimal_1, letter_a_minimal_1, letter_y, letter_n, letter_t_minimal_1]
	# template_letters = [letter_j, letter_a, letter_y, letter_n, letter_t]
	# template_letters = [letter_p, letter_r, letter_a, letter_k, letter_s]
	# template_letters = [letter_p, letter_r, letter_a, letter_k, letter_h]
	# template_letters = [letter_p, letter_r, letter_a, letter_k, letter_h]
	# template_letters = [letter_j_minimal_1]
	# template_letters = [letter_a]

	# template_letters = [letter_j_minimal_1]
	# template_letters = [ letter_y, letter_n, letter_t,letter_j_minimal_1, letter_a_minimal_1]
	
	for i,letter in enumerate(template_letters):
		letter.color = all_colors[i % len(all_colors)]

	initial_drawing = Drawing(pts = 1, coords = [(0,0)], lines = [], num_fig_columns = num_fig_columns)
	# initial_drawing = Drawing(pts = 11, 
	# 	coords = [(0, 0), (-2, 1), (-2, -1), (-4, 0), (-4, 2), (-5, -2), (-4, -2), (-2, -3), (-2, 3), (-4, -4), (-1, 3)], 
	# 	lines = [(0, 1), (1, 2), (2, 0), (2, 3), (3, 1), (1, 4), (3, 4), (3, 5), (3, 6), (2, 7), (6, 7), (2, 6), (1, 8), (4, 8), (6, 9), (5, 9), (9, 7), (1, 10)], 
	# 	num_fig_columns = num_fig_columns
	# )
	
	my_drawing = copy.deepcopy(initial_drawing)
	# my_drawing = drawing2(pts = 1, coords = [(0,0)])
	my_drawing.show(display = DISPLAY_WORKING)
	# sys.exit()
	drawing_counter = 0
	removal_freq = 2
	total_found = 0

	letters_to_improve_on = []
	# while(True):
	cprint(f"jumps are {jumps}", "yellow")
	for _ in tqdm(range(10000)):
		try:
			print(f"total_found was {total_found}")
			drawing_counter += 1
			old_pt = random.choice(list(range(my_drawing.pts)))
			if np.random.rand() < (1 - PROB_CONNECT_OLD_POINTS) or my_drawing.pts == 1:
				# trying to find a new pt using the jump method
				old_pt = my_drawing.coords[old_pt]
				chosen_jump = random.choice(jumps)
				dx, dy = chosen_jump
				x, y = old_pt
				potential_new = (x + dx, y + dy)
				if args.delta_step:
					cprint(f"Trying to improve {[x.actual_letter for x in letters_to_improve_on]}", "yellow")
					if len(letters_to_improve_on) == 0:
						letters_to_improve_on = template_letters
					letter_to_improve_on = random.choice(letters_to_improve_on)
					best_cost = 1
					possibilites_for_connection = []
					
					# can pick only one old pt for a speed up here
					coords_drawing = my_drawing.coords.copy()
					shuffled_jumps = jumps.copy()
					random.shuffle(coords_drawing)
					random.shuffle(shuffled_jumps)
					for existing in coords_drawing:
						if best_cost == 0:
							break
						for chosen_jump in shuffled_jumps:
							already_existed = False
							dx, dy = chosen_jump
							x, y = existing
							try_out = (x + dx, y + dy)
							# if try_out in my_drawing.coords:
							# 	continue
							if try_out in my_drawing.coords:
								pt_index = my_drawing.coords.index(try_out)
								old_pt_index = my_drawing.coords.index(existing)
								if (pt_index, old_pt_index) in my_drawing.lines or (old_pt_index, pt_index) in my_drawing.lines:
									# optimisation
									continue
								already_existed = True
							else:
								pt_index = my_drawing.pts

							my_drawing.connect_new_pt(existing, try_out, connect_collinear_directly = CONNECT_COLLINEAR_DIRECTLY) 
							_, letter_cost, _ = my_drawing.check_letter(letter_to_improve_on, find_all = False, display = False, must_include = pt_index)
							
							if not already_existed:
								my_drawing.remove_pt(try_out)
							if letter_cost < best_cost:
								best_cost = letter_cost
								possibilites_for_connection = [(existing, try_out)]
							elif letter_cost == best_cost:
								possibilites_for_connection.append((existing, try_out))
							if best_cost == 0:
								break
					cprint(f"the best cost was {best_cost}", "green")
					# print(f"found_possibilities {possibilites_for_connection}")
					if len(possibilites_for_connection) != 0:
						old_pt, potential_new = random.choice(possibilites_for_connection)
						print(f"chose to connect {old_pt} and  {potential_new}")
					# time.sleep(1)
			else:
				# adding an edge between the old points
				another_old_pt = random.choice(list(range(my_drawing.pts)))
				if old_pt == another_old_pt:
					continue
				old_pt = my_drawing.coords[old_pt]
				# name is misleading
				potential_new = my_drawing.coords[another_old_pt]



			# my_drawing.add_new_pt(potential_new) 
			my_drawing.connect_new_pt(old_pt, potential_new, connect_collinear_directly = CONNECT_COLLINEAR_DIRECTLY) 
			my_drawing.show(display = DISPLAY_WORKING)
			# success = my_drawing.contains_this_letter(letter_j) # draw with different color?
			# success = template_letter.check_drawing(my_drawing) # draw with different color?
			success = True
			atleast_one = False
			all_chosen_pts = []
			net_cost = 0
			worst_performance = 0
			letters_to_improve_on = []

			for letter in template_letters:
				# cprint(f"checking letter {letter.actual_letter}", "green")
				# temp, letter_cost, importances = my_drawing.check_letter(letter)
				found, letter_cost, importances = my_drawing.check_letter(letter, find_all = True, display = DISPLAY_WORKING)
				success = success and found # draw with different color?
				all_chosen_pts.append((letter_cost, importances))
				net_cost += letter_cost
				if not found:
					letters_to_improve_on.append(letter)
				# if letter_cost > worst_performance:
				# 	worst_performance = letter_cost
				# 	letters_to_improve_on = [letter]
				# elif letter_cost == worst_performance:
				# 	letters_to_improve_on.append(letter)

				# time.sleep(1)

			print(f"net cost was {net_cost}")
			if success:
				# displaying when found
				prefix = datetime.datetime.now().strftime("%Y-%b-%d_time_%H-%M-%S")
				print("found")
				cprint("Pruning", "red")
				my_drawing.show()
				_ = [my_drawing.check_letter(letter, dots = False) for letter in template_letters_for_display]
				plt.savefig(f"junk/{name}/{prefix}_found_without_pruning.png")
				time.sleep(2)
				cprint("Pruning", "red")
				# time.sleep(5)
				# cprint(f"Earlier {my_drawing.pts}pts and {len(my_drawing.lines)}lines", "cyan")
				my_drawing = my_drawing.prune(template_letters)
				# cprint(f"Now {my_drawing.pts}pts and {len(my_drawing.lines)}lines", "cyan")
				my_drawing.show()
				# time.sleep(5)
				# drawing again
				_ = [my_drawing.check_letter(letter, dots = False) for letter in template_letters_for_display]
				plt.savefig(f"junk/{name}/{prefix}_found.png")
				time.sleep(2)
				my_drawing = copy.deepcopy(initial_drawing)
				my_drawing.show()
				total_found += 1
				if not DISPLAY_WORKING:
					plt.close()
				# break

			# if drawing_counter % removal_freq == 0:
				# not success because the state is altered in the the if success code

				# removing one point at random
				
				# remove the point with min connections
				# connections = [0 for _ in range(my_drawing.pts)]
				# for x,y in my_drawing.lines:
				# 	connections[x] += 1
				# 	connections[y] += 1
				# to_remove = connections.index(min(connections))
				
				# remove the point with min connections and has similar nbrs
				
				# when using the line model
			# exit_loop = False
			exit_loop = my_drawing.pts <= DRAWING_NUM_POINTS_UPPER_LIMIT 
			while (my_drawing.pts > DRAWING_NUM_POINTS_LOWER_LIMIT) and (not success) and (not exit_loop):
				# exit_loop = False
				# while (not exit_loop):
				if np.random.rand() < PROB_GREEDY_REMOVAL:
					hits = [0 for _ in range(my_drawing.pts)]
					for i,(letter_cost, importances) in enumerate(all_chosen_pts):
						print(importances)
						noramlise_importance = max(importances)
						if noramlise_importance == 0:
							continue
						for pt,imp in enumerate(importances):
							if imp != 0:
								# hits[pt] += (((1 - letter_cost)*imp)/noramlise_importance)
								hits[pt] += (((1 - letter_cost)*imp)/noramlise_importance)*letter_toughness(template_letters[i].pts, len(template_letters[i].lines))

					print((hits, max(hits), min(hits)))
					if max(hits) >= 1 and len(template_letters) > 1:
						# enters if one letter was found or one point was crucial to two constructions
						mini = min(hits)
						indices = [i for i,el in enumerate(hits) if el == mini]
						to_remove = random.choice(indices)
						if mini != 0:
							exit_loop = True

					else:
						connections = [[] for _ in range(my_drawing.pts)]
						for x,y in my_drawing.lines:
							connections[x].append(y)
							connections[y].append(x)
						scores = [sum(len(connections[a]) for a in connections[x]) for x in range(my_drawing.pts)]
						to_remove = scores.index(min(scores))
						exit_loop = True
						
				else:
					to_remove = random.choice(list(range(my_drawing.pts)))
					exit_loop = True

				cprint(f"removing pt {to_remove}", "cyan")
				# time.sleep(0.1)
				my_drawing.remove_pt(to_remove)
				my_drawing.show(display = DISPLAY_WORKING)
				if not exit_loop:
					# for hit calc
					all_chosen_pts = []
					for letter in template_letters:
						temp, letter_cost, importances = my_drawing.check_letter(letter, find_all = True, display = DISPLAY_WORKING)
						all_chosen_pts.append((letter_cost, importances))

		except Exception as e:
			print("Exception caught")
			print(e)
			print(e.__class__.__name__)
			traceback.print_exc()
			# time.sleep(10)
			sys.exit()
