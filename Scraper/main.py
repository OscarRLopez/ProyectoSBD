import requests
from bs4 import BeautifulSoup
import json

url = 'http://consulta.siiau.udg.mx/wco/sspseca.consulta_oferta'
r = requests.post('http://consulta.siiau.udg.mx/wco/sspseca.consulta_oferta', data = {'ciclop':'201910','cup':'D','majrp':'INCO','mostrarp':'1000'})
soup = BeautifulSoup(r.text, 'html.parser')
items = soup.findAll("tr")
cont = 0
lista = []

for i in range(1,524):
    n = ((i * 3) - 1) + cont
    nrc = items[n].contents[1].contents[0]  # nrc
    clave = items[n].contents[3].contents[0].contents[0]  # clave
    nmateria = items[n].contents[5].contents[0].contents[0]  # materia
    seccion = items[n].contents[7].contents[0]  # seccion
    creditos = items[n].contents[9].contents[0]  # creditos
    cupos = items[n].contents[11].contents[0]  # cupos
    disponibles = items[n].contents[13].contents[0]  # disponibles
    try:
        horas = items[n].contents[15].contents[1].contents[1].contents[2].contents[0]  # horas
        dias = items[n].contents[15].contents[1].contents[1].contents[3].contents[0]  # dias
        edificio = items[n].contents[15].contents[1].contents[1].contents[4].contents[0]  # Edificio
        aula = items[n].contents[15].contents[1].contents[1].contents[5].contents[0]  # Aula
        periodo = items[n].contents[15].contents[1].contents[1].contents[6].contents[0]  # Periodo
    except:
        horas = "-"
        dias = "-"
        edificio = "-"
        aula = "-"
        periodo = "-"
        cont = cont - 1

    try:
        profesor = items[n].contents[17].contents[0].contents[0].contents[3].contents[0]  # profesor
    except:
        profesor = "-"
        cont = cont - 1

    try:
        dia2 = items[n].contents[15].contents[1].contents[3].contents[2].contents[0]  # dias2
        edificio2 = items[n].contents[15].contents[1].contents[3].contents[3].contents[0]  # Edificio2
        aula2 = items[n].contents[15].contents[1].contents[3].contents[4].contents[0]  # Aula2
        try:
            horas2 = items[n].contents[15].contents[1].contents[5].contents[1].contents[0] #horas2
            dia3 = items[n].contents[15].contents[1].contents[5].contents[2].contents[0] #dias3
            edificio3 = items[n].contents[15].contents[1].contents[5].contents[3].contents[0]  #edificio3
            aula3 = items[n].contents[15].contents[1].contents[5].contents[4].contents[0]  #aula8
            cont = cont+1
        except:
            horas2 = "-"
            dia3 = "-"
            edificio3 = "-"
            aula3 = "-"
        cont = cont + 1
    except:
        dia2 = "-"
        edificio2 = "-"
        aula2 = "-"
        horas2 = "-"
        dia3 = "-"
        edificio3 = "-"
        aula3 = "-"
    materia = {"nrc": nrc,
               "clave": clave,
               "materia": nmateria,
               "seccion": seccion,
               "creditos": creditos,
               "cupos": cupos,
               "disponibles": disponibles,
               "horas": horas,
               "dias": dias,
               "edificio": edificio,
               "aula": aula,
               "periodo": periodo,
               "dias2": dia2,
               "edificio2": edificio2,
               "aula2": aula2,
               "profesor:": profesor,
               "horas2": horas2,
               "dias3": dia3,
               "edificio3": edificio3,
               "aula3": aula3,
            }
    lista.append(materia)

with open('agendaINCO.json', 'w') as archivo:
    json.dump(lista, archivo, sort_keys=False, indent = 4)


r = requests.post('http://consulta.siiau.udg.mx/wco/sspseca.consulta_oferta', data = {'ciclop':'201910','cup':'D','majrp':'INNI','mostrarp':'500'})
soup = BeautifulSoup(r.text, 'html.parser')
items = soup.findAll("tr")
cont = 0
lista = []

for i in range(1,426):
    n = ((i * 3) - 1) + cont
    nrc = items[n].contents[1].contents[0]  # nrc
    clave = items[n].contents[3].contents[0].contents[0]  # clave
    nmateria = items[n].contents[5].contents[0].contents[0]  # materia
    seccion = items[n].contents[7].contents[0]  # seccion
    creditos = items[n].contents[9].contents[0]  # creditos
    cupos = items[n].contents[11].contents[0]  # cupos
    disponibles = items[n].contents[13].contents[0]  # disponibles
    try:
        horas = items[n].contents[15].contents[1].contents[1].contents[2].contents[0]  # horas
        dias = items[n].contents[15].contents[1].contents[1].contents[3].contents[0]  # dias
        edificio = items[n].contents[15].contents[1].contents[1].contents[4].contents[0]  # Edificio
        aula = items[n].contents[15].contents[1].contents[1].contents[5].contents[0]  # Aula
        periodo = items[n].contents[15].contents[1].contents[1].contents[6].contents[0]  # Periodo
    except:
        horas = "-"
        dias = "-"
        edificio = "-"
        aula = "-"
        periodo = "-"
        cont = cont - 1

    try:
        profesor = items[n].contents[17].contents[0].contents[0].contents[3].contents[0]  # profesor
    except:
        profesor = "-"
        cont = cont - 1

    try:
        dia2 = items[n].contents[15].contents[1].contents[3].contents[2].contents[0]  # dias2
        edificio2 = items[n].contents[15].contents[1].contents[3].contents[3].contents[0]  # Edificio2
        aula2 = items[n].contents[15].contents[1].contents[3].contents[4].contents[0]  # Aula2
        try:
            horas2 = items[n].contents[15].contents[1].contents[5].contents[1].contents[0] #horas2
            dia3 = items[n].contents[15].contents[1].contents[5].contents[2].contents[0] #dias3
            edificio3 = items[n].contents[15].contents[1].contents[5].contents[3].contents[0]  #edificio3
            aula3 = items[n].contents[15].contents[1].contents[5].contents[4].contents[0]  #aula8
            cont = cont+1
        except:
            horas2 = "-"
            dia3 = "-"
            edificio3 = "-"
            aula3 = "-"
        cont = cont + 1
    except:
        dia2 = "-"
        edificio2 = "-"
        aula2 = "-"
        horas2 = "-"
        dia3 = "-"
        edificio3 = "-"
        aula3 = "-"
    materia = {"nrc": nrc,
               "clave": clave,
               "materia": nmateria,
               "seccion": seccion,
               "creditos": creditos,
               "cupos": cupos,
               "disponibles": disponibles,
               "horas": horas,
               "dias": dias,
               "edificio": edificio,
               "aula": aula,
               "periodo": periodo,
               "dias2": dia2,
               "edificio2": edificio2,
               "aula2": aula2,
               "profesor:": profesor,
               "horas2": horas2,
               "dias3": dia3,
               "edificio3": edificio3,
               "aula3": aula3,
            }
    lista.append(materia)

with open('agendaINNI.json', 'w') as archivo:
    json.dump(lista, archivo, sort_keys=False, indent = 4)

r = requests.post('http://consulta.siiau.udg.mx/wco/sspseca.consulta_oferta', data = {'ciclop':'201910','cup':'D','majrp':'IGFO','mostrarp':'100'})
soup = BeautifulSoup(r.text, 'html.parser')
items = soup.findAll("tr")
cont = 0
lista = []

for i in range(1,74):
    n = ((i * 3) - 1) + cont
    nrc = items[n].contents[1].contents[0]  # nrc
    clave = items[n].contents[3].contents[0].contents[0]  # clave
    nmateria = items[n].contents[5].contents[0].contents[0]  # materia
    seccion = items[n].contents[7].contents[0]  # seccion
    creditos = items[n].contents[9].contents[0]  # creditos
    cupos = items[n].contents[11].contents[0]  # cupos
    disponibles = items[n].contents[13].contents[0]  # disponibles
    try:
        horas = items[n].contents[15].contents[1].contents[1].contents[2].contents[0]  # horas
        dias = items[n].contents[15].contents[1].contents[1].contents[3].contents[0]  # dias
        edificio = items[n].contents[15].contents[1].contents[1].contents[4].contents[0]  # Edificio
        aula = items[n].contents[15].contents[1].contents[1].contents[5].contents[0]  # Aula
        periodo = items[n].contents[15].contents[1].contents[1].contents[6].contents[0]  # Periodo
    except:
        horas = "-"
        dias = "-"
        edificio = "-"
        aula = "-"
        periodo = "-"
        cont = cont - 1

    try:
        profesor = items[n].contents[17].contents[0].contents[0].contents[3].contents[0]  # profesor
    except:
        profesor = "-"
        cont = cont - 1

    try:
        dia2 = items[n].contents[15].contents[1].contents[3].contents[2].contents[0]  # dias2
        edificio2 = items[n].contents[15].contents[1].contents[3].contents[3].contents[0]  # Edificio2
        aula2 = items[n].contents[15].contents[1].contents[3].contents[4].contents[0]  # Aula2
        try:
            horas2 = items[n].contents[15].contents[1].contents[5].contents[1].contents[0] #horas2
            dia3 = items[n].contents[15].contents[1].contents[5].contents[2].contents[0] #dias3
            edificio3 = items[n].contents[15].contents[1].contents[5].contents[3].contents[0]  #edificio3
            aula3 = items[n].contents[15].contents[1].contents[5].contents[4].contents[0]  #aula8
            cont = cont+1
        except:
            horas2 = "-"
            dia3 = "-"
            edificio3 = "-"
            aula3 = "-"
        cont = cont + 1
    except:
        dia2 = "-"
        edificio2 = "-"
        aula2 = "-"
        horas2 = "-"
        dia3 = "-"
        edificio3 = "-"
        aula3 = "-"
    materia = {"nrc": nrc,
               "clave": clave,
               "materia": nmateria,
               "seccion": seccion,
               "creditos": creditos,
               "cupos": cupos,
               "disponibles": disponibles,
               "horas": horas,
               "dias": dias,
               "edificio": edificio,
               "aula": aula,
               "periodo": periodo,
               "dias2": dia2,
               "edificio2": edificio2,
               "aula2": aula2,
               "profesor:": profesor,
               "horas2": horas2,
               "dias3": dia3,
               "edificio3": edificio3,
               "aula3": aula3,
            }
    lista.append(materia)

with open('agendaIGFO.json', 'w') as archivo:
    json.dump(lista, archivo, sort_keys=False, indent = 4)

r = requests.post('http://consulta.siiau.udg.mx/wco/sspseca.consulta_oferta', data = {'ciclop':'201910','cup':'D','majrp':'INBI','mostrarp':'400'})
soup = BeautifulSoup(r.text, 'html.parser')
items = soup.findAll("tr")
cont = 0
lista = []

for i in range(1,351):
    n = ((i * 3) - 1) + cont
    nrc = items[n].contents[1].contents[0]  # nrc
    clave = items[n].contents[3].contents[0].contents[0]  # clave
    nmateria = items[n].contents[5].contents[0].contents[0]  # materia
    seccion = items[n].contents[7].contents[0]  # seccion
    creditos = items[n].contents[9].contents[0]  # creditos
    cupos = items[n].contents[11].contents[0]  # cupos
    disponibles = items[n].contents[13].contents[0]  # disponibles
    try:
        horas = items[n].contents[15].contents[1].contents[1].contents[2].contents[0]  # horas
        dias = items[n].contents[15].contents[1].contents[1].contents[3].contents[0]  # dias
        edificio = items[n].contents[15].contents[1].contents[1].contents[4].contents[0]  # Edificio
        aula = items[n].contents[15].contents[1].contents[1].contents[5].contents[0]  # Aula
        periodo = items[n].contents[15].contents[1].contents[1].contents[6].contents[0]  # Periodo
    except:
        horas = "-"
        dias = "-"
        edificio = "-"
        aula = "-"
        periodo = "-"
        cont = cont - 1

    try:
        profesor = items[n].contents[17].contents[0].contents[0].contents[3].contents[0]  # profesor
    except:
        profesor = "-"
        cont = cont - 1

    try:
        dia2 = items[n].contents[15].contents[1].contents[3].contents[2].contents[0]  # dias2
        edificio2 = items[n].contents[15].contents[1].contents[3].contents[3].contents[0]  # Edificio2
        aula2 = items[n].contents[15].contents[1].contents[3].contents[4].contents[0]  # Aula2
        try:
            horas2 = items[n].contents[15].contents[1].contents[5].contents[1].contents[0] #horas2
            dia3 = items[n].contents[15].contents[1].contents[5].contents[2].contents[0] #dias3
            edificio3 = items[n].contents[15].contents[1].contents[5].contents[3].contents[0]  #edificio3
            aula3 = items[n].contents[15].contents[1].contents[5].contents[4].contents[0]  #aula8
            cont = cont+1
        except:
            horas2 = "-"
            dia3 = "-"
            edificio3 = "-"
            aula3 = "-"
        cont = cont + 1
    except:
        dia2 = "-"
        edificio2 = "-"
        aula2 = "-"
        horas2 = "-"
        dia3 = "-"
        edificio3 = "-"
        aula3 = "-"
    materia = {"nrc": nrc,
               "clave": clave,
               "materia": nmateria,
               "seccion": seccion,
               "creditos": creditos,
               "cupos": cupos,
               "disponibles": disponibles,
               "horas": horas,
               "dias": dias,
               "edificio": edificio,
               "aula": aula,
               "periodo": periodo,
               "dias2": dia2,
               "edificio2": edificio2,
               "aula2": aula2,
               "profesor:": profesor,
               "horas2": horas2,
               "dias3": dia3,
               "edificio3": edificio3,
               "aula3": aula3,
            }
    lista.append(materia)

with open('agendaINBI.json', 'w') as archivo:
    json.dump(lista, archivo, sort_keys=False, indent = 4)

r = requests.post('http://consulta.siiau.udg.mx/wco/sspseca.consulta_oferta', data = {'ciclop':'201910','cup':'D','majrp':'INCE','mostrarp':'600'})
soup = BeautifulSoup(r.text, 'html.parser')
items = soup.findAll("tr")
cont = 0
lista = []

for i in range(1,502):
    n = ((i * 3) - 1) + cont
    nrc = items[n].contents[1].contents[0]  # nrc
    clave = items[n].contents[3].contents[0].contents[0]  # clave
    nmateria = items[n].contents[5].contents[0].contents[0]  # materia
    seccion = items[n].contents[7].contents[0]  # seccion
    creditos = items[n].contents[9].contents[0]  # creditos
    cupos = items[n].contents[11].contents[0]  # cupos
    disponibles = items[n].contents[13].contents[0]  # disponibles
    try:
        horas = items[n].contents[15].contents[1].contents[1].contents[2].contents[0]  # horas
        dias = items[n].contents[15].contents[1].contents[1].contents[3].contents[0]  # dias
        edificio = items[n].contents[15].contents[1].contents[1].contents[4].contents[0]  # Edificio
        aula = items[n].contents[15].contents[1].contents[1].contents[5].contents[0]  # Aula
        periodo = items[n].contents[15].contents[1].contents[1].contents[6].contents[0]  # Periodo
    except:
        horas = "-"
        dias = "-"
        edificio = "-"
        aula = "-"
        periodo = "-"
        cont = cont - 1

    try:
        profesor = items[n].contents[17].contents[0].contents[0].contents[3].contents[0]  # profesor
    except:
        profesor = "-"
        cont = cont - 1

    try:
        dia2 = items[n].contents[15].contents[1].contents[3].contents[2].contents[0]  # dias2
        edificio2 = items[n].contents[15].contents[1].contents[3].contents[3].contents[0]  # Edificio2
        aula2 = items[n].contents[15].contents[1].contents[3].contents[4].contents[0]  # Aula2
        try:
            horas2 = items[n].contents[15].contents[1].contents[5].contents[1].contents[0] #horas2
            dia3 = items[n].contents[15].contents[1].contents[5].contents[2].contents[0] #dias3
            edificio3 = items[n].contents[15].contents[1].contents[5].contents[3].contents[0]  #edificio3
            aula3 = items[n].contents[15].contents[1].contents[5].contents[4].contents[0]  #aula8
            cont = cont+1
        except:
            horas2 = "-"
            dia3 = "-"
            edificio3 = "-"
            aula3 = "-"
        cont = cont + 1
    except:
        dia2 = "-"
        edificio2 = "-"
        aula2 = "-"
        horas2 = "-"
        dia3 = "-"
        edificio3 = "-"
        aula3 = "-"
    materia = {"nrc": nrc,
               "clave": clave,
               "materia": nmateria,
               "seccion": seccion,
               "creditos": creditos,
               "cupos": cupos,
               "disponibles": disponibles,
               "horas": horas,
               "dias": dias,
               "edificio": edificio,
               "aula": aula,
               "periodo": periodo,
               "dias2": dia2,
               "edificio2": edificio2,
               "aula2": aula2,
               "profesor:": profesor,
               "horas2": horas2,
               "dias3": dia3,
               "edificio3": edificio3,
               "aula3": aula3,
            }
    lista.append(materia)

with open('agendaINCE.json', 'w') as archivo:
    json.dump(lista, archivo, sort_keys=False, indent = 4)

r = requests.post('http://consulta.siiau.udg.mx/wco/sspseca.consulta_oferta', data = {'ciclop':'201910','cup':'D','majrp':'INRO','mostrarp':'400'})
soup = BeautifulSoup(r.text, 'html.parser')
items = soup.findAll("tr")
cont = 0
lista = []

for i in range(1,77):
    n = ((i * 3) - 1) + cont
    nrc = items[n].contents[1].contents[0]  # nrc
    clave = items[n].contents[3].contents[0].contents[0]  # clave
    nmateria = items[n].contents[5].contents[0].contents[0]  # materia
    seccion = items[n].contents[7].contents[0]  # seccion
    creditos = items[n].contents[9].contents[0]  # creditos
    cupos = items[n].contents[11].contents[0]  # cupos
    disponibles = items[n].contents[13].contents[0]  # disponibles
    try:
        horas = items[n].contents[15].contents[1].contents[1].contents[2].contents[0]  # horas
        dias = items[n].contents[15].contents[1].contents[1].contents[3].contents[0]  # dias
        edificio = items[n].contents[15].contents[1].contents[1].contents[4].contents[0]  # Edificio
        aula = items[n].contents[15].contents[1].contents[1].contents[5].contents[0]  # Aula
        periodo = items[n].contents[15].contents[1].contents[1].contents[6].contents[0]  # Periodo
    except:
        horas = "-"
        dias = "-"
        edificio = "-"
        aula = "-"
        periodo = "-"
        cont = cont - 1

    try:
        profesor = items[n].contents[17].contents[0].contents[0].contents[3].contents[0]  # profesor
    except:
        profesor = "-"
        cont = cont - 1

    try:
        dia2 = items[n].contents[15].contents[1].contents[3].contents[2].contents[0]  # dias2
        edificio2 = items[n].contents[15].contents[1].contents[3].contents[3].contents[0]  # Edificio2
        aula2 = items[n].contents[15].contents[1].contents[3].contents[4].contents[0]  # Aula2
        try:
            horas2 = items[n].contents[15].contents[1].contents[5].contents[1].contents[0] #horas2
            dia3 = items[n].contents[15].contents[1].contents[5].contents[2].contents[0] #dias3
            edificio3 = items[n].contents[15].contents[1].contents[5].contents[3].contents[0]  #edificio3
            aula3 = items[n].contents[15].contents[1].contents[5].contents[4].contents[0]  #aula8
            cont = cont+1
        except:
            horas2 = "-"
            dia3 = "-"
            edificio3 = "-"
            aula3 = "-"
        cont = cont + 1
    except:
        dia2 = "-"
        edificio2 = "-"
        aula2 = "-"
        horas2 = "-"
        dia3 = "-"
        edificio3 = "-"
        aula3 = "-"
    materia = {"nrc": nrc,
               "clave": clave,
               "materia": nmateria,
               "seccion": seccion,
               "creditos": creditos,
               "cupos": cupos,
               "disponibles": disponibles,
               "horas": horas,
               "dias": dias,
               "edificio": edificio,
               "aula": aula,
               "periodo": periodo,
               "dias2": dia2,
               "edificio2": edificio2,
               "aula2": aula2,
               "profesor:": profesor,
               "horas2": horas2,
               "dias3": dia3,
               "edificio3": edificio3,
               "aula3": aula3,
            }
    lista.append(materia)

with open('agendaINRO.json', 'w') as archivo:
    json.dump(lista, archivo, sort_keys=False, indent = 4)