import math

#while-loop (refer to discussion activity)
dummy_variable = False
while dummy_variable == False:
    try:
        mean = float(input("Please the enter the mean of the distribution (It can be any value between [–∞ to +∞]): ") or 0)
    except ValueError:
        print("Invalid input, numerical value only please.")
        continue
    else:
        dummy_variable = True
    print(f"Mean distribution is: {mean}.")

    break

#opening of a user defined function(seminar 2)
def value_variance():
    global valuevar
    while True:
        try:
            valuevar = float(input("Please enter the variance and it must be greater than 0! ") or 1)
            if valuevar >= 1:
                print(f"Varience is: {valuevar}.")
            elif valuevar <= 0:
                print("You have entered a value < 0, try again!")
                return value_variance()
            else:
                print("Variance is 1")
            break
        except ValueError:
            print("Amount must be a number, try again")
        continue

value_variance()


check_input = False
while check_input == False:
    try:
        value_x = float(input("Please the enter the value of X (It can be any value between [–∞ to +∞]): "))
    except ValueError:
        print("Invalid input, numerical value only.")
        continue
    else:
        valid_input = True
    break

print(f"X value is: {value_x}.")

def pdf(x, mean_value, variance):
    formpdf = (1 / math.sqrt(2 * math.pi * valuevar)) * math.exp(-(float(x) - float(mean)) ** 2 / (2 * valuevar))
    return formpdf

x = value_x
mean_value = mean
variance = valuevar
result = pdf(x, mean_value, variance)
print (f"The probability density based on your inputs is float {result:.4f}. The mean and variance used is: {mean}, {variance}, respectively")

#Start of Part (f)
#To allow user to input alpha value, no value will default to alpha 0.01

alpha_value = False
while alpha_value == False:
    try:
        alpha = float(input("Please enter alpha value (default is 0.01 for maximum accuracy!): ") or 0.01)
        if alpha < 0:
            raise ValueError
    except ValueError:
        print("Invalid input, numerical value only please.")
        continue
    else:
        alpha_value = True
    print(f"Alpha is: {alpha}.")
    break

#Allow user to input their required 'a' value
valid_a_value = False
while valid_a_value == False:
    try:
        a_value = float(input("Please the enter the a value [–∞ to -100]): ") or -100)
        if a_value > -100:
          raise ValueError
    except ValueError:
        print("Invalid input as a value is too great.")
        continue
    else:
        valid_a_value = True
    print(f"a_value is: {a_value}.")
    break


#Part f program for user to input their values to calculate based on part (c) of the question whereby X is their input in (c)
sum = 0
    #initialize value with a_value, start the sequence from (-100) and incrementally update according to alpha value
initial_a_value = a_value
    #As loop reaches value_x, loop stops
while initial_a_value != round(value_x, 3):
        #CDF sequence
    sum = sum + pdf(initial_a_value, mean_value, variance)
        #add alpha for next iteration
    initial_a_value = initial_a_value + alpha
    initial_a_value = round(initial_a_value, 3)

sum = sum+pdf(value_x, mean_value, variance)

print("--------------------------------------------------")

print(f"Probability of X <= {value_x} Computed BY CDF term with \n-------------------------------------------------- \n\na = {a_value}\nAlpha = {alpha}\nMean = {mean} \nVarience = {valuevar} \nK = {value_x} \n\nis as follows:\n\nP(X<={value_x}) = {sum * alpha}")

#Part f - Check the values of 0, 1.64, 1.94 - Similar to the above program
#storing all k values that are required for checking into a list
k = [0, 1.64, 1.96]
cdf = []
for i in range(len(k)):
    sum = 0
    initial_a_value = a_value
    # As loop reaches k[i] value, loop stops
    while initial_a_value != round(k[i], 3):
        sum = sum + pdf(initial_a_value, mean_value, variance)
        initial_a_value = initial_a_value + alpha
        initial_a_value = round(initial_a_value, 3)

    sum = sum + pdf(k[i], mean_value,variance)
    cdf.append(sum * alpha)

print(f"\nThe CDF for 0, 1.64 and 1.96 are: {cdf}, respectively.")

#Part (h)
sum=0
#Define dictionary to be created
probabilities={}
#Initialize with the start value of -5.0 and incrementally increase by 0.1
initial_value = -5.0
#Loop to be terminated as value turns 5.1 (to ensure that it has run till 5.0)
while initial_value != 5.1:
    #Rounding off the value
    h = round(initial_value,2)
    #find the CDF value
    sum = sum + pdf(h, 0, 1)
    #Append into the dictionary
    probabilities[h] = sum * alpha
    #Update result with round() function
    initial_value = round(initial_value + alpha, 2)

probabilities

print(f"\n\nFor probabilities of X values between 2 and -2\n(For mean = {mean}, variance = {variance}, alpha = {alpha}, and a = {a_value}) \n ")

#Printing probabilities between -2 and 2 with step width 0.5
initial_value = -2.0
while initial_value != 2.5:
  print(str(initial_value) +" : "+ str(probabilities[initial_value]))
  initial_value = round(initial_value +0.5,1)
