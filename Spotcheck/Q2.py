#Tony K.
#19/01/2015
#Spotcheck Q2 - part d

def initialise_frequency_array():
    one = []
    two = []
    three = []
    four = []
    five = []
    six = []
    
    result = [
        one,
        two,
        three,
        four,
        five,
        six
        ]
    return result

def simulate_die_throwing(result):
    import random
    for count in range(1,20):
        random_number = random.randint(1,6)
        for count in range(1,6):
            if random_number == count:
                number = count - 1
                get_number = result[number[0]] + 1
                
    return result

def display_result_array(result):
    print("{0:>6} {1:>10}".format("Score","Frequecy"))
    for count in range(1,6):
        print("{1:>6} {1:>10}".format(count,result[count])


def main():
    result = initialise_frequency_array()
    result = simulate_die_throwing(result)
    display_result_array(result)
                

        
            
