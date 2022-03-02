def summary(a,b):
    return a+b
def extraction(a,b):
    return a-b
def multiply(a,b):
    return a*b
def division(a,b):
    return a/b

def process(f1, f2, f3, f4, processName):
    if processName == "summary":
        print(f1(2,3))
    elif processName == "extraction":
        print(f2(5,3))
    elif processName == "multiply":
        print(f3(3,4))
    elif processName == "division":
        print(f4(10,2))
    else:
        print("invalid process")

process(summary, extraction, multiply, division, "summary")
process(summary, extraction, multiply, division, "extraction")
process(summary, extraction, multiply, division, "multiply")
process(summary, extraction, multiply, division, "division")
process(summary, extraction, multiply, division, "summaryy")
