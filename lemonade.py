#Lemonade
def LemonChanges(bills:List[int]):
    five=0
    ten=0
    for i in range(len(bills)):
        if bills[i]==5:
            five=five+1
        elif bills[i]==10:
            if five>0:
               five=five-1
               ten=ten-1
            elif bills[i]==20:
                if ten>0 and five>0:
                   five=five-1
                   ten=ten-1
            elif five>=3:
                five=five-3
            else:
                return False
    return True
