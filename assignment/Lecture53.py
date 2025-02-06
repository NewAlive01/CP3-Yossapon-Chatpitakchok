totalprice = int(input())
def vatcal(totalprice):
    result = (totalprice*7/100)
    return result + totalprice
print(vatcal(totalprice))