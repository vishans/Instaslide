

from parsing import parse
from PIL import Image, ImageFont, ImageDraw
from writingMechanism import writeText

class PosterBG:

    def __init__(self,resolution, backgroundColor, text, fontSize= 25,Xspacing= 20, Yspacing= 20, initialTextPos = (-10,-10), fontPath = r'Assets\Helvetica Neue W01 66 Medium It.ttf'):
        self.resolution = resolution
        self.backgroundColor = backgroundColor
        self.initalTextPos = initialTextPos
        self.fontSize = fontSize
        self.text = text
        self.Xspacing = Xspacing
        self.Yspacing = Yspacing

        self.fontPath = fontPath

      

    def createPoster(self):
        poster = Image.new('RGBA', self.resolution,self.backgroundColor)
        initXPos, initYPos = self.initalTextPos
        xPos, yPos = self.initalTextPos
        width, height = self.resolution

        params, text = parse(self.text)

        d = ImageDraw.Draw(Image.new('L',(0,0)))
        fontobj = ImageFont.truetype(self.fontPath,self.fontSize)
        textSizeWidth, textSizeHeight = d.textsize(text,fontobj)
        
        
        while yPos < height:
            xPos = initXPos
            while xPos < width:

                writeText(text,params,poster,self.fontPath,(xPos,yPos),fontSize=self.fontSize)

                xPos += self.Xspacing + textSizeWidth

            yPos += self.Yspacing + textSizeHeight
            




        return poster







# PosterBG((400,400),'blue', 'h<white>e</white>llo').createPoster().show()