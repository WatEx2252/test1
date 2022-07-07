def task(array):
    i=array.find("0")
    if i != -1:
        return i
    else:
        return "не найдено 0 в строке"

print(task(input()))
