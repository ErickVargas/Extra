import web
# @
from web import form
from datos import Clientes
from datos import Peliculas
render=web.template.render('templates')
urls = (
    '/(.*)', 'index'
)

db = web.database(dbn='mysql', db='ydpt5o2tl1mxn17v', user='r74fodj940btft9l', pw='xaau4khjomcm5ltu', host='o61qijqeuqnj9chh.cbetxkdyhwsb.us-east-1.rds.amazonaws.com')

Clientes = Clientes()  
Clientes.read()
Pelis=Peliculas()
Pelis.read()
myform = form.Form( 
    form.Dropdown('Cliente', Clientes.getClientes()), 
    
    form.Dropdown('Pelicula',Pelis.getPeliculas()), 
    form.Dropdown('Formato', ["Blueray","DVD"]),
    form.Dropdown('Tiempo', ["1","2","3","4","5","6","7"])
    
    ) 
class index:
    def GET(self,results):
        form = myform()
        resultado=db.select('resumen')
        return render.index(form,resultado)
        
    def POST(self,results): 
        form = myform() 
        if not form.validates(): 
            return render.index(form)
        else:
            costo=0
            if form.d.Formato=="Blueray":
                costo=20
            elif form.d.Formato=="DVD":
                costo=10
            total=int(form.d.Tiempo)*costo
            db.insert('resumen',pelicula=form.d.Pelicula, formato=form.d.Formato,cliente=form.d.Cliente, tiempo=form.d.Tiempo,total=total)
            
            resultado=db.select('resumen')
            # form.d.boe and form['boe'].value are equivalent ways of
            # extracting the validated arguments from the form.
            return render.index(form,resultado)
    

if __name__ == "__main__":
    
    app = web.application(urls, globals())
    app.run()
