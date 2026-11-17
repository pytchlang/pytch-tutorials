# Script-ar-script Buail an t-úll

Tá tú chun cluiche a scríobh in Python ina gcaithfidh an t-imreoir
cliceáil ar thorthaí chun pointí a fháil. Má tá beagán eolais agat ar
Scratch, feicfidh tú go bhfuil Pytch cosúil le Scratch i mórán
bealaí. Ach tá sé ceart go leor mura bhfuil Scratch úsáidte agat
roimhe seo.

![screenshot](screenshot.png#img-center)

Ba mhaith linn buíochas a ghabháil leis an [gComhairle um Oideachas
Gaeltachta agus Gaelscolaíochta](https://cogg.ie/) (COGG) as an rang
teagaisc seo a aistriú go Gaeilge.

---

## Bain úsáid as cúlra níos suimiúla

Rith an cluiche folamh anois, trí chliceáil ar an gcnaipe seinnte
glas. Feicfidh tú nach dtarlaíonn mórán. Tagann tá_cúlra_ ag an
_ardán_ aníos, agus is é sin an rud a fheiceann tú, ach níl sa chúlra
tosaigh ach dronuilleog bhán, rud nach bhfuil an-suimiúil.

{{< learner-task >}}

Cuir cúlra níos suimiúla le do chluiche. Tá ceann amháin i leabharlann
meán Pytch le patrún de dhuilleoga glasa a dhéanfaidh an chúis go
maith. `leafy-background.png` a thugtar air.

{{< learner-task-help >}}

{{< jr-commit add-leafy-Backdrop add-medialib-appearance ["leafy-background.png"] >}}

{{< /learner-task >}}

Bain triail as an gcluiche anois. Feicfidh tú nach bhfuil aon athrú
tagtha air. An chúis atá leis sin go dtaispeánann Pytch _an chéad_
chúlra den Ardán, arb é sin fós dronuilleog bhán sholadach.

{{< learner-task >}}

Scrios an cúlra `solid-white.png` ón Ardán.

{{< learner-task-help >}}

{{< jr-commit remove-default-backdrop delete-appearance >}}

{{< /learner-task >}}

Anois ba cheart go mbeadh an cúlra nua i do chluiche.

{{< learner-task >}}

Bain triail as! Cliceáil an cnaipe seinnte glas chun do chluiche a
rith. Ba chóir duit an cúlra glas duilleogach a fheiceáil.

{{< /learner-task >}}


## Cruthaigh an toradh

Anois teastaíonn _sprid_ uait, le seasamh don toradh a chaithfidh an
t-imreoir a bhualadh.

{{< learner-task >}}

Cuir sprid dar teideal `Fruit` le do chluiche. Ní mór don ainm a
bheith i mBéarla toisc go bhfuil sé mar chuid den chód.

{{< learner-task-help >}}

{{< jr-commit add-Fruit-sprite add-sprite >}}

{{< /learner-task >}}

Ansin, teastaíonn roinnt _cultacha_ ó do sprid chun a chur in iúl
dúinn faoin gcuma atá air.

{{< learner-task >}}

Ó leabharlann na meán, cuir an beart íomhánna "Cartoon fruit" isteach
mar cultacha do do sprid. An chéad chulaith, úll a bhfuil aoibh gháire
air, a úsáidfidh an sprid mar réamhshocrú. Caithfidh "Cartoon fruit" a
bheith i mBéarla, an Ghaeilge air sin ná "toradh cartúin".

{{< learner-task-help >}}

{{< jr-commit costumes-for-Fruit add-medialib-appearances-entry ["Cartoon fruit"] >}}

{{< /learner-task >}}

Anois ba chóir go mbeadh úll i do chluiche.

{{< learner-task >}}

Bain triail as! Cliceáil an cnaipe seinnte glas chun do chluiche a
rith. Ba chóir duit an cúlra glas duilleogach le húll sa lár a
fheiceáil.

**Cad atá cearr?**

{{< learner-task-help >}}

Tá an t-úll i bhfad ró-mhór!

{{< /learner-task >}}

### Socraigh méid an toraidh

Bheadh an cluiche i bhfad ró-éasca dá mbeadh an t-úll chomh mór
sin. Caithfidh tú roinnt cóid a scríobh chun an t-úll a dhéanamh níos
lú.

In Pytch (mar atá in Scratch), tá do chlár comhdhéanta de
_scripteanna_. Ritheann script nuair a tharlaíonn rud éigin, mar
shampla, nuair a chliceáiltear ar an mbratach ghlas chun an cluiche a
thosú. Am maith é seo chun méid an úill a shocrú.

{{< learner-task >}}

Cuir script _nuair a chliceáiltear an bhratach ghlas_ le do sprid
Fruit.

{{< learner-task-help >}}

{{< jr-commit add-empty-Fruit-init-size-script add-script >}}

{{< /learner-task >}}

Ag an bpointe seo, tá an script seo folamh — níl aon chód Python ann.

{{< learner-task >}}

Cuir líne de chód Python le do script a shocraíonn méid an Fruit go
méid éigin atá níos ciallmhaire.

{{< learner-task-help >}}

Má dhéanann tú an Fruit aon cheathrú cuid dá ghnáthmhéid, is dócha go
mbeidh sé ceart go leor. Má tá Scratch ar eolas agat, b'fhéidir go
bhfuil a fhios agat go ndéanfaidh

``` scratch
set size to (25) %
```

an méid sin. Féach sa chabhair chun a fháil amach conas an rud céanna
a dhéanamh in Pytch.

{{< learner-task-help >}}

Is é an modh Pytch a theastaíonn uait ná

``` python-expression
self.set_size()
```

agus uimhir idir na `()`anna a thugann le fios cén méid atá uait.

{{< learner-task-help >}}

Le "aon cheathrú den ghnáthmhéid" a rá, is féidir leat an luach `0.25`
a úsáid.

{{< learner-task-help >}}

{{< jr-commit add-Fruit-init-size-script-body edit-script >}}

{{< /learner-task >}}

Anois ba chóir go mbeadh an Fruit ar mhéid níos fearr.

{{< learner-task >}}

Bain triail as! Cliceáil an cnaipe seinnte glas chun do chluiche a
rith. Ba chóir duit úll ar mhéid níos ciallmhaire ar an gcúlra
duilleogach a fheiceáil.

{{< /learner-task >}}


## Lig don imreoir cliceáil ar an toradh

Ní mór duit ligean do rud éigin tarlú nuair a chliceálann an t-imreoir
ar an Fruit — ba chóir go n-imeodh sé as radharc. Má tá Scratch ar
eolas agat, b'fhéidir go bhfuil rud éigin ar nós

```scratch
when this sprite clicked
hide
```

ar eolas agat.

Mar a chonaic tú díreach nuair a scríobh tú cód chun méid an Fruita
shocrú, tá rudaí an-chosúil leis sin in Pytch.

{{< learner-task >}}

Cuir script leis an sprid Fruit a rithfidh nuair a chliceálfaidh an
t-imreoir air.

{{< learner-task-help >}}

{{< jr-commit add-Fruit-when-clicked-script add-script >}}

{{< /learner-task >}}

Arís, ní theastaíonn ach líne amháin cóid uait sa script nua.

{{< learner-task >}}

Cuir cód leis an script seo a fhágann go gcuirtear an Fruit i
bhfolach.

{{< learner-task-help >}}

Is féidir leat an chabhair a fhiosrú chun a chinntiú cén modh Pytch a
chuirfidh an Fruit i bhfolach.

{{< learner-task-help >}}

Is é an modh atá uait ná

``` python-expression
self.hide()
```

Níl aon eolas eile le tabhairt agat, ach caithfidh tú fós na `()`anna
a úsáid.

{{< learner-task-help >}}

{{< jr-commit hide-when-hit edit-script >}}

{{< /learner-task >}}

Is smaoineamh maith é do chluiche a thástáil tar éis gach athrú a
dhéanamh.

{{< learner-task >}}

Bain triail as! Cliceáil an cnaipe seinnte glas chun do chluiche a rith, ansin:

* D'aon ghnó, ná cliceáil ar an úll, ach cliceáil ar an gcúlra ina
  ionad sin. _Níor_ chóir go n-imeodh an t-úll as radharc.
* Cliceáil ar an úll. Ba chóir go n-imeodh sé as radharc.

{{< /learner-task >}}


## Déan an t-úll a thaispeáint arís tar éis é a bhualadh

Níl an cluiche thar a bheith spéisiúil go fóill. Nuair a chliceálann
an t-imreoir ar an úll, imíonn sé, agus sin é. Ní mór duit an t-úll a
thabhairt ar ais chun go mbeidh an t-imreoir in ann leanúint leis an
imirt.

Tar éis don Fruit é féin a chur i bhfolach, ba chóir dó fanacht ar
feadh tamaillín beag, agus ansin é féin a thaispeáint arís. Má tá
Scratch ar eolas agat, b'fhéidir go gcuirfeá na bloic seo a leanas ag
bun na scripte 'nuair a chliceáiltear an sprid seo':

```scratch
wait [1] seconds
show
```

In Python, cuireann tú dhá líne chóid le do script.

{{< learner-task >}}

Bain úsáid as an gcabhair chun a fháil amach cé na ráitis in Pytch a
dhéanfaidh an méid seo a leanas:

* An script a chur ag fanacht ar feadh soicind amháin.
* A dhéanfaidh an t-úll é féin a thaispeáint.

{{< learner-task-help >}}

Chun fanacht ar feadh tréimhse áirithe ama, is féidir leat modh

``` python-expression
self.wait_seconds()
```

a úsaid agus an líon soicindí ar mian leat go mbeadh an fanacht ann a
chur idir na `()`anna.

{{< learner-task-help >}}

Chun go dtaispeánfaidh sprid é féin, is féidir leat an modh

``` python-expression
self.show()
```

a úsáid. Ní theastaíonn aon rud uait idir na `()`anna, ach is gá na
`()` anna a bheith ann.

{{< learner-task-help >}}

{{< jr-commit wait-then-show edit-script >}}

{{< /learner-task >}}

Arís, is smaoineamh maith é do chluiche a thástáil de réir mar a
théann tú ar aghaidh.

{{< learner-task >}}

Bain triail as! Cliceáil an cnaipe seinnte glas chun do chluiche a
rith, ansin:

* Cliceáil ar an úll. Ba chóir dó imeacht as radharc, ansin teacht ar
  ais tar éis soicind. Cliceáil air cúpla uair eile le bheith cinnte.

{{< /learner-task >}}


## Déan an t-úll a thaispeáint arís in áit éigin eile

Tá an cluiche níos fearr anois, ach fós níl sé thar a bheith
spéisiúil. Tá a fhios ag an imreoir an áit a mbeidh an t-úll le
feiceáil. Teastaíonn uainn go dtiocfaidh an t-úll ar ais in áit
randamach ar an Ardán.

Tá bloc seo in Scratch

``` scratch
go to (random position v)
```

agus tá rud éigin cosúil leis sin in Pytch. Is féidir leat

``` python
self.go_to_random_position()
```

a úsáid chun do sprid a bhogadh go dtí suíomh randamach ar an ardán.

{{< learner-task >}}

Cuir an líne chóid seo leis an script _nuair a chliceáiltear ar an
sprid seo_ de chuid do Fruit.  Smaoinigh ar an áit ar chóir an líne
nua cóid a chur isteach sa tsraith de línte cóid atá ann cheana féin.

{{< learner-task-help >}}

Áit chiallmhar is ea tar éis an líne `self.wait_seconds(1)` ach roimh
an líne `self.show()`.

{{< learner-task-help >}}

{{< jr-commit go-to-random-position edit-script >}}

{{< /learner-task >}}

### Bain triail as!

{{< learner-task >}}

Rith do chlár leis an mbratach ghlas. Gach uair a chliceálann tú ar an
Fruit, ba chóir dó imeacht as radharc, ansin tar éis soicind, teacht
ar ais in áit randamach.

{{< /learner-task >}}


## Taispeáin scór an imreora

Bheadh sé go maith dá mbeadh a fhios ag an imreoir cé chomh maith agus
a bhí ag éirí leis nó léi. Ba chóir don chluiche *scór* a choimeád,
agus pointe a thabhairt don imreoir gach uair a bhuaileann siad Fruit.

### Cruthaigh **athróg** chun an scór a choimeád

Cuimhneoidh do chód ar an scór in *athróg*. Oibríonn siad seo go
han-chosúil le hathróga in Scratch. In Python, ní gá duit 'cruthaigh
athróg' a úsáid go soiléir — ní dhéanann tú ach athróg a shocrú ar
luach, agus cruthaítear an athróg duit.

In Python, is gnách athróga a úsáid 'a bhaineann' leis an an Ardán nó
le sprid áirithe.

Is rud é an scór a gcaithfidh an Fruit agus an tArdán araon oibriú
leis.  Níl aon chúis an-láidir ann chun an scór a shocrú i gceann
amháin nó ceann eile. Tabharfaimid an jab don Ardán.

Ba chóir don chluiche an scór a shocrú ag náid ag tús an chluiche, mar
sin teastaíonn script ó do chlár a ritheann nuair a thosaíonn an
cluiche.

{{< learner-task >}}

Bí cinnte go bhfuil tú ag obair leis **an Ardán** — cliceáil ar an
Ardán i bpána an Ardáin agus na Spride, agus bí cinnte go bhfuil na
táib seo a leanas "Cód", "Cúlraí", agus "Fuaimeanna" sa limistéar
códaithe.

{{< /learner-task >}}

{{< learner-task >}}

Cuir script **leis an Ardán** a rithfidh nuair a thosóidh an cluiche.

{{< learner-task-help >}}

{{< jr-commit add-Stage-setup-script add-script >}}

{{< /learner-task >}}

Ní mór don athróg scóir a bheith ann i ngach script, mar sin
úsáidfimid athróg 'a bhaineann' leis an Ardán. Ní bhaineann an t-eolas
ar fad faoi conas a oibríonn sé seo ar fad leis an teagasc seo, ach
faoi láthair níl le bheith ar eolas agat ach go bhfuil tú ag caint
faoi athróg ar a dtugtar `score` a bhaineann leis an Ardán leis an
abairt in Python. (Caithfidh an focal scór a bheith i mBéarla “score”
toisc go bhfuil sé sa chód)

``` python-expression
Stage.score
```

{{< learner-task >}}

Cuir líne chóid le script nua don Ardán a shocraíonn athróg
`Stage.score` go náid. (Ní mór don fhocal 'Stage' a bheith i mBéarla
toisc gur cód atá ann).

{{< learner-task-help >}}

{{< jr-commit init-Stage-score edit-script >}}

{{< /learner-task >}}

### An scór a thaispeáint

In Scratch, cuireann tú tic i mbosca chun athróg a thaispeáint ar an
Ardán. In Pytch, scríobhann tú cód chun é sin a dhéanamh. Cuirfear an
cód díreach i ndiaidh an chóid chun an scór a thosú ag náid.

{{< learner-task >}}

Cuir líne chóid isteach chun an athróg `Stage.score` a thaispeáint.

{{< learner-task-help >}}

Féach sa chabhair chun a fháil amach cén modh Pytch a dhéanann é sin.

{{< learner-task-help >}}

Anseo, is é `"score"` ainm na hathróige.

{{< learner-task-help >}}

{{< jr-commit show-score edit-script >}}

{{< /learner-task >}}

### Bain triail as!

{{< learner-task >}}

Rith do chlár leis an mbratach ghlas. Déan cinnte go bhfeiceann tú an
scór ag an mbarr ar chlé. Cliceáil ar an Toradh cúpla uair.

**Cad ata cearr?**

{{< learner-task-help >}}

Ní athraíonn an scór!

{{< /learner-task >}}

Go dtí seo níl aon bhealach ag do chlár chun go bhfaighidh an
t-imreoir pointí, mar sin fanfaidh an scór ag náid. Cuirfidh an chéad
chaibidil eile é sin ina cheart.


## Tabhair pointí don imreoir

Chun scór an imreora a mhéadú, d'fhéadfá an méid seo a leanas a
dhéanamh in Scratch

``` scratch
change [score v] by [1]
```

Tá oibreoir `+=` in Python ('athraigh trí shuimiú'), a oibríonn An
bealach céanna. Mar shampla, dá mbeadh an athróg `Stage.health` i do
chód, is é an cód chun cúig a chur a shuimiú ná

``` python
Stage.health += 5
```

{{< learner-task >}}

Bí cinnte go bhfuil tú ag obair leis **an sprid Toradh** — cliceáil ar
an Sprid Toradh sa phána Ardán agus Sprideanna, agus bí cinnte go
bhfuil na táib "Cód", "Cultacha" agus "Fuaimeanna" sa limistéar
códaithe.

{{< /learner-task >}}

{{< learner-task >}}

**Sa sprid don Toradh**, cuir líne chóid sa script a ritheann nuair a
chliceáiltear ar an Toradh, rud a fhágann go bhfaigheann an t-imreoir
pointe amháin.

Smaoinigh faoin áit sa script ar chóir an líne nua chóid a chur.

{{< learner-task-help >}}

Chun pointe a fháil, ní mór duit ceann a chur leis an athróg
`Stage.score`.

{{< learner-task-help >}}

{{< jr-commit award-point-when-hit edit-script >}}

{{< /learner-task >}}

B'fhéidir gur thug tú faoi deara go mbíonn línte bána sa chód sa
teagasc seo. Déanann Python neamhaird ar línte bána, ach déanann siad
an cód níos éasca do dhuine a léamh.

### Bain triail as!

{{< learner-task >}}

Rith do chlár leis an mbratach ghlas. Déan cinnte go dtéann an scór
suas nuair a a chliceálann tú ar an Toradh.

{{< /learner-task >}}


## Caill pointí má théann an t-imreoir amú

Bheadh an cluiche níos dúshlánaí dá gcaillfeadh an t-imreoir pointí
nuair nach mbuaileann siad an Toradh.

Is féidir le do chlár freagairt má théann an t-imreoir amú má ritheann
an tArdán roinnt cóid nuair a chliceáiltear *é*.

{{< learner-task >}}

Bí cinnte go bhfuil tú ag obair leis **an Ardán** — cliceáil ar an
Ardán i bpána an Ardáin agus na Sprideanna, agus bí cinnte go bhfuil
na táib seo a leanas "Cód", "Cúlraí", agus "Fuaimeanna" sa limistéar
códaithe.

{{< /learner-task >}}

{{< learner-task >}}

Cuir script _nuair a chliceáiltear ardán_ **leis an Ardán**.

{{< learner-task-help >}}

{{< jr-commit add-stage-clicked-script add-script >}}

{{< /learner-task >}}

Ba cheart go gcaillfeadh an t-imreoir roinnt pointí mar gheall ar an
gcód sa script seo.  Tá `-=` ('athraigh trí dhealú') in Python chun é
sin a dhéanamh. Mar shampla, más rud é go raibh athróg `Stage.health`
i do chlár, d'fhéadfadh an cód

``` python-expression
Stage.health -= 10
```

deich bpointe a bhaint den scór.

{{< learner-task >}}

Cuir líne chóid le do script a bhaineann cúig ón athróg `Stage.score`.

{{< learner-task-help >}}

{{< jr-commit lose-points-on-miss edit-script >}}

{{< /learner-task >}}

Ba chóir go mbeadh a fhios agat faoi seo cad atá le déanamh sa chéad
chéim eile!

{{< learner-task >}}

Bain triail as! Rith do chlár leis an mbratach ghlas. Déan cinnte go
dtéann an scór suas nuair a a chliceálann tú ar an Toradh. Déan cinnte
go dtéann an scór síos nuair a cliceálann tú ar an Ardán d'aon ghnó.

**Cén fhadhb atá ann?**

{{< learner-task-help >}}

Má tá an scór níos lú ná cúig nuair a théann an t-imreoir amú, is scór
diúltach a bheidh ann.

{{< /learner-task >}}

### Cuir stop leis an scór a bheith ag éirí diúltach

Más é an chéad rud a dhéanfaidh an t-imreoir ná gan an Toradh a
bhualadh, is é scór `-5` a bheidh ann. Níl sé sin róchiallmhar.

Tar éis cúig phointe a bhaint, ní mór don chód a thástáil an bhfuil an
an scór tar éis éirí diúltach. Más amhlaidh go bhfuil, ba cheart an
scór a shocrú ag náid ina ionad sin.

Chun roinnt cóid a rith má chomhlíontar coinníoll éigin, tá ráiteas
`if` in Python. Má tá Scratch ar eolas agat, oibríonn sé ar an
mbealach céanna le bloc `if` in Scratch.

{{< learner-task >}}

Cuir isteach ráiteas `if` faoin líne `Stage.score -= 5`. Ba chóir don
ráiteas `if` a thástáil an bhfuil `Stage.score` diúltach, agus, má tá,
`Stage.score` a shocrú go náid.

{{< learner-task-help >}}

Tugtar roinnt samplaí sa chabhair maidir leis an mbealach a n-oibríonn
sé seo. Cuardaigh _Má/ansin_ sa rannóg _Rialú_. Tabhair faoi deara, in
Python, an tslí a bhfuil _corp_ an ráitis `if` _eangaithe_ — bogtha
trasna ón imeall ar chlé ceithre spás.

Ní mór duit a oibriú amach cén abairt Python ba chóir a úsáid don
_tástáil_, agus oibrigh amach cén cód a théann i _gcorp_ an ráitis
`if`.

{{< learner-task-help >}}

Is é an tástáil atá uait ná

* _An bhfuil an athróg `Stage.score` níos lú ná náid?_

An abairt Python dó sin is ea

``` python-expression
Stage.score < 0
```

{{< learner-task-help >}}

{{< jr-commit clamp-score-at-zero edit-script >}}

{{< /learner-task >}}


## Tá an cluiche críochnaithe!

Is cluiche é seo is féidir a imirt anois atá scríofa le Python —
comhghairdeas!

{{< learner-task >}}

Imir cúpla cluiche agus féach cé chomh tapa agus is féidir leat pointí
a scóráil.

{{< /learner-task >}}


## Sa bhreis: Cuir toradh eile leis

Chun go mbeidh an cluiche níos suimiúla, is féidir leat cineál eile
toraidh a chur isteach.

### Roghnaigh culaith randamach

Bain úsáid as an bhfeidhm seo in Python

``` python-expression
random.choice()
```

chun rud randamach ó liosta a roghnú. Is féidir leat é sin a úsáid
chun athróg a shocrú le hainm randamach ar chulaith a chaithfidh an
Toradh nuair a atá sé le feiceáil arís.

{{< learner-task >}}

Cuir cód le script _nuair a chliceáiltear an sprid seo_ de chuid an
Toraidh. Ba ba chóir don chód:

* Culaith randamach a roghnú, agus na roghanna `"Apple-1.png"` agus
  `"Orange-1.png"` a bheith ann. Is féidir leat féachaint ar an táb
  _Cultacha_ chun roghanna eile cultacha eile a fheiceáil, más fearr
  leat iad.

* Socraigh athróg `new_costume` ar ainm na culaithe a roghnaíodh.
  (Caithfidh `new_costume` a bheith i mBéarla toisc gur cód atá ann
  seachas `culaith_nua`.)

{{< learner-task-help >}}

Tá sampla sa chabhair maidir le rogha a dhéanamh ó liosta. Féach sa
rannóg _Oibreoirí_ le haghaidh `random.choice()`.

{{< learner-task-help >}}

Ní mór duit _liosta_ roghanna a thabhairt do `random.choice()`.
Ciallaíonn an abairt Python

``` python-expression
["Apple-1.png", "Orange-1.png"]
```

go bhfuil liosta ann ina bhfuil dhá rud — an t-ainm `"Apple-1.png"`
agus an an t-ainm `"Orange-1.png"`.

{{< learner-task-help >}}

{{< jr-commit choose-random-new-costume edit-script >}}

**Nóta maidir leis an leagan amach:** Anseo, taispeántar an cód nua
roinnte i dtrí líne fhisiciúla. Más fearr leat, is féidir leat é go
léir a chlóscríobh mar líne amháin.

{{< /learner-task >}}

### Athraigh go dtí an chulaith roghnaithe

Má tá Scratch ar eolas agat, b'fhéidir gur bhain tú úsáid as bloc

``` scratch
switch costume to [Apple-1 v]
```

chun a rá le sprid culaith dhifriúil a úsáid. Is féidir le Pytch an
rud céanna a dhéanamh.

{{< learner-task >}}

Tar éis na líne `random.choice()`, cuir isteach líne chóid a athraíonn
an chulaith a roghnaíodh.

{{< learner-task-help >}}

{{< jr-commit switch-to-random-costume edit-script >}}

{{< /learner-task >}}

Agus ar deireadh:

{{< learner-task >}}

Bain triail as! Rith do chlár. Déan cinnte go bhfaighidh tú meascán de
chineálacha torthaí.

{{< /learner-task >}}


## Dúshláin

An féidir leat do chlár a athrú chun na dúshláin seo a réiteach?

* Roghnaigh ó roghanna de níos mó cultacha, ní hamháin úll nó oráiste.
* Tabhair 10 bpointe don imreoir as gach toradh a bhuaileann siad in
  ionad 1 phointe amháin.
* Tabhair 5 phointe don imreoir as úll a bhualadh agus 10 bpointe as
  oráiste a bhualadh.  (_Leid:_ Is féidir leat an abairt
  `self.costume_name` a úsáid chun ainm na culaithe atá ar an sprid
  faoi láthair a aimsiú.)
* Déan an Toradh níos lú, ionas go mbeidh sé níos deacra é a bhualadh.
* _Dúshlán níos deacra:_ Déan an Toradh níos lú má tá níos mó pointí
  ag an imreoir. Fágann sé sin go mbíonn an cluiche níos deacra de
  réir mar a éiríonn an t-imreoir níos fearr aige.

### Creidiúintí le haghaidh acmhainní an teagaisc seo

{{< asset-credits >}}
