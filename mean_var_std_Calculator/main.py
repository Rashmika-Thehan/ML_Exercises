from mean_var_std import calculate


#nums = [int(input(f"Enter Number {i+1}: ")) for i in range(9)]

nums=[1,5,6,7,8,6,7,2,7]

if len(nums) != 9:
    raise ValueError("List must contain 9 numbers..")

print(calculate(nums))
    