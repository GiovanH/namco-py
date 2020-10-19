# Schema

## Scene

```xml
<scene id="s_day0" xmlns="http://datenighto.com/schemas/htmlvn/0.1" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://datenighto.com/schemas/htmlvn/0.1 ./htmlvn.xsd">
```

Root element

Has attributes
- id -- scene id ("s_day0")

Contains children
- Assets
- Events

### Assets

Contains children
- TextAsset

#### TextAsset

```xml
<TextAsset key="t_salbatros00.00">
    <value key="en">Psst. Hey, kid.</value>
</TextAsset>
```

String localization.

Has `key` attribute that defines the string id.

Contains children `value` with `key` language and text contents.

### Events

Contains children
- actorcrossfade
- actorevent
- actorcreate
- actordepth
- actorfade
- actorflip
- actorimage
- actormove
- actordestroy
- actorscale
- actorreset
- audioevent
- audiocreate
- audiodestroy
- audiooneshot
- jumpevent
- yesnochoice
- consoleevent
- ifequal
- ifgte
- iflte
- iftrue
- iffalse
- creditsevent
- lockoutchoice
- fadeevent
- gameover
- hardswap
- nhscenechange
- parallelevent
- settingchange
- textevent
- varensure
- varset
- varinc
- macro
- battlemacro
- silhouettemacro
- explorationmacro
- branchmacro
- normalendmacro
- badendmacro
- supersecretmacro


#### actorcrossfade



#### actorevent



#### actorcreate



#### actordepth



#### actorfade



#### actorflip



#### actorimage



#### actormove



#### actordestroy



#### actorscale



#### actorreset



#### audioevent



#### audiocreate



#### audiodestroy



#### audiooneshot



#### jumpevent



#### yesnochoice



#### consoleevent



#### ifequal



#### ifgte



#### iflte



#### iftrue



#### iffalse



#### creditsevent



#### lockoutchoice



#### fadeevent



#### gameover



#### hardswap



#### nhscenechange



#### parallelevent



#### settingchange



#### textevent



#### varensure



#### varset



#### varinc



#### macro



#### battlemacro



#### silhouettemacro



#### explorationmacro



#### branchmacro



#### normalendmacro



#### badendmacro



#### supersecretmacro




