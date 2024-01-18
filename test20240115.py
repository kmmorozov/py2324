import requests

result = requests.get('https://nadejnei234.net/doku.php',verify=False )

print(result.text)