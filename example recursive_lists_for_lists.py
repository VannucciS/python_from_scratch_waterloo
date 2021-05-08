def change(salaries, booster):
    if len(salaries) == 0:
        return []
    else:
        print(salaries)
        return [salaries[0]*booster[0]] + change(salaries[1:], booster[1:])


print(change([2,2,2,2], [1,2,3,4]))  
