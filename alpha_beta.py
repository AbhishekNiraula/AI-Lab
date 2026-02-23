import math

# Depth for Starting Node, is_max is for Either Maximum/Minimum in that node 
def alpha_beta(depth, index, is_max, score, max_depth, alpha, beta):
    if depth == max_depth:
        return score[index]
    if is_max:
        best_value = -math.inf
        for i in range(2):
			# Index * 2 + I will return the next node to process
            value = alpha_beta(depth + 1, index*2 + i, False, score, max_depth, alpha, beta)
            best_value =  max(best_value, value)
            alpha = max(alpha, best_value)
            # Prune the node that makes no contributions to final result.
            if alpha >= beta:
                print(f"Node Pruned")
                break
        return best_value
    else:
        best_value = math.inf
        for i in range(2):
            value = alpha_beta(depth + 1, index * 2 + i, True, score, max_depth, alpha, beta)
            best_value = min(best_value, value)
            beta = min(beta, best_value)
            if alpha >= beta:
                print("Node Pruned")
                break
        return best_value
        
score = [2, 3, 5, 9, 0, 1, 7, 5]

max_depth = int(math.log2(len(score)))

v = alpha_beta(0, 0, True, score, max_depth, alpha = -math.inf, beta = math.inf)
print(v)