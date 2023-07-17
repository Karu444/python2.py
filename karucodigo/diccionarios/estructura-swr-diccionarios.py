empls = {5: {
            "nombre": "carlos",
            "hrs_trabajadas": 5,
            "vlr_hora": 10
            },
         7: {
             "nombre": None,
            "hrs_trabajadas": None,
            "vlr_hora": None
            },
         }

empls[5]["nombre"] = "David"
empls[21]["nombre"]= "Javier"
empls[21]["hrs_trabajadas"] = 50
empls[21]["sexo"] = "M"

empls = {5: {
            "nombre": "carlos",
            "hrs_trabajadas": 5,
            "vlr_hora": 10
            },
         7: {
             "nombre": None,
            "hrs_trabajadas": None,
            "vlr_hora": None
            },
         21: {
             "nombre":"javier",
             "hrs_trabajadas": 50,
             "sexo": "M"
         }}

empls2 = empls.copy()