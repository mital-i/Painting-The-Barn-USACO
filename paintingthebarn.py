#input everything

input_value = input().split()
num_rectangles = int(input_value[0])
coats_paint = int(input_value[1])

paint_squares=[]

for i in range(num_rectangles):
    square=input().split()
    paint_squares.append(square)
    
print(paint_squares)

#make a grid 
#make a prefix sum grid
