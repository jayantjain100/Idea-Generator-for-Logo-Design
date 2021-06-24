from utils import *

letter_a = Letter(5, actual_letter = "a")
# letter_a.lines = [(0,1), (1,2), (2,3), (3,4), (1,3)]
letter_a.lines = [(0,1), (1,2), (2,3), (1,3), (3,4)]
# letter_a.add_line_interaction(1,3, foo = hinged_relative_line_angle, low = -120, high = -30)
# letter_a.add_line_interaction(3,1, foo = hinged_relative_line_angle, low = 30, high = 120)
# letter_a.add_line_interaction(3,4, foo = hinged_relative_line_angle, low = 60, high  = 150)
# letter_a.add_line_interaction(0,1, foo = hinged_relative_line_angle, low = 120, high = 180 )
letter_a.add_line_interaction(0,1, foo = hinged_relative_line_angle, exact = 180 ) #A's slant line should be straight - Rajas's suggestion
letter_a.add_line_interaction(1,2, foo = hinged_relative_line_angle, low = 10, high = 120)
# letter_a.add_line_interaction(2,4, foo = hinged_relative_line_angle, low = 120, high = 180 )
letter_a.add_line_interaction(2,4, foo = hinged_relative_line_angle, exact = 180) #A's slant line should be straight - Rajas's suggestion
letter_a.add_line_interaction(3, None,  foo = absolute_line_angle_with_x_axis, low = 0, high = 45) 
letter_a.add_pt_interaction(0,4, foo = pts_x_axis ,left = True, strict = True)
letter_a.add_pt_interaction(4,2, foo = pts_y_axis ,bottom = True, strict = True)
letter_a.add_pt_interaction(0,2, foo = pts_y_axis ,bottom = True, strict = True)
letter_a.add_pt_interaction(0,1, foo = pts_y_axis ,bottom = True, strict = True)
letter_a.add_pt_interaction(4,3, foo = pts_y_axis ,bottom = True, strict = True)
letter_a.add_pt_interaction(3,2, foo = pts_y_axis ,bottom = True, strict = True)
letter_a.add_pt_interaction(1,2, foo = pts_y_axis ,bottom = True, strict = True)

letter_a_minimal_1 = Letter(3, actual_letter = "a")
letter_a_minimal_1.lines = [(0,1), (1,2)]
letter_a_minimal_1.add_line_interaction(0,1, foo = hinged_relative_line_angle, low = 30, high = 120)
# letter_a_minimal_1.add_line_interaction(0,1, foo = line_length_ratio, exact = 1)
letter_a_minimal_1.add_pt_interaction(0,1,foo = pts_y_axis, bottom = True, strict = True)
letter_a_minimal_1.add_pt_interaction(2,1,foo = pts_y_axis, bottom = True, strict = True)
letter_a_minimal_1.add_pt_interaction(0,2,foo = pts_x_axis, left = True)
letter_a_minimal_1.add_pt_interaction(0,2,foo = pts_y_axis, exact = True)


letter_i = Letter(2, actual_letter = "i")
letter_i.lines = [(0,1)]
letter_i.add_line_interaction(0,None, foo = absolute_line_angle_with_x_axis, low = 60, high = 90)
letter_i.add_pt_interaction(0,1, foo = pts_y_axis, bottom = True, strict = True)

letter_m = Letter(5, actual_letter = "m")
letter_m.lines = [(0,1), (1,2), (2,3), (3,4)]
letter_m.add_line_interaction(0,None, foo=absolute_line_angle_with_x_axis,low=45,high=120)
letter_m.add_line_interaction(0,1,foo=hinged_relative_line_angle,low = 30,high = 135)
letter_m.add_pt_interaction(0,1,foo = pts_y_axis, bottom = True, strict = True)
letter_m.add_pt_interaction(2,1,foo = pts_y_axis, bottom = True, strict = True)
letter_m.add_pt_interaction(2,3,foo = pts_y_axis, bottom = True, strict = True)
letter_m.add_line_interaction(2,3,foo=hinged_relative_line_angle,low = 30,high = 135)
letter_m.add_pt_interaction(4,3,foo = pts_y_axis, bottom = True, strict = True)


letter_e = Letter(6, actual_letter = "e")
letter_e.lines = [(0,1), (1,2), (2,3), (1,4), (0,5)]
letter_e.add_line_interaction(0,1, foo = hinged_relative_line_angle, low = 120, high = 240 )
letter_e.add_line_interaction(2,3, foo = ambiguous_relative_line_angle, exact = 0)
letter_e.add_line_interaction(3,4, foo = ambiguous_relative_line_angle, exact = 0)
letter_e.add_pt_interaction(4,3, foo = pts_x_axis, left = True)
letter_e.add_pt_interaction(4,5, foo = pts_x_axis, left = True)
letter_e.add_pt_interaction(2,3, foo = pts_x_axis, left = True, strict = True)
letter_e.add_pt_interaction(1,4, foo = pts_x_axis, left = True, strict = True)
letter_e.add_pt_interaction(0,5, foo = pts_x_axis, left = True, strict = True)
letter_e.add_pt_interaction(0,1, foo = pts_y_axis, bottom = True, strict = True)
letter_e.add_pt_interaction(1,2, foo = pts_y_axis, bottom = True, strict = True)

letter_f = Letter(5, actual_letter = "f")
letter_f.lines = [(0,1), (1,2), (2,3), (1,4)]
letter_f.add_line_interaction(0,1, foo = hinged_relative_line_angle, low = 150, high = 210 )
letter_f.add_line_interaction(2,3, foo = ambiguous_relative_line_angle, exact = 0)
letter_f.add_pt_interaction(4,3, foo = pts_x_axis, left = True)
letter_f.add_pt_interaction(2,3, foo = pts_x_axis, left = True, strict = True)
letter_f.add_pt_interaction(1,4, foo = pts_x_axis, left = True, strict = True)
letter_f.add_pt_interaction(0,1, foo = pts_y_axis, bottom = True, strict = True)
letter_f.add_pt_interaction(1,2, foo = pts_y_axis, bottom = True, strict = True)
letter_f.add_pt_interaction(0,4, foo = pts_y_axis, bottom = True, strict = True)



# letter_e.add_line_interaction()
letter_s = Letter(4, actual_letter = "s")
letter_s.lines = [(0,1), (1,2), (2,3)]
letter_s.add_pt_interaction(0,2,foo = pts_y_axis, bottom = True)
letter_s.add_pt_interaction(1,3,foo = pts_y_axis, bottom = True)
letter_s.add_pt_interaction(0,1,foo = pts_x_axis, left = True, strict = True)
letter_s.add_pt_interaction(2,3,foo = pts_x_axis, left = True, strict = True)
# reconsider?
letter_s.add_pt_interaction(2,1,foo = pts_x_axis, left = True, strict = True)
letter_s.add_line_interaction(1,2, foo = hinged_relative_line_angle, low = 30, high = 90)
letter_s.add_line_interaction(1,0, foo = hinged_relative_line_angle, low = 30, high = 90)


letter_h = Letter(6, actual_letter = "h")
letter_h.lines = [(0,1), (1,2), (1,4),(4,3),(4,5)]
letter_h.add_line_interaction(0,1, foo = hinged_relative_line_angle, exact = 180)
letter_h.add_line_interaction(3,4, foo = hinged_relative_line_angle, exact = 180)
letter_h.add_pt_interaction(2,5, foo = pts_x_axis, left = True, strict = True)
letter_h.add_pt_interaction(0,3, foo = pts_x_axis, left = True, strict = True)
letter_h.add_pt_interaction(1,4, foo = pts_x_axis, left = True, strict = True)
letter_h.add_pt_interaction(0,1, foo = pts_y_axis, bottom = True, strict = True)
letter_h.add_pt_interaction(1,2, foo = pts_y_axis, bottom = True, strict = True)
letter_h.add_pt_interaction(3,4, foo = pts_y_axis, bottom = True, strict = True)
letter_h.add_pt_interaction(4,5, foo = pts_y_axis, bottom = True, strict = True)
letter_h.add_line_interaction(2,1, foo = hinged_relative_line_angle, low = 30, high = 150)
letter_h.add_line_interaction(0,2, foo = hinged_relative_line_angle, low = 30, high = 150)
letter_h.add_line_interaction(2,3, foo = hinged_relative_line_angle, low = 30, high = 150)
letter_h.add_line_interaction(4,2, foo = hinged_relative_line_angle, low = 30, high = 150)

letter_d = Letter(3, actual_letter = "d")
letter_d.lines = [(0,1), (1,2),(2,0)]
letter_d.add_pt_interaction(0,2,foo = pts_x_axis, left = True, strict = True)
letter_d.add_pt_interaction(1,2,foo = pts_x_axis, left = True, strict = True)
letter_d.add_pt_interaction(0,1, foo = pts_y_axis, bottom = True, strict = True)
letter_d.add_pt_interaction(0,2, foo = pts_y_axis, bottom = True, strict = True)
letter_d.add_line_interaction(0, None, foo = absolute_line_angle_with_x_axis, low = 45, high = 135)





letter_v = Letter(3, actual_letter = "v")
letter_v.lines = [(0,1),(1,2)]
letter_v.add_line_interaction(1,0, foo = hinged_relative_line_angle, low = 30, high = 120)
letter_v.add_pt_interaction(0,2,foo = pts_x_axis, left = True, strict = True)
letter_v.add_pt_interaction(1,0,foo = pts_y_axis, bottom = True, strict = True)
letter_v.add_pt_interaction(1,2,foo = pts_y_axis, bottom = True, strict = True)

# family of four letters - p,r,k,b
letter_p = Letter(4, actual_letter = "p")
letter_p.lines = [(0,1), (1,2), (2,3), (3,1)]
letter_p.add_pt_interaction(0,1,foo = pts_y_axis, bottom = True, strict = True)
letter_p.add_pt_interaction(1,2,foo = pts_y_axis, bottom = True, strict = True)
letter_p.add_pt_interaction(2,3,foo = pts_x_axis, left = True, strict = True)
letter_p.add_line_interaction(0,1,foo = hinged_relative_line_angle, exact = 180)
letter_p.add_pt_interaction(1,3,foo = pts_y_axis, bottom = True)


letter_r = Letter(5, actual_letter = 'r')
letter_r.lines = [(0,1), (1,2), (2,3), (3,1), (1,4)]
letter_r.add_pt_interaction(0,1,foo = pts_y_axis, bottom = True, strict = True)
letter_r.add_pt_interaction(1,2,foo = pts_y_axis, bottom = True, strict = True)
letter_r.add_pt_interaction(2,3,foo = pts_x_axis, left = True, strict = True)
letter_r.add_line_interaction(0,1,foo = hinged_relative_line_angle, exact = 180)
letter_r.add_pt_interaction(1,3,foo = pts_y_axis, bottom = True)
letter_r.add_pt_interaction(0,4,foo = pts_x_axis, left = True, strict = True)
letter_r.add_pt_interaction(4,1,foo = pts_y_axis, bottom = True, strict = True)



letter_k = Letter(5, actual_letter = 'k')
letter_k.lines = [(0,1), (1,2), (3,1), (1,4)]
letter_k.add_pt_interaction(0,1,foo = pts_y_axis, bottom = True, strict = True)
letter_k.add_pt_interaction(1,2,foo = pts_y_axis, bottom = True, strict = True)
letter_k.add_pt_interaction(2,3,foo = pts_x_axis, left = True, strict = True)
letter_k.add_line_interaction(0,1,foo = hinged_relative_line_angle, exact = 180)
letter_k.add_pt_interaction(1,3,foo = pts_y_axis, bottom = True)
letter_k.add_pt_interaction(0,4,foo = pts_x_axis, left = True, strict = True)
letter_k.add_pt_interaction(4,1,foo = pts_y_axis, bottom = True, strict = True)


letter_b = Letter(5, actual_letter = 'b')
letter_b.lines = [(0,1), (1,2), (2,3), (3,1), (1,4), (0,4)]
letter_b.add_pt_interaction(0,1,foo = pts_y_axis, bottom = True, strict = True)
letter_b.add_pt_interaction(1,2,foo = pts_y_axis, bottom = True, strict = True)
# letter_b.add_pt_interaction(2,3,foo = pts_x_axis, left = True, strict = True)
letter_b.add_pt_interaction(2,3,foo = pts_x_axis, left = True)
letter_b.add_line_interaction(0,1,foo = hinged_relative_line_angle, exact = 180)
letter_b.add_pt_interaction(1,3,foo = pts_y_axis, bottom = True)
letter_b.add_pt_interaction(0,4,foo = pts_x_axis, left = True, strict = True)
letter_b.add_pt_interaction(4,1,foo = pts_y_axis, bottom = True)
letter_b.add_line_interaction(4,5,foo = hinged_relative_line_angle, low = 10, high = 120)
letter_b.add_line_interaction(2,3,foo = hinged_relative_line_angle, low = 10, high = 120)

# Realisation: need one interaction with xaxis etc, otherwise you can get a rotated version
# remember that the absolute_angle_with_xaxis is on the undirected line seg 
letter_j = Letter(5, actual_letter = "j")
letter_j.lines = [(0,1), (1,2), (2,3), (2,4)]
letter_j.add_line_interaction(1,0, foo = hinged_relative_line_angle, low = 20, high = 135 )
letter_j.add_line_interaction(2,1, foo = hinged_relative_line_angle, low = 45, high = 135 )
letter_j.add_line_interaction(2,3, foo = hinged_relative_line_angle, exact = 180 )
letter_j.add_pt_interaction(0,3, foo = pts_y_axis, bottom = True, strict = True)
letter_j.add_pt_interaction(1,3, foo = pts_y_axis, bottom = True, strict = True) #J's top should touch the bottom
letter_j.add_pt_interaction(1,4, foo = pts_y_axis, bottom = True, strict = True) #J's top should touch the bottom
letter_j.add_pt_interaction(1,2, foo = pts_y_axis, bottom = True)
letter_j.add_pt_interaction(0,2, foo = pts_y_axis, bottom = True)
letter_j.add_pt_interaction(1,3, foo = pts_y_axis, bottom = True)
letter_j.add_pt_interaction(0,2, foo = pts_x_axis, left = True, strict = True)
letter_j.add_line_interaction(1, None,  foo = absolute_line_angle_with_x_axis, low = 60, high = 120) 

letter_j_minimal_1 = Letter(3, actual_letter = "j")
letter_j_minimal_1.lines = [(0,1), (1,2)]
letter_j_minimal_1.add_line_interaction(1,0,foo = hinged_relative_line_angle, low = 30, high = 135)
letter_j_minimal_1.add_line_interaction(1,None,foo = absolute_line_angle_with_x_axis, low = 45, high = 135)
letter_j_minimal_1.add_pt_interaction(1,2, foo = pts_y_axis, bottom = True)
letter_j_minimal_1.add_line_interaction(0,1, foo = line_length_ratio, low = 0.3, high = 1)
letter_j_minimal_1.add_pt_interaction(0,2, foo = pts_y_axis, bottom = True, strict = True)


letter_n = Letter(4, actual_letter = "n")
letter_n.lines = [(0,1), (1,2), (2,3)]
letter_n.add_line_interaction(0, None, foo = absolute_line_angle_with_x_axis, low = 45, high = 135)
letter_n.add_line_interaction(1, None, foo = absolute_line_angle_with_x_axis, low = 45, high = 135)
letter_n.add_line_interaction(2, None, foo = absolute_line_angle_with_x_axis, low = 45, high = 135)
letter_n.add_line_interaction(0, 1, foo = hinged_relative_line_angle, low = 30, high = 120)
letter_n.add_line_interaction(2, 1, foo = hinged_relative_line_angle, low = 30, high = 120)
letter_n.add_pt_interaction(0,1, foo = pts_y_axis, bottom = True)
letter_n.add_pt_interaction(1,2, foo = pts_x_axis, left = True)
letter_n.add_pt_interaction(2,1, foo = pts_y_axis, bottom = True, strict = True)
letter_n.add_pt_interaction(2,3, foo = pts_y_axis, bottom = True)
letter_n.add_pt_interaction(0,3, foo = pts_y_axis, bottom = True, strict = True) # start of N below end of N, otherwise looks like a z


letter_t_minimal_1 = Letter(3, actual_letter = "t")
letter_t_minimal_1.lines = [(0,1), (1,2)]
letter_t_minimal_1.add_line_interaction(0,1,foo = hinged_relative_line_angle, low = 30, high = 150)
letter_t_minimal_1.add_pt_interaction(0,1, foo = pts_y_axis, bottom = True, strict = True)
letter_t_minimal_1.add_pt_interaction(1,2, foo = pts_x_axis, left = True, strict = True)
letter_t_minimal_1.add_pt_interaction(0,2, foo = pts_y_axis, bottom = True, strict = True)
letter_t_minimal_1.add_line_interaction(0, None, foo = absolute_line_angle_with_x_axis, low = 45, high = 135)
#rightward hi jayega yeh
letter_t_minimal_1.add_line_interaction(1, None, foo = absolute_line_angle_with_x_axis, low = 0, high = 45 )

letter_t = Letter(4, actual_letter = "t")
letter_t.lines = [(0,1), (1,2), (1,3)]
letter_t.add_line_interaction(0,1,foo = hinged_relative_line_angle, low = 30, high = 150)
letter_t.add_line_interaction(2,1,foo = hinged_relative_line_angle, exact = 180)
letter_t.add_pt_interaction(0,1, foo = pts_y_axis, bottom = True, strict = True)
letter_t.add_pt_interaction(0,2, foo = pts_y_axis, bottom = True, strict = True)
letter_t.add_pt_interaction(0,3, foo = pts_y_axis, bottom = True, strict = True)
letter_t.add_pt_interaction(1,2, foo = pts_x_axis, left = True, strict = True)
letter_t.add_pt_interaction(3,1, foo = pts_x_axis, left = True, strict = True)
letter_t.add_line_interaction(0, None, foo = absolute_line_angle_with_x_axis, low = 45, high = 135)
#rightward hi jayega yeh
# letter_t.add_line_interaction(1, None, foo = absolute_line_angle_with_x_axis, low = 0, high = 45 )


letter_y = Letter(4, actual_letter = "y")
letter_y.lines = [(0,1), (1,2), (1,3)]
letter_y.add_line_interaction(1, None, foo=absolute_line_angle_with_x_axis, low = 45, high = 90)
letter_y.add_line_interaction(2, 0, foo=hinged_relative_line_angle, low = 30, high = 120)
letter_y.add_pt_interaction(1,0, foo = pts_y_axis, bottom = True, strict = True)
# letter_y.add_pt_interaction(1,0, foo = pts_y_axis, bottom = True)
letter_y.add_pt_interaction(1,3, foo = pts_y_axis, bottom = True, strict = True)
letter_y.add_pt_interaction(2,1, foo = pts_y_axis, bottom = True, strict = True)	
letter_y.add_line_interaction(0, 1, foo=hinged_relative_line_angle, low = 90, high = 150)