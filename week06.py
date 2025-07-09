# load and analyze temperature data
path_to_file = "/workspaces/comp-170-su-2025-week-06-delaney-rager/data/temperatures.txt"
def load_to_list(filepath: str) -> list[float]: #input is a file path (string) and output is a list of floats
    list_of_temp = []       #initializes an empty list so that we can add to it later       
    with open(filepath, 'r') as file:       #opening the file
        for line in file:           #going through the lines in the file and adding it to our empty list using append
            list_of_temp.append(float(line))
    return list_of_temp    #returning our list of floats

def descriptive_statistics(source_data: list[float])-> None: #input is a list of floats and our output is None
    count = 0           #initializing as 0 because we will add to these values once we execute our loop
    average = 0
    compare = 0
    compare2 = float('inf')          #initializing as some high value because the lowest temperature will be lower than this regardless
    for temp in source_data:
        count += 1          #each time we execute the loop, we will add one to count which will tell us the total number of temperatures
        average += temp         #adds the temperature to the average each loop
        if compare < temp:      #this if statement is getting the largest temp
            compare = temp
        if compare2 > temp:         #this if statment gets the lowest temp
            compare2 = temp    
    average /= count            # divides the total of the temperatures by the count which is equal to the average
    temp_average = round(average,2)    #rounding to two decimal places
    print(f"There are {count} values in the data source.\n The average value is {temp_average}. \n The highest value is {compare} and the smallest value is {compare2}")                     #print statement because there is no return

list = load_to_list(path_to_file)       #TESTING THE FUNCTION
descriptive_statistics(list)

#apply simple Markup to text
path_to_file2 = "/workspaces/comp-170-su-2025-week-06-delaney-rager/data/markup.txt"

def apply_markup(filepath: str)-> None: #input is a string of the file path and the output is None meaning nothing is returned
    with open(filepath, 'r') as file:
        result = ''            #initializing empty string
        for line in file:       #takes each line of the txt file
            i = 0
            while i < len(line):        #this loop goes through each character in the line until the length of the line is fully transversed
                curr_character = line[i]        #sets the current character to the character at index i
                if curr_character == '.':           #if we detect a period
                    i += 1                      #goes to the character after the period    
                    upper_case = ''
                    while i < len(line) and line[i] != ' ' and line[i]!= '\n':     #goes through the word but stops either at the end of the line or if there is a space
                        upper_case += line[i]       #adds character
                        i += 1
                    result += upper_case.upper()     #makes the characters uppercase and adds to result
                elif curr_character == '_':           #checks if there is an underscore
                    i+=1                #goes to the next character other than the underscore
                    spaces = ''
                    while i < len(line) and line[i] != ' ' and line[i]!='\n':     #runs the loop until the end of the line in the file or until there is a space
                        spaces += line[i]+ ' '      #makes spaces between the characters
                        i+= 1
                    result += spaces
                else:
                    result += curr_character        #adds the other characters in the line
                    i+=1
    print(result)   

apply_markup(path_to_file2)    #TESTING THE FUNCTION                
#--------------------------------------------------------------------------------#
# ⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎  WRITE YOUR CODE ABOVE THIS  LINE ⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎

# ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓  DO NOT MODIFY THE CODE BELOW THIS LINE ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
#--------------------------------------------------------------------------------#
# 
