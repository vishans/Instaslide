from PIL import Image
# from PIL import ImageFilter
from colorthief import ColorThief


'''
fitImage resizes an image keeping its aspect ratio 
to fit 'dimensionToFit' and puts it 
at the centre of another image having <dimensionToFit> dimensions.

I found out PIL thumbnail method does not really do what I needed. So I wrote my own function.

working principles:
it take the 'img' that nees to be resized. 
It calculates the height and width of the img which allow the img to fit the 'dimensionToFit' value. 
Then it resizes the img to the calculated width and height and
puts the resized img at the centre of another image (let's call this image, Image B) that it creates,that has the exact dimension specified by 'dimensionToFit'.
If preferredColorBg is None, ColorThief is used to determine the color of Image B.

---parameters---

img: (PIL Image object) image to resize

dimensionToFit: (2-value-int-tuple) see working principles above

the path parameter is important since ColorThief cannot take an img object from PIL.
ColorThief has to open the image itself, so the path has to be provided.

preferredColorBg: (str or str-hex) a color of Image B. See working principles above. If this is None, ColorThief takes over.



'''

'''fitInImage seems to work fine for the most part. However I think it's probably w'''

def fitInImage(img: Image.Image, dimensionToFit, path='', preferredColorBg = None):
    x_d,y_d = dimensionToFit
    x,y = img.size

    

    current_y = y_d
    current_x = int((current_y/y) * x)

    while not(current_x <= x_d and current_y <= y_d):
        # print('h')

        current_y-=1
        current_x = ((current_y/y) * x)

    # print(current_x,current_y)
    r_img = img.resize((int(current_x), int(current_y))) 
    

    c = ColorThief(path).get_color(10) if not preferredColorBg else preferredColorBg

    


    n = Image.new('RGB',dimensionToFit,c)

    '''
    The commented code below was supposed to blur Image B.
    IMO it didn't look good or hardly made any difference because
    of the way blur worked, blurring a solid color does not do anything. So I removed this feature by commenting the code.
    (If you don't know what Image B is, please take a look 
    at working principle above. 
    )
    '''
    # for i in range(20):
    #     n = n.filter(ImageFilter.BLUR)
    # n.show()


    x,y = dimensionToFit
    n.paste(r_img,((int(x-current_x)//2),(int(y-current_y)//2)))
    return n


# def fitInImage(img: Image.Image, dimensionToFit, path='', preferredColorBg = None):
#     x_d,y_d = dimensionToFit
#     x,y = img.size

    

#     current_y = y_d
#     current_x = int((current_y/y) * x)

#     current_x = x_d
#     current_y = int((current_x/x) * y)

#     while not(current_x <= x_d and current_y <= y_d):
#         # print('h')

#         current_x-=1
#         current_y = ((current_x/x) * y)

        

#     # print(current_x,current_y)
#     r_img = img.resize((int(current_x), int(current_y))) 
    

#     c = ColorThief(path).get_color(10) if not preferredColorBg else preferredColorBg

    


#     n = Image.new('RGB',dimensionToFit,c)

#     '''
#     The commented code below was supposed to blur Image B.
#     IMO it didn't look good or hardly made any difference because
#     of the way blur worked, blurring a solid color does not do anything. So I removed this feature by commenting the code.
#     (If you don't know what Image B is, please take a look 
#     at working principle above. 
#     )
#     '''
#     # for i in range(20):
#     #     n = n.filter(ImageFilter.BLUR)
#     # n.show()


#     x,y = dimensionToFit
#     n.paste(r_img,((int(x-current_x)//2),(int(y-current_y)//2)))
#     return n

