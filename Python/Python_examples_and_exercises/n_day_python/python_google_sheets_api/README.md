#### Python Google Sheets API

1. En _GCP_ crear un proyecto
2. En el proyecto creado ir a `APIS & Services`
    - En `ENABLE APIS AND SERVICES` habilitar `Google Drive API`
3. En el proyecto creado ir a `APIS & Services`
    - En `ENABLE APIS AND SERVICES` habilitar `Google Sheets API`
4. Crear las credenciales en `Create credentials`
    - Seleccionar `Google Drive API`
    - En `What data will you be accessing? *` es **Application Data**
    - En `Are you planning to use this API with Compute Engine, Kubernetes Engine, App Engine, or Cloud Functions?` es **No**
    - El nombre en `Service account details` le ponemos `sand-box-sheets-api-test-python`
    - `CREAR AND CONTINUE`
    - En `Grant this service account access to project` asignar **Basic > Editor**
    - `Done`
5. En `Apis and Services > Credentials` seleccionar la que se creo para poder asignarle una llave
6. Seleccionar la pestaña `KEYS` > `ADD KEY` > `CREATE NEW KEY` y seleccionar tipo _JSON_
7. Descargar la llave 🔑
8. Guardar el valor de `client_email`
9. En el _Google Sheet_ en el que queremos W/R lo compartimos con el valor de `client_email`
10. En el anviente virtual istalar las librerias `gspread` `oauth2client`
11. `google_sheets_py.py`
