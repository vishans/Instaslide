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





# slide images are already in a specific folder
# the program will visit the folder
# and use the correct image for each slide
# note that the front cover is called slide0      



# creating the post
p = Post()

# adding front cover
title = '<#494F55>Ban aktialité</#494F55>'
sub_title = '<#494F55>20&/01</#494F55>'
p.addFrontCover(frameColor='#7C7C7C', title = title, sub_title=sub_title, swipeIconColor=(73, 79, 85))

# p.addFrontCover()
#

article = '''Plizier lendroit dans <red>M</red><blue>or</blue><gold>i</gold><green>s</green> ti <blue>innondé</blue> hier akoz tiena <blue>gro lapli</blue>. <blue>Piton</blue> ou Pitan comme dirait arjoon, ti emba délo. La route ti innondé - délo ti p fini rent dans bus tout.
Dan le sud si ban place couma <blue>La Flora</blue> ek <blue>Rose Belle</blue> inn bien gagné.
Bnla p dire tiena <#3944BC>vague</#3944BC> tout dans <#3944BC>lopital Rose Belle</#3944BC>.
<gray>Vidéo lor 2 prochain page</gray>'''

p.addSlide(article=article, flairColor='#1338BE', flairText='Pié dan lo')


p.skipAPage()
p.skipAPage()

#

article ='''Encore dans thème gros lapli meme. <red>Madagascar</red> finn experience ban <orangered>la pli torrentiel</orangered> ces derniers zours. Dan capital, Antananarivo, plis ki <orangered>500</orangered> dimoune in <orangered>perdi zot lakaz</orangered>. 
Ek <red>10 dimoune in mort</red>. La plipart ban victime la in périr dans <orangered>glissement terrain</orangered>. Ban Malgache p attan zot à encore plis lapli.
Ban expert p dir sa ban gros lapli la p arrivé akoz <red>dérèglement climatique</red>. '''

p.addSlide(article=article, flairColor='grey',flairText='madagascar')

#

article = '''Ena enn rézo <hotpink>prostitution</hotpink> ki p deroule dans l'ouest. Dapre lord cervo operation la enn <orangered>couple franco-morisien</orangered>. Banla amen fam dpi la <red>Russie</red> ek <red>Ukraine</red> pou chocho. Selmn ban fam la <red>pa rod chocho avec morisien</red> zot rod zis <red>etranzé</red>. Cervo la ti dir enn des ban prostitué la, Liudmila, dormi avc enn morisien. Fam la pann dakor. Lerlaem caca in alle fanné. Liudmila in alle dévwal zot secret la police. By the way, enn la nuit coute <red>Rs 130 000</red>.'''

p.addSlide(article=article, flairText='seks', flairColor='hotpink')

article = '''Tiena enn <red>eruption volcanique</red> dan <red>Tongatapu</red>, enn <orangered>l'île</orangered> dan l'océan Pacfique. Sa inn déclanse enn <blue>tsunami</blue>. Omoin <red>3 dimoun in mort</red> ek <orangered>150 lakaz in endomazé</orangered>. L'Australie, la France ek Nouvelle Zelande p rod avoy laide, mais avion pas p kav atterrir akoz ena enta lasann volcanique.
<gray>Tongatapu cest l'île principal Tonga, enn group l'île dans l'océan Pacifique. Tongatapu </gray><red>meme</red><gray> grandeur ar district</gray> <orangered>Rivière Noire</orangered>.'''

p.addSlide(article=article, flairText='tongatapu')


article = '''L'<red>Allemagne</red> ek <red>Brésil</red> finn enregistré enn <red>record</red> nombre cas <crimson>covid</crimson> <red>sans précédent</red> en 1 zour.
<red>Australie</red> so main dev in paralysé akoz virus la. Ban expert p dire cest <red>Omicron</red> ki p kass fess coumsa la. <red>Japon</red> so gouvernment inn dir li pou récoumense met restriction en place. La <red>Chine</red> inn arrete vende ticket pou <blue>Jeux olympiques d'hiver</blue> akoz covid. <gray>JO d'hiver sipozé ena lieu à Pékin (Beijing) le 4 ziska le 20 février 2022.</gray> '''

p.addSlide(article=article, flairText='covid-19',flairColor='#99241C')




article ='''<orangered>Microsoft</orangered> inn asté <orangered>Activision Blizzard</orangered> pou <red>$69 milliard</red>. 
Activision meme ki develop ban zoué kouma <orangered>Call of Duty</orangered>, <orangered>Candy Crush</orangered> ek <orangered>World of Warcraft</orangered>. Microsoft pou met sa ban zoué dans so Xbox Game Pass.'''


p.addSlide(article=article, flairText='tech',flairColor='silver')

# p.addFrontCover()



p.compile(fList=['.jpg']*2 + ['.jfif']+['.jpg']*2 + ['.jpeg', '.jpg'])






