import mysql.connector

conexion = mysql.connector.connect(user = 'root',database = 'agendabd' )
cursor = conexion.cursor()

query = "SELECT * FROM oferta_academica"
horarios = "SELECT * FROM horario WHERE id_nrc = %s"
#selectOferta = "SELECT * FROM oferta_academica WHERE nrc = %s"
selectProf = "SELECT * FROM profesores WHERE id = %s"
selectMat = "SELECT * FROM materias WHERE clave = %s"
selectSec = "SELECT * FROM secciones WHERE id = &s"
selectHora = "SELECT * FROM horas WHERE id = %s"
selectDia = "SELECT * FROM dias WHERE id = %s"
selectEdif = "SELECT * FROM edificios WHERE id = %s"
selectAula = "SELECT * FROM aulas WHERE id = %s"
selectPeriodo = "SELECT * FROM periodos"

cursor.execute(query)
ofertas = cursor.fetchall()
lista_oferta = []
for oferta in ofertas:
    print(oferta)
    #cursor.execute(horarios, (oferta[0],))
    #horario = cursor.fetchall()
    #print(horario)
    #print(horario[1][2])
    print("--------------------------------------------------------------------")