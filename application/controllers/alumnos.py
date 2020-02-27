import web
import app
import json
import csv

render = web.template.render('application/controllers/')   #En esta no se ocupa

class Alumnos:
    def GET(self):
        try:
            datos=web.input()     #Los datos introducidos por el usuario se almacenaran en datos
            if datos['token']=="1234":     #Si el usuario ingresa bien el token se declarara lo siguiente
                if datos['action']=="get":        #Si accion es get va a hacer lo siguiente
                    result=[]           #Un arreglo
                    result2={}          #Un diccionario
                    result2['app_version']="0.2.0" #visualizacion de datos lista
                    result2['status']="200 OK"
                    with open('static/csv/alumnos.csv','r') as csvfile:   #Ruta del archivo csv que va a leer, r es de lectura, csvfile es una variable cualquiera
                        reader = csv.DictReader(csvfile)         #Lector del archivo, DictReader te almacena los datos como en diccionario en este caso en la variable reader
                        for row in reader:              #Lee la primer fila y la manda la arreglo
                            result.append(row)          #Lo manda al arreglo result
                            result2['alumnos']=result      #Result2 en la posicion alumnos, sera lo que va a almacenar en result
                    return json.dumps(result2)          #Va a regresar un json del result2 que es lo que va almacenando el arreglo
                
                if datos['action']=="insert":
                    result={} 
                    result['app_version']="0.2.0" 
                    result['status']="200 OK"
                    matricula = str(datos['matricula'])
                    nombre = str(datos['nombre'])
                    primer_apellido = str(datos['primer_apellido'])
                    segundo_apellido = str(datos['segundo_apellido'])
                    carrera = str(datos['carrera'])

                    result = [] #Crea array
                    result.append(matricula)
                    result.append(nombre)
                    result.append(primer_apellido)
                    result.append(segundo_apellido)
                    result.append(carrera)

                    resultado={}
                    resultado['matricula']=matricula
                    resultado['nombre']=nombre
                    resultado['primer_apellido']=primer_apellido
                    resultado['segundo_apellido']=segundo_apellido
                    resultado['carrera']=carrera
                    
                    result2=[]
                    result2.append(resultado)

                    with open('static/csv/alumnos.csv', 'a+', newline='') as variable_cualquiera:
                        writer = csv.writer(variable_cualquiera) 
                        writer.writerow(result)
                    return result

            else:
                result={}
                result['app_version']="0.2.0" #visualizacion de datos lista
                result['status']="Los datos insertados son incorrectos"
                return json.dumps(result)

        except Exception as e:
            result={}
            result['app_version']="0.2.0" #visualizacion de datos lista
            result['status']=("Faltan valores por insertar{}".format(e.args))
            return json.dumps(result)