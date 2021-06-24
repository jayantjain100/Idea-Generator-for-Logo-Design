# args.py

from argparse import ArgumentParser

def make_args():
	parser = ArgumentParser()
	parser.add_argument("-display", action = "store_true", dest = "display", help = "pass this argument to display the working")
	parser.add_argument("-upper_limit", type = int, dest = "upper_limit", help = "upper limit on the number of points in the final drawing")
	parser.add_argument("-connect_collinear", action = "store_true", dest = "connect_collinear", help = "connects collinear line segments to create new line segments increasing the degrees of freedom")
	parser.add_argument("-new_angle", action = "store_true", dest = "new_angle", help = "explores additional angles, creating more complex designs")
	parser.add_argument("-mega_jump", action = "store_true", dest = "mega_jump", help = "allows larger jump sizes, creating more complex designs")
	parser.set_defaults(display = False)
	parser.set_defaults(upper_limit = 10)
	parser.set_defaults(connect_collinear = False)
	parser.set_defaults(new_angle = False)
	parser.set_defaults(mega_jump = False)
	args = parser.parse_args()
	return args