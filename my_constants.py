
abs_delta = 1
jumps = [(x,y) for x in range(-abs_delta, abs_delta + 1) for y in range(-abs_delta, abs_delta + 1)]

MEGAJUMP = True
if MEGAJUMP:
	new_jumps = set()
	for x,y in jumps:
		tup = (2*x, 2*y)
		new_jumps.add(tup)
	new_jumps.update(set(jumps))
	jumps = list(new_jumps)

jumps.remove((0,0))
EPSILON = 0.01
all_colors = ["blue", "red", "cyan", "magenta", "yellow", "orange", "lawngreen", "pink"]
FIGURE_COLUMNS = 3

# PROB_GREEDY_REMOVAL = 0.8
PROB_GREEDY_REMOVAL = 1

DRAWING_NUM_POINTS_UPPER_LIMIT = 12
DRAWING_NUM_POINTS_LOWER_LIMIT = 5

PROB_CONNECT_OLD_POINTS = 0
# PROB_CONNECT_OLD_POINTS = 0.02
# PROB_CONNECT_OLD_POINTS = 0.1

CONNECT_COLLINEAR_DIRECTLY = False
# DISPLAY_WORKING = False
DISPLAY_WORKING = False

# LATER
# can we use opencv to go through an image/pdf file and look at handdrawn letters and add these interactions on its own

