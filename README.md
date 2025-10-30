# Entornos virtuales creados
Proyecto A
Nombre del entorno: venv_1
Comando utilizado:
python -m venv venv_1

Proyecto B
Nombre del entorno: venv_2
Comando utilizado:
python -m venv venv_2
# Activación de entornos virtuales
venv_1\Scripts\activate
venv_2\Scripts\activate

# Instalación de paquetes
Proyecto A — Jupyter
pip install jupyter
pip freeze > requirements.txt

Proyecto B — Pandas
pip install pandas
pip freeze > requirements.txt

# Ejecución de scripts
Proyecto A
python src/algoritmo_a.py

Proyecto B
python src/algoritmo_b1.py
python src/algoritmo_b2.py

![Uploading image.png…]()

