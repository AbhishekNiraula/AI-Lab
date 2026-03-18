import numpy as np

class DecisionTreeID3:
    def __init__(self):
        self.tree = None
        
    def entropy(self, y):
        classes, values = np.unique(y, return_counts = True)
        entropy = 0
        for count in values:
            p = count / len(y)
            entropy = entropy - p * np.log2(p+1e-25)
        return entropy
    
    def informationgain(self, x, y, feature):
        totalEntropy = self.entropy(y)
        classes, count = np.unique(x[feature], return_counts = True)
        weightedEntropy = 0
        for v, c in zip(classes, count):
             subset_y = y[x[feature] == v]
             weightedEntropy += (c / len(y)) * self.entropy(subset_y)
        return totalEntropy - weightedEntropy
    
    def build_tree(self, x, y, features):
        if len(np.unique(y)) == 1:
            return y.iloc[0]
        
        if len(features) == 0:
            return y.mode()[0]
        
        gains = [self.informationgain(x, y, f) for f in features]
        best_features = features[np.argmax(gains)]
        tree = {
			best_features:{}
		}
        for v in np.unique(x[best_features]):
            subset_x = x[x[best_features] == v]
            subset_y = y[x[best_features] == v]
            
            remaining_features = []
            for f in features:
                if f!= best_features:
                    remaining_features.append(f)
            subtree = self.build_tree(subset_x.drop(columns = [best_features]), subset_y, remaining_features)
            
            tree[best_features][v] = subtree
        return tree
    
    def fit(self, x, y):
        features = x.columns
        self.tree = self.build_tree(x, y, features)
    
    def predict_single(self, x, tree):
        if not isinstance(tree, dict):
            return tree
        
        feature = next(iter(tree))
        subtree = tree[feature]
        feature_value = x[feature]
        
        if feature_value in subtree:
            return self.predict_single(x, subtree[feature_value])
        else:
            return None
    def predict(self, x):
        return x.apply(lambda row: self.predict_single(row, self.tree), axis = 1)