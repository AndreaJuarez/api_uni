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
                result=[]           #Un arreglo
                result2={}          #Un diccionario

                #METODO DE CONSULTAR TODO
                if datos['action']=="get":        #Si accion es get va a hacer lo siguiente
                    result2['app_version']="0.2.0" #visualizacion de datos lista
                    result2['status']="200 OK"
                    with open('static/csv/alumnos.csv','r') as csvfile:   #Ruta del archivo csv que va a leer, r es de lectura, csvfile es una variable cualquiera
                        reader = csv.DictReader(csvfile)         #Lector del archivo, DictReader te almacena los datos como en diccionario en este caso en la variable reader
                        for row in reader:              #Lee la primer fila y la manda la arreglo
                            result.append(row)          #Lo manda al arreglo result
                            result2['alumnos']=result      #Result2 en la posicion alumnos, sera lo que va a almacenar en result
                    return json.dumps(result2)          #Va a regresar un json del result2 que es lo que va almacenando el arreglo

                #METODO DE BUSQUEDA
                elif datos['action']=="search":
                    result2={}
                    result2['version']="0.3.0"
                    result2['status']="200 ok"
                   
                    with open('static/csv/alumnos.csv','r') as csvfile:
                        reader = csv.DictReader(csvfile)
                        result = []
                        for row in reader:
                            if str(row['matricula'])==datos['matricula']:
                                result.append(row)
                    return json.dumps(result)

                #METODO DE INSERCION
                elif datos['action']=="put":
                    result2={} 
                    result2['app_version']="0.5.0" 
                    result2['status']="200 OK"
                    
                    matricula = str(datos['matricula'])
                    nombre = str(datos['nombre'])
                    primer_apellido = str(datos['primer_apellido'])
                    segundo_apellido = str(datos['segundo_apellido'])
                    carrera = str(datos['carrera'])

                    result = [] 
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
                
                #METODO DE ACTUALIZAR
                elif datos['action'] == "update":
                    with open ('static/csv/alumnos.csv','r') as csvfiles:
                        reader =csv.DictReader(csvfiles)
                        final = []
                        for row in reader:
                            result = []
                            if  str(row['matricula']) == datos['matricula']:
                                with open ('static/csv/alumnos.csv','w') as csvfile:
                                    writer = csv.writer(csvfile)
                                    writer.writerow(row)
                                    dato1 = datos["matricula"]
                                    dato2 = datos["nombre"]
                                    dato3 = datos["primer_apellido"]
                                    dato4 = datos["segundo_apellido"]
                                    dato5 = datos["carrera"]
                                    result.append(dato1)
                                    result.append(dato2)
                                    result.append(dato3)
                                    result.append(dato4)
                                    result.append(dato5)
                                    final.append(result)
                            else:
                                primero = row['matricula'] 
                                segundo = row['nombre']
                                tercero = row['primer_apellido']
                                cuarto = row['segundo_apellido']
                                quinto = row['carrera']
                                result.append(primero)
                                result.append(segundo)
                                result.append(tercero)
                                result.append(cuarto)
                                result.append(quinto)
                                final.append(result)
                        with open ('static/csv/alumnos.csv','a+', newline = '') as csvfiles:
                            writer = csv.writer(csvfiles)
                            for x in final:
                                writer.writerow(x)
                    return json.dumps("Actualizado")

                #METODO DE ELIMINAR

            else:
                result={}
                result['app_version']="0.4.0" #visualizacion de datos lista
                result['status']="Los datos insertados son incorrectos"
                return json.dumps(result)

        except Exception as e:
            result={}
            result['app_version']="0.4.0" #visualizacion de datos lista
            result['status']=("Faltan valores por insertar{}".format(e.args))
            return json.dumps(result)