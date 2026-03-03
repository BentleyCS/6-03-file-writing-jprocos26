import hw_6_03 as HW

def test_writeFile():
    testList = ["apple", "banana", "cherry"]
    HW.writeFile(testList, "test_output.txt")
    
    f = open("test_output.txt", "r")
    lines = []
    for line in f:
        lines.append(line.strip())
    f.close()
    
    assert lines == ["apple", "banana", "cherry"]
print(test_writeFile())
def test_sortNames():
    f = open("names.txt", "w")
    f.write("Zoe\n")
    f.write("Alice\n")
    f.write("Mike\n")
    f.write("Bob\n")
    f.close()
    
    HW.sortNames("names.txt", "namesNew.txt")
    
    f = open("namesNew.txt", "r")
    sorted_names = []
    for line in f:
        sorted_names.append(line.strip())
    f.close()
    
    assert sorted_names == ["Alice", "Bob", "Mike", "Zoe"]


def test_highScore():
    f = open("scores.txt", "w")
    f.write("80\n")
    f.write("90\n")
    f.write("70\n")
    f.close()
    
    avg = HW.highScore(100)
    
    assert avg == 85.0
