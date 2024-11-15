#Program 3 – Girl Guide Cookies
#Description:   The organizers of the annual Girl Guide cookie sale event want to raise 
#               the stakes on the number of cookies sold and are offering cool prizes to
#               those guides who go above and beyond in their sales efforts. The organizers
#               want a program to print the guide list and their prizes.

#Student #: W0433704
#Student Name:  Zachary Rudolf
#initialize 
guides = []
cookies = []
avg=0.0
topPrize = "Trip to Girl Guide Jamboree in Aruba!"
abvAvg = "Super Seller Badge"
abvZero = "Left over cookies"
zero = ""

#Opening/greeting
def greeting():
    print("Welcome to the Cookie Calculator!\n")
#Input to fill list of guides
def getGuideNo():
    number = int(input("Enter the number of guides selling cookies: "))
    return number 

#function to determine average

def boxSales(boxCount): #2d lists break my brain
    boxes = []
    for i in boxCount:          #i didnt even need to do this!!
        for j in i:
            integer = isinstance(j, int) 
            if integer == True:
                boxes.append(j) 
            else: 
                pass
    return boxes 

def getGuideSales(): 
    boxCount=[]
    guideAmt = getGuideNo()
    for i in range(guideAmt):
        guides = []
        name = input(f"\nEnter the name of guide #{i+1}: ")
        cookies = int(input(f"Enter the number of boxes sold by {name}: ")) #input to fill list of boxes sold
        guides.append(name)
        guides.append(cookies) 
        boxCount.append(guides) 
    boxes = boxSales(boxCount) 
    avg = sum(boxes)/(len(boxes)) 
    print("\n \nThe average number of boxes sold by each guide was: {0:.1f}\n".format(avg))    
#function to determine prizes (0=nothing 1st=trip above average=super badge at least one=left overs) 
    print("Guide\t\tPrizes won: ")
    print("==============================================================")
    for i in range(len(boxes)):
        if boxes[i] == (max(boxes)): 
            prize = topPrize 
        elif boxes[i] > avg:
            prize = abvAvg 
        elif boxes[i] > 0 and boxes[i] < avg:
            prize = abvZero 
        elif boxes[i] <= 0 or boxes[i] == "": 
            prize = "" 
        print(f"{boxCount[i][0]}\t\t - {prize}") 



def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)
    greeting()
    getGuideSales()
    # YOUR CODE ENDS HERE

main()