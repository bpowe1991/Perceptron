""""
Programmer: Briton A. Powe          Program Homework Assignment #5
Date: 5/2/18                       Class: Introduction to A.I.
Version: 1.3.1
File: main.py
------------------------------------------------------------------------
Program Description:
Program to construct a perceptron on training data and classify on testing data.
***This program uses Python 3.6.4***

References:
Example 1 to illustrate process - https://blog.dbrgn.ch/2013/3/26/perceptrons-in-python/
Example 2 to illustrate process - https://machinelearningmastery.com/implement-perceptron-algorithm-scratch-python/
"""

import random

#Function to get training data
def get_training_data():
    training_data_set = []
    training_data = None

    #Loop to get input file
    while training_data is None:
        try:
            training_data = input("Please enter the name of the training data file: ")
            
            #Opening input file called
            input_training_data = open(training_data, 'r')
        except OSError:
            print('\nError accessing file. Enter the correct filename with extension.\n\n')
            training_data = None

    input_training_data.__next__()

    #Creating input training data and parsing
    for line in input_training_data:
        line = line.rstrip('\n')
        training_data_set.append(line.split(" "))

    #Change all values to integers
    for index_1 in range(len(training_data_set)):
        for index_2 in range(len(training_data_set[0])):
            training_data_set[index_1][index_2] = int(training_data_set[index_1][index_2])
    
    #Output the training data
    print("Training Data List:")
    for each in training_data_set:
        print(each)
    print("\n")

    #Close training data file
    input_training_data.close()

    return training_data_set

#Function to set intial weights
def set_intial_weights(num_variables):
    weights = []

    #Generating random weights between 0 and 1
    for _ in range(num_variables):
        weights.append(random.uniform(0,1))
    
    return weights

#Fuction to adjust weights
def adjust_weights(row, weights, actual_output, learning_rate):
    for index in range(len(row)-1):
        weights[index] = weights[index]+(learning_rate*(row[-1]-actual_output))*row[index]
    
    return weights

#Function to sum inputs multiplied by respective weights
def sum_inputs(row, weights):
    total_sum = 0.0

    #Summing the inputs multiplied by weights
    for index in range(len(row)-1):
        total_sum += row[index]*weights[index]
    
    return total_sum

#Threshold function
def determine_output(variable_sum):
    if variable_sum > 0:
        return 1
    else:
        return -1

#Main function for training the perceptron
def train_perceptron(training_set, weights, learning_rate, iterations):
    
    error_rate = error_counter = 0
    
    #Training loop for perceptron
    print("Training Perceptron . . .\n")
    for iteration in range(iterations):
        error = 0
        
        #Training on each row
        for row in training_set:
            row_sum = sum_inputs(row, weights)
            output = determine_output(row_sum)
            if output != row[-1]:
                error += 1
            weights = adjust_weights(row, weights, output, learning_rate)
        error_rate = error/len(training_set)
        print("Training Iteration -", iteration+1)
        print("Error Rate:", error_rate, "\n")

        #If the error rate reaches 0 continously, break when count reaches 10
        if error_rate == 0.0:
            error_counter += 1
            if error_counter == 10:
                break
        else:
            error_counter = 0.0

    return weights

#Function to get testing data
def get_testing_data():
    testing_data_set = []
    testing_data = None

    #Loop to get input file
    while testing_data is None:
        try:
            testing_data = input("Please enter the name of the testing data file: ")
            
            #Opening input file called
            input_testing_data = open(testing_data, 'r')
        except OSError:
            print('\nError accessing file. Enter the correct filename with extension.\n\n')
            testing_data = None

    input_testing_data.__next__()

    #Creating input data list and parsing
    for line in input_testing_data:
        line = line.rstrip('\n')
        testing_data_set.append(line.split(" "))

    #Change all values to integers
    for index_1 in range(len(testing_data_set)):
        for index_2 in range(len(testing_data_set[0])):
            testing_data_set[index_1][index_2] = int(testing_data_set[index_1][index_2])
    
    #Output the testing data
    print("Testing Data List:")
    for each in testing_data_set:
        print(each)
    print("\n")

    #Close testing data file
    input_testing_data.close()

    return testing_data_set

#Function to classify testing data
def classify_data(test_data, weights):

    #Looping over all test data and classifying
    for row in test_data:
        row_sum = sum_inputs(row, weights)
        output = determine_output(row_sum)
        print("Current Row:", row)
        print("Predicted Class:", output, "\n")

learning_rate = 0.1
iterations = 500
training_set = []
testing_set = []
weights = []

#Start of training Perceptron
print("::Train Perceptron::")
print("Learning Rate:", learning_rate)
print("Number of iterations:", iterations, "\n\n")
training_set = get_training_data()
weights = set_intial_weights(len(training_set[0])-1)
weights = train_perceptron(training_set, weights, learning_rate, iterations)
print("\n\nClassifying Data . . .")
classify_data(training_set, weights)

#Start of classifying testing data
print("\n\n::Test Perceptron::")
print("Learning Rate:", learning_rate)
print("Number of iterations:", iterations, "\n\n")
testing_set = get_testing_data()
print("\n\nClassifying Data . . .\n")
classify_data(testing_set, weights)