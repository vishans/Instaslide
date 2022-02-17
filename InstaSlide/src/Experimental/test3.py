from PIL import Image, ImageFont, ImageDraw



def rze(img: Image.Image,y_d=None,x_d=None):
    
    x,y = img.size

    
    if y_d:
        current_y = y_d
        current_x = int((current_y/y) * x)

    if x_d:
        current_x = x_d
        current_y = int((current_x/x) * y)

    
    r_img = img.resize((int(current_x), int(current_y))) 
    
    
    return r_img



img = Image.open(r'Assets\throwbackBIN.png')
# img = img.convert('RGB')

img = rze(img,80)

pixels = img.load() # create the pixel map
data = []
for i in range(img.size[0]): # for every pixel:
    for j in range(img.size[1]):
        # print(pixels[i,j])
        if pixels[i,j] == (255,255,255):
            # change to white if not black
            pixels[i,j] = (255, 0 ,0)
        

    # print()

img.show()

