from post import Post


'''Always use the  post API to generate slides or story slides.
Do NOT use CorePostCreator. 
Post is a wrapper around CorePostCreator to abstract and simplify its operation.
Use CorePostCreator only if you need to modify core parameters not possible through Post.
Beware that CorePostCreator was not designed to be used by the user.'''
