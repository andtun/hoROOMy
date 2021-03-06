from . import *


def delliter(stri):
    while True:
        l = stri.find('<')
        g = stri.find('>')
        delit = stri[l:g + 1]
        if delit == '<br/>':
            stri = stri.replace(delit, '\n')
        else:
            stri = stri.replace(delit, '')

        if l == -1:
            break
    return stri


def parse(**kwargs):
    logger = kwargs['logger']

    u = 'http://msk.posrednikovzdes.net/adv.php?city=73&oper=3'
    text = requests.get(u).text
    pages = str(text)[str(text).find('Страницы'):]
    pages = pages[:pages.find('<TBODY>')]
    s = BeautifulSoup(pages, 'lxml')
    a = str(s.find_all('a')[-1].get('href'))
    a = int(a[a.find('page=') + 5:a.rfind('&')])
    for al in range(1, a + 1):
        u = 'http://msk.posrednikovzdes.net/adv.php?city=73&oper=3&metro=0&realty=0&oplt=0&price1=0&price2=11&page=%s&paiin=0' % al
        text = requests.get(u).text
        soup = BeautifulSoup(text, "lxml")
        table = soup.find('table', {'class': 'tab'})
        tr = table.find_all('tr')  # [/// , /// , ///]
        for i in tr:
            td = i.find_all('td')
            if len(td) == 9:
                dat = delliter(str(td[1]))
                idd = dat[dat.find('№') + 1:]
                idd = re.sub(r" |\n", '', idd)
                url = 'http://msk.posrednikovzdes.net/offer.php?id=%s' % idd

                dat = dat[:dat.find('№')]
                dat = re.sub(r'\d\d:\d\d:\d\d', '', dat)
                if "Сегодня" in dat:
                    dat = datetimedate.today().strftime("%d.%m.%Y")
                elif "Вчера" in dat:
                    yesterday = datetimedate.today() - timedelta(1)
                    dat = yesterday.strftime("%d.%m.%Y")

                obj = delliter(str(td[2]))
                obj = obj.split('\n')
                distr = None
                street = None
                metro = None
                for j in range(len(obj)):
                    obj[j] = re.sub(r'\xa0|\t|\r', '', obj[j])
                    if 'Район' in obj[j]:
                        distr = obj[j]
                    if "Улица" in obj[j]:
                        street = obj[j]
                    if 'Метро' in obj[j]:
                        metro = obj[j]
                room = obj[1]
                if "квартира" in room:
                    room = int(re.sub(r'квартира|к\.|-| ', '', room))
                elif "Койко-место" in room:
                    room = -1
                elif "Комната" in room:
                    room = 0

                pay = delliter(str(td[3]))
                pay = re.sub(r'\xa0|\t|\r', '', pay).split('\n')
                if len(pay) < 3:
                    payment = "no"
                else:
                    payment = pay[0] + pay[1] + pay[2]
                payment = re.sub(r'Помесячно| |Предоплата|Посуточно|Залог', '', payment)
                if 'тыс.руб.' in payment:
                    payment = re.sub(r'тыс\.руб\.', '', payment)
                    if '.' in payment:
                        payment = payment.replace('.', '')
                        payment += '00'
                    else:
                        payment += '000'
                elif 'руб.' in payment:
                    payment = re.sub(r'руб\.', '', payment)

                floor = delliter(str(td[4]))

                area = delliter(str(td[5]))
                if "Общ" in area:
                    area = area.split('\n')
                    area = float(re.sub(r'м2| ', '', area[1]))
                elif len(area) == 0:
                    area = 0
                else:
                    area = area.split('\n')
                    area = float(re.sub(r'м2| ', '', area[1]))

                descript = td[7].find('span', {'style': "color:#CC0000; "}).text

                phone = delliter(str(td[7]))
                phone = re.sub(r'\xa0|\t|\r', '', phone).split('\n')
                for z in phone:
                    if "Контакты" in z:
                        ph = z[z.find('+'):]
                        ph = ph[:17]

                photo = str(td[7])
                allPhoto = []
                if 'Фото' in photo:
                    photo = photo[photo.find('javascript:showfoto'):]
                    photo = photo[photo.find('(') + 1:photo.find(')')]
                    photo = re.sub(r'\'|jpeg|z|\.|,', '', photo)
                    photo = re.sub(idd, '', photo)
                    photo = int(photo[-1])
                    for a in range(1, photo + 1):
                        uu = 'http://www.posrednikovzdes.net/foto/files2/%s_b_%s.jpeg' % (idd, a)
                        allPhoto.append(uu)

                x = {"type": "owner", 'room_num': room, 'metro': metro, 'pics': allPhoto,
                     "cost": payment, "floor": floor, "contacts": dict(phone=ph, person_name=None), "loc": "",
                     "url": url, "date": dat, "area": area, "adr": str(distr) + " " + str(street), "descr": descript}

                logger.info("One more renter with PosrednikovNet")
                yield x

