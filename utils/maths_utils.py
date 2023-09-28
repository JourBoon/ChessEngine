import numpy as np

class MathsUtils:

    @staticmethod
    def dot(a, b):
        """
        Return the scalaire product of a and b.
        """
        return None
    
    @staticmethod
    def tanh(x):
        return np.tanh(x);

    @staticmethod
    def tanh_prime(x):
        return 1-np.tanh(x)**2;

    @staticmethod
    def mse(y_true, y_pred):
        return np.mean(np.power(y_true-y_pred, 2));

    @staticmethod
    def mse_prime(y_true, y_pred):
        return 2*(y_pred-y_true)/y_true.size;