from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
  return "Api para calculo do Teorema de Pitagoras"

@app.route("/calcula")
def calcula():
  a = int(request.args.get('a'))
  b = int(request.args.get('b'))
  c = int(request.args.get('c'))

  retangulo = False

  if ((a == 0 and b == 0 and c == 0) or (a != 0 and b != 0 and c != 0)):
    reposta = {
      'retangulo': retangulo,
      'motivo': "Insira dois valores para calcular o lado que falta!"
    }
    return jsonify(reposta)

  if ((a == 0 and b == 0) or (a == 0 and c == 0) or (c == 0 and b == 0)):
    reposta = {
      'retangulo': retangulo,
      'motivo': "Insira dois valores para calcular o lado que falta!"
    }
    return jsonify(reposta)

  if ((a < 0 or b < 0 or c < 0)):
    reposta = {
      'retangulo': retangulo,
      'motivo': "Os valores devem ser maiores que 0!"
    }
    return jsonify(reposta)

  if a == 0:
    resultado = (b**2 + c**2)**0.5
    retangulo = True
    valorQFalta = 'a'
  elif b == 0:
    if (a > c):
      resultado = (a**2 - c**2)**0.5
      retangulo = True
      valorQFalta = 'b'
    else:
      motivo = "O valor de a deve ser maior que o valor de c."
  elif c == 0:
    if (a > b):
      resultado = (a**2 - b**2)**0.5
      retangulo = True
      valorQFalta = 'c'
    else:
      motivo = "O valor de a deve ser maior que o valor de b."

  if retangulo == True:
    reposta = {
      'retangulo': retangulo,
      'resultado': resultado,
      'valorQFalta': valorQFalta
    }
  else:
    reposta = {'retangulo': retangulo, 'motivo': motivo}

  return jsonify(reposta)

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=5000)
