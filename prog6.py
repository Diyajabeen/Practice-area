numbers=[]
while len(numbers)<5:
    num=int(input(f"enter number {len(numbers)+1}(1-100):"))
    if 1<= num<=100:
        numbers.append(num)
    else:
            print("Number must be between 1 and 100 . try again.")

print("\nNumbers:",numbers)    
print("sum:",sum(numbers)) 
print("max:",max(numbers)) 
print("min:",min(numbers))
print("sorted:",sorted(numbers) )         