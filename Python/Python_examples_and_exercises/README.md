# Python examples and exercises

It is a repository where I have examples and exercises in python

- a. :octocat: [Importing - Internal & External - Python](https://github.com/macknilan/python-examples-and-exercises/tree/main/n_day_python/importing_internal__external-python)
- b. :octocat: [Send Email & Read Inbox](https://github.com/macknilan/python-examples-and-exercises/tree/main/n_day_python/send_email__read_inbox)
- c. :octocat: [Files - Create, Read & Download](https://github.com/macknilan/python-examples-and-exercises/tree/main/n_day_python/files__create_read__download)
- d. :octocat: [Web Scraping Box Office $$ Numbers](https://github.com/macknilan/python-examples-and-exercises/tree/main/n_day_python/web_scraping_box_office_numbers)
- e. :octocat: [Scrape & Automate behind Password Protected Apps with Selenium & Python](https://github.com/macknilan/python-examples-and-exercises/tree/main/n_day_python/scrape__automate_behind_password_protected_apps_with_selenium__python)
- f. :octocat: [The Spotify API - jupyter notebook](https://github.com/macknilan/python-examples-and-exercises/tree/main/n_day_python/the_spotify_api)
- g. :octocat: [Python Google Sheets API](https://github.com/macknilan/python-examples-and-exercises/tree/main/n_day_python/python_google_sheets_api)
- h. :octocat: [Api Python Google Sheets](https://github.com/macknilan/python-examples-and-exercises/tree/main/n_day_python/api_python_google_sheets)

Black

```bash
black */*.py
```

Flake8

```bash
flake8 */*.py
```

isort multiples configuraciones

```bash
# sort multiple files
isort views.py urls.py

# show a diff before applying any change
isort views.py --diff

# just check for errors
isort urls.py --check-only
```

Aplicar cambios o verificar errores recursivamente

```bash
# check which files will be sorted
isort --recursive --check-only

# sort the whole project
isort --recursive .
```

pylint

```bash
pylint */*.py
```

## Jupyter notebook

Install the classic Jupyter Notebook with:

```bash
pip install notebook
```

To run the notebook:

```bash
jupyter notebook
# or
pipenv run jupyter notebook
```
