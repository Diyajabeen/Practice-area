numbers=[]
for i in range(5):
    num=int(input(f"enter number {i+1}:"))
    numbers.append(num)

print("\nNumbers entered:",numbers)

print("Sum:",sum(numbers))
print("Maximum:",max(numbers))
print("Minimum:",min(numbers))
print("Sorted (Ascending):",sorted(numbers))