# # The extreme approach, keeping only white pixels
# img = Image.open("img1.png")
# pixels = img.load() # create the pixel map

# for i in range(img.size[0]):    # for every col:
#     for j in range(img.size[1]):    # For every row
#         # if the pixel isn't white, set it to black
#         if pixels[i][j] != (255,255,255):
#             pixels[i][j] = (0,0,0)
# img.show()

