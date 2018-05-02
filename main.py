import random


def get_training_data():
    training_data_set = []
    training_data = None

    #Loop to get input file
    while training_data is None:
        try:
            training_data = input("Please enter the name of the training data file: ")
            
            #Opening input file called input.txt
            input_training_data = open(training_data, 'r')
        except OSError:
            print('\nError accessing file. Enter the correct filename with extension.\n\n')

    input_training_data.__next__()

    #Creating input sample list and parsing
    for line in input_training_data:
        line = line.rstrip('\n')
        training_data_set.append(line.split(" "))

    #Change all values to integers
    for index_1 in range(len(input_training_data)):
        for index_2 in range(len(input_training_data[0])):
            input_training_data[index_1][index_2] = int(input_training_data[index_1][index_2])
    
    #Output the training data
    print("Training Data List:")
    for each in training_data_set:
        print(each)
    print("\n")

    #Close training data file
    input_training_data.close()

    return training_data_set

def set_intial_weights(num_variables):
    weights = []

    #Generating random weights between 0 and 1
    for _ in range(num_variables):
        weights.append(random.uniform(0,1))
    
    return weights

def adjust_weights(row, weights, actual_output, learning_rate):
    for index in range(len(row)-1):
        weights[index] = weights[index]+(learning_rate*(row[-1]-actual_output))*row[index]
    
    return weights

def sum_inputs(row, weights):
    total_sum = 0.0

    for index in range(len(row)-1):
        total_sum += row[index]*weights[index]
    
    return total_sum

def determine_output(variable_sum):
    if variable_sum > 0:
        return 1
    else:
        return -1

def train_perceptron(training_set, weights, learning_rate, iterations):
    
    error_rate = error_counter = 0
    
    #Training loop for perceptron
    print("Training Perceptron . . .")
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
        print("Training Iteration -", iteration)
        print("Error Rate:", error_rate)

        #If the error rate reaches 0 continously, break when count reaches 10
        if error_rate == 0.0:
            error_counter += 1
            if error_counter == 10:
                break
        else:
            error_counter = 0.0

    return weights

def get_testing_data():
    testing_data_set = []
    testing_data = None

    #Loop to get input file
    while testing_data is None:
        try:
            testing_data = input("Please enter the name of the training data file: ")
            
            #Opening input file called input.txt
            input_testing_data = open(testing_data, 'r')
        except OSError:
            print('\nError accessing file. Enter the correct filename with extension.\n\n')

    input_testing_data.__next__()

    #Creating input sample list and parsing
    for line in input_testing_data:
        line = line.rstrip('\n')
        testing_data_set.append(line.split(" "))

    #Change all values to integers
    for index_1 in range(len(input_testing_data)):
        for index_2 in range(len(input_testing_data[0])):
            input_testing_data[index_1][index_2] = int(input_testing_data[index_1][index_2])
    
    #Output the training data
    print("Testing Data List:")
    for each in testing_data_set:
        print(each)
    print("\n")

    #Close training data file
    input_testing_data.close()

    return testing_data_set

def classify_data(test_data, weights):
    error = 0

    for row in test_data:
        row_sum = sum_inputs(row, weights)
        output = determine_output(row_sum)
        if output != row[-1]:
            error += 1
        print("Current Row:", row)
        print("Predicted Class:", output)
    error_rate = error/len(test_data)
    print("Error Rate:", error_rate)

