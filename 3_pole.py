size_of_pole=100
left_cockroach_speed=1
right_cockroach_speed=2

#left cockroach movement
time_for_left_cockroach= size_of_pole / left_cockroach_speed    #time=distance/speed
extra_moves_backword_left=10*2                                  #extra move due to backword movement
total_time_for_left_cockroach = time_for_left_cockroach + extra_moves_backword_left

#right cockroach movement
time_for_right_cockroach= size_of_pole / right_cockroach_speed            #time=distance/speed
extra_moves_backword_right=20*1                                           #extra move due to backword movement
total_time_for_right_cockroach = time_for_right_cockroach + extra_moves_backword_right

print("total_time_for_left_cockroach for pass rod in seconds:",total_time_for_left_cockroach)
print("total_time_for_right_cockroach for pass rod in seconds:",total_time_for_right_cockroach)

total_speed_for_left_cockroach= size_of_pole / total_time_for_left_cockroach       #speed=distance/time
total_speed_for_right_cockroach= size_of_pole / total_time_for_right_cockroach

time_after_both_cockroach_meet= size_of_pole/ (total_speed_for_left_cockroach+total_speed_for_right_cockroach)
print("time_after_both_cockroach_meet in seconds :",time_after_both_cockroach_meet)

distance_covered_by_left_cockroach_meet=(total_speed_for_left_cockroach)*time_after_both_cockroach_meet
print("distance coverd by left side cockroach for meet in meter is :",distance_covered_by_left_cockroach_meet)
distance_covered_by_right_cockroach_meet=(total_speed_for_right_cockroach)*time_after_both_cockroach_meet
print("distance coverd by right side cockroach for meet in meter is :",distance_covered_by_right_cockroach_meet)
