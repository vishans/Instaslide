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

size = 150
# actualImg = Image.open(r'Assets\throwback.png')
# actualImg = rze(actualImg,size)
# actualImg =actualImg.convert('RGBA')

img_ = Image.open(r'Assets\throwbackBIN.png')
img = rze(img_,size)


zezi = Image.open(r'zezi.jpg')
zezi = zezi.convert('RGBA')

zezi.paste(Image.new('RGB',img.size,(255,255,0)),(50,50),img)

zezi.show()