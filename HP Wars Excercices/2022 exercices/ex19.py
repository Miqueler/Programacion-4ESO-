import math

distance=int(input())
angle=int(input())
rad_angle=(angle*math.pi)/180

min_distance=distance-3+(0.0427/2)
max_distance=distance+3-(0.0427/2)
min_time=math.sqrt((2*min_distance*math.sin(rad_angle))/(9.8*math.cos(rad_angle)))
max_time=math.sqrt((2*max_distance*math.sin(rad_angle))/(9.8*math.cos(rad_angle)))
min_speed=min_distance/(math.cos(rad_angle)*min_time)
max_speed=max_distance/(math.cos(rad_angle)*max_time)
print(f"The maximum speed is: {round(max_speed,2)} m/s.")
print(f"The minimum speed is: {round(min_speed,2)} m/s.")