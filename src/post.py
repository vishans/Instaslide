from kernel import CorePostCreator
from copy import deepcopy

class Post:

    '''
    Improvement???
    For each slide generate a CorePostCreator object is created. The latter is however 
    destroyed before the next slide generation. 
    I am thinking of using a single CorePostCreator object for every slide. I will have to test this out. I will  implement this if, it works.'''

    def __init__(self) -> None:
        
        self.frontCover = False
        self.pageNumber = 0  # also numerator 
        self.denomenator = 0
        self.queue = []
        

        self.imageSaveFormat = '.png'
        self.saveDir = r'slides'

        # it's probably better to create one CorePostCreator object here
        # and to use it 
        # instead of creating an object everytime
        # added to next to do!!!
        # improvement may be. we'll see


    def addSlide(self,imagePath = r'C:\Users\VISHAN\Desktop\InstaSlide\zezi32.jpg', article='Include an article', flairText = 'Include a flair',flairColor = '#ff0800',finalImageSavePath = ''):

        d = locals()
        self.incrementPageNumber()
        d['finalImageSavePath'] = self.getSavePath()
        d['numerator'] = self.getPageNumber()
        params = {k:d[k] for k in d if k != 'self'}

        self.queue.append(params)
        self.incrementDenomenator()
        # print(params)
        
        # CorePostCreator().createSlide(**params)


    def addFrontCover(self, imagePath = 'zezi.jpg', title='Les 5 Actus du', sub_title='', frameColor='', swipeIconColor = (242,242,242)):
        
        if self.frontCover:
            print('You can only add a single Front Cover per Post/n')
            return


        self.frontCover = True
        if not isinstance(swipeIconColor, tuple):
            if len(swipeIconColor) != 3:
                print('swipeIconColor should be a 3-value [0,255] RGB tuple.')
                print('front cover failed to render.')

                return

        
        d = locals()
        d['finalImageSavePath'] = self.saveDir + '\\' + 'slide' + '0' +self.imageSaveFormat
        params = {k:d[k] for k in d if k != 'self'}
        # print(params)
        self.queue.insert(0,params)
       
        


    def getSavePath(self):
        pg_num = self.saveDir + '\\' + 'slide' + str(self.pageNumber)+self.imageSaveFormat
        return pg_num

    def getPageNumber(self):
        return str(self.pageNumber)

    def incrementPageNumber(self):
        self.pageNumber +=1



    def skipAPage(self):
        self.pageNumber+=1
        self.incrementDenomenator()


    def __incrementDenomenator(self):
        self.denomenator+=1

    def incrementDenomenator(self):

        self.__incrementDenomenator()

        #print(self.queue)
        for i,d in enumerate(self.queue):

            if self.frontCover and i == 0:
                continue

            d['denomenator'] = str(self.denomenator)
           




    def showLast(self):
        params = deepcopy(self.queue[-1])
        params['finalImageSavePath'] = ''
        # print(self.queue[-1])
        CorePostCreator().createSlide(**params)



    def compile(self,Imagespath = 'articleImages', fList =[]):
        
        if Imagespath:

            '''Automatic path labelling requires the right image name for each slide.
            For example, if you are rendering the cover, you have provide a image0.png.
            if you then skipped a page. now u r rendering slide 2 since slide 1 has been skipped,
            you have to provide an image1.jpg. 
            Note slide0 is always the front cover.'''

            self.__automaticImagePathLabelling(Imagespath, fList)

        if self.frontCover:
            front, slides = self.queue[0], self.queue[1:]

            print(front['finalImageSavePath'])
            
            CorePostCreator().frontPage(**front)


        else:
            slides = self.queue

        
        for d in slides:
            print(d['finalImageSavePath'])
            CorePostCreator().createSlide(**d)




    # def showPrevious(self):
    #     if not self.frontCover:
    #         CorePostCreator().createSlide(**self.queue[self.pageNumber])

    #     else:
    #         CorePostCreator().createSlide(**self.queue[self.pageNumber + 1])


    
    def __automaticImagePathLabelling(self, path, fList = []):

        for i, d in enumerate(self.queue):
            d['imagePath']= path + '\\' +((d['finalImageSavePath'].split('\\'))[-1]).replace('slide', 'image')
            if fList:
               d['imagePath']= d['imagePath'].split('.')[0] + fList[i]

            # print(d['imagePath'])


    def slidesRundown(self):
        pass


    def setSaveDir(self, newval:str):
        if len(newval)>0:
            while newval[-1] == '/' or newval[-1] == '\\' :
                newval = newval[:-1]

        self.saveDir = newval














