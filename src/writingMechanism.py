from PIL import ImageFont, ImageDraw


'''
writeText working principles:
The 'text' and 'param' parameters are essentially responsible for 
writing character of specific colors.
'param' is a list of 3-value-tuple 
The 3 values are:
1. start  (in algorithm refered as s)
2. end    (s)
3. color  (col)

An example would be (0,5,'red')
This means that characters 0 through 5 inclusive would be painted
red.

writeText is an algoritm that parses param and write the text on 
an image, respecting the color specified in param.
                              
For example, consider text = 'hello world/n'
                    params = [(0,4,'red'), (7,8,'blue')]

The characters 0 through 4 inclusive would be painted red, i.e,
'hello' will be painted red.

Now notice that character 5 and 6  has not been specified any color. If this is ever the case writeText will use the 'defaultColor' specified which is by default black.

Then afterwards characters 7 through 8 inclusive will be painter blue, i.e,
'or' in 'word' will be painted blue.

When a newline character is encountered, textWrite will start 
writing at (startPos[0], startPos[1] + lineSpacing), essentially
changing line.

-------other parameters-----

image: (a PIL Image object) image on which to write text

fontPath: (str) path to font that should be used to write the text
           This argument is important. There is no fall back.
           If a fontPath is not provided, an error will occur.


startPos: (2-value-int-tuple) x,y co-ord specifying where in the 
           image the text should start.


defaultColor: (str or str-hex, see PIL doc)
               fall back color if color is not specified in param.

lineSpacing: (int) distance between each line.

fontSize: (int) specifies the size of the font.

'''

def writeText(text, param, image,fontPath ,startPos = (10,100), defaultColor = 'black', lineSpacing=55, fontSize = 45):

    d = ImageDraw.Draw(image)
    fnt = ImageFont.truetype(fontPath, fontSize)

    current = startPos
    color = defaultColor
    p_index = 0 # param index
    index = -1

    unknownErrorDict = {} 
    # if an error is triggered once, it is saved so that it 
    # it does not get triggered more than once
    # for example if user has a wrong color 'yello' several times
    # the error for unknown color yello will be triggered only once
    # despite occuring more than once

    for c in text:
        index+=1

        if c == '\n': 
            
            xt, yt = current
            current = (startPos[0],yt+lineSpacing)
            continue

            '''
            change line 
            '''
            
        if len(param):

            s, e, col = param[p_index]

            '''
            if param is empty 
            s,e get set to -1.
            -1 triggers the defaultColor.
            '''

        else:
            s,e = -1,-1

        if (s <= index <= e):
            color = col

        else: 
            color = defaultColor

        
        x,y = d.textsize(('abc' + c + 'abc'), fnt)

        x_, y_ = d.textsize('abcabc',fnt)

        '''
        this is a trick to get the proper size of a character
        and to know by how much we should advance along the x-axis
        '''

        x= x - x_

        try:
            d.text(current,c , font=fnt, fill=color)

        except ValueError as error:
            str_err = str(error)
            index_ = str_err.find(':')
            unkCol = str_err[index_:]
            if not unkCol in unknownErrorDict:
                print(f'\tAn unknown color value: {unkCol}  was obtained. Text of that color was rendered in black.\n')
                
                unknownErrorDict[unkCol] = 0

            d.text(current,c , font=fnt, fill='black')


        xt, yt = current

        current = (xt+x,yt)

        if index == e and p_index < len(param) - 1:
            p_index+=1


    # image.show()
    


   