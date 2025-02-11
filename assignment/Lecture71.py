menuList = []
priceList = []
total = []
def Total():
    total = sum(priceList)
    print(f"Total {total}")

def showBill():
    print("---- My Food----")
    for number in range(len(menuList)):
        print(menuList[number], priceList[number])
        total = sum(priceList)

while True:
    menuName = input("Plese Enter Menu :")
    if(menuName.lower() == "exit"):
        break
    else:
        menuPrice = int(input("Price :"))
        menuList.append(menuName)
        priceList.append(menuPrice)

showBill()
Total()