#### Api Python Google Sheets

-   :link: [Python Quickstart](https://developers.google.com/sheets/api/quickstart/python)
-   :link: [Using OAuth 2.0 for Server to Server Applications](https://developers.google.com/identity/protocols/oauth2/service-account#python)
-   :link: [Google Sheets API](https://developers.google.com/sheets/api/reference/rest) :rotating_light:
-   :link: [Google Sheets API Samples](https://developers.google.com/sheets/api/samples/reading) :rotating_light:
-   :link: :video_camera: [Google Sheets - Python API, Read & Write Data](https://www.youtube.com/watch?v=4ssigWmExak)

1. En _GCP_ crear un proyecto
2. En el proyecto creado ir a `APIS & Services`
    - En `ENABLE APIS AND SERVICES` habilitar `Google Sheets API`
3. Crear las credenciales en `Create credentials`
    - Seleccionar `Google Drive API`
    - En `What data will you be accessing? *` es **Application Data**
    - En `Are you planning to use this API with Compute Engine, Kubernetes Engine, App Engine, or Cloud Functions?` es **No**
    - El nombre en `Service account details` le ponemos `sand-box-sheets-api-test-python`
    - `CREAR AND CONTINUE`
    - En `Grant this service account access to project` asignar **Basic > Editor**
    - `Done`
4. En `Apis and Services > Credentials` seleccionar la que se creo para poder asignarle una llave
5. Seleccionar la pestaña `KEYS` > `ADD KEY` > `CREATE NEW KEY` y seleccionar tipo _JSON_
6. Descargar la llave 🔑
7. Guardar el valor de `client_email`
8. En el _Google Sheet_ en el que queremos W/R lo compartimos con el valor de `client_email`
9. En el anviente virtual istalar las librerias `google-api-python-client google-auth-httplib2 google-auth-oauthlib`
10. `api_python_google_sheets.py`
