import numpy as np

def sigmoid(x):
    return 1/(1 + np.exp(-x))

class LogisticRegression:
    def __init__(self, lr = 0.01, n_iters = 1000):
        self.lr = lr
        self.n_iters = n_iters
        self.weights = None
        self.bias = None
        self.loss_history = []
    
    def fit(self, x, y):
        n_samples, n_features = x.shape
        self.weights = np.zeros(n_features)
        self.bias = 0
        for _ in range(self.n_iters):
            y_pred = np.dot(x, self.weights) + self.bias
            prediction = sigmoid(y_pred)
            
            dw = (1/n_samples) * np.dot(x.T, (prediction - y))
            db = (1/n_samples) * np.sum(prediction - y)
            
            self.weights -= self.lr * dw
            self.bias -= self.lr * db
            
            # Loss
            loss = - np.mean(y * np.log(prediction + 1e-15) + (1 -  y)*np.log(1 - prediction + 1e-15))
            self.loss_history.append(loss)
        
    
    def predict(self, x):
        pred = np.dot(x, self.weights) + self.bias
        predicted = sigmoid(pred)
        return predicted
    
    def prob(self, x):
        probability = self.predict(x)
        return np.where(probability >= 0.5, 1, 0)
    