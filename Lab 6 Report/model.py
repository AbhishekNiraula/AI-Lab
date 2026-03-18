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


# Logic: XOR = (x1 OR x2) AND (NOT(x1 AND x2))
# Simplified Logic: XOR = (x1 OR x2) AND (x1 NAND x2)
class XORPerceptron:
    def __init__(self, lr = 0.01, epoch = 100):
        self.lr = lr
        self.epoch = epoch
        self.perceptron_nand = Perceptron(lr = lr, epoch = epoch)
        self.perceptron_or = Perceptron(lr = lr, epoch = epoch)\
        
        # Perceptron_and is special : It is for the hidden layer. It performs and to the output of the hidden layer i.e perceptron_nand and perceptron_or
        self.perceptron_and = Perceptron(lr = lr, epoch = epoch)
    
    def fit(self, x, y):
        # Resultand array of or and nand operation
        y_or = np.array([0, 1, 1, 1])
        y_nand = np.array([1, 1, 1, 0])
        self.perceptron_nand.fit(x, y_or)
        self.perceptron_or.fit(x, y_nand)
        # Hidden Layer
        hidden_outut = []
        for i in range(len(x)):
            
            # Z1 and Z2 are the perceptron output logic before passing it to the step function i.e z = w1x1 + w2x2 + b
            z1 = np.dot(x[i], self.perceptron_nand.weight) + self.perceptron_nand.bias
            z2 = np.dot(x[i], self.perceptron_or.weight) + self.perceptron_or.bias
            
            out1 = self.perceptron_nand.step_function(z1)
            out2 = self.perceptron_or.step_function(z2)
            
            # Input to the third perceptron layer is the outputs of NAND and OR gates.
            hidden_outut.append([out1, out2])
        
        hidden_outut = np.array(hidden_outut)
        self.perceptron_and.fit(hidden_outut, y)
        
    # Same prediction logic as single Perceptron
    def predict(self, x):
        prediction = []
        for sample in x:
            z1 = np.dot(sample, self.perceptron_nand.weight) + self.perceptron_nand.bias
            out1 = self.perceptron_nand.step_function(z1)
            
            z2 = np.dot(sample, self.perceptron_or.weight) + self.perceptron_or.bias
            out2 = self.perceptron_or.step_function(z2)
            
            hidden = np.array([out1, out2])
            z3 = np.dot(hidden, self.perceptron_and.weight) + self.perceptron_and.bias
            y_pred = self.perceptron_and.step_function(z3)
            
            prediction.append(y_pred)
        
        return prediction