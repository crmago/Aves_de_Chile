import requests
import json

#1. solicito los datos de las aves
url = 'https://aves.ninjas.cl/api/birds'
response = requests.get(url)

#2. transformo el resultado a una lista de cosas
birds = json.loads(response.text)

#3. acortamos la lista a las primeras 20
birds = birds[0:216]

#4. Armamos el texto que contien todas las col´s 3
cols_3 = ''
for bird in birds:
    cols_3 += f'''
    <div class="col-3">
                <div class="card" style="width: 18rem; overflow: hidden;">
                    <img src="{bird['images']['full']}"
                        class="card-img-top" alt="..."
                        onmouseover="this.style.transform = 'scale(1.1)'; this.style.transition = 'transform 0.3s ease';"
                        onmouseout="this.style.transform = 'scale(1)'; this.style.transition = 'transform 0.3s ease';">
                    <div class="card-body">
                        <h5 class="card-title">{bird['name']['spanish']}</h5>
                    </div>
                    <ul class="list-group list-group-flush">
                        <li class="list-group-item">{bird['name']['english']}</li>
                        <li class="list-group-item">{bird['name']['latin']}</li>
                    </ul>
                </div>
            </div>
    '''

#5. creamos HTML completo interpolando cols-3
html_completo = f'''
<!doctype html>
<html lang="en">

<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Aves de Chile</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
    <link rel="stylesheet" href="assets/style.css">
</head>

<body style="background-color: darkolivegreen;">
    <nav class="navbar fixed-top bg-body-tertiary navbar bg-primary" data-bs-theme="dark">
        <div class="container-fluid">
            <span class="navbar-brand navbar-brand mb-0 h1 d-block mx-auto h1 ">Aves De Chile</span>
        </div>
    </nav>
    <div class="container" style="padding-top: 150px;">
        <div class="row">
            <!-- aca van los col-3-->
            {cols_3}
        </div>
    </div>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"
        integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz"
        crossorigin="anonymous"></script>
</body>

</html>
'''
print(html_completo)

#6. Escribir el contenido del HTML en un archivo
with open('index.html', 'w', encoding='utf-8') as file:
    file.write(html_completo)

print("Archivo HTML generado con éxito.")