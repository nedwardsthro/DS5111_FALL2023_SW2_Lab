'''
This is my docstring. This class is used to be in a test to see if the linting works. 
'''
class Perceptron():
    '''
    This is my docstring. This class is used to be in a test to see if the linting works. 
    '''
    def train(self, inputs, labels):
        '''
        This module trains the model. It requires two inputs to the model:
            inputs: independent variable to train the model
            labels: dependent variable that is the outcome of the model
        '''
        dummied_inputs = [xer + [-1] for xer in inputs]
        self._weights = [0.2] * len(dummied_inputs[0])
        for _ in range(5000):
            for train_input, label in zip(dummied_inputs, labels):
                label_delta = label - self.predict(train_input)
                for index, xer in enumerate(train_input):
                    self._weights[index] += .1 * xer * label_delta
    def predict(self, predict_input):
        '''
        This model predicts using the model created with train.
        The only input is the data used to predict the label.
        '''
        if len(predict_input) == 0:
            return None
        predict_input = predict_input + [-1]
        #pylint: disable = R1728
        return int(0 < sum([x[0]*x[1] for x in zip(self._weights, predict_input)]))
        