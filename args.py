# args.py

from argparse import ArgumentParser

def make_args():
	parser = ArgumentParser()
	parser.add_argument("-display", action = "store_true", dest = "display", help = "pass this argument to display the working")
	parser.add_argument("-upper_limit", type = int, dest = "upper_limit", help = "upper limit on the number of points in the final drawing")
	parser.add_argument("-connect_collinear", action = "store_true", dest = "connect_collinear", help = "connects collinear line segments to create new line segments increasing the degrees of freedom")
	parser.add_argument("-new_angle", action = "store_true", dest = "new_angle", help = "explores additional angles, creating more complex designs")
	parser.add_argument("-mega_jump", action = "store_true", dest = "mega_jump", help = "allows larger jump sizes, creating more complex designs")
	parser.add_argument("-name", type = str, dest = "name", help = "name of the person/thing you want to create the design for")
	parser.add_argument("-delta_step", action = "store_true", dest = "delta_step", help = "whether or not to choose the step smartly (improves iter quality, lowers speed)")
	parser.add_argument("-prob_connect_old_pts", type = float, dest = "prob_connect_old_pts", help = "Prob of making a connection between existing points in each iteration")
	
	parser.set_defaults(display = False)
	parser.set_defaults(upper_limit = 10)
	parser.set_defaults(connect_collinear = False)
	parser.set_defaults(new_angle = False)
	parser.set_defaults(mega_jump = False)
	parser.set_defaults(name = "jayant")
	parser.set_defaults(delta_step = False)
	parser.set_defaults(prob_connect_old_pts = 0.0)
	args = parser.parse_args()
	return args