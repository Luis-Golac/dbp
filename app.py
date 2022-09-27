#Imports:



import sys

import random
from flask import (
    Flask,
    abort,
    jsonify, 
    render_template, 
    request,
    redirect,
    url_for
)
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

#Configuration:
app = Flask(__name__)
#Conectandome con la Base de Datos: 
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1234@localhost:5432/lab_1' #Mi URI <- Nos permite conectarnos a nuestra Base de Datos.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #Salia como Warning al correr, poniendo esto, ya no sale <- Es solo pa que no moleste, no es nada del otro mundo (ntp)
db = SQLAlchemy(app) #es necesario para conectarme a SQL (100pre hacerlo) <- es la instancia con la base de datos a traves SQLAlchemy (les damos el medio para que esten conectados entre si)
# migrate = Migrate(app, db) <- Luego descomentar

#Models/Tablas
#Basicamente nuestro modulo"Simular" esta heredando de la clase Padre "db.Model"
class Simular(db.Model): #El db.Model va por defecto, la clase Padre es "db.Model" (los demas modelos heredan de el)
    id=db.Column(db.Integer, primary_key=True) #este es necesario, 100pre poner xd
    Nombres = db.Column(db.String(), nullable = False) 
    Apellidos = db.Column(db.String(), nullable = False)
    Sexo = db.Column(db.String(), nullable = False)
    Tipo_de_documento = db.Column(db.String(), nullable = False)
    Numero_de_documento = db.Column(db.String(), nullable = False)
    Email = db.Column(db.String(), nullable = False)
    Valor_del_vehiculo = db.Column(db.Integer, nullable = False)
    Monto_de_cuota_inicial = db.Column(db.Integer,nullable = False)
    
    #Nose si lo de abajo el "__repr__" esta bien definido (+ que nada en la parte del "return"), luego ver 
    def __repr__(self): #El dunder represent <- nos permitir entender a nosotros (los humanos) una instancia (informacion) cualquiera de un usuario (Columna) <- funciona como un traductor, que nos permite leerlo de manera entendible.
        return f'Simular: nombres = {self.Nombres}, apellidos = {self.Apellidos}, sexo = {self.Sexo}, tipo_de_documento = {self.Tipo_de_documento},nro_de_documento = {self.Numero_de_documento}, email = {self.Email}, valor_del_vehiculo = {self.Valor_del_vehiculo} , monto_de_cuota_inicial = {self.Monto_de_cuota_inicial}'
db.create_all() #Sincroniza los modelos con la Base de Datos <- Detecta que Modelos tienes aqui, y a partir de eso los crea en la Base de Datos (si estos no existen en la Base de Datos)

#Controller:
#DECLARO RUTAS:

data = None
@app.route('/', methods=['GET']) #RUTA
#Este Metodo llamado "index" <- viene a ser el home x asi decirlo
def index(): #METODO (ES LA RUTA PARA LA PAGINA SIMULA TU CREDITO QUE PIDEN)
    #LA FORMA DE TRABAJAR ES CREANDO PLANTILLAS ESPECIFICAS PARA CADA RUTA A LA CUAL DESEEMOS ACCEDER PARA VER UN RESULTADO EN FORMATO HTML
    return render_template('principal.html')

        
    '''if data is None:
        return render_template('principal.html')
    else:
        return render_template('simular.html',data=Simular.query.filter().order_by(desc('id')).first(), num=random.randint(100,1000))'''
     #Ahora en vez de retonar un string retorno una plantilla y dentro de ella coloco todo el contenido 
    #que quiero que se muestre en mi app en el sitio web (ahi si pongo parrafos, strings, etc...).
    #NOTA: EL "render_template('BUSCA LA PLANTILLA')" <- lo que hace es buscar la plantilla dentro de la carpeta template, ese es su trabajo
    #yo solo le tengo que pasar el nombre :)
@app.route('/Simular', methods=['POST'])
def simular():
    response = {}
    try:
        nombres = request.get_json()['nombres']
        apellidos = request.get_json()['apellidos']
        sexo = request.get_json()['sexo']
        tipo_doc = request.get_json()['tipo_doc']
        num_doc = request.get_json()['num_doc']
        Email = request.get_json()['Email']
        Valor_vehic_sol = request.get_json()['Valor_vehic_sol']
        Monto = request.get_json()['Monto']
        simular = Simular(Nombres=nombres, Apellidos=apellidos,
                          Sexo=sexo, Tipo_de_documento=tipo_doc,
                          Numero_de_documento=num_doc, Email=Email,
                          Valor_del_vehiculo=Valor_vehic_sol,
                          Monto_de_cuota_inicial=Monto)
        db.session.add(simular)
        db.session.commit()
        num = random.randint(100,1000)
        result = num*int(Monto)- (int(Valor_vehic_sol)/500 )
        if result < 50000:
            response['status'] = True
        else:
            response['status'] = False
        response['nombres']=nombres
        response['apellidos'] = apellidos
        response['sexo']=sexo
        response['tipo_doc']=tipo_doc
        response['num_doc']=num_doc
        response['Email'] = Email
        response['Valor_vehic_sol']= Valor_vehic_sol
        response['Monto'] = Monto
    except Exception as e:
        print(e)
        print(sys.exc_info())
        db.session.rollback()
    finally:
        db.session.close()
    return jsonify(response)

if __name__ =='__main__':
    app.run(debug=True, port = 5001) #cambio el puerto que esta x defecto (5000 a 5001)

#La sintexis comun para que corra la app es la siguiente:
#if __name__ =='__main__':
    #app.run(debug=True)

#NOTAS: GET<-PASAS LA INFO POR URL-QUERY-PARAMETERS(PASAS INFO POR LA URL) (SOLO RECIBE INFORMACION), POST<-NO VES QUE PASAS LA INFO POR URL-PARAMETERS (ES + SEGURO) Y SIRVE PARA RECOGER Y CREAR INFORMACION EN LA BASE DE DATOS.
