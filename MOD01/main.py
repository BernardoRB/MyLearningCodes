import requests
import pandas as pd

url = 'https://loterias.caixa.gov.br/Paginas/Download-Resultados.aspx'
r = requests.get(url)

r_text = r.text

df = pd.read_html(r_text)