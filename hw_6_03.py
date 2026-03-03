import random

def writeFile(inputList, fileName):
    # Creates a file of the given name and adds each value from the list to said file with each line being an index from the list.
    f = open(fileName, "w")
    for item in inputList:
        f.write(str(item) + "\n")
    f.close()
#commetn

def sortNames(fileName, targetFile):
    # Modify the below function such that it takes in source file and a target file.
    # Sort all of the values from the source file and write them to the target file
    # I recommend using .sort() for this. You do not need to write the sorting algorithm yourself.
    
    # Read all names from the source file
    f = open(fileName, "r")
    names = []
    for line in f:
        names.append(line.strip())
    f.close()
    
    # Sort the names
    names.sort()
    
    # Write sorted names to target file
    f = open(targetFile, "w")
    for name in names:
        f.write(name + "\n")
    f.close()


def highScore(newScore: int):
    # Modify the function such that it adds a new score to the file scores.txt
    # Then return the average score from all of the scores in scores.txt
    
    # Add the new score to the file
    f = open("scores.txt", "a")
    f.write(str(newScore) + "\n")
    f.close()
    
    # Read all scores and calculate average
    f = open("scores.txt", "r")
    scores = []
    for line in f:
        score = int(line.strip())
        scores.append(score)
    f.close()
    
    # Calculate and return average
    total = 0
    for score in scores:
        total = total + score
    average = total / len(scores)
    
    return average