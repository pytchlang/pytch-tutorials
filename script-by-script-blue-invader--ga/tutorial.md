# Ionróirí Gorma

Sa chluiche seo, déanfaidh an t-imreoir an domhan a chosaint ó
ionróirí gorma contúirteacha trí chliceáil orthu. Ach ní féidir leis
an imreoir na heachtráin ghlasa chairdiúla a mharú trí dhearmad!

---

## Socraigh an cúlra

Is é an chéad rud atá le déanamh ná an cúlra dár gcluiche a
chruthú. Tá íomhá de réaltra i leabharlann meán Pytch, ar féidir linn
í a úsáid.

{{< learner-task >}}

Cuir an cúlra “galaxy” leis an Ardán ón leabharlann meán.

{{< learner-task-help >}}

{{< jr-commit add-starry-backdrop add-medialib-appearance ["galaxy.png"] >}}

{{< /learner-task >}}

Má ritheann tú do chluiche anois, ní fheicfidh tú do chúlra nua. An
chúis atá leis seo ná go bhfuil an cúlra bán soladach réamhshocraithe
fós san Ardán, agus is é an cúlra sin an chéad cheann, mar sin is é
sin an ceann a thaispeántar.

{{< learner-task >}}

Scrios an cúlra `solid-white.png` ón ardán.

{{< learner-task-help >}}

{{< jr-commit remove-white-backdrop delete-appearance >}}

{{< /learner-task >}}

Cliceáil ar an gcnaipe seinnte glas anois — ba cheart duit cúlra nua
an chluiche a fheiceáil.

## Cruthaigh an chéad eachtrán

Nuair a bheidh sé críochnaithe, beidh go leor eachtrán sa chluiche,
ach ní bheidh ach ceann amháin ann ar dtús.

Beidh sprid `Alien` ann a mbeidh cultacha éagsúla air.  Nuair a bhíonn
culaith amháin ar an sprid seo (ceann gorm), meastar gur ionróir spáis
naimhdeach é, agus nuair a bhíonn culaith eile air (ceann glas), is
cuairteoir cairdiúil é. (Ní mór don ainm sin a bheith i mBéarla toisc
gur cuid den chód é.)

### Cruthaigh sprid _Alien_

Teastaíonn sprid nua ón togra le bheith mar eachtrán.

{{< learner-task >}}

Cuir sprid darb ainm `Alien` le do thogra.

{{< learner-task-help >}}

{{< jr-commit create-alien-sprite add-sprite >}}

{{< /learner-task >}}

### Tabhair roinnt cultacha don _Alien_

Ansin, teastaíonn cultacha ón sprid nua. Tá bearta de chultacha
oiriúnacha i leabharlann meán Pytch.

{{< learner-task >}}

Cuir beart na n-íomhánna ‘Space aliens’ ón leabharlann meán leis mar
chultacha don sprid `Alien`. (Ní mór don ainm “Space Aliens” a bheith
i mBéarla. Eachtrán spáis an Ghaeilge atá air sin.)

{{< learner-task-help >}}

{{< jr-commit add-alien-costumes add-medialib-appearances-entry ["Space aliens"] >}}

{{< /learner-task >}}

Má ritheann tú do thogra anois, ba cheart duit ionróir naimhdeach gorm
a fheiceáil I lár an scáileáin. Is amhlaidh atá sé sin toisc go
gcuireann Pytch tús le sprid agus a chéad chulaith air.

{{< learner-task >}}

Bain triail as do chluiche. Cad atá cearr?

{{< learner-task-help >}}

Tá an t-eachtrán i bhfad rómhór!

{{< /learner-task >}}

### Caithfear an t-eachtrán a dhéanamh ar mhéid réasúnta

An chéad rud ba chóir don eachtrán a dhéanamh ná a mhéid a shocrú go
go méid éigin atá níos réasúnta.

{{< learner-task >}}

Cuir script nua fholamh leis an sprid `Alien` le bloc hata “nuair a
chliceáiltear an bhratach ghlas”.

{{< learner-task-help >}}

{{< jr-commit add-drift-down-skeleton add-script >}}

{{< /learner-task >}}

Ní mór don chód sa script seo méid an alien a shocrú. In Pytch,
ciallaíonn méid `1` an bunmhéid, ciallaíonn `0.5` leathmhéid, agus mar
sin de.  Is féidir leat a sheiceáil go bhfuil méid `0.15` ceart go
leor.

{{< learner-task >}}

Cuir cód le do script a shocraíonn méid an alien ag `0.15`.

{{< learner-task-help >}}

{{< jr-commit set-Alien-size edit-script >}}

{{< /learner-task >}}

### Cuir an alien ag bogadh síos an scáileán

Ba chóir don eachtrán sleamhnú ó bharr an scáileáin go dtí an bun,
ansin dul ar ais go dtí an barr ar an bpointe agus tosú ag sleamhnú
arís.

Is féidir leat cód a chur le do script a oibríonn ar an tslí chéanna
le bloc *síoraí* Scratch. In Python, is féidir leat `while True:` a
scríobh, agus línte *eangaithe* a chur isteach faoi chun an méid ba
chóir a bheith ag tarlú a chur in iúl.

Mar shampla, seo cód a bhogann sprid go mall trasna an scáileáin:

``` python
while True:
    self.change_x(1)
```

{{< learner-task >}}

Cuir cód le deireadh do scripte a chuireann faoi deara don alien dul
go barr an scáileáin agus ansin sleamhnú go dtí an bun arís agus arís
eile.

{{< learner-task-help >}}

Chun a rá leis an eachtrán dul chuig áit ingearach shonrach ar an
scáileán, is féidir leat rud éigin mar seo a leanas a úsáid

``` python
self.set_y(50)
```

Is é an uimhir `50` anseo an comhordanáid *y* ar chóir don eachtrán
dul chuici.  Níl an chomhordanáid *x* tar éis athrú. Bogfaidh an alien
go díreach suas nó síos.

{{< learner-task-help >}}

Chun a chur ina luí ar an alien bogadh go réidh go háit éagsúil ar an
scáileán, is féidir leat rud éigin ar nós

``` python
self.glide_to_xy(0, -50, 2.5)
```

a úsáid. Is comhordanáidí *x* agus *y* iad na huimhreacha ar chóir don
eachtrán dul chucu, agus cé chomh fada (líon na soicindí) a ghlacfaidh
sé chun bogadh ann. B'fhéidir go mbeadh sé úsáideach duit úsáid a
bhaint as

``` python-expression
self.x_position
```

seachas uimhir *x* dáiríre, ag féachaint chun cinn go dtí go mbeidh
an-chuid eachtrán ann, agus suíomh *x* féin ag gach ceann acu.

{{< learner-task-help >}}

{{< jr-commit add-drift-down-body edit-script >}}

{{< /learner-task >}}


## Meascán d'eachtráin naimhdeacha agus chairdiúla

Ní mór roinnt de na aliens a shleamhnaíonn síos an scáileán a bheith
ina naimhde, agus roinnt acu a bheith cairdiúil. Cuimhnigh go ndéantar
é seo trí chur faoi deara don alien culaith éagsúil a chaitheamh.

Díreach mar atá in Scratch, is féidir leat an chulaith a athrú trí áit
nua na culaithe ar an liosta cultacha a thabhairt, nó trína ainm a
thabhairt. Sa chas seo beidh sé beagán níos éasca an chulaith a roghnú
de réir a áite ar an liosta. Is féidir leat breathnú ar an táb
“Cultacha” chun na cultacha atá atá ar fáil a fheiceáil agus cén t-ord
ina bhfuil siad.

In Python:

* úsáideann daoine an focal _innéacs_ chun a rá cén áit ar an liosta
  atá rud éigin;

* liostaítear rudaí ar liosta ó *náid*, mar sin tá an chéad rud ar
  liosta mar seo ‘index&nbsp;0’, an dara rud ‘index&nbsp;1’, agus mar
  sin de.

Maidir lenár n-eachtráin, is iad na cultacha ag index&nbsp;0 agus
index&nbsp;2 na cinn chearta, mar sin ba chóir don chód ceann acu sin
a roghnú go randamach as na huimhreacha sin.

*D'fhéadfaí* é sin a dhéanamh ar fad i líne chóid amháin, ach má
roinntear an tasc ina dhá chéim é, beidh sé níos éasca le tuiscint:

* Roghnaigh innéacs culaithe go randamach (0 nó 2).

* Athraigh go dtí an chulaith roghnaithe

### Roghnaigh an chulaith go randamach

Déanfaidh an fheidhm `random.choice(list_of_choices)` an jab sin.

Teastaíonn *liosta* roghanna ón bhfeidhm `random.choice()` ónar cheart
rogha a dhéanamh. Anseo, is iad `0` agus `2` na roghanna. In Python,
scríobhtar an liosta ina bhfuil `0` agus `2` mar `[0, 2]`.

{{< learner-task >}}

Cuir líne chóid leis a roghnaíonn `0` nó `2` go randamach chun a
bheith mar innéacs na culaithe nua, agus a stórálann an rogha in
athróg ar a dtugtar `costume_index`.

{{< learner-task-help >}}

Ba cheart an cód nua a chur ag barr an choirp eangaithe den lúb `while
True`.

{{< learner-task-help >}}

{{< jr-commit choose-random-costume edit-script >}}

{{< /learner-task >}}

### Athraigh go dtí an chulaith roghnaithe

Nuair a bheidh an uimhir roghnaithe in athróg, is féidir leis an
eachtrán athrú go dtí an chulaith sin.

{{< learner-task >}}

Cuir líne chóid leis a athraíonn go dtí an chulaith a bhfuil a
hinnéacs in athróg `costume_index`.

{{< learner-task-help >}}

{{< jr-commit switch-to-chosen-costume edit-script >}}

{{< /learner-task >}}

### Bain triail as!

{{< learner-task >}}

Bain triail as do chluiche. Má ritheann tú an togra, ba cheart duit
eachtrán a fheiceáil ag sleamhnú síos ar an scáileán. Ba chóir go
mbeadh meascán randamach de cinn ghorma agus cinn ghlasa ann.

{{< /learner-task >}}


## Déan níos mó eachtrán

Chun níos mó ná eachtrán amháin a dhéanamh, bainfidh an clár úsáid as
*clóin*. Oibríonn siad mar a oibríonn siad in Scratch — faigheann tú
níos mó ná cóip amháin den sprid chéanna.

Déanfaidh an clár an t-eachtrán a chlónáil cúig huaire. In éineacht
leis an gcéad eachtrán, tá sé eachtrán ann san iomlán.

Ag baint úsáid as na suíomhanna *x*, bogfaidh

> -150, -90, -30, 30, 90, agus 150

na heachtráin ó chlé go deas trasna an scáileáin.

Seo an smaoineamh:

* Bog an buneachtrán go dtí an chéad áit (suíomh *x* de `-150`).

* Cruthaigh clón ag an suíomh sin, ansin bog an buneachtrán go dtí an
  chéad áit eile (`x = -90`).

* Cruthaigh clón eile, agus bog an buneachtrán go `x = -30`.

* agus mar sin de.

{{< learner-task >}}

Cuir script *bratach ghlas* fholamh leis an eachtrán.

{{< learner-task-help >}}

{{< jr-commit add-make-clones-script add-script >}}

{{< /learner-task >}}

Tá cód de dhíth ar an script sin anois chun na clóin nua a chruthú
agus a bhogadh.

{{< learner-task >}}

Cuir líne chóid leis an script seo a bhogann an t-eachtrán go dtí an
áit ar an ardán ag suíomh *x* `-150` agus suíomh *y* `180`.

{{< learner-task-help >}}

{{< jr-commit move-first-alien-to-position edit-script >}}

{{< /learner-task >}}

{{< learner-task >}}

Cuir dhá líne chóid leis an script seo. Ba cheart don chéad líne clón
a dhéanamh den eachtrán. Ba cheart don dara líne an buneachtrán a
bhogadh go dtí an áit ar an ardán ag suíomh *x* `-90` agus suíomh *y*
`180`.

{{< learner-task-help >}}

{{< jr-commit make-first-clone edit-script >}}

{{< /learner-task >}}

{{< learner-task >}}

Cuir an chuid eile den chód is gá leis, a bheidh an-chosúil leis na
cóipeanna de na línte a chuir tú leis anois díreach. Ba cheart go
mbeadh clóin agat ag suíomhanna *x*

> -150, -90, -30, 30, agus 90

agus an buneachtrán ag suíomh *x* 150.

{{< learner-task-help >}}

{{< jr-commit make-rest-of-clones edit-script >}}

{{< /learner-task >}}

(B'fhéidir go gceapann tú go bhfuil bealach níos fearr ann chun é seo
a dhéanamh ná cód atá beagnach mar an gcéanna a chóipeáil agus a
ghreamú. Tá an ceart agat, ach tá sé sin lasmuigh de scóp an teagaisc
seo!)

### Bain triail as!

{{< learner-task >}}

Bain triail as do chluiche. Cad a tharlaíonn?

{{< learner-task-help >}}

Tagann níos mó eachtrán i láthair, ach ní bhogann ach ceann amháin acu.

{{< /learner-task >}}

### Ní oibríonn sé mar is ceart!

Má ritheann tú an cluiche anois, ní oibríonn sé i gceart dáiríre. Tá
níos mó eachtrán ag barr an scáileáin, ach níl ach ceann amháin acu ag
sleamhnú síos.  Tá sé sin amhlaidh toisc nach dtugann Pytch aon
ghealltanas faoin ord ina rithfear an dá script *bratach ghlas*, agus
tá an script faoin sleamhnú ag tarlú sula ndéantar na clóin go léir.

Mínítear sa chéad chaibidil eile conas é sin a réiteach.


## Craoltaí a úsáid chun rialú a dhéanamh ar an uair a rithtear scripteanna

Chun a chinntiú go dtarlaíonn gach rud san ord ceart, úsáidfidh an
clár píosa eile ó Pytch a bhféadfadh eolas a bheith agat faoi ó
Scratch — *craoltaí*. Is féidir le sprid teachtaireacht a ‘bhéiceadh’,
agus is féidir le haon sprid (an sprid chéanna a rinne an bhéic san
áireamh!) a bheith ag éisteacht leis an teachtaireacht sin, agus cód
éigin a rith aon uair a chloisfidh an sprid an teachtaireacht.

Ní mór don chlár a chinntiú go ndéanfar na clóin go léir sula dtosóidh
an sleamhnú. Beidh an tArdán i gceannas chun é sin a chur i gcrích.

Ós rud é go n-úsáidfidh an clár craoltaí chun rudaí a chomhordú, ní
mór don script a scríobh tú díreach anois, a chruthaíonn na clóin go
léir, rith nuair a nuair a fhaigheann sé teachtaireacht chraolta chuí.

{{< learner-task >}}

Cuir an script a chruthaíonn na clóin go léir ag rith nuair a
fhaigheann an t-eachtrán an teachtaireacht `"make-clones"` a fháil (ní
nuair a chliceáiltear ar an mbratach ghlas).

{{< learner-task-help >}}

Fanann an cód mar an gcéanna. Ní gá duit ach bloc hata na scripte a
athrú. Tá sé sin cosúil leis an uair a bhaineann tú bloc hata scripte
in Scratch agus ceann difriúil a cheangal leis.

{{< learner-task-help >}}

{{< jr-commit make-clones-when-receive change-hat-block >}}

{{< /learner-task >}}

{{< learner-task >}}

Cuir script *bratach ghlas* **leis an ardán** a chraolann an
teachtaireacht `"make-clones"`, agus a fhanann go gcríochnóidh na
scripteanna éisteachta ag rith. Tá ciall leis an script a chur leis an
ardán toisc gurb é an áit lárnach é chun an cód rialaithe ardleibhéil
go léir a chur.

{{< learner-task-help >}}

{{< jr-commit broadcast-make-clones add-script >}}

{{< /learner-task >}}

### Fan go mbeidh na clóin go léir ann sula dtosaíonn an sleamhnú

Úsáideann an cód a chuir tú leis díreach anois
`broadcast_and_wait()`. Díreach mar atá in Scratch, ní théann do chlár
ar aghaidh go dtí an chéad ráiteas eile go dtí go mbeidh gach rud atá
ag éisteacht leis an teachtaireacht `"make-clones"` críochnaithe ag
déanamh pé rud a dhéanann siad nuair a chloiseann siad é. Mar sin, ní
rithfidh aon chód i ndiaidh `broadcast_and_wait()` go dtí go mbeidh na
clóin go léir ann.

Seo mar is féidir leis an gclár an uair a thosaíonn na heachtráin ag
sleamhnú a rialú.

{{< learner-task >}}

Athraigh do chlár ionas go rithfidh an cód sleamhnaithe sa sprid
`Eachtrán` nuair a chloiseann eachtrán (an buneachtrán nó clón)
teachtaireacht `"play-game"` (agus ní nuair a chliceáiltear ar an
mbratach ghlas).

{{< learner-task-help >}}

Díreach mar a bhí nóiméad ó shin, fanann an cód mar an gcéanna. Níl le
déanamh agat ach bloc hata na scripte a athrú.

{{< learner-task-help >}}

{{< jr-commit descend-on-play-game-broadcast change-hat-block >}}

{{< /learner-task >}}

### Bain triail as!

{{< learner-task >}}

Bain triail as do chluiche. Cad a tharlaíonn? Cén fáth?

{{< learner-task-help >}}

Fanann _gach_ eachtrán ag barr an scáileáin. Ní ritheann an cód
sleamhnaithe ach amháin nuair a chraolann duine éigin an
teachtaireacht `"play-game"`, agus níl aon duine á dhéanamh sin.

{{< /learner-task >}}

Anois is féidir leat cód a chur san áit cheart a chraolann an
teachtaireacht ar bhfuil na heachtráin ag fanacht.

{{< learner-task >}}

Cuir faoi deara don Ardán an teachtaireacht `"play-game"` a chraoladh,
nuair a bheidh na clóin go léir cruthaithe.

{{< learner-task-help >}}

{{< jr-commit broadcast-play-game edit-script >}}

{{< /learner-task >}}

### Bain triail as!

{{< learner-task >}}

Rith do thogra. Ba chóir duit tonnta eachtrán a fheiceáil ag sleamhnú
síos an an scáileáin, meascán de chinn ghorma agus ghlasa gach
uair. (Uaireanta, de sheans gheobhaidh tú tonn atá go hiomlán gorm nó
atá go hiomlán glas.)

{{< /learner-task >}}

Tá sé sin ceart go leor, ach bheadh sé níos fearr dá rachadh roinnt
eachtrán níos tapúla ná cinn eile.


## Déan an t-am sleamhnaithe randamach

I láthair na huaire, glacann gach clón eachtráin go díreach
3&nbsp;seconds chun sleamhnú síos an scáileán. Bheadh an cluiche níos
fearr le beagán éagsúlachta, trí chur faoi deara do gach clón eachtrán
am randamach a ghlacadh chun sleamhnú síos an scáileán.  Mar thoradh
air sin bogfaidh eachtráin áirithe níos tapúla ná cinn eile agus beidh
sé níos suimiúla.

Ní mór cód alien `"play-game"`a athrú ionas go nglacfaidh gach
eachtrán am randamach idir, abair, 3 agus 5 shoicind.

Úsáideann do chlár `random.choice()` cheana féin. Tá an fheidhm
`random.uniform()` in Python chomh maith, a roghnaíonn uimhir
randamach áit ar bith idir dhá theorainn. Is féidir le do chlár é sin
a úsáid chun uimhir randamach a fháil aon áit idir 3.0 agus 5.0
(codáin san áireamh).

{{< learner-task >}}

I script `"play-game"` an eachtráin, cuir líne chóid leis díreach
roimh an `self.glide_to_xy()` a úsáideann `random.uniform()` chun
uimhir randamach idir 3 agus 5 a fháil agus a chuireann an toradh le
hathróg ar a dtugtar `glide_time`.

{{< learner-task-help >}}

Ginfidh an abairt Python

``` python-expression
random.uniform(3.0, 5.0)
```

an uimhir randamach atá uait.

{{< learner-task-help >}}

Cuimhnigh gur úsáid tú an cód

``` python
costume_index = random.choice([0, 2])
```

chun rogha randamach a dhéanamh ón liosta `[0, 2]`, agus an toradh a
chur leis an athróg `costume_index`. Is mian leat rud éigin cosúil
leis sin a dhéanamh.

{{< learner-task-help >}}

Tá uimhir randamach uait anseo aon áit idir 3 agus 5, agus aon chodán
san áireamh. Déanfaidh an fheidhm

``` python-expression
random.uniform()
```

é sin duit. Féach sa chabhair chun a fháil amach conas é a úsáid.

{{< learner-task-help >}}

{{< jr-commit define-glide-time edit-script >}}

{{< /learner-task >}}

Anois is féidir leat an athróg seo a úsáid chun a chur in iúl cé chomh
fada ba cheart don ghluaiseacht sleamhnaithe a bheith.

{{< learner-task >}}

Athraigh an cód atá ann cheana chun an athróg nua `glide_time` a úsáid
in ionad uimhir sheasta `3.0` san fheidhm `glide_to_xy()`.

{{< learner-task-help >}}

{{< jr-commit use-glide-time edit-script >}}

{{< /learner-task >}}

### Bain triail as!

{{< learner-task >}}

Rith do thogra. Ba chóir duit roinnt eachtrán a fheiceáil ag titim
níos tapúla ná na cinn eile, agus tar éis tamaill ghearr is cosúil go
bhfuil na heachtráin ag teacht i láthair go randamach.

{{< /learner-task >}}


## Cliceáil ar na heachtráin!

Anois tá cuma an-deas ar do thogra, ach ní *cluiche* é toisc nach
bhfuil aon rud le déanamh ag an imreoir. Sin é an chéad jab eile.

### Freagair tar éis a bheith buailte

Ba chóir do na heachtráin (an buneachtrán agus na clóin) freagairt
nuair a chliceálann an t-imreoir orthu.

{{< learner-task >}}

Cuir script *nuair-a-chliceáiltear-an-sprid-seo* le do sprid `Alien`.

{{< learner-task-help >}}

{{< jr-commit add-when-hit-skeleton add-script >}}

{{< /learner-task >}}

Anois go bhfuil an script agat, ní mór duit a chód a scríobh.

{{< learner-task >}}

Cuir cód le do script nua a chuireann faoi deara don eachtrán é féin a
chur faoi cheilt.

{{< learner-task-help >}}

{{< jr-commit hide-when-hit edit-script >}}

{{< /learner-task >}}

### Bain triail as!

{{< learner-task >}}

Rith do chluiche. Seiceáil an féidir leat cliceáil ar na heachtráin
chun iad a chur ó radharc.

{{< /learner-task >}}

Ach anois tá fadhb eile ann — nuair a chliceálann an t-imreoir ar
eachtrán, ní thagann an t-eachtrán ar ais ar an scáileán arís.

### Tagann sé ar ais i láthair ag barr an scáileáin

Ní mór do gach eachtrán a chinntiú go bhfuil sé le feiceáil díreach
sula dtosaíonn sé ag sleamhnú síos an scáileán.

{{< learner-task >}}

Smaoinigh ar an áit i gcód spride do `Alien` ar chóir duit a chinntiú
go bhfuil gach eachtrán le feiceáil, agus cuir cód leis chun é sin a
dhéanamh.

{{< learner-task-help >}}

Cuimhnigh go rialaítear gluaiseacht na n-eachtrán le cód sa script
`"play-game"`.

{{< learner-task-help >}}

Áit mhaith chun an t-eachtrán le cur ar taispeáint ná tar éis dó
culaith randamach a roghnú agus tar éis dó bogadh go barr an
scáileáin, ach sula sleamhnaíonn sé síos an scáileán.

{{< learner-task-help >}}

{{< jr-commit show-when-starting-descent edit-script >}}

{{< /learner-task >}}

### Bain triail as!

{{< learner-task >}}

Rith do chluiche. Ba cheart do na heachtráin teacht ar ais ar an
scáileán tar eis duit cliceáil orthu.

{{< /learner-task >}}


## Coimeád an scór

Chun a chur in iúl don imreoir conas atá ag éirí leo, ba chóir don
chluiche scór a choimeád.  Díreach mar atá in Scratch, cuimhníonn do
chlár ar uimhreacha (nó teaghráin, nó liostaí, nó aon rud eile) ag
baint úsáid as *athróg*. In Python, ní gá duit athróg a dhéanamh go
sainráite. Má shocraíonn tú athróg nua le luach cruthaíonn sé an
athróg sin duit.

### Tosaigh an scór ag náid

Coinneoidh an tArdán súil ar scór an imreora, in athróg a bhaineann
leis an Ardán.

Mar shampla, chun athróg `time` a bhaineann leis an Ardán a chruthú,
chun luach `60` a shocrú leis, bheadh an cód mar seo a leanas

``` python
Stage.time = 60
```

{{< learner-task >}}

Bain úsáid as an sampla seo chun cód a scríobh a shocraíonn athróg
Ardán `score` ar luach `0`. Ba chóir an athróg sin a chruthú nuair a
thosaíonn do chlár ag rith, mar sin, smaoinigh ar an áit ar chóir don
chód a bheith curtha.

{{< learner-task-help >}}

Chun a chinntiú go rithfidh an cód nua ag tús an chluiche, ba cheart é
a chur ag barr script *bratach ghlas* an Ardáin.

{{< learner-task-help >}}

{{< jr-commit define-global-score edit-script >}}

{{< /learner-task >}}

### Taispeáin an scór

In Scratch, cuireann tú tic i mbosca chun a rá gur mian leat an athróg
a bheith feicthe. In Pytch déanann tú é sin trí roinnt cóid a
scríobh. Ba chóir athróg `scór` an Ardáin a thaispeáint a luaithe a
thosaíonn an cluiche, díreach tar éis don athróg a bheith cruthaithe.

Mar shampla, chun athróg `am` a bhaineann leis an Ardán a chruthú,
d'fhéadfá an cód seo a chur le script san Ardán:

``` python
self.show_variable("time")
```

Tá an bealach a n-oibríonn sé seo neamhghnách — úsáideann tú *ainm* na
hathróige, scríofa mar *teaghrán*. Tá an fáth leis seo lasmuigh de
scóp an teagaisc seo!

{{< learner-task >}}

Cuir cód leis a thaispeánann athróg `score` an Ardáin. Smaoinigh faoin
áit ar chóir an cód sin dul.

{{< learner-task-help >}}

Ba chóir go mbeadh an cód díreach i ndiaidh an chóid a chruthaíonn an
athróg `Stage.score`. (Caithfidh “Stage” anseo a bheith i mBéarla, sin
an focal Béarla ar Ardán.)

{{< learner-task-help >}}

{{< jr-commit show-score edit-script >}}

{{< /learner-task >}}

### Tabhair pointí as namhaid a bhualadh

Tabharfaimid 10&nbsp;points don imreoir nuair a chliceálann siad ar
ionróir naimhdeach. Tá roinnt cóid ann cheana a chuireann ar an
eachtrán é féin a cheilt nuair a chliceáiltear air, mar sin is áit
mhaith é seo chun an cód a chur leis a dhéanann uasdátú ar an scór.

{{< learner-task >}}

Cuir cód leis a thugann deich bpointe don imreoir gach uair a
chliceálann siad ar *aon* eachtrán. (I gceann nóiméid amháin athróidh
tú an cód seo ionas nach dtabharfaidh ach eachtráin naimhdeacha pointí
duit.)

{{< learner-task-help >}}

In Scratch, cuireann an cód

``` scratch
athraigh [score v] faoi (10)
```

`10` le hathróg ar a dtugtar `score`. Féach sa chabhair (úsáid an an
deilbhín ‘comhartha ceiste i gciorcal’ ag barr an bharra gníomhaíochta
chun é a thaispeáint) chun a fháil amach conas an rud céanna a
dhéanamh in Python. Cuimhnigh gurb é an athróg is mian leat a athrú ná
`Stage.score`.

{{< learner-task-help >}}

Seo a leanas an cód Python chun é sin a dhéanamh

``` python
Stage.score += 10
```

Smaoinigh faoin áit ar chóir an cód seo a chur.

{{< learner-task-help >}}

{{< jr-commit award-score-on-any-hit edit-script >}}

{{< /learner-task >}}

### Bain triail as!

{{< learner-task >}}

Rith do chluiche. Seiceáil go bhfaighidh tú 10 bpointe as gach
eachtrán ar a gcliceálann tú.

{{< /learner-task >}}

### Faigh pointí as eachtráin naimhdeacha amháin

{{< learner-task >}}

Bog an cód seo ionas go mbeidh sé ‘laistigh de thástáil `if` — ná
tabhair pointí don imreoir ach amháin i gcás eachtrán namhaideach.

{{< learner-task-help >}}

Is féidir leat a thástáil an eachtrán naimhdeach atá ann trí sheiceáil
an é náid an uimhir atá ar an gculaith.

{{< learner-task-help >}}

In Scratch, is mar seo a leanas a scríobhfá cód mar sin

``` scratch
if <(costume_number) = (0)> then
change [score v] by (10)
```

Féach sa chabhair chun a fháil amach conas an rud céanna a dhéanamh in
Python.

{{< learner-task-help >}}

{{< jr-commit award-score-just-for-enemy edit-script >}}

{{< /learner-task >}}

### Bain triail as!

{{< learner-task >}}

Rith do chluiche. Ba chóir duit 10 bpointe a fháil as gach namhaid
ghorm a gcliceálann tú air, agus faic as cliceáil ar eachtrán glas.

{{< /learner-task >}}


## Déan comhaireamh ar na saolta

Tá an cluiche réasúnta maith anois, ach níl aon rud ann a chuireann
bac ar an imreoir as a bheith ag cliceáil in áit ar bith. Níl aon
phionós ann as eachtrán cairdiúil a bhualadh.

Beidh trí shaol ag an imreoir. Má scriosann tú eachtrán cairdiúil
caillfidh tú saol.

### Cuntas a choimeád ar an líon saolta

Stórálfaidh athróg an méad saol atá ag an imreoir. Beidh an cód
an-chosúil leis an gcód a scríobh tú chun an athróg `score` a chruthú
agus a thaispeáint.

{{< learner-task >}}

Ag baint úsáid as an athróg `Stage.score` mar shampla, cruthaigh athróg
`Stage.lives` a bhfuil an luach `3` aige ag tús an chluiche.

{{< learner-task-help >}}

{{< jr-commit define-global-lives edit-script >}}

{{< /learner-task >}}

Ní mór don imreoir a bheith ábalta a fheiceáil cá mhéad saol atá
acu. Ní mór do ‘lives’ a bheith le feiceáil os cionn na háite ina
bhfuil an ‘scór’ le feiceáil, áfach. Is féidir a insint don fheidhm
`self.show_variable()` cá háit ar chóir é a thaispeáint.

Mar shampla, chun an athróg `Stage.time` a thaispeáint ag barr an
ardáin ar dheis, d'fhéadfadh script san Ardán an cód seo a úsáid

``` python
self.show_variable("time", right=236)
```

{{< learner-task >}}

Taispeáin an athróg `Stage.lives` ag barr an ardáin ar dheis.

{{< learner-task-help >}}

{{< jr-commit show-lives edit-script >}}

{{< /learner-task >}}

Agus ar deireadh, ba chóir do do chlár saol amháin a bhaint gach uair
a chliceálann an t-imreoir ar eachtrán cairdiúil.

{{< learner-task >}}

Ina script *nuair a chliceáiltear air*, tá cód ag do eachtrán cheana
féin a thugann pointí don imreoir ach amháin má tá culaith ‘enemy’ ar
an eachtrán

(i.e., uimhir chulaithe `0`).

Cuir cód cosúil leis sin leis a bhaineann saol amháin ach amháin má tá
an t-eachtrán sin ag caitheamh culaith ‘friendly’ (i.e., culaith
uimhir `2`).

{{< learner-task-help >}}

{{< jr-commit decrement-lives-if-friendly edit-script >}}

{{< /learner-task >}}

### Bain triail as!

{{< learner-task >}}

Rith do chluiche. Ba cheart duit a fheiceáil go dtéann `lives` síos
gach uair a chliceálann tú ar eachtrán glas.

**Tá fabht ann — cad é?**

{{< learner-task-help >}}

Ní stopann an cluiche nuair a ritheann tú amach as saolta.

{{< /learner-task >}}

Cé go gcailleann an t-imreoir saol nuair a chliceálann siad ar
eachtrán cairdiúil, leanann an cluiche ar aghaidh fiú nuair a bhíonn
na saolta go léir caillte ag an imreoir. Socróidh tú é sin sa chéad
chaibidil eile.


## Cuir deireadh leis an gcluiche nuair nach bhfuil aon saol fágtha

Is é an chuid dheireanach den obair an cluiche a stopadh nuair a
bhíonn na saolta go léir caillte ag an imreoir. Bíonn a fhios ag an
gclár gur tharla sé sin nuair a bheidh an athróg `Stage.lives` ag
náid.

### Cuir stop le heachtráin a bheith ag sleamhnú nuair a bheidh an cluiche thart

Ar an gcéad dul síos, ba chóir do na heachtráin stopadh de bheith ag
sleamhnú síos an scáileán nuair a bheidh an cluiche thart. I láthair
na huaire, ní stopann siad ag sleamhnú riamh, mar gheall ar `while
True`. Ina ionad sin, níor cheart dóibh sleamhnú ach amháin fad is atá
roinnt saolta fágtha ag an imreoir.

{{< learner-task >}}

Níl sa ‘choinníoll’ den lúb `while` faoi láthair ach an tairiseach
`True`, mar sin ritheann an lúb `while` go deo.  Cuir comparáid in
ionad `True` a thástálann an bhfuil níos mó ná líon saolta níos mó ná
náid fágtha.

{{< learner-task-help >}}

Is féidir leat a fháil amach an bhfuil líon saolta níos mó ná náid
leis an abairt Python

``` python-expression
Stage.lives > 0
```

{{< learner-task-help >}}

{{< jr-commit stop-descent-loop-when-game-over edit-script >}}

{{< /learner-task >}}

### Bain triail as!

{{< learner-task >}}

Rith do chluiche. Cliceáil ar thrí aliens ghlasa d'aon turas. Ba chóir
go bhfeicfeá nach dtagann aon eachtrán eile i láthair. Ina ionad sin,
stopann na heachtráin ag bun an scáileáin.

{{< /learner-task >}}

Ach leanann aon aliens atá leathbhealach síos an scáileán ag dul ar
aghaidh go dtí go mbaineann siad bun an scáileáin amach. Ní mór é sin
a dheisiú freisin.

Ba chóir do gach aliens imeacht láithreach nuair a théann saolta an
imreora go náid. Má chraoltar teachtaireacht nuair a bheidh gach saol
an imreora imithe déanfar an méid sin.

{{< learner-task >}}

Tar éis duit ceann amháin a bhaint de `Stage.lives`, seiceáil an
bhfuil `Stage.lives` cothrom le náid. Más amhlaidh atá, déan an
teachtaireacht `"game-over"` a chraoladh.

{{< learner-task-help >}}

Beidh ráiteas `if` de dhíth ort. Maidir leis an “condition”, is féidir
leat a fhiafraí an bhfuil saolta an imreora ar fad caillte leis an
tástáil

``` python-expression
Stage.lives == 0
```

Tabhair faoi deara go bhfuil dhá chomhartha 'cothrom le' ann!

{{< learner-task-help >}}

{{< jr-commit broadcast-game-over edit-script >}}

{{< /learner-task >}}

### Bain triail as!

{{< learner-task >}}

Rith do chluiche. Cliceáil ar thrí eachtrán ghlasa d'aon turas. Cad a
tharlaíonn?

{{< learner-task-help >}}

Rud ar bith i ndáiríre!

{{< /learner-task >}}

Ní tharlaíonn aon rud i ndáiríre nuair a ritheann an cód seo, toisc
nach bhfuil aon rud *ag éisteacht* leis an teachtaireacht seo.

{{< learner-task >}}

Cuir script leis an eachtrán a rithfidh nuair a chraolfar an
teachtaireacht `"game-over"`.  Laistigh den script sin, scríobh líne
chóid chun an t-eachtrán a cheilt.

{{< learner-task-help >}}

{{< jr-commit hide-when-receive-game-over add-script >}}

{{< /learner-task >}}

## Tá an cluiche críochnaithe!

Déan tástáil ar do chluiche anois agus bí cinnte go n-oibríonn sé i
gceart.


## Dúshláin agus ceisteanna

Seo roinnt bealaí ar féidir leat an cluiche a dhéanamh níos fearr fós:

* Cuir faoi deara do na heachtráin bogadh níos tapúla de réir mar a
  théann scór an imreora suas.

* Cuir eachtrán dearg neamhchoitianta leis a bhfuil luach 50 pointe
  aige. Tá eachtrán dearg sa bheart íomhánna “Space aliens”, a chuir
  tú leis an togra. Tá go leor dathanna eile ann freisin más mian leat
  ceann difriúil a roghnú!

* Cuir gluaiseacht randamach ó chlé go deas leis an áit a dtosaíonn na
  heachtráin.

* Ag tús an chluiche, feiceann tú na heachtráin á gclónáil féin agus
  iad fós rómhór. An féidir leat fáil réidh leis an locht seo?

Is féidir leat smaoineamh ar na ceisteanna seo freisin:

* An aontaíonn tú gurb é an t-ardán an áit cheart don phríomhscript
  maidir le rialú (an ceann a chraolann na teachtaireachtaí)? An
  n-oibríonn an cluiche fós má tá an script seo sa sprid `Alien`?

### Creidiúintí

Spreag an cluiche *Red Alert* sa leabhar DK an togra seo go garbh
[*Cluichí códaithe in
Python*](https://www.dk.com/us/book/9781465473615-coding-games-in-python/).

### Creidiúintí mionsonraithe

{{< asset-credits >}}
