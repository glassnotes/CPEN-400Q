import pennylane as qml
from pennylane import numpy as np
import matplotlib.pyplot as plt

def plot_data(data, labels):
    """Plot the data and colour by class.
    
    Args:
        data (array[float]): Input data. A list with shape N x 2
            representing points on a 2D plane.
        labels (array[int]): Integers identifying the class/label of 
            each data point.
    """
    plt.scatter(data[:, 0], data[:, 1], c=labels)


def make_predictions(data, model, weights):
    """Predict the labels of all points in a data set for a given model.
    
    Args:
        data (array[float]): Input data. A list with shape N x 2
            representing points on a 2D plane.
        model (qml.QNode): A QNode whose output expectation value will be
            used to make predictions of the labels of data.
        weights (array[float]): The trainable model parameters for the QNode. 
            
    Returns:
        array[int]: The array of predictions for each data point made by 
        the model QNode. 
    """
    preds = []
    
    for idx in range(len(data)):
        estimated_expval = model(data[idx], weights)
        
        if estimated_expval > 0:
            preds.append(1)
        else:
            preds.append(-1)
            
    return preds


def compute_accuracy(predictions, true_labels):
    """Compute the accuracy of our predictions.
    
    Args:
        predictions (array[int]): Predicted values to 
        true_labels (array[int]): Integers identifying the class/label of 
            each data point.
    
    Returns:
        float: Accuracy of the predictions, returned as a percentage.
    """    
    n_samples = len(predictions)
    
    return np.sum(
        [predictions[x] == true_labels[x] for x in range(n_samples)
    ]) / n_samples


def make_loss_function(data, labels, model):

    def loss(weights):
        loss_sum = 0.0

        for idx in range(len(data)):
            point = data[idx]
            true_expval = labels[idx]

            estimated_expval = model(point, weights)
            loss_sum += (estimated_expval - true_expval) ** 2

        return loss_sum / len(data)
    
    return loss

