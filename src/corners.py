from PIL import Image, ImageDraw

'''
add rounded corners to a rectangle.
used to round the flair rectangle.
the code was taken from stackoverflow
i forgot from who if ever i come across the post again
i will include the link here
the original code rounded all 4 corners to the image
i commented the lines adding corners to the top-left,
bottom-left and bottom-right
since i only wanted the flair rect to have a top-right rounded corner
'''

def add_corners(im, rad):
    circle = Image.new('L', (rad * 2, rad * 2), 0)
    draw = ImageDraw.Draw(circle)
    draw.ellipse((0, 0, rad * 2, rad * 2), fill=255)
    alpha = Image.new('L', im.size, 255)
    w, h = im.size
    # alpha.paste(circle.crop((0, 0, rad, rad)), (0, 0))
    # alpha.paste(circle.crop((0, rad, rad, rad * 2)), (0, h - rad))
    alpha.paste(circle.crop((rad, 0, rad * 2, rad)), (w - rad, 0))
    # alpha.paste(circle.crop((rad, rad, rad * 2, rad * 2)), (w - rad, h - rad))
  
    im.putalpha(alpha)
    return im

def full_corners(im, rad):
    circle = Image.new('L', (rad * 2, rad * 2), 0)
    draw = ImageDraw.Draw(circle)
    draw.ellipse((0, 0, rad * 2, rad * 2), fill=255)
    alpha = Image.new('L', im.size, 255)
    w, h = im.size
    alpha.paste(circle.crop((0, 0, rad, rad)), (0, 0))
    alpha.paste(circle.crop((0, rad, rad, rad * 2)), (0, h - rad))
    alpha.paste(circle.crop((rad, 0, rad * 2, rad)), (w - rad, 0))
    alpha.paste(circle.crop((rad, rad, rad * 2, rad * 2)), (w - rad, h - rad))
  
    im.putalpha(alpha)
    return im
