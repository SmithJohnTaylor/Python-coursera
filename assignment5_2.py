largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    try : 
        num = int(num)
        if largest is None:
            largest = num
        if smallest is None:
            smallest = num
    except: 
        if num == "done":
            break
        print("Invalid input")
        continue

    if num > largest:
        largest = num
    elif smallest > num:
        smallest = num

print("Maximum is", largest)
print("Minimum is", smallest)