import numpy as np

class Perceptron:
    
    def __init__(self, lr = 0.01, epoch = 100, weight = None, bias = None):
        self.lr = lr
        self.epoch = epoch
        self.bias = bias
        self.weight = weight
        
    def step_function(self, z):
        if z >= 0:
            return 1
        else:
            return 0
    
    def fit(self, x, y):
        n_sample, n_features = x.shape
        self.weight = np.zeros(n_features)
        self.bias = 0
        
        for e in range(self.epoch):
            for i in range(n_sample):
                z = np.dot(x[i], self.weight) + self.bias
                y_pred = self.step_function(z)
                error = y[i] - y_pred
                self.weight += self.lr * error * x[i]
                self.bias += self.lr * error
                
    def predict(self, x):
        prediction = []
        for sample in x:
            z = np.dot(sample, self.weight) + self.bias
            y_pred = self.step_function(z)
            prediction.append(y_pred)
        return prediction