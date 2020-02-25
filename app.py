# TODO buscar comandos de git en consola de visual, git con linea de comandos 
# TODO ingresar el metodo para que salga el error

import web

from web.template import ALLOWED_AST_NODES
ALLOWED_AST_NODES.append('Constant') bjcbsjcb

urls = (
	'/alumnos?', 'application.controllers.alumnos.Alumnos' #el simbolo ? inidca que recibira variables en la URL
)
app = web.application(urls, globals())

#render = web.template.render('templates/')  #dice que la carpeta de las paginas web sera templates

if __name__ == "__main__":
	web.config.debug = False
	app.run()