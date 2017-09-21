#import FILE WITH NERON FUNCTS

class FPS_judge():

    def __init__(self, training_data, answers):

        self.data = training_data
        self.ans = answers
        self.nerons = []

    # sigmoid function
    def nonlin(x,deriv=False):
        if(deriv == True):
            return x*(1-x)
        return 1/(1+np.exp(-x))
