input_num = int(input("Enter the number you showed: "))
output_num = int()

if(input_num > 0):
    output_num = input_num * input_num
    print("Square = " , output_num)
elif(input_num < 0):
    output_num = input_num * input_num * input_num
    print("Cube = ", output_num)
else:
    print("Zero")