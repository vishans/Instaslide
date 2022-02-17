
from random import randint
from PIL import Image, ImageDraw, ImageFilter, ImageFont
from corners import full_corners
from sizer import fitInImage
from writingMechanism import writeText
from parsing import parse, syntaxCheck
from formatting import formatParagraph
from time import strftime
import PIL
import os
from colorthief import ColorThief
from posterBG import PosterBG


class CorePostCreator:

    def __init__(self) -> None:
        dir = os.path.abspath(__file__)
        (dir.split('\\'))
        os.chdir('\\'.join(dir.split('\\')[:-2]))
        
       
        self.backgroundImagePath = r'Assets\bg-blue.jpg'
        self.HEIGHT = 1080
        self.WIDTH = 1080

        self.INNER_RECT_HEIGHT = 1000
        self.INNER_RECT_WIDTH = 900

        self.INTRA_IMG_HEIGHT = 500 # modifiable

        self.accentColor = self.getAccentColor(self.backgroundImagePath)

        self.flairFont = r'Assets\BebasNeue-Regular.ttf'
        self.falirFontSize = 44
        self.flairFontColor = 'white'
        self.flairTextPositionWithinFlair = (115,454)

        self.articleFont = r'Assets\AsapCondensed-Regular.ttf'#r'Assets\JosefinSans-Regular.ttf'
        
        self.articleWidth = 43 # number of characters in 1 line of article
        self.articleLineSpacing = 55
        self.articleFontSize = 45
        self.articleArticleStartPos = (110,533)
        self.articleTextDefaultColor = 'black'

        self.PageNoFont =r'Assets\Anton-Regular.ttf'
        


        self.backgroundColor = '#a8d0e6'
        self.articleAreaColor = '#f2f2f2'

        self.frontPageFont =  r'Assets\Mukta-SemiBold.ttf'


        self.logoFont = r'Assets\Helvetica Neue W01 66 Medium It.ttf'

        self.instaGradientBackgroundPath = r'Resources\stroryoutline.jpg'
        



    def __drawRoundedRectAtCentre(self,img,color, rect_h = None, rect_w = None):

        draw = ImageDraw.Draw(img)

        rect_h = self.INNER_RECT_HEIGHT if not rect_h else rect_h
        rect_w = self.INNER_RECT_WIDTH if not rect_w else rect_w

        # placing round rectangle at the center
        


        h,w = (self.HEIGHT - rect_h)//2,(self.WIDTH - rect_w)//2
        draw.rounded_rectangle(((w, h), (w+rect_w,h+rect_h)), 20, fill=color)


    def __drawRoundedRectAtCentre2(self,img,color = 'white', rect_h = None, rect_w = None):

        

        rect_h = self.INNER_RECT_HEIGHT if not rect_h else rect_h
        rect_w = self.INNER_RECT_WIDTH if not rect_w else rect_w

        # placing round rectangle at the center
       

        h,w = (self.HEIGHT - rect_h)//2,(self.WIDTH - rect_w)//2

        outline = Image.open(self.instaGradientBackgroundPath).convert('RGBA')

        outline = outline.resize((self.WIDTH,self.HEIGHT))
        

        mask = Image.new('L',(self.WIDTH,self.HEIGHT))
        mask_draw = ImageDraw.Draw(mask)
        mask_draw.rounded_rectangle(((w, h), (w+rect_w,h+rect_h)), 20, fill=color)
        solid_c = Image.new('RGBA', (self.WIDTH,self.HEIGHT), self.backgroundColor)
        
        rainbow = Image.composite(outline,solid_c, mask)
        return rainbow
        


    

    def createSlide(self,imagePath, autoResize= True, offset = (0,0), article='hello world', flairText = None,flairColor = '',backgroundImage = 'default', finalImageSavePath = '', numerator = '1',denomenator = '5',PosterbackgroundColor = 'red', Postertext = '<brown>a</brown>ktialité', PosterfontSize= 25,PosterXspacing= 20, PosterYspacing= 20, PosterinitialTextPos = (-10,-10), PosterfontPath = r'Assets\Helvetica Neue W01 66 Medium It.ttf'):


        if backgroundImage == 'gradient':
        
            img = Image.open(self.backgroundImagePath)
            img = img.resize((self.HEIGHT,self.WIDTH),Image.ANTIALIAS)

        elif backgroundImage == 'default':

            img = Image.new('RGB',(self.WIDTH,self.HEIGHT),color=self.backgroundColor)

        elif backgroundImage == 'poster':

            img = PosterBG((1080,1080), PosterbackgroundColor, Postertext,PosterfontSize,PosterXspacing,PosterYspacing,PosterinitialTextPos, PosterfontPath).createPoster()

        self.__drawRoundedRectAtCentre(img,self.articleAreaColor)

        # draw = ImageDraw.Draw(img)

        # # placing round rectangle at the center
        # h,w = (self.HEIGHT - self.INNER_RECT_HEIGHT)//2,(self.WIDTH - self.INNER_RECT_WIDTH)//2
        # draw.rounded_rectangle(((w, h), (w+self.INNER_RECT_WIDTH,h+self.INNER_RECT_HEIGHT)), 20, fill="blue")


        mask = Image.new('1',(self.WIDTH,self.HEIGHT))

        self.__drawRoundedRectAtCentre(mask,'white')
        draw = ImageDraw.Draw(mask)
        draw.rectangle(((0,self.INTRA_IMG_HEIGHT),(self.WIDTH,self.HEIGHT)), fill='black')

        intra_img  = Image.open(imagePath)
       

        if autoResize:
            
            intra_img = fitInImage(intra_img,(901,500),imagePath)
            intra_new = Image.new('RGBA',(1080,1080),'green')
            intra_new.paste(intra_img,(90,40))
            
        else:

            intra_img = intra_img.crop((0+ offset[0],0+offset[1],901 + offset[0],self.INTRA_IMG_HEIGHT+offset[1]))

            intra_new = Image.new('RGBA',(1080,1080),'green')
            intra_new.paste(intra_img,(90,40))

        
        cmpo = Image.composite(intra_new,img,mask)
        
        # article rendering
        self.writeArticle(cmpo, article,self.articleWidth)
        
        #flair rendering
        if flairText:
            cl = ColorThief(imagePath).get_palette(10)
            flairColor = cl[3] if flairColor == '' else flairColor
            
            # print( colorthief.ColorThief(imagePath).get_palette(4))
            
            self.addFlairText(flairText,cmpo, flairColor)


        self.addPageNumber(cmpo,numerator=numerator,denomenator=denomenator)

        self.addLogo(cmpo)

        
        if finalImageSavePath:
            cmpo.save(finalImageSavePath)

        else:
            cmpo.show()

        
            
    def addFlairText(self, flairText, cmpo, flairColor):

        Flairtxtparams , formattedFlairText = parse(flairText)

        if '\n' in formattedFlairText:
            print('\t--- FLAIR TEXT ERROR ---')
            print('\t Flair text should only be a single line.')
            print('\t' + '-' * 24 + '\n')
            print('\tFlair failed to render\n')
        elif len(formattedFlairText) > 40:
            print('\t--- FLAIR LENGTH TEXT ERROR ---')
            print('\t Flair text is too long.')
            print('\t' + '-' * 31 + '\n')
            print('\tFlair failed to render\n')


        else:
            if syntaxCheck(flairText):
                d = ImageDraw.Draw(cmpo)
                fnt = ImageFont.truetype(self.flairFont, self.falirFontSize)
                xF, yF = d.textsize(formattedFlairText,fnt)

                width = xF + 55#(len(formattedFlairText) * 19) +(20-len(formattedFlairText))
                try:
                   
                    self.addFlair(cmpo,width=width, col=flairColor)
                except:
                    print('\t An unknown error occurred when rendering flair text. Flair background color fall back triggered: red. ')
                    self.addFlair(cmpo,width=width, col='red')


                writeText(formattedFlairText,Flairtxtparams,cmpo,self.flairFont,self.flairTextPositionWithinFlair,fontSize=self.falirFontSize,defaultColor=self.flairFontColor)

                print('\tFlair successfully rendered.\n')

            else:
                print('\t--- SYNTAX ERROR ---')
                print('\t There was a syntax error in the flair text.')
                print('\t' + '-' * 20 + '\n')
                print('\tFlair failed to render.\n')


        



        


    def addPageNumber(self, image, color = 'white', position=(1015,950), numerator='3', denomenator = '5'):

        numNdenSeparation = 60
        x_p, y_p = position
        font = self.PageNoFont
        fnt = ImageFont.truetype(font,50)
        d = ImageDraw.Draw(image)
        x, y = d.textsize(denomenator, font=fnt)
        xx,yy = x,y
        x_, y_ = d.textsize(numerator,font=fnt)

        x, y = (x-x_)//2 , (y-y_)//2
       

        d.text((x_p+x,y_p+y),numerator,fill=color, font=fnt)

        lineWidth = 4
        yL = ((y_p+yy)+(numNdenSeparation-yy)//2)+int(1.5*lineWidth)
       
        d.line([(x_p, yL),(x_p+xx, yL)],fill=color,width=lineWidth)

        d.text((x_p,y_p+numNdenSeparation),denomenator,fill=color, font=fnt)


        


    def addFlair(self,image: Image.Image, col = None, width = 500):
        col = self.getAccentColor(self.backgroundImagePath) if col == None else col
        flair_size = (width,45)
        new_im = Image.new('RGBA',flair_size, color = col)

        from corners import add_corners
        new_im = add_corners(new_im,20)


        image.paste(f :=new_im,(90,500-flair_size[1]),f)

        # image.show()

    def addLogo(self, img:Image):

        params,logoText = parse('@Aktialit<brown>e_</brown>')
        
        writeText(logoText,params,img,self.logoFont,(22,35), defaultColor='white') #20 20


    def addSwipeToReadIcon(self,img,  pos=(0,0), swipeIconColor = (255,0,0)):
        swipe_ = Image.open(r'Assets/small_swipe.png').convert('RGBA')
        swipe = self.swapPixel(swipe_,swipeIconColor)
        img.paste(swipe,pos,self.swapPixel(swipe_).convert('L'))
        
        

    def swapPixel (self,im, colTo = (255,255,255,255)):
        newimdata = []
        redcolor = (255,0,0)
        blackcolor = (0,0,0,255)
        
        for color in im.getdata():
            if color == blackcolor:
                newimdata.append(colTo )
            else:
                newimdata.append( blackcolor )
        newim = Image.new(im.mode,im.size)
        newim.putdata(newimdata)
        return newim
       

        


    def getAccentColor(self, imagePath):

        im = Image.open(imagePath)
        im.resize((1,1))
        return im.getpixel((0,0))



    def writeArticle(self, image,  article,articlewidth, formatLine=True):
        
        if syntaxCheck(article):
            # p, formattedArticle = parse(article)
            formattedArticle = formatParagraph(article,articlewidth)

            if formattedArticle:
           
                params,article = parse(formattedArticle)
                
                writeText(article,params,image,defaultColor=self.articleTextDefaultColor,startPos=self.articleArticleStartPos,fontPath=self.articleFont, fontSize=self.articleFontSize,lineSpacing=self.articleLineSpacing)

                print('\tArticle successfully rendered.\n')
                return

            else:
                print('\t--- LONG WORD ERROR ---')
                print('\t One or more words are too long.')
                print('\t'+ '-' * 23 +'\n')

           


        else:
            print('\t--- SYNTAX ERROR ---')
            print('\t There was a syntax error in the article')
            print('\t' + '-' * 20 + '\n')

        print('\tArticle could not be rendered\n')

    
    def frontPage(self,imagePath,title ='Ban aktialité', sub_title='', fontSize = 95, finalImageSavePath = '', frameColor = '', swipeIconColor = None, order_text=2, order_frame= 2, textColor = None ):
        
        photo = Image.open(imagePath).convert('RGBA')
        # xp, yp = photo.size

        # if xp//yp == 1:
        #     img = photo.resize((1080,1080))
        # else:
        #     xp, yp = (xp-1080)//2,(yp-1080)//2
        #     img = photo.crop((xp,yp,xp+1080,yp +1080))
        if photo.size != (1080,1080):
            img = fitInImage(photo,(1080,1080), imagePath)
        
        

        

        d = ImageDraw.Draw(img)

        param, text = parse(title)


        x,y = d.textsize(text,ImageFont.truetype(self.frontPageFont,fontSize))
        param, text = parse(sub_title)

        x_sub,y_sub = d.textsize(text,ImageFont.truetype(self.frontPageFont,150))

        ytemp = y 
        xtemp = max(x,x_sub)

        xc,yc = (self.WIDTH-xtemp)//2,((self.HEIGHT-ytemp)//2)+150
        x_offset = 25
        box =  (xc-x_offset, yc, xc+xtemp+x_offset, yc+300)
        f =img.crop(box)
        
        for i in range(10):  # with the BLUR filter, you can blur a few times to get the effect you're seeking
            f = f.filter(ImageFilter.BLUR)

        # f.show()
        img.paste(f,box)


        # textColor = '#E4E4E4'
        textColor = (ColorThief(imagePath).get_palette(5))[order_text] if not textColor else textColor
        param, text = parse(title)

        writeText(text,param,img,self.frontPageFont, startPos=((self.WIDTH-x)//2,((self.HEIGHT-y)//2)+150), defaultColor=textColor,fontSize=fontSize)

        sub_title = strftime('%d&/%m') if sub_title == '' else sub_title
        param, text = parse(sub_title)

        x_sub,y_sub = d.textsize(text,ImageFont.truetype(self.frontPageFont,150))
        writeText(text,param,img,self.frontPageFont, startPos=((self.WIDTH-x_sub)//2,((self.HEIGHT-y_sub)//2)+170+ytemp), defaultColor=textColor,fontSize=150)
        

        mask = Image.new('L',(1080,1080))
        d = ImageDraw.Draw(mask)
        offset = 40
        d.rectangle((offset,offset,1080-offset,1080-offset),'grey')
        offset = 65
        d.rectangle((offset,offset,1080-offset,1080-offset),'black')
        # mask.show()
        
        # mask.show()
        solidcolor = Image.new('RGB',(1080,1080), (ColorThief(imagePath).get_palette(10))[order_frame] if not frameColor else frameColor)
        #'#DF021B')

        
        # solidcolor.show()
        final_image = Image.composite(solidcolor,img,mask)
        self.addSwipeToReadIcon(final_image,(900,900),swipeIconColor=textColor if not swipeIconColor else swipeIconColor)
        # # mask.show()
        print('\t Front cover successfully rendered.\n')
        if finalImageSavePath:
            final_image.save(finalImageSavePath)
        else:
            final_image.show()
       


    def addThrowBackEmoji():
        pass


    def createStory(self,imagePath, autoResize= True, offset = (0,0), article='hello world', flairText = None,flairColor = '#ff0800',backgroundImage = None, finalImageSavePath = ''):

        self.backgroundColor = '#C8E3F8'
        self.articleAreaColor='#CCCCCC'

        if backgroundImage:
        
            img = Image.open(self.backgroundImagePath)
            img = img.resize((self.HEIGHT,self.WIDTH),Image.ANTIALIAS)

        else:

            img = Image.new('RGB',(self.WIDTH,self.HEIGHT),color=self.backgroundColor)

        
        outline = 15
        img = self.__drawRoundedRectAtCentre2(img,rect_h=self.INNER_RECT_HEIGHT+outline,rect_w=self.INNER_RECT_WIDTH+outline)


        self.__drawRoundedRectAtCentre(img,self.articleAreaColor)



        mask = Image.new('1',(self.WIDTH,self.HEIGHT))

        self.__drawRoundedRectAtCentre(mask,'white')
        draw = ImageDraw.Draw(mask)
        draw.rectangle(((0,self.INTRA_IMG_HEIGHT),(self.WIDTH,self.HEIGHT)), fill='black')

        intra_img  = Image.open(imagePath)
       

        if autoResize:
            
            intra_img = fitInImage(intra_img,(901,500),imagePath)
            intra_new = Image.new('RGBA',(1080,1080),'green')
            intra_new.paste(intra_img,(90,40))
            
        else:

            intra_img = intra_img.crop((0+ offset[0],0+offset[1],901 + offset[0],self.INTRA_IMG_HEIGHT+offset[1]))

            intra_new = Image.new('RGBA',(1080,1080),'green')
            intra_new.paste(intra_img,(90,40))

        
        cmpo = Image.composite(intra_new,img,mask)
       

        self.writeArticle(cmpo, article,self.articleWidth)
        
        #flair rendering
        if flairText:
            
            Flairtxtparams , formattedFlairText = parse(flairText)

            if '\n' in formattedFlairText:
                print('\t--- FLAIR TEXT ERROR ---')
                print('\t Flair text should only be a single line.')
                print('\t' + '-' * 24 + '\n')
                print('\tFlair failed to render\n')
            elif len(formattedFlairText) > 40:
                print('\t--- FLAIR LENGTH TEXT ERROR ---')
                print('\t Flair text is too long.')
                print('\t' + '-' * 31 + '\n')
                print('\tFlair failed to render\n')


            else:
                if syntaxCheck(flairText):
                    d = ImageDraw.Draw(cmpo)
                    fnt = ImageFont.truetype(self.flairFont, self.falirFontSize)
                    xF, yF = d.textsize(formattedFlairText,fnt)

                    width = xF + 55#(len(formattedFlairText) * 19) +(20-len(formattedFlairText))
                    try:
                        self.addFlair(cmpo,width=width, col=flairColor)
                    except:
                        print('\t An unknown error occurred when rendering flair text. Flair background color fall back triggered: red. ')
                        self.addFlair(cmpo,width=width, col='red')


                    writeText(formattedFlairText,Flairtxtparams,cmpo,self.flairFont,self.flairTextPositionWithinFlair,fontSize=self.falirFontSize,defaultColor=self.flairFontColor)

                    print('\tFlair successfully rendered.\n')

                else:
                    print('\t--- SYNTAX ERROR ---')
                    print('\t There was a syntax error in the flair text.')
                    print('\t' + '-' * 20 + '\n')
                    print('\tFlair failed to render.\n')



        # self.addPageNumber(cmpo,numerator=numerator,denomenator=denomenator)

        # self.addLogo(cmpo)
        mask = Image.new('L',(self.WIDTH,self.HEIGHT))
        d = ImageDraw.Draw(mask)
        horizontol_lineWidth = 10
        align = (horizontol_lineWidth//2) -1
        d.line((90,500+align,90+900,500+align), width=horizontol_lineWidth,fill='white')
        # mask.show()

        cmpo = Image.composite(Image.open(self.instaGradientBackgroundPath).resize((1080,1080)),cmpo,mask)
        # print(finalImageSavePath)
       
        self.addVerticalLogo(cmpo)


        if finalImageSavePath:
            cmpo.save(finalImageSavePath)

        else:
            cmpo.show()


    def addVerticalLogo(self, img:Image.Image):
        
        fontSize = 25
        text = '@Aktialite_ '
        text_logo = Image.new('RGBA', (0,0))
        draw = ImageDraw.Draw(text_logo)
        x,y = draw.textsize(text, ImageFont.truetype(self.logoFont, fontSize))
        padding = 10
        text_logo = Image.new('RGBA', (x+padding,y+padding),self.backgroundColor)
        full_corners(text_logo,15)
        # # draw = ImageDraw.Draw(text_logo)
        params,logoText = parse('@Aktialit<brown>e_</brown>')
        writeText(logoText,params, text_logo,self.logoFont,(8,(padding//2)-1),'black', fontSize=fontSize)
        text_logo = text_logo.rotate(-90,expand=1, resample = PIL.Image.NEAREST)
        # text_logo.show()
        # text_logo.show()

        # solid = Image.new('L',(1080,1080))
        # solid.paste(Image.new('L',(x,y),color='white'))
        # solid.show()
        # print(img.size)
        img.paste(text_logo,(1080-padding-y-40,1080-padding-x-40), text_logo)  #(1080-padding-y-40,1080-padding-x-40)


        

       

   

# to add syntax check and error return in textWrite done
# implement ur own  textwrap \n processing before parsing done 
# add special characters support on new text wrap done

# create full article page? pending

#create front cover? done 

#revamp syntax check algo pending

#implement ui and compiling mechanism functional but prolly not complete



if __name__ == '__main__':

    article = '''<#4CAF50>zezi</#4CAF50>'''
    
    CorePostCreator().createSlide(imagePath='zezi.jpg', article=article, flairText='hello')