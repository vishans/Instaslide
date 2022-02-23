
from post import Post


'''Always use the  post API to generate slides or story slides.
Do NOT use CorePostCreator. 
Post is a wrapper around CorePostCreator to abstract and simplify it's operation.
Use CorePostCreator only if you need to modify core parameters that can't be modified through Post.
Beware that CorePostCreator was not designed to be used by the user.'''

p = Post()

p.addFrontCover(frameColor='red')

p.addSlide(article='hel')

p.addSlide(article='zizag', backgroundImage='poster', PosterbackgroundColor='black')



p.compile()