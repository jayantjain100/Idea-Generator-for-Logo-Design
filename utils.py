import time 
from matplotlib import pyplot as plt
import math
import random
import traceback
from itertools import permutations, combinations
import numpy as np
from termcolor import cprint, colored
from my_constants import *
import copy
from inspect import signature
from tqdm import tqdm
import networkx as nx  

# cprint = lambda x,y="white" : tqdm.write(colored(str(x) + '\n', y))
cprint = lambda x,y="white" : tqdm.write(colored(str(x), y))
# print = lambda x : tqdm.write(str(x) + '\n')
print = lambda x : tqdm.write(str(x))

# what characterises a letter?
# num of points (int)
# lines (list of tuples of pts), undirected?

# focus on correctness first, will optimise later

# model as a search problem, quantify constraint importance and codify the desired aesthetic



# constraints
# hinged line angle interactions

# # POTE - doesnt give the directed angle
# def theta(v, w): 
# 	radians = np.arccos(v.dot(w)/(np.norm(v)*np.norm(w)))
# 	# degrees = (radians*180)/np.pi
# 	degrees = np.degrees(radians)
# 	return degrees

# https://stackoverflow.com/a/35134034/9311953
def letter_toughness(num_pts, num_lines):
	return 1
	# return (num_pts/4)*0.5 + (num_lines/4)*0.5 

def theta(v, w):
	radians = np.math.atan2(np.linalg.det([v,w]),np.dot(v,w))
	degrees = np.degrees(radians)
	# print(f"found {degrees} degrees")
	#POTE?
	# print(degrees)
	if degrees < 0:
		degrees += 360
	
	return degrees

# unhinged line angle interactions - absolute sense - parallel perp type ki cheez check karne ke liye
# (180 - theta) and (theta) - cant distinguish easily
def ambiguous_relative_line_angle(l1, l2, low = None, high = None, exact = None):
	if exact is not None:
		low = exact
		high = exact
	vec1 = np.array(l1[1]) - np.array(l1[0])
	vec2 = np.array(l2[1]) - np.array(l2[0])
	# abs_angle = abs(theta(vec1, vec2))
	# angle = min(abs_angle, 180 - abs_angle)
	angle = theta(vec1, vec2)
	angle = angle % 180
	assert 0 <= angle <= 180, "what?"
	return low - EPSILON <= angle <= high + EPSILON
	
def hinged_relative_line_angle(l1, l2, low = None, high = None, exact = None):
	assert ((low is None or low >= 0) and (high is None or high >= 0)), "invalid args"
	if exact is not None:
		low = exact
		high = exact
	l1p1, l1p2 = l1 
	l2p1, l2p2 = l2
	if l1p1 != l2p1:
		# assert (l1p1 == l2p2) or (l1p2 == l2p1), "no common point in these lines - received - {},{}".format(l1, l2)
		if l1p1 == l2p2:
			l2p1, l2p2 = l2p2, l2p1
		elif l1p2 == l2p1:
			l1p1, l1p2 = l1p2, l1p1
		elif l1p2 == l2p2:
			l2p1, l2p2 = l2p2, l2p1
			l1p1, l1p2 = l1p2, l1p1
		else:
			assert (l1p1 == l2p2) or (l1p2 == l2p1), "no common point in these lines - received: l1={}, l2={}".format(l1, l2)
			print("no common point in these lines - received: l1={}, l2={}".format(l1, l2))
			print("missing hinge")
			return False 

	hinge = l1p1
	vec1 = np.array(l1p2) - np.array(hinge)
	vec2 = np.array(l2p2) - np.array(hinge)
	angle = theta(vec1, vec2)
	return low - EPSILON <= angle <= high + EPSILON

# POTE the line is not considered directed
def absolute_line_angle_with_x_axis(line, low = None, high = None, exact = None):
	#returns angle made with xaxis - +ve version
	assert (min(low,high) >= 0 and max(low,high)<=180), "check given params"
	line_vec = np.array(line[1]) - np.array(line[0])
	xaxis = np.array([1,0])
	# bug tha
	# angle = theta(line_vec, xaxis)
	angle = theta(xaxis, line_vec)
	# if angle < 0:
	# 	angle += 180
	angle = angle % 180

	return low - EPSILON <= angle <= high + EPSILON

# length interactions - bounds on ratios - sameness checking is iska subset
def line_length_ratio(l1, l2, low = None, high = None, exact = None) -> bool:
	if exact is not None:
		low = exact
		high = exact
	len1 = np.linalg.norm(np.array(l1[1]) - np.array(l1[0]))
	len2 = np.linalg.norm(np.array(l2[1]) - np.array(l2[0]))
	return low - EPSILON <= len2/len1 <= high + EPSILON

# point x axis and y axis interactions, for example, these 2 pts must have the same x coord

# directionality, positioning of pts
def pts_x_axis(pt1, pt2, left = None, exact = None, strict = False):
	assert left is not None or exact is not None, "too many params set"
	if exact is not None:
		if exact:
			return abs(pt1[0] - pt2[0]) <= EPSILON
		else:
			return abs(pt1[0] - pt2[0]) > EPSILON
	elif left:
		if strict:
			return pt1[0] <= pt2[0] - EPSILON
		else:
			return pt1[0] <= pt2[0] + EPSILON
	else:
		if strict:
			return pt1[0] >= pt2[0] + EPSILON
		else:
			return pt1[0] >= pt2[0] - EPSILON


def pts_y_axis(pt1, pt2, bottom = None, exact = None, strict = False):
	assert bottom is not None or exact is not None, "too many params set"
	if exact is not None:
		if exact:
			return abs(pt1[1] - pt2[1]) <= EPSILON
		else:
			return abs(pt1[1] - pt2[1]) > EPSILON
	if bottom:
		if strict:
			return pt1[1] <= pt2[1] - EPSILON
		else:
			return pt1[1] <= pt2[1] + EPSILON
	else:
		if strict:
			return pt1[1] >= pt2[1] + EPSILON
		else:
			return pt1[1] >= pt2[1] - EPSILON

def var_name(var, dictionary = globals()):
	# returns the first var_name that points to the object
	print(list(dictionary.keys()))
	for k in dictionary:
		if var == dictionary[k]:
			return k
	raise Exception("variable not found error")

def func_name(func):
	# since we're using it just for functions
	return func.__name__


class Letter():
	def __init__(self, pts, lines = None, color = "blue", actual_letter = None):
		self.pts = pts
		self.lines = lines
		self.interactions = [] #list of functions to check
		self.named_interactions = []
		self.coords = None
		self.color = color
		self.actual_letter = actual_letter

	def add_pt_interaction(self, pt1, pt2, foo, **kwargs):
		self.interactions.append( lambda coords : foo(coords[pt1], coords[pt2], **kwargs))
		self.named_interactions.append(f"point interaction bw points {pt1} and {pt2}\ntype: {foo.__name__}, args: {kwargs}\n")

	def add_line_interaction(self, l1, l2, foo, **kwargs):
		if l2 is not None:
			self.interactions.append( lambda coords : foo(tuple(coords[a] for a in self.lines[l1]), tuple(coords[a] for a in self.lines[l2]), **kwargs))
			self.named_interactions.append(f"line interaction bw lines {l1} and {l2} i.e bw (pt{self.lines[l1][0]},pt{self.lines[l1][1]}) and (pt{self.lines[l2][0]},pt{self.lines[l2][1]})\ntype: {(foo.__name__)}, args: {kwargs}\n")
		else:
			self.interactions.append( lambda coords : foo(tuple(coords[a] for a in self.lines[l1]), **kwargs))
			self.named_interactions.append(f"line interaction bw lines {l1}(pt{self.lines[l1][0]},pt{self.lines[l1][1]}) and xaxis \ntype: {(foo.__name__)}, args: {kwargs}\n")

	# def check_drawing(self, drawing):

	# 	num_pts_needed = self.pts
	# 	available = drawing.pts
	# 	if num_pts_needed > available:
	# 		print("not enough points")
	# 		return False 

	# 	# was not needed, but saves a lot of time
	# 	if len(self.lines) > len(drawing.lines):
	# 		print("not enough lines")
	# 		return False

	# 	# LATER - can be made faster by making selections using a dfs based scheme
	# 	# also, no need to check each thing independently i think
	# 	# nCp loop
	# 	counter = 0
	# 	for selection in combinations(list(range(available)), num_pts_needed):
	# 		for perm in permutations(selection):
	# 			counter += 1
	# 			print(f"analysing perm {perm}")
	# 			set_pts = set(perm)
	# 			inverse_map = {v:k for k,v in enumerate(perm)}
	# 			# subset_lines = [(x,y) for x,y in drawing.lines if (x in set_pts or y in set_pts)]
	# 			subset_lines = [(x,y) for x,y in drawing.lines if (x in set_pts and y in set_pts)]
	# 			renamed_lines = [(inverse_map[x], inverse_map[y]) for x,y in subset_lines]
	# 			renamed_lines_set = set(renamed_lines)
	# 			coords = [drawing.coords[i] for i in perm]
	# 			#each line in the template letter must be a part of the subset drawing
	# 			# print(f"set_pts is {set_pts}")
	# 			# print(f"inverse_map is {inverse_map}")
	# 			# print(f"subset_lines is {subset_lines}")
	# 			# print(f"renamed_lines is {renamed_lines}")
	# 			# print(f"renamed_lines_set is {renamed_lines_set}")
	# 			# print(f"coords is {coords}")

	# 			success = True
	# 			for x,y in self.lines:
	# 				# waah
	# 				# if ((x,y) and (y,x) not in renamed_lines_set):
					
	# 				if (((x,y) not in renamed_lines_set) and (y,x) not in renamed_lines_set):
	# 					print(f"missed true segment {(x,y)}, created segs were {(renamed_lines_set)}")
	# 					success = False
	# 					break 
	# 			if not success:
	# 				continue

	# 			# if these things match toh ab we have an isomorphic graph, and now we need to check the spatial sanity
	# 			# connectevity is correct, checking the lengths and angles ab
				
	# 			for constraint, description in zip(self.interactions, self.named_interactions):
	# 				if not constraint(coords):
	# 					# print("invalid constraint {}".format((constraint.__name__)))
	# 					cprint("failed", "red")
	# 					print(description)
	# 					success = False
	# 					# sys.exit()
	# 					break

	# 			if success:
	# 				to_draw = [(perm[x], perm[y]) for x,y in self.lines]
	# 				# drawing.show(color = "blue", overwrite= True, subset = set_pts)
	# 				drawing.show(color = "blue", fresh= False, subset_lines = to_draw, mark_points = coords)
	# 				cprint(f"Analysed {counter} Permutation-Combinations and found :)", "magenta")
	# 				return True
	# 	cprint(f"Analysed {counter} Permutation-Combinations but could not find", "magenta")
	# 	return False


'''
so the interaction we have are - 
	ambiguous_relative_line_angle
	hinged_relative_line_angle
	absolute_line_angle_with_x_axis
	line_length_ratio
	pts_x_axis
	pts_y_axis
'''

#LATER - 
# if adding a new line intersects some old segments, do we want to break those?

# letter_a.add_line_interaction()

# class interaction():
# 	def __init__():
# 		pass

# #POTE
# class CustomFloat():
# 	def __init__(self, val):
# 		self.val = float(val)

# 	def __eq__(self, other):
# 		if isinstance(other, CustomFloat):
# 			other = other.val
# 		return abs(self.val - other) <= EPSILON:
		

#LATER - might want to store coords as a dictionary for faster removal etc
#Profile and see
class Drawing():
	def __init__(self, pts, coords, lines, num_fig_columns = FIGURE_COLUMNS):
		assert len(coords) == pts, "incorrect initialisation of the drawing"
		self.pts = pts
		self.coords = coords
		self.lines = lines #each line is a tuple of 2 point_ids
		self.diff_x = 0
		self.diff_y = 0
		self.plot_figs = 1
		self.num_fig_columns = num_fig_columns

	def connect_new_pt(self, old_pt, new_pt, connect_collinear_directly = False):
		assert old_pt != new_pt, "Cant create a line bw the 2 same pts"
		assert old_pt in self.coords, "invalid existing pt to make a new connection"
		# assert new_pt not in self.pts
		old_pt_index = self.coords.index(old_pt)
		if new_pt in self.coords:
			new_pt_index = self.coords.index(new_pt)
		else:
			new_pt_index = self.pts 
			self.coords.append(new_pt) 
			self.pts += 1

		if (old_pt_index, new_pt_index) in self.lines or (new_pt_index, old_pt_index) in self.lines:
			cprint("connection already exists, dropped", "cyan")
		else:
			self.lines.append((old_pt_index, new_pt_index))

		if connect_collinear_directly:
			# check for collinear sets
			# sys.exit()
			to_connect = []
			for hinge in range(self.pts):
				vectors = []
				hinge_vec = np.array(self.coords[hinge])
				for x,y in self.lines:
					if y == hinge:
						x, y = y, x
					other_pt_vec = np.array(self.coords[y]) - hinge_vec
					vectors.append((y, other_pt_vec))
				for i in range(len(vectors)):
					for j in range(i + 1, len(vectors)):
						pt1, vec1 = vectors[i]
						pt2, vec2 = vectors[j]
						if abs(theta(vec1, vec2) - 180) < EPSILON:
							to_connect.append((pt1, pt2))

			for pt1, pt2 in to_connect:
				if (pt1,pt2) not in self.lines and (pt2, pt1) not in self.lines:
						self.lines.append((pt1,pt2))
						# time.sleep(3)
						# cprint(f"look here, added {(pt1,pt2)}", "cyan")



	def remove_pt(self, pt):
		#pt is supposed to be a 2d pt
		if isinstance(pt, (int)):
			#most probably pt index was given
			# print("warning")
			pt = self.coords[pt]

		assert pt in self.coords, "invalid existing pt to make a new connection"

		pt_index = self.coords.index(pt)
		remapper = lambda x: x if x < pt_index else x - 1

		self.coords.remove(pt)
		self.pts -= 1
		self.lines = [(remapper(x),remapper(y)) for x,y in self.lines if (x!=pt_index and y!=pt_index)]

	# @profile
	# def check_letter(self, letter, display = True, dots = True, find_all = False):
	# 	num_pts_needed = letter.pts
	# 	available = self.pts
	# 	if num_pts_needed > available:
	# 		print("not enough points")
	# 		return False, 1, [0]*self.pts 
	# 	if len(letter.lines) > len(self.lines):
	# 		print("not enough lines")
	# 		return False, 1, [0]*self.pts

	# 	counter = 0
	# 	actual_counter = 0
	# 	min_invalid_constaints = len(letter.interactions) + 1
	# 	already_drawn = False
	# 	best_config = (1, [0]*self.pts)

	# 	for selection in combinations(list(range(available)), num_pts_needed):
	# 		for perm in permutations(selection):
	# 			counter += 1
	# 			# print(f"analysing perm {perm}")
	# 			set_pts = set(perm)
	# 			inverse_map = {v:k for k,v in enumerate(perm)}
	# 			subset_lines = [(x,y) for x,y in self.lines if (x in set_pts and y in set_pts)]
	# 			renamed_lines = [(inverse_map[x], inverse_map[y]) for x,y in subset_lines]
	# 			renamed_lines_set = set(renamed_lines)
	# 			coords = [self.coords[i] for i in perm]
	# 			success = True
	# 			for x,y in letter.lines:
	# 				if (((x,y) not in renamed_lines_set) and (y,x) not in renamed_lines_set):
	# 					# print(f"missed true segment {(x,y)}, created segs were {(renamed_lines_set)}")
	# 					success = False
	# 					break 
	# 			if not success:
	# 				continue
				
	# 			actual_counter += 1
	# 			print(f"analysing perm {perm}")
	# 			num_invalid_constraints = 0
	# 			for constraint, description in zip(letter.interactions, letter.named_interactions):
	# 				try:
	# 					if not constraint(coords):
	# 						# cprint("failed", "red")
	# 						# print(description)

	# 						# to_draw = [(perm[x], perm[y]) for x,y in letter.lines]
	# 						# self.show(color = letter.color, fresh= False, subset_lines = to_draw, mark_points = coords, opacity = 0.7)
	# 						# time.sleep(10)
	# 						# sys.exit()
							
	# 						num_invalid_constraints += 1
	# 						success = False
	# 						# break

	# 				except Exception as e:
	# 					cprint(f"problem in checking constraint - {description}", "cyan")
	# 					raise e

	# 			if num_invalid_constraints <= min_invalid_constaints:
	# 				if (num_invalid_constraints < min_invalid_constaints):
	# 					# if stricly less					
	# 					importance = [0]*self.pts
	# 					min_invalid_constaints = num_invalid_constraints
	# 				for el in perm:
	# 					importance[el] += 1
	# 				best_config = (round(min_invalid_constaints/len(letter.interactions),2), importance)


	# 			if success:
	# 				to_draw = [(perm[x], perm[y]) for x,y in letter.lines]
	# 				if display and not already_drawn:
	# 					self.show(color = letter.color, fresh= False, subset_lines = to_draw, mark_points = coords if dots else None, opacity = 0.7)
	# 					already_drawn = True
	# 				if not find_all:
	# 					cprint(f"Analysed {counter} Permutation-Combinations and found :)", "magenta")
	# 					return (True, *best_config)

	# 	if display:
	# 		if min_invalid_constaints !=0:
	# 			cprint(f"Analysed {counter} Permutation-Combinations but could not find", "magenta")
	# 		else :
	# 			cprint(f"Analysed {counter} Permutation-Combinations and found it!", "magenta")
		
	# 	print(f"actual_counter was {actual_counter}")
	# 	return ((min_invalid_constaints == 0), *best_config)
	
	def check_letter(self, letter, display = True, dots = True, find_all = False, must_include = None):
		num_pts_needed = letter.pts
		available = self.pts
		if num_pts_needed > available:
			# print("not enough points")
			return False, 1, [0]*self.pts 
		if len(letter.lines) > len(self.lines):
			# print("not enough lines")
			return False, 1, [0]*self.pts

		counter = 0
		min_invalid_constaints = len(letter.interactions) + 1
		already_drawn = False
		best_config = (1, [0]*self.pts)

		graph_drawing = nx.Graph()
		graph_drawing.add_edges_from(self.lines)
		# graph_drawing.add_edges_from(self.lines + [(y,x) for x,y in self.lines])
		graph_letter = nx.Graph()
		graph_letter.add_edges_from(letter.lines)

		# graph_letter.add_edges_from([(x+1,y+1) for x,y in letter.lines])

		GM = nx.algorithms.isomorphism.GraphMatcher(graph_drawing, graph_letter)

		# huge difference between the "SubGraph isomorphism problem" and "induced subgraph isomorphism problem"
		# check wikipedia
		# for mapping in GM.subgraph_isomorphisms_iter():
		for mapping in GM.subgraph_monomorphisms_iter():
			# print(mapping)
			# the mapping is from graph_drawing nodes to graph_letter nodes
			# perm[i] is supposed to have graph_drawings node for node i of graph_letter
			if ((must_include is not None) and (not (must_include in mapping))):
				continue
			perm = [-1 for _ in range(letter.pts)]
			for k in mapping:
				perm[mapping[k]] = k
			# breakpoint()
			counter += 1
			# print(f"analysing perm {perm}")
			set_pts = set(perm)
			inverse_map = {v:k for k,v in enumerate(perm)}
			subset_lines = [(x,y) for x,y in self.lines if (x in set_pts and y in set_pts)]
			renamed_lines = [(inverse_map[x], inverse_map[y]) for x,y in subset_lines]
			renamed_lines_set = set(renamed_lines)
			coords = [self.coords[i] for i in perm]
			success = True
			for x,y in letter.lines:
				if (((x,y) not in renamed_lines_set) and (y,x) not in renamed_lines_set):
					# print(f"missed true segment {(x,y)}, created segs were {(renamed_lines_set)}")
					success = False
					break 
			if not success:
				continue
			# print(f"analysing perm {perm}")
			num_invalid_constraints = 0
			for constraint, description in zip(letter.interactions, letter.named_interactions):
				try:
					if not constraint(coords):
						# cprint("failed", "red")
						# print(description)
						# # failed = description

						# to_draw = [(perm[x], perm[y]) for x,y in letter.lines]
						# self.show(color = letter.color, fresh= False, subset_lines = to_draw, mark_points = coords, opacity = 0.7)
						# time.sleep(10)
						# sys.exit()
						
						num_invalid_constraints += 1
						success = False
						# break

				except Exception as e:
					cprint(f"problem in checking constraint - {description}", "cyan")
					raise e

			if num_invalid_constraints <= min_invalid_constaints:
				if (num_invalid_constraints < min_invalid_constaints):
					# if stricly less					
					importance = [0]*self.pts
					min_invalid_constaints = num_invalid_constraints
				for el in perm:
					importance[el] += 1
				best_config = (round(min_invalid_constaints/len(letter.interactions),2), importance)
				# print(failed)

			if success:
				to_draw = [(perm[x], perm[y]) for x,y in letter.lines]
				if display and not already_drawn:
					self.show(color = letter.color, fresh= False, subset_lines = to_draw, mark_points = coords if dots else None, opacity = 0.7)
					already_drawn = True
				if not find_all:
					# cprint(f"Analysed {counter} Permutation-Combinations and found :)", "magenta")
					return (True, *best_config)

		# if display:
		# 	if min_invalid_constaints !=0:
		# 		cprint(f"Analysed {counter} Permutation-Combinations but could not find", "magenta")
		# 	else:
		# 		cprint(f"Analysed {counter} Permutation-Combinations and found it!", "magenta")
		# print(f"counter was {counter}")
		return ((min_invalid_constaints == 0), *best_config)
	


	def prune_pts(self, list_of_letters):
		for can_remove in range(self.pts):
			copied_drawing = copy.deepcopy(self)
			copied_drawing.remove_pt(can_remove)
			if False not in [copied_drawing.check_letter(l, display = False)[0] for l in list_of_letters]:
				return copied_drawing.prune(list_of_letters)
		return self

	def prune_lines(self, list_of_letters):
		for can_remove in self.lines:
			copied_drawing = copy.deepcopy(self)
			copied_drawing.lines.remove(can_remove)
			if False not in [copied_drawing.check_letter(l, display = False)[0] for l in list_of_letters]:
				return copied_drawing.prune(list_of_letters)
		return self

	def prune(self,list_of_letters):
		answer = self.prune_pts(list_of_letters)
		answer = answer.prune_lines(list_of_letters)
		return answer

	def show(self, display = True, duration = 0.001, fresh = True, color = "green", subset = None, subset_lines = None, mark_points = None, pt_color = "red", opacity = 1, show_full = True):
		global plt
		if not display:
			return
		if fresh:
			plt.clf()
			plt.title(f"drawing has {self.pts} points {len(self.lines)} lines")
			self.diff_x = 0
			self.diff_y = 0
			self.plot_figs = 1 
		else:
			all_xs = [x for x,y in self.coords]
			all_ys = [y for x,y in self.coords]
			width = max(all_xs) - min(all_xs)  + 1
			height = max(all_ys) - min(all_ys) + 1
			self.plot_figs += 1 
			self.diff_x += width
			if (self.plot_figs - 1) % self.num_fig_columns == 0:
				self.diff_x = 0
				# self.diff_x = width
				self.diff_y -= height


		if subset is not None:
			chosen_lines = [(x,y) for (x,y) in self.lines if (x in subset and y in subset)]
		elif subset_lines is not None:
			chosen_lines = subset_lines
		else:
			chosen_lines = self.lines

		for (pt1, pt2) in chosen_lines:
			x1, y1 = self.coords[pt1]
			x2, y2 = self.coords[pt2]
			# plt.plot((x1, x2), (y1, y2), color=color, alpha = opacity)
			plt.plot(self.diff_x + np.array((x1, x2)), self.diff_y + np.array((y1, y2)), color=color, alpha = opacity)

		if show_full:
			for (pt1, pt2) in self.lines:
				x1, y1 = self.coords[pt1]
				x2, y2 = self.coords[pt2]
				# plt.plot((x1, x2), (y1, y2), color=color, alpha = opacity)
				plt.plot(self.diff_x + np.array((x1, x2)), self.diff_y + np.array((y1, y2)), color= signature(self.show).parameters['color'].default, alpha = 0.05)


		if mark_points is not None:
			xs = [x for x,y in mark_points]
			ys = [y for x,y in mark_points]
			# plt.scatter(xs, ys, color = pt_color)
			plt.scatter(self.diff_x + np.array(xs), self.diff_y + np.array(ys), color = pt_color, s=16)
			for i,(x,y) in enumerate(mark_points):
				# plt.annotate(str(i), (x+0.03, y + 0.03), fontsize=12)
				plt.annotate(str(i), (x+0.03 + self.diff_x, y + 0.03 + self.diff_y), fontsize=9)


		# plt.show(block = False)
		plt.tight_layout()
		plt.draw()	
		plt.pause(duration)
		# print("sleeping")
		# time.sleep(duration)

# class drawing2():
# 	def __init__(self, pts, coords):
# 		assert len(coords) == pts, "incorrect initialisation of the drawing"
# 		self.pts = pts
# 		self.coords = coords

# 	def add_new_pt(self, new_pt):
# 		if new_pt in self.coords:
# 			return
# 		else:
# 			new_pt_index = self.pts 
# 			self.coords.append(new_pt) 
# 			self.pts += 1

# 	def remove_pt(self, pt):
# 		if isinstance(pt, (int)):
# 			print("warning")
# 			pt = self.coords[pt]

# 		assert pt in self.coords, "invalid existing pt to make a new connection"
# 		# pt_index = self.coords.index(pt)
# 		# remapper = lambda x: x if x < pt_index else x - 1

# 		self.coords.remove(pt)
# 		self.pts -= 1
# 		# self.lines = [(remapper(x),remapper(y)) for x,y in self.lines if (x!=pt_index and y!=pt_index)]

# 	def check_letter(self, letter ):
# 		num_pts_needed = letter.pts
# 		available = self.pts
# 		if num_pts_needed > available:
# 			print("not enough points")
# 			return False 

# 		counter = 0
# 		for selection in combinations(list(range(available)), num_pts_needed):
# 			for perm in permutations(selection):
# 				counter += 1
# 				print(f"analysing perm {perm}")
# 				set_pts = set(perm)
# 				inverse_map = {v:k for k,v in enumerate(perm)}
# 				# subset_lines = [(x,y) for x,y in self.lines if (x in set_pts and y in set_pts)]
# 				# renamed_lines = [(inverse_map[x], inverse_map[y]) for x,y in subset_lines]
# 				# renamed_lines_set = set(renamed_lines)
# 				coords = [self.coords[i] for i in perm]
# 				success = True
# 				# for x,y in letter.lines:
# 				# 	if (((x,y) not in renamed_lines_set) and (y,x) not in renamed_lines_set):
# 				# 		print(f"missed true segment {(x,y)}, created segs were {(renamed_lines_set)}")
# 				# 		success = False
# 				# 		break 
# 				# if not success:
# 				# 	continue
				
# 				for constraint, description in zip(letter.interactions, letter.named_interactions):
# 					if not constraint(coords):
# 						cprint("failed", "red")
# 						print(description)
# 						success = False
# 						break

# 				if success:
# 					to_draw = [(perm[x], perm[y]) for x,y in letter.lines]
# 					self.show(color = letter.color, fresh= False, subset_lines = to_draw, mark_points = coords, opacity = 0.7)
# 					cprint(f"Analysed {counter} Permutation-Combinations and found :)", "magenta")
# 					return True

# 		cprint(f"Analysed {counter} Permutation-Combinations but could not find", "magenta")
# 		return False

	

# 	def show(self, duration = 0.001, fresh = True, color = "green", subset = None, subset_lines = None, mark_points = None, pt_color = "red", opacity = 0.2):
# 		global plt
# 		if fresh:
# 			plt.clf()
# 			plt.title(f"drawing has {self.pts} points")
			
# 		all_lines = [(i,j) for i in range(self.pts) for j in range(i+1, self.pts)]
# 		if subset is not None:
# 			chosen_lines = [(x,y) for (x,y) in all_lines if (x in subset and y in subset)]
# 		elif subset_lines is not None:
# 			chosen_lines = subset_lines
# 		else:
# 			chosen_lines = all_lines

# 		for (pt1, pt2) in chosen_lines:
# 			x1, y1 = self.coords[pt1]
# 			x2, y2 = self.coords[pt2]
# 			plt.plot((x1, x2), (y1, y2), color=color, alpha = opacity)

# 		if mark_points is not None:
# 			xs = [x for x,y in mark_points]
# 			ys = [y for x,y in mark_points]
# 			plt.scatter(xs, ys, color = pt_color)
# 			for i,(x,y) in enumerate(mark_points):
# 				plt.annotate(str(i), (x+0.03, y + 0.03), fontsize=12)


# 		# plt.show(block = False)
# 		plt.tight_layout()
# 		plt.draw()	
# 		plt.pause(duration)
# 		print("sleeping")
# 		# time.sleep(duration)

# def foo(*args, **kwargs):
# 	# print(type(args), args, *args)
# 	# print(type(kwargs), kwargs, **kwargs)
# 	return args, kwargs


if __name__ == '__main__':
	plt.ion()
	plt.tight_layout()
	plt.show()
	# test the config and interations
	template_letter = letter_j
	# my_drawing = drawing(pts = 5, coords = [(0,0), (1,2), (2,4), (3,2), (4,0)] , lines = [(0,1), (1,2), (2,3), (1,3), (3,4)])

	# check extra points
	# my_drawing = drawing(pts = 6, coords = [(0,0), (1,2), (2,4), (3,2), (4,0), (2,3)] , lines = [(0,1), (1,2), (2,3), (1,3), (3,4), (0,5), (5,3)])
	# my_drawing.show()
	# check - permuted points
	# my_drawing = drawing(pts = 5, coords = [ (1,2), (0,0), (2,4), (3,2), (4,0)] , lines = [(0,1), (0,2), (2,3), (0,3), (3,4)])

	# check - permuted lines
	# my_drawing = drawing(pts = 5, coords = [(3,0), (1,2), (2,4), (3,2), (4,0)] , lines = [(1,0), (1,2), (1,3), (3,4), (2,3)])
	
	# check - shifted points
	# my_drawing = drawing(pts = 5, coords = [(10,10), (11,12), (12,14), (13,12), (14,10)] , lines = [(0,1), (1,2), (2,3), (1,3), (3,4)])
	
	# success = template_letter.check_drawing(my_drawing)
	# print(f'found : {success}')
	# time.sleep(5)
	
	# check a couple custom drawings pehle 

	# with plt.ion():


	# d = drawing((5,5))
	# # LATER - making lines between exisiting points?
	# # think abt choosing smart lines

	# my_drawing = drawing(pts = 1, coords = [(0,0)], lines = [])
	# my_drawing.show()
	
	# drawing_counter = 0
	# removal_freq = 2
	# while(True):
	# 	try:
	# 		drawing_counter += 1
	# 		old_pt = random.choice(list(range(my_drawing.pts)))
	# 		old_pt = my_drawing.coords[old_pt]
	# 		chosen_jump = random.choice(jumps)
	# 		dx, dy = chosen_jump
	# 		x, y = old_pt
	# 		potential_new = (x + dx, y + dy)
	# 		my_drawing.connect_new_pt(old_pt, potential_new) 
	# 		my_drawing.show()
	# 		# success = my_drawing.contains_this_letter(letter_j) # draw with different color?
	# 		success = template_letter.check_drawing(my_drawing) # draw with different color?
	# 		if success:
	# 			print("found")
	# 			time.sleep(20)
	# 			plt.savefig("junk/found.png")
	# 			break

	# 		# if drawing_counter % removal_freq == 0:
	# 		if my_drawing.pts > 7:
	# 			# removing one point at random
				
	# 			# remove the point with min connections
	# 			# connections = [0 for _ in range(my_drawing.pts)]
	# 			# for x,y in my_drawing.lines:
	# 			# 	connections[x] += 1
	# 			# 	connections[y] += 1
	# 			# to_remove = connections.index(min(connections))
				
	# 			# remove the point with min connections and has similar nbrs
	# 			connections = [[] for _ in range(my_drawing.pts)]
	# 			for x,y in my_drawing.lines:
	# 				connections[x].append(y)
	# 				connections[y].append(x)
	# 			scores = [sum(len(connections[a]) for a in connections[x]) for x in range(my_drawing.pts)]
	# 			to_remove = scores.index(min(scores))
				

	# 			cprint(f"removing pt {to_remove}", "cyan")
	# 			# time.sleep(0.1)
	# 			my_drawing.remove_pt(to_remove)
	# 			my_drawing.show()

	# 	except Exception as e:
	# 		print("Exception caught")
	# 		print(e)
	# 		print(e.__class__.__name__)
	# 		traceback.print_exc()
	# 		sys.exit()
