def change(salaries, booster):
    if len(salaries) == 0:
        return []
    else:
        print(salaries)
        return [salaries[0]*booster] + change(salaries[1:], booster)


print(change([2,2,2,2], 4))  
