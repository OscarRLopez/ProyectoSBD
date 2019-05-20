import glob
import json
import mysql.connector

conexion = mysql.connector.connect(user = 'root', database = 'ofertas')
cursor = conexion.cursor()

files = glob.glob('*.json')

def existe_profesor(reg):
    select = 'SELECT * FROM profesores WHERE nombre = %s'
    cursor.execute(select, (reg['profesor:'],))
    rows = cursor.fetchall()
    if len(rows) > 0:
        return True
    else:
        return False

def insertar_profesor(reg):
    insert = 'INSERT INTO profesores(nombre) VALUES (%s)'
    cursor.execute(insert, (reg['profesor:'],))
    conexion.commit()
    return cursor.lastrowid

def get_id_prof(profe):
    select = 'SELECT id FROM profesores WHERE nombre = %s'
    cursor.execute(select, (profe,))
    rows = cursor.fetchall()
    return rows[0][0]

def existe_aula(aula):
    select = 'SELECT * FROM aulas WHERE aula = %s'
    cursor.execute(select, (aula,))
    rows = cursor.fetchall()
    if len(rows) > 0:
        return True
    else:
        return False

def insertar_aula(aula):
    insert = 'INSERT INTO aulas(aula) VALUES (%s)'
    cursor.execute(insert, (aula,))
    conexion.commit()
    return cursor.lastrowid

def get_id_aula(aula):
    select = 'SELECT id FROM aulas WHERE aula = %s'
    cursor.execute(select, (aula,))
    rows = cursor.fetchall()
    return rows[0][0]

def existe_dia(dia):
    select = 'SELECT * FROM dias WHERE dia = %s'
    cursor.execute(select, (dia,))
    rows = cursor.fetchall()
    if len(rows) > 0:
        return True
    else:
        return False

def insertar_dia(dia):
    insert = 'INSERT INTO dias(dia) VALUES (%s)'
    cursor.execute(insert, (dia,))
    conexion.commit()
    return cursor.lastrowid

def get_id_dia(dia):
    select = 'SELECT id FROM dias WHERE dia = %s'
    cursor.execute(select, (dia,))
    rows = cursor.fetchall()
    return rows[0][0]

def existe_edificio(edi):
    select = 'SELECT * FROM edificios WHERE edificio = %s'
    cursor.execute(select, (edi,))
    rows = cursor.fetchall()
    if len(rows) > 0:
        return True
    else:
        return False

def insertar_edificio(edi):
    insert = 'INSERT INTO edificios(edificio) VALUES (%s)'
    cursor.execute(insert, (edi,))
    conexion.commit()
    return cursor.lastrowid

def get_id_edificio(edi):
    select = 'SELECT id FROM edificios WHERE edificio = %s'
    cursor.execute(select, (edi,))
    rows = cursor.fetchall()
    return rows[0][0]

def existe_hora(hora):
    select = 'SELECT * FROM horas WHERE hora = %s'
    cursor.execute(select, (hora,))
    rows = cursor.fetchall()
    if len(rows) > 0:
        return True
    else:
        return False

def insertar_hora(hora):
    insert = 'INSERT INTO horas(hora) VALUES (%s)'
    cursor.execute(insert, (hora,))
    conexion.commit()
    return cursor.lastrowid

def get_id_hora(hora):
    select = 'SELECT id FROM horas WHERE hora = %s'
    cursor.execute(select, (hora,))
    rows = cursor.fetchall()
    return rows[0][0]

def existe_seccion(reg):
    select = 'SELECT * FROM secciones WHERE seccion = %s'
    cursor.execute(select, (reg['seccion'],))
    rows = cursor.fetchall()
    if len(rows) > 0:
        return True
    else:
        return False

def insertar_seccion(reg):
    insert = 'INSERT INTO secciones(seccion) VALUES (%s)'
    cursor.execute(insert, (reg['seccion'],))
    conexion.commit()
    return cursor.lastrowid

def get_id_seccion(seccion):
    select = 'SELECT id FROM secciones WHERE seccion = %s'
    cursor.execute(select, (seccion,))
    rows = cursor.fetchall()
    return rows[0][0]

def existe_materia(reg):
    select = 'SELECT * FROM materias WHERE clave = %s'
    cursor.execute(select, (reg['clave'],))
    rows = cursor.fetchall()
    if len(rows) > 0:
        return True
    else:
        return False

def insertar_materia(reg):
    insert = 'INSERT INTO materias(clave, nombre, creditos) VALUES (%s, %s, %s)'
    cursor.execute(insert, (reg['clave'], reg['materia'], reg['creditos'], ))
    conexion.commit()
    return reg['clave']

def existe_nrc(reg):
    select = 'SELECT * FROM oferta_academica WHERE nrc = %s'
    cursor.execute(select, (reg['nrc'],))
    rows = cursor.fetchall()
    if len(rows) > 0:
        return True
    else:
        return False

def insertar_nrc(reg, id_m, id_s, id_p):
    insert = 'INSERT INTO oferta_academica(nrc, cupos, disponibles, id_materia, id_seccion, id_profesor) VALUES (%s, %s, %s, %s, %s, %s)'
    cursor.execute(insert, (reg['nrc'], reg['cupos'], reg['disponibles'], id_m, id_s, id_p,))
    conexion.commit()
    #return cursor.lastrowid

def insertar_horario(reg, id_hora, id_dia, id_edificio, id_aula):
    insert = 'INSERT INTO horario(id_hora, id_dia, id_edificio, id_aula, id_nrc) VALUES (%s, %s, %s, %s, %s)'
    cursor.execute(insert, (id_hora, id_dia, id_edificio, id_aula, reg['nrc'],))
    conexion.commit()

for file in files:
    with open(file) as f:
        registros = json.load(f)
        for reg in registros:
            print(reg)
            if not existe_nrc(reg):
                if not existe_profesor(reg):
                    id_prof = insertar_profesor(reg)
                else:
                    id_prof = get_id_prof(reg['profesor:'])

                if not existe_seccion(reg):
                    id_seccion = insertar_seccion(reg)
                else:
                    id_seccion = get_id_seccion(reg['seccion'])

                if not existe_materia(reg):
                    id_mat = insertar_materia(reg)
                else:
                    id_mat = (reg['clave'])
                insertar_nrc(reg, id_mat, id_seccion, id_prof)

                ########################################################################## 1ra

                if not existe_aula(reg['aula']):
                    id_aula1 = insertar_aula(reg['aula'])
                else:
                    id_aula1 = get_id_aula(reg['aula'])

                if not existe_dia(reg['dias']):
                    id_dia1 = insertar_dia(reg['dias'])
                else:
                    id_dia1 = get_id_dia(reg['dias'])

                if not existe_edificio(reg['edificio']):
                    id_edi1 = insertar_edificio(reg['edificio'])
                else:
                    id_edi1 = get_id_edificio(reg['edificio'])

                if not existe_hora(reg['horas']):
                    id_hora1 = insertar_hora(reg['horas'])
                else:
                    id_hora1 = get_id_hora(reg['horas'])

                insertar_horario(reg, id_hora1, id_dia1, id_edi1, id_aula1)

                ########################################################################## 2da

                if not existe_aula(reg['aula2']):
                    id_aula2 = insertar_aula(reg['aula2'])
                else:
                    id_aula2 = get_id_aula(reg['aula2'])

                if not existe_dia(reg['dias2']):
                    id_dia2 = insertar_dia(reg['dias2'])
                else:
                    id_dia2 = get_id_dia(reg['dias2'])

                if not existe_edificio(reg['edificio2']):
                    id_edi2 = insertar_edificio(reg['edificio2'])
                else:
                    id_edi2 = get_id_edificio(reg['edificio2'])

                insertar_horario(reg, id_hora1, id_dia2, id_edi2, id_aula2)

                ########################################################################## 3ra

                if not existe_aula(reg['aula3']):
                    id_aula3 = insertar_aula(reg['aula3'])
                else:
                    id_aula3 = get_id_aula(reg['aula3'])

                if not existe_dia(reg['dias3']):
                    id_dia3 = insertar_dia(reg['dias3'])
                else:
                    id_dia3 = get_id_dia(reg['dias3'])

                if not existe_edificio(reg['edificio3']):
                    id_edi3 = insertar_edificio(reg['edificio3'])
                else:
                    id_edi3 = get_id_edificio(reg['edificio3'])

                if not existe_hora(reg['horas2']):
                    id_hora3 = insertar_hora(reg['horas2'])
                else:
                    id_hora3 = get_id_hora(reg['horas2'])

                insertar_horario(reg, id_hora3, id_dia3, id_edi3, id_aula3)

                ###########################################################################

            #if not existe_nrc(reg):
            #    id_nrc = insertar_nrc(reg, id_mat, id_seccion, id_prof)
            #else:
            #    id_nrc = (reg['nrc'])