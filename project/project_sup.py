img = [
 [[215, 209, 223], [108, 185, 135], [ 54, 135,  36]],\
 [[184,  20, 245], [ 32,  52, 249], [243, 155,  96]],\
 [[108,  66, 116], [ 65, 200,  34], [  2, 213, 238]] \
]

avg_pixels = []

for row in range(len(img)):
    for col in img[row]:
        avg_pixels.append(sum(img[row][col])//3)

print(avg_pixels)