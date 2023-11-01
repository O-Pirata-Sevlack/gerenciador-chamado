from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        P1 = request.form['P1']
        P2 = request.form['P2']
        P3 = request.form['P3']
        P4 = request.form['P4']
        P5 = request.form['P5']
        P6 = request.form['P6']
        arquivo = "registro.txt"
        with open(arquivo, "a") as arquivo:
            arquivo.write((" Nome de quem ligou: " + P1 + "\n"))
            arquivo.write((" Ramal: " + P2 + "\n"))
            arquivo.write((" Setor: " + P3 + "\n"))
            arquivo.write((" Foi realizado o chamado: " + P4 + "\n"))
            if P6 == int:
                arquivo.write((" Código do chamado: " + P6 + "\n"))
            arquivo.write((" Qual a solicitação: " + P5 + "\n"))
            arquivo.write("\n")
            arquivo.write("\n")
            arquivo.close()
            
    return render_template('index.html')

@app.route('/readfile')
def read_txt_file():
    with open('registro.txt', 'r') as file:
        data = file.read()
    return data

if __name__ == '__main__':
    app.run(debug=True)