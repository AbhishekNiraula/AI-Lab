import math

# Depth for Starting Node, is_max is for Either Maximum/Minimum in that node 
def min_max(depth, index, is_max, score, max_depth):
    if depth == max_depth:
        return score[index]
    if is_max:
        best_value = -math.inf
        for i in range(2):
			# Index * 2 + I will return the next node to process
            value = min_max(depth + 1, index*2 + i, False, score, max_depth)
            best_value =  max(best_value, value)
        return best_value
    else:
        best_value = math.inf
        for i in range(2):
            value = min_max(depth + 1, index * 2 + i, True, score, max_depth)
            best_value = min(best_value, value)
        return best_value
        
score = [2, 3, 5, 9, 0, 1, 7, 5]

max_depth = int(math.log2(len(score)))

v = min_max(0, 0, True, score, max_depth)
print(v)