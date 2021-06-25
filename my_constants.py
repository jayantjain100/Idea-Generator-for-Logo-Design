from args import *
args = make_args()

abs_delta = 1
jumps = [(x,y) for x in range(-abs_delta, abs_delta + 1) for y in range(-abs_delta, abs_delta + 1)]


NEW_ANGLES = args.new_angle
if NEW_ANGLES:
	# jumps = [(2,1), (1,2)]
	jumps = [(2,1), (1,2), (0,2)]
	# jumps = [(2,0), (2,1), (1,2)]
	# jumps = [(2,0), (2,1), (1,2), (0,2)]
	# jumps = [(2,0), (2,1), (1,2), (0,2), (2,2)]
	new_jumps = set()
	for x,y in jumps:
		for mult1 in (-1,1):
			for mult2 in (-1,1):
				new_jumps.add((mult1*x, mult2*y))
	jumps = list(new_jumps)
	

MEGAJUMP = args.mega_jump
if MEGAJUMP:
	new_jumps = set()
	for x,y in jumps:
		tup = (2*x, 2*y)
		new_jumps.add(tup)
	new_jumps.update(set(jumps))
	jumps = list(new_jumps)

assert not(MEGAJUMP and NEW_ANGLES), "not allowed"

if (0,0) in jumps:
	jumps.remove((0,0))

EPSILON = 0.01
all_colors = ["blue", "red", "cyan", "magenta", "yellow", "orange", "lawngreen", "pink"]
FIGURE_COLUMNS = 3

# PROB_GREEDY_REMOVAL = 0.8
PROB_GREEDY_REMOVAL = 1

DRAWING_NUM_POINTS_UPPER_LIMIT = args.upper_limit
DRAWING_NUM_POINTS_LOWER_LIMIT = 5

PROB_CONNECT_OLD_POINTS = args.prob_connect_old_pts
# PROB_CONNECT_OLD_POINTS = 0.02
# PROB_CONNECT_OLD_POINTS = 0.1

CONNECT_COLLINEAR_DIRECTLY = args.connect_collinear
# DISPLAY_WORKING = False
DISPLAY_WORKING = args.display

# LATER
# can we use opencv to go through an image/pdf file and look at handdrawn letters and add these interactions on its own

