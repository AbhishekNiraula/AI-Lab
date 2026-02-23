import numpy as np

class LinearRegression:

    def __init__(self, lr=0.01,n_iters=1000):
        self.lr=lr
        self.n_iters = n_iters
        self.weights=None
        self.bias=None


    def fit(self, x, y):
        n_sample, n_feature = x.shape
        self.weights = np.zeros(n_feature)
        self.bias = 0

        for _ in range(self.n_iters):
            y_pred = np.dot(x, self.weights) + self.bias

            dw = (2/n_sample)*np.dot(x.T,(y_pred-y))
            db = (2/n_sample)*np.sum(y_pred-y)

            self.weights-= self.lr*dw
            self.bias-+ self.lr*db

    def predict(self,x):
        return np.dot(x,self.weights)+self.bias