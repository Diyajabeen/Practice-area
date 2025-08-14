def get_numbers():
    nums=[]

    for i in range(10):
        num=int(input(f"enter number {i+1} : "))
        
        nums.append(num)

    return nums
def display_status(nums):
    print("\nsum:",sum(nums))
    print("max:", max(nums))
    print("min:", min(nums))
    print("sorted",sorted(nums))
    print("Average:", sum(nums) / len(nums))

numbers=get_numbers()
display_status(numbers)
