# Импорт цен акций за указанный период
import urllib.request
import datetime
import time
import random
import matplotlib.pyplot as plt

# Тиккеры акций и их id в система Abyfv
tickers={'ABRD':82460,'AESL':181867,'AFKS':19715,'AFLT':29,'AGRO':399716,'AKRN':17564,'ALBK':82616,'ALNU':81882,'ALRS':81820,'AMEZ':20702,'APTK':13855,'AQUA':35238,'ARMD':19676,'ARSA':19915,'ASSB':16452,'AVAN':82843,'AVAZ':39,'AVAZP':40,'BANE':81757,'BANEP':81758,'BGDE':175840,'BISV':35242,'BISVP':35243,'BLNG':21078,'BRZL':81901,'BSPB':20066,'CBOM':420694,'CHEP':20999,'CHGZ':81933,'CHKZ':21000,'CHMF':16136,'CHMK':21001,'CHZN':19960,'CLSB':16712,'CLSBP':16713,'CNTL':21002,'CNTLP':81575,'DASB':16825,'DGBZ':17919,'DIOD':35363,'DIXY':18564,'DVEC':19724,'DZRD':74744,'DZRDP':74745,'ELTZ':81934,'ENRU':16440,'EPLN':451471,'ERCO':81935,'FEES':20509,'FESH':20708,'FORTP':82164,'GAZA':81997,'GAZAP':81998,'GAZC':81398,'GAZP':16842,'GAZS':81399,'GAZT':82115,'GCHE':20125,'GMKN':795,'GRAZ':16610,'GRNT':449114,'GTLC':152876,'GTPR':175842,'GTSS':436120,'HALS':17698,'HIMC':81939,'HIMCP':81940,'HYDR':20266,'IDJT':388276,'IDVP':409486,'IGST':81885,'IGST03':81886,'IGSTP':81887,'IRAO':20516,'IRGZ':9,'IRKT':15547,'ISKJ':17137,'JNOS':15722,'JNOSP':15723,'KAZT':81941,'KAZTP':81942,'KBSB':19916,'KBTK':35285,'KCHE':20030,'KCHEP':20498,'KGKC':83261,'KGKCP':152350,'KLSB':16329,'KMAZ':15544,'KMEZ':22525,'KMTZ':81903,'KOGK':20710,'KRKN':81891,'KRKNP':81892,'KRKO':81905,'KRKOP':81906,'KROT':510,'KROTP':511,'KRSB':20912,'KRSBP':20913,'KRSG':15518,'KSGR':75094,'KTSB':16284,'KTSBP':16285,'KUBE':522,'KUNF':81943,'KUZB':83165,'KZMS':17359,'KZOS':81856,'KZOSP':81857,'LIFE':74584,'LKOH':8,'LNTA':385792,'LNZL':21004,'LNZLP':22094,'LPSB':16276,'LSNG':31,'LSNGP':542,'LSRG':19736,'LVHK':152517,'MAGE':74562,'MAGEP':74563,'MAGN':16782,'MERF':20947,'MFGS':30,'MFGSP':51,'MFON':152516,'MGNT':17086,'MGNZ':20892,'MGTS':12984,'MGTSP':12983,'MGVM':81829,'MISB':16330,'MISBP':16331,'MNFD':80390,'MOBB':82890,'MOEX':152798,'MORI':81944,'MOTZ':21116,'MRKC':20235,'MRKK':20412,'MRKP':20107,'MRKS':20346,'MRKU':20402,'MRKV':20286,'MRKY':20681,'MRKZ':20309,'MRSB':16359,'MSNG':6,'MSRS':16917,'MSST':152676,'MSTT':74549,'MTLR':21018,'MTLRP':80745,'MTSS':15523,'MUGS':81945,'MUGSP':81946,'MVID':19737,'NAUK':81992,'NFAZ':81287,'NKHP':450432,'NKNC':20100,'NKNCP':20101,'NKSH':81947,'NLMK':17046,'NMTP':19629,'NNSB':16615,'NNSBP':16616,'NPOF':81858,'NSVZ':81929,'NVTK':17370,'ODVA':20737,'OFCB':80728,'OGKB':18684,'OMSH':22891,'OMZZP':15844,'OPIN':20711,'OSMP':21006,'OTCP':407627,'PAZA':81896,'PHOR':81114,'PHST':19717,'PIKK':18654,'PLSM':81241,'PLZL':17123,'PMSB':16908,'PMSBP':16909,'POLY':175924,'PRFN':83121,'PRIM':17850,'PRIN':22806,'PRMB':80818,'PRTK':35247,'PSBR':152320,'QIWI':181610,'RASP':17713,'RBCM':74779,'RDRB':181755,'RGSS':181934,'RKKE':20321,'RLMN':152677,'RLMNP':388313,'RNAV':66644,'RODNP':66693,'ROLO':181316,'ROSB':16866,'ROSN':17273,'ROST':20637,'RSTI':20971,'RSTIP':20972,'RTGZ':152397,'RTKM':7,'RTKMP':15,'RTSB':16783,'RTSBP':16784,'RUAL':414279,'RUALR':74718,'RUGR':66893,'RUSI':81786,'RUSP':20712,'RZSB':16455,'SAGO':445,'SAGOP':70,'SARE':11,'SAREP':24,'SBER':3,'SBERP':23,'SELG':81360,'SELGP':82610,'SELL':21166,'SIBG':436091,'SIBN':2,'SKYC':83122,'SNGS':4,'SNGSP':13,'STSB':20087,'STSBP':20088,'SVAV':16080,'SYNG':19651,'SZPR':22401,'TAER':80593,'TANL':81914,'TANLP':81915,'TASB':16265,'TASBP':16266,'TATN':825,'TATNP':826,'TGKA':18382,'TGKB':17597,'TGKBP':18189,'TGKD':18310,'TGKDP':18391,'TGKN':18176,'TGKO':81899,'TNSE':420644,'TORS':16797,'TORSP':16798,'TRCN':74561,'TRMK':18441,'TRNFP':1012,'TTLK':18371,'TUCH':74746,'TUZA':20716,'UCSS':175781,'UKUZ':20717,'UNAC':22843,'UNKL':82493,'UPRO':18584,'URFD':75124,'URKA':19623,'URKZ':82611,'USBN':81953,'UTAR':15522,'UTII':81040,'UTSY':419504,'UWGN':414560,'VDSB':16352,'VGSB':16456,'VGSBP':16457,'VJGZ':81954,'VJGZP':81955,'VLHZ':17257,'VRAO':20958,'VRAOP':20959,'VRSB':16546,'VRSBP':16547,'VSMO':15965,'VSYD':83251,'VSYDP':83252,'VTBR':19043,'VTGK':19632,'VTRS':82886,'VZRZ':17068,'VZRZP':17067,'WTCM':19095,'WTCMP':19096,'YAKG':81917,'YKEN':81766,'YKENP':81769,'YNDX':388383,'YRSB':16342,'YRSBP':16343,'ZHIV':181674,'ZILL':81918,'ZMZN':556,'ZMZNP':603,'ZVEZ':82001,'FIVE':7,'DSKY':8,'SFIN':9,'RNFT':9}
# Акции, входящие в индекс
RTSI=['GAZP','SBER','SBERP','LKOH','GMKN','YNDX','NVTK','TATN','TATNP','ROSN','SNGS','SNGSP','MGNT','FIVE','MTSS','POLY','ALRS','CHMF','PLZL','IRAO','NLMK','VTBR','MOEX','PHOR','TRNFP','MAGN','RTKM','RUAL','AFLT','PIKK','HYDR','FEES','AFKS','LSRG','CBOM','UPRO','DSKY','LNTA','SFIN','RNFT','MVID']
# Число акций
Q=[23673512900, 21586948000, 1000000000, 715000000, 158245476, 292567655, 3036306000, 2178690700, 147508500, 10598177817, 35725994705, 7701998235, 101911355, 271572872, 1998381575, 470183404, 7364965630, 837718660, 133561119, 104400000000, 5993227240, 12960541337338, 2276401458, 129500000, 1554875, 11174330000, 2574914954, 15193014862, 1110616299, 660497344, 426288813551, 1274665323063, 9650000000, 103030215, 27079709866, 63048706145, 739000000, 487929660, 111637791, 294120000, 179768227]
# Веса в %
W=[15.00,	13.84,	1.16,	13.43,	6.26,	5.31,	5.31,	4.50,	0.81,	4.41,	2.28,	1.68,	2.48,	2.38,	2.22,	1.90,	1.73,	1.56,	1.52,	1.37,	1.33,	1.26,	1.16,	0.77,	0.69,	0.69,	0.62,	0.60,	0.46,	0.43,	0.41,	0.38,	0.34,	0.31,	0.27,	0.25,	0.21,	0.21,	0.19,	0.14,	0.13]

N=41


# Формируем дату и время
def dtformed(d,mn,y,h=0,m=0,s=0):
    return datetime.datetime(y,mn,d,h,m,s)


# Возвращает ID инструмента по его имени (внутренная функция)
def getID(name):
    return tickers[name]

# Выгрузка данных
def load(name, dtstart=datetime.datetime.today(),dtfin=datetime.datetime.today(),step=8, market=1, MSOR=1, mstimever=0, sourse='finam',moment='close'):
    # market - инструмент
    # 0 — начала свечи, 1 — окончания свечи
    # mstimever - не московское — mstimever=0; московское — mstime='on', mstimever='1'
    #  период котировок (тики, 1 мин., 5 мин., 10 мин., 15 мин., 30 мин., 1 час, 1 день, 1 неделя, 1 месяц)
    id =getID(name) # id инстурмента
    e = '.txt' # расширение получаемого файла: .txt либо .csv
    yf = str(dtstart.year)
    yt = str(dtfin.year)
    month_start = str(dtstart.month)
    day_start = str(dtstart.day)
    month_end = str(dtfin.month)
    day_end = str(dtfin.day)
    dtf = '3' # формат даты (1 — ггггммдд, 2 — ггммдд, 3 — ддммгг, 4 — дд/мм/гг, 5 — мм/дд/гг)
    tmf = '1' # формат времени (1 — ччммсс, 2 — ччмм, 3 — чч: мм: сс, 4 — чч: мм)
    sep = '5' # параметр разделитель полей (1 — запятая (,), 2 — точка (.), 3 — точка с запятой (;), 4 — табуляция (»), 5 — пробел ( ))
    sep2 = '1' # параметр разделитель разрядов (1 — нет, 2 — точка (.), 3 — запятая (,), 4 — пробел ( ), 5 — кавычка ('))
    datf = '1' # Перечень получаемых данных (1-6)
    at = '0' # добавлять заголовок в файл (0 — нет, 1 — да)

    year_start = yf[2:]
    year_end = yt[2:]
    mf = (int(month_start.replace('0', ''))) - 1
    mt = (int(month_end.replace('0', ''))) - 1
    df = (int(day_start.replace('0', ''))) - 1
    dt = (int(day_end.replace('0', ''))) - 1

    # Запрос
    str1='http://export.finam.ru/' + str(name) + '_' + str(year_start) + str(month_start) + str(
            day_start) + '_' + str(year_end) + str(month_end) + str(day_end) + str(e) + '?market=' + str(
            market) + '&em=' + str(id) + '&code=' + str(name) + '&apply=0&df=' + str(df) + '&mf=' + str(
            mf) + '&yf=' + str(yf) + '&from=' + str(day_start) + '.' + str(month_start) + '.' + str(yf) + '&dt=' + str(
            dt) + '&mt=' + str(mt) + '&yt=' + str(yt) + '&to=' + str(day_end) + '.' + str(month_end) + '.' + str(
            yt) + '&p=' + str(step) + '&f=' + str(name) + '_' + str(year_start) + str(month_start) + str(
            day_start) + '_' + str(year_end) + str(month_end) + str(day_end) + '&e=' + str(e) + '&cn=' + str(
            name) + '&dtf=' + str(dtf) + '&tmf=' + str(tmf) + '&MSOR=' + str(MSOR) + '&mstimever=' + str(
            mstimever) + '&sep=' + str(sep) + '&sep2=' + str(sep2) + '&datf=' + str(datf) + '&at=' + str(at)
    result = urllib.request.urlopen(str1)

    # Выделение нужных данных
    content = str(result.read())
    print(name)
    stokelist=content.split(r'\r\n')
    n=len(stokelist)
    price=list()
    for k in range(n-1):
        stokelist1=stokelist[k].split(' ')
        price.append(stokelist1[7])

    return price


PRICE=[]
PRICE1=[]

print('Импорт цен акций...')

k=0
while k<N:
    try:
        PRICE.append(load(RTSI[k], dtformed(3, 1, 2019), dtformed(31,12,2019)))
        k=k+1
    except:
        continue
    finally:
        time.sleep(random.randint(1, 2))
k=0
while k<N:
    try:
        PRICE1.append(load(RTSI[k], dtformed(3, 1, 2019), dtformed(3, 1, 2020),step=10))
        k=k+1
    except:
        continue
    finally:
        time.sleep(random.randint(1, 2))


L=len(PRICE[0])



# Расчёт индекса
def getindex(PRICE):
    indexat030119 = 1086.8 # Значение индекса на 1-й торговый день 2019 года
    s=list()
    I=list()
    L=len(PRICE[0])
    for j in range(L):
        s1=0.0
        for k in range(N):
            s1=s1+Q[k]*float(PRICE[k][j])*(W[k]/100)
        s.append(s1)
        I.append(indexat030119*s[j]/s[0])
    return I


# Перемножает списки (перенести)
def prodlist(x,y):
    n=len(x)
    p=list()
    for k in range(n):
        p.append(x[k]*y[k])
    return p


# Вычисление коэффициентов линейной регрессии
def linMMQ(x,y):
    n=len(x)
    a = (n*sum(prodlist(x,y))-sum(x)*sum(y))/(n*sum(prodlist(x,x))-(sum(x))**2)
    b = (sum(y)-a*sum(x))/n
    return [a, b]

# Вычисление значений линии регрессии
def linspace(x,a,b):
    n=len(x)
    y=list()
    for k in range(n):
        y.append(a*x[k]+b)
    return y


X=list(range(1,L+1))
Y=getindex(PRICE)
[a, b]=linMMQ(X,Y)

# Построение графиков

plt.figure(figsize=(9, 9))
plt.subplot(2, 1, 1)
plt.plot(X, Y)
plt.plot(X, linspace(X,a,b))
plt.title("Индекс RTSI за 2019 год по дням и месяцам")
plt.xlabel("Дни")
plt.grid()
plt.subplot(2, 1, 2)
X=list(range(1,13))
Y=getindex(PRICE1)
[a, b]=linMMQ(X,Y)
plt.plot(X, Y)
plt.plot(X, linspace(X,a,b))
plt.xlabel("Месяцы")
plt.grid()
plt.show()
