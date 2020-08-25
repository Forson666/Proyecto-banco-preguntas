from flask import Flask, redirect, url_for, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import inspect, MetaData
from sqlalchemy.orm import relationship

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///BasesDeDatos/BancoPreguntas.db'
app.config['SECRET_KEY'] = "123456789"

db = SQLAlchemy(app)
inspector = inspect(db.engine)

class categoria(db.Model):
   __tablename__ = 'Categorias'
   id = db.Column('cat_id', db.Integer, primary_key = True)
   cat_nombre = db.Column(db.String(100), nullable=False)
   cat_tipo = db.Column(db.Integer, db.ForeignKey('Tipos de categoria.tca_id'), unique=False, nullable=False)

   def __init__(self, nombre, tipo):
       self.cat_nombre = nombre
       self.cat_tipo = tipo

class tipo_categoria(db.Model):
   __tablename__ = 'Tipos de categoria'
   id = db.Column('tca_id', db.Integer, primary_key = True)
   tca_nombre = db.Column(db.String(50), unique=True,nullable=False)

   categorias = relationship("categoria", backref="tipo")

   def __init__(self, nombre):
       self.tca_nombre = nombre

class pregunta(db.Model):
   __tablename__ = 'Preguntas'
   id = db.Column('pre_id', db.Integer, primary_key = True)
   pre_texto = db.Column(db.String(150))
   cat_id = db.Column(db.Integer, db.ForeignKey('Categorias.cat_id'), unique=False, nullable=False) 
   com_id = db.Column(db.Integer, db.ForeignKey('Competencias.com_id'), unique=False, nullable=False)
   tpr_id = db.Column(db.Integer, db.ForeignKey('Tipos de pregunta.tpp_id'), unique=False, nullable=False)

   def __init__(self, texto, categoria, tipo, competencia):
      self.pre_texto = texto
      self.cat_id = categoria
      self.com_id = competencia
      self.tpr_id = tipo

class competencia(db.Model):
   __tablename__ = 'Competencias'
   id = db.Column('com_id', db.Integer, primary_key = True)
   com_nombre = db.Column(db.String(100))
   com_tipo = db.Column(db.Integer, db.ForeignKey('Tipos de competencia.tco_id'), unique=False, nullable=False)
   com_desc = db.Column(db.String(200))

   def __init__(self, nombre, tipo, desc):
       self.com_nombre = nombre
       self.com_tipo = tipo
       self.com_desc = desc

class tipo_competencia(db.Model):
   __tablename__ = 'Tipos de competencia'
   id = db.Column('tco_id', db.Integer, primary_key = True)
   tco_nombre = db.Column(db.String(50))

   def __init__(self, nombre):
       self.tco_nombre = nombre 

class tipo_pregunta(db.Model):
   __tablename__ = 'Tipos de pregunta'
   id = db.Column('tpp_id', db.Integer, primary_key = True)
   tpp_nombre = db.Column(db.String(50))

   def __init__(self, nombre):
       self.tpp_nombre = nombre 

class respuesta(db.Model):
   __tablename__ = 'Respuestas'
   id = db.Column('res_id', db.Integer, primary_key = True)
   res_texto = db.Column(db.String(100))

   def __init__(self, texto):
       self.res_texto = texto

class usuario(db.Model):
   __tablename__ = 'Usuarios'
   id = db.Column('user_id', db.Integer, primary_key = True)
   user_nombre = db.Column(db.String(30))
   user_apellido = db.Column(db.String(30))
   user_passw = db.Column(db.String(30))
   user_email = db.Column(db.String(60))
   user_proy = db.Column(db.String(30))
   user_cod = db.Column(db.String(30))
   rol_id = db.Column(db.Integer, db.ForeignKey('Roles.rol_id'), unique=False, nullable=False) 

   def __init__(self, nombre, apellido, passw, email, proy, cod, rol_id):
      self.user_nombre = nombre
      self.user_apellido = apellido
      self.user_passw = passw
      self.user_email = email
      self.user_proy = proy
      self.user_cod = cod
      self.rol_id = rol_id

class rol(db.Model):
   __tablename__ = 'Roles'
   id = db.Column('rol_id', db.Integer, primary_key = True)
   rol_nombre = db.Column(db.String(50))

   def __init__(self, nombre):
       self.rol_nombre = nombre

class evaluacion(db.Model):
   __tablename__ = 'Evaluaciones'
   id = db.Column('eval_id', db.Integer, primary_key = True)
   eval_nombre = db.Column(db.String(50))
   eval_pporPag = db.Column(db.Integer)
   eval_maxPuntos = db.Column(db.Integer)
   eval_puntosP = db.Column(db.Integer)
   pregunta_id = db.Column(db.Integer)
   eval_conjunta = db.Column(db.Boolean) 

   def __init__(self, nombre, pporPag, maxPuntos, puntosP, pregunta_id, conjunta):
      self.eval_nombre = nombre
      self.eval_pporPag = pporPag
      self.eval_maxPuntos = maxPuntos
      self.eval_puntosP = puntosP
      self.pregunta_id = pregunta_id
      self.eval_conjunta = conjunta

@app.route('/')
def home():
   entidades = db.engine.table_names()
   campos = inspector.get_columns(entidades[0])
   m = MetaData()
   m.reflect(bind=db.engine)
   registros = db.session.query(m.tables[entidades[0]]).all()
   # buscar metadata 
   return render_template('index.html', entidades = entidades, nav = entidades[0], campos = campos, registros = registros)

@app.route('/crear/<entidad>', methods=["POST", "GET"])
def crear(entidad):
   if entidad == "Tipos de categoria":
      crearTipoCategoria(request.form['tca_nombre'])
   elif entidad == "Categorias":
      crearCategoria(request.form['cat_nombre'], request.form['cat_tipo'])
   elif entidad == "Tipos de competencia":
      crearTipoCompetencia(request.form['tco_nombre'])
   elif entidad == "Competencias":
      crearCompetencia(request.form['com_nombre'], request.form['com_tipo'], request.form['com_desc'])
   elif entidad == "Tipos de pregunta":
      crearTipoPregunta(request.form['tpp_nombre'])
   elif entidad == "Preguntas":
      crearPregunta(request.form['pre_texto'], request.form['tpr_id'], request.form['cat_id'], request.form['com_id'])
   elif entidad == "Roles":
      crearRol(request.form['rol_nombre'])
   elif entidad == "Usuarios":
      crearUsuario(request.form['user_nombre'], request.form['user_apellido'], request.form['user_passw'], request.form['user_email'], request.form['user_proy'], request.form['user_cod'], request.form['rol_id'])
   elif entidad == "Evaluaciones":
      if request.form['eval_conjunta'] == 'false':
         crearEvaluacion(request.form['eval_nombre'], request.form['eval_pporPag'], request.form['eval_maxPuntos'], request.form['eval_puntosP'], request.form['pregunta_id'], False)
      else:
         crearEvaluacion(request.form['eval_nombre'], request.form['eval_pporPag'], request.form['eval_maxPuntos'], request.form['eval_puntosP'], request.form['pregunta_id'], True)
   elif entidad == "Respuestas":
      crearRespuesta(request.form['res_texto'])
   
   flash("Se ha registrado en " + entidad)

   return nav(entidad)

@app.route('/crearTipoCategoria/<nombre>')
def crearTipoCategoria(nombre):
   tipo = tipo_categoria(nombre)
   db.session.add(tipo)
   db.session.commit()

@app.route('/crearCategoria/<nombre>/<tipo>')
def crearCategoria(nombre, tipo):
   cat = categoria(nombre, tipo)
   db.session.add(cat)
   db.session.commit()

@app.route('/crearTipoCompetencia/<nombre>')
def crearTipoCompetencia(nombre):
   tipo = tipo_competencia(nombre)
   db.session.add(tipo)
   db.session.commit()

@app.route('/crearCompetencia/<nombre>/<tipo>/<desc>')
def crearCompetencia(nombre, tipo, desc):
   com = competencia(nombre, tipo, desc)
   db.session.add(com)
   db.session.commit()

@app.route('/crearTipoPregunta/<nombre>')
def crearTipoPregunta(nombre):
   tipo = tipo_pregunta(nombre)
   db.session.add(tipo)
   db.session.commit()

@app.route('/crearPregunta/<texto>/<tipo>/<cat>/<com>')
def crearPregunta(texto, tipo, cat, com):
   pre = pregunta(texto, cat, tipo, com)
   db.session.add(pre)
   db.session.commit()

@app.route('/crearRol/<nombre>')
def crearRol(nombre):
   r = rol(nombre)
   db.session.add(r)
   db.session.commit()

@app.route('/crearUsuario/<nombre>/<apellido>/<passw>/<email>/<proy>/<cod>/<rol_id>')
def crearUsuario(nombre, apellido, passw, email, proy, cod, rol_id):
   usr = usuario(nombre, apellido, passw, email, proy, cod, rol_id)
   db.session.add(usr)
   db.session.commit()

@app.route('/crearEvaluacion/<nombre>/<pporPag>/<maxPuntos>/<puntosP>/<pregunta_id>/<conjunta>')
def crearEvaluacion(nombre, pporPag, maxPuntos, puntosP, pregunta_id, conjunta):
   eva = evaluacion(nombre, pporPag, maxPuntos, puntosP, pregunta_id, conjunta)
   db.session.add(eva)
   db.session.commit()

@app.route('/crearRespuesta/<res_texto>')
def crearRespuesta(res_texto):
   res = respuesta(res_texto)
   db.session.add(res)
   db.session.commit()

@app.route('/borrar/<entidad>/<id>')
def borrar(entidad, id):
   #m = MetaData()
   #m.reflect(bind=db.engine)
   #tmp = db.session.query(m.tables[entidad]).filter_by(id=int(id)).delete()
   
   getClass(entidad).query.filter_by(id=int(id)).delete()
   
   db.session.commit()
   flash("Se ha borrado un registro de " + entidad)
   return nav(entidad)

@app.route('/editar/<entidad>/<id>', methods=["POST", "GET"])
def editar(entidad, id):
   campos = inspector.get_columns(entidad)
   for campo in campos[1:]:
      db.session.query(getClass(entidad)).filter_by(id=int(id)).update({f"{campo['name']}": request.form[f"{id}{campo['name']}"]})
   
   db.session.commit()
   flash("Se ha editado un registro de " + entidad)
   return nav(entidad)

@app.route('/nav/<entidad>')
def nav(entidad):
   entidades = db.engine.table_names()
   campos = inspector.get_columns(entidad)
   m = MetaData()
   m.reflect(bind=db.engine)
   registros = db.session.query(m.tables[entidad]).all()
   # para las variables tambien se puede -> session['campos'] = campos
   return render_template('index.html', entidades = entidades, nav = entidad, campos = campos, registros = registros)

def getClass(entidad):
   if entidad == "Categorias":
      return categoria
   elif entidad == "Tipos de categoria":
      return tipo_categoria
   elif entidad == "Preguntas":
      return pregunta
   elif entidad == "Competencias":
      return competencia
   elif entidad == "Tipos de competencia":
      return tipo_competencia
   elif entidad == "Tipos de pregunta":
      return tipo_pregunta
   elif entidad == "Respuestas":
      return respuesta
   elif entidad == "Usuarios":
      return usuario
   elif entidad == "Roles":
      return rol
   elif entidad == "Evaluaciones":
      return evaluacion

if __name__ == '__main__':
   db.drop_all()
   db.create_all()
   app.run(debug = True)