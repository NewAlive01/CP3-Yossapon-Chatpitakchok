systemMenu = {"ไก่ทอด": 35, "เป็ดทอด": 45, "ปลาทอด": 55, "ผักทอด": 20}
menuList = []

def showBill():
    print("---- My Food----")
    total_price = 0
    for number in range(len(menuList)):
        print(menuList[number][0],menuList[number][1])
        total_price += menuList[number][1]
    print(f'ราคารวม : {total_price}')


while True:
    menuName = input("Plese Enter Menu :")
    if(menuName.lower() == "exit"):
        break
    else:
        menuList.append([menuName,systemMenu[menuName]])
# print(menuList)
showBill()