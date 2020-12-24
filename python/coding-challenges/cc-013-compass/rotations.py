def final_direction(startpoint, rotations):
    directions = ["N", "E", "S", "W"]     
    counter = 0
    for i in rotations: 
        if i == "R":
            counter += 1
        else:
            counter -= 1
    index_number = (counter + directions.index(startpoint)) % 4
    endpoint = directions[index_number]
    return endpoint

# def final_direction(i, t):
#     	l = {"N": "W", "W": "S", "S": "E", "E":"N"}
# 	r = {"N": "E", "E": "S", "S": "W", "W":"N"}
# 	for j in t:
# 		if j == "L":
# 			i = l[i]
# 		else:
# 			i = r[i]
# 	return i