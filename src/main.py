from matplotlib.pyplot import title
from post import Post


'''Always use the  post API to generate slides or story slides.
Do NOT use CorePostCreator. 
Post is a wrapper around CorePostCreator to abstract and simplify it's operation.
Use CorePostCreator only if you need to modify core parameter not possible through Post.
Beware that CorePostCreator was not designed to be used by the user.'''


p = Post()

p.addFrontCover()

# slide 1

article = '''<red>Pena lekol zordi</red>. To kav rémonte lor lili.
A 4hr du matin, <red>Moris</red> touzour en alerte cyclonik <red>class III</red>.
<red>Batsirai</red> li à <red>210km</red>  <red>nord-nord-est</red> Moris.
Si li contine coumsa, li kav pou pass 120km <red>pres</red> ar <red>Grand Baie ver midi parla</red>.
'''

p.addSlide(article=article, flairText='Pena lekol - cyclone class 3', flairColor='red')

article = '''Ban <red>pays Occidentaux</red> finn <red>refiz</red> ban proprozition la <red>Russie</red>. Enn de sa ban propozition la ct <red>arrete elarzisment NATO</red>. B <red>Ukraine</red> p rod <red>rentre dans NATO</red> la. Saem p truv Putin p bend koumsa.
Nou pas tro koné ki Putin p plan pou fer la. Li dire li envi <red>négocier</red>. Boris Johnson, l'Angleterre so PM, p dir la Russie present enn danzer pou Ukraine. '''

p.addSlide(article=article, flairText='ukraine', flairColor='red')


article = '''<red>Apple</red> inn azoute <red>ban nouvo emoji</red> dans <red>iOS 15.4</red>.
Parmi sa ban emoji la banla finn azout bann emoji 
<red>zom enceint</red>. Sa p fer polémik.

'''
p.addSlide(article=article, flairText='Apple')

article = '''Kan enn dimoune ena <red>diabete type 1</red>, so lekor so system immunitaire <red>detruire</red> so <red>insuline</red>. <red>Insuline</red> c enn <red>hormone</red> ki <red>balance nivo disik dan disan</red>. Insuline li normalmen prodir par to <red>pancreas</red>. L'<red>Université Cambridge</red> in develop enn <red>implant</red> pou aide ban <red>zenfan diabétik</red>. Zafer la control nivo disik zenfan la <red>otomatikmen</red>. Ban zenfan ena enn ti <red>app lor zot portable</red> ki link avec implant la tout.'''

p.addSlide(article=article, flairText='Pancreas Artificiel')



article = '''The <red>UN's World Meteorological Organization (WMO)</red> inn annoncé ki <red>2021</red> ti parmi <red>top 7 ban lannée kot ti fer pli so</red>.
WMO in dir ki sa c enn <red>leffet direk</red> de <red>resofmen la Terre</red> ek <red>sanzment climatik</red>. Ena tro boukou <red>gaz a effet de serre</red> dans latmosphere. A <red>COP26</red>, en novam lannée derniere, ban dirizan ban pays finn <red>koz ennta</red> soidizan zot pou arret sa. Mais ziskaler zot pas p fer em <red>nnier</red>...
'''

p.addSlide(article=article, flairText='sanzment climatik')

article = '''<red>Mason Greenwood</red>, enn <red>attakan Man Utd</red>, finn etre akizé de <red>viol</red> ek <red>aggression</red> lor so copine (aster so ex-copine). Banla inn fini met Greenwood dan caso. Fam la, <red>Harriet Robson</red>, inn posté enn <red>recording audio</red> ek ban <red>foto</red> lor Instagram pou <red>montré kot linn ggn baté</red>. Banla inn ouvert enn lenket. <red>La justice pencor prononce Greenwood coupab.</red>
<red>EA</red> inn dir zot p <red>tir</red> Greenwood dans <red>FIFA 22</red>. '''

p.addSlide(article=article, flairText='prison fc', flairColor='red')


p.compile()


