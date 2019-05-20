from flask import Flask, jsonify

app = Flask(__name__)

import mysql.connector

conexion = mysql.connector.connect(user = 'root',database = 'ofertas')
cursor = conexion.cursor()

@app.route("/api/v1/agenda")
def hello():
    query = "SELECT * FROM oferta_academica"
    horarios = "SELECT * FROM horario WHERE id_nrc = %s"
    #selectOferta = "SELECT * FROM oferta_academica WHERE nrc = %s"
    selectProf = "SELECT * FROM profesores WHERE id = %s"
    selectMat = "SELECT * FROM materias WHERE clave = %s"
    selectSec = "SELECT * FROM secciones WHERE id = %s"
    selectHora = "SELECT * FROM horas WHERE id = %s"
    selectDia = "SELECT * FROM dias WHERE id = %s"
    selectEdif = "SELECT * FROM edificios WHERE id = %s"
    selectAula = "SELECT * FROM aulas WHERE id = %s"
    selectPeriodo = "SELECT * FROM periodos"

    cursor.execute(query)
    ofertas = cursor.fetchall()
    lista_oferta = []
    lista_final = []
    for oferta in ofertas:
        cursor.execute(horarios, (oferta[0],))
        horario = cursor.fetchall()
        cursor.execute(selectHora, (horario[0][1],))
        hora = cursor.fetchall()
        cursor.execute(selectHora, (horario[2][1],))
        hora2 = cursor.fetchall()
        cursor.execute(selectDia, (horario[0][2],))
        dia = cursor.fetchall()
        cursor.execute(selectDia, (horario[1][2],))
        dia2 = cursor.fetchall()
        cursor.execute(selectDia, (horario[2][2],))
        dia3 = cursor.fetchall()
        cursor.execute(selectEdif, (horario[0][3],))
        edificio = cursor.fetchall()
        cursor.execute(selectEdif, (horario[1][3],))
        edificio2 = cursor.fetchall()
        cursor.execute(selectEdif, (horario[2][3],))
        edificio3 = cursor.fetchall()
        cursor.execute(selectAula, (horario[0][4],))
        aula = cursor.fetchall()
        cursor.execute(selectAula, (horario[1][4],))
        aula2 = cursor.fetchall()
        cursor.execute(selectAula, (horario[2][4],))
        aula3 = cursor.fetchall()
        cursor.execute(selectMat, (oferta[3],))
        materia = cursor.fetchall()
        cursor.execute(selectSec, (oferta[4],))
        seccion = cursor.fetchall()
        cursor.execute(selectProf, (oferta[5],))
        profesor = cursor.fetchall()
        cursor.execute(selectPeriodo)
        periodo = cursor.fetchall()

        o = {"nrc": oferta[0],
             "clave": oferta[3],
            "materia": materia[0][1],
            "seccion": seccion[0][1],
            "creditos": materia[0][2],
            "cupos": oferta[1],
            "disponibles": oferta[2],
            "horas": hora[0][1],
            "dias": dia[0][1],
            "edificio": edificio[0][1],
            "aula": aula[0][1],
            "dias2": dia2[0][1],
            "edificio2": edificio2[0][1],
            "aula2": aula2[0][1],
            "horas2": hora2[0][1],
            "dias3": dia3[0][1],
            "edificio3": edificio3[0][1],
            "aula3": aula3[0][1],
            "profesor": profesor[0][1],
            "periodo": periodo[0][1],
             }
        lista_oferta.append(o)
    lista_final.append(lista_oferta)
    return jsonify(lista_final)
app.run()
