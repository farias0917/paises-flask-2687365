#importar las dependencias
from flask import Flask,render_template

#Crear el objeto flask

app = Flask(__name__)

# Crear una ruta de prueba
@app.route("/holis")
def hola():
    return "<h1>holi</h1>"

# Ruta paises
@app.route("/paises")
def paises():
    userName = "Emanuel Farias"
    continentes=[
        {
        'nombre':'America',
        'poblacion':1036900579,
        'superficie':42549000,
        'densidad':'22.8 hab./km²',
        "numPaises":34,
          "paises":[
            {
                "nom":"Colombia",
                "mon":"Peso",
                "cap":"Bogotá"
            },
            {  "nom":"Perú",
                "mon":"Sol",
                "cap":"Lima"
            },
            {
                "nom":"Argentina",
                "mon":"Peso Argentino",
                "cap":"Buenos Aires"
            }
        ]
    },
    {
        'nombre':'Europa',
        'poblacion':747747395,
        'superficie':10530751 ,
        'densidad':'71 hab./km²',
          "numPaises":34,
          "paises":[
            {
                "nom":"España",
                "mon":"Euro",
                "cap":"Madrid"
            },
            {
                "nom":"Francia",
                "mon":"Euro",
                "cap":"Paris"
            },
            {
                "nom":"Italia",
                "mon":"Euro",
                "cap":"Roma"
            }
        ]

    },
    {
        'nombre':'Asia',
        'poblacion':4598168800,
        'superficie':44541138,
        'densidad':'103,2 hab./km²',
        "numPaises":34,
          "paises":[
            { 
                "nom":"Corea",
                "mon":"Won",
                "cap":"seul"
            },
            {
                "nom":"China",
                "mon":"yuan",
                "cap":"Pekin"
            },
            {
                "nom":"Japon",
                "mon":"Yen",
                "cap":"Tokio"
            }
        ]
    },
       {
        'nombre':'Africa',
        'poblacion':1320000000,
        'superficie':30221535,
        'densidad':'43,7 hab./km²',
        "numPaises":34,
        "paises":[
            {
                "nom":"nigeria",
                "mon":"Naira",
                "cap":"Abuya"
            },
            {
                "nom":"Marruecos",
                "mon":"Dírham",
                "cap":"Rabat"
            },
            {
                "nom":"Kenia",
                "mon":"Chelín",
                "cap":"Nairobi"
            }
        ]
    }
    ]
    return render_template('paises.html',
                           userName = userName,
                           continentes = continentes)