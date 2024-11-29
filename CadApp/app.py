from flask import Flask, render_template, request

app = Flask("CADASTRO")


@app.route('/')
def home():
    return render_template('cad_form.html')

@app.route('/cadview', methods=['POST'])
def cad_view():
    try:
        cadastro_cliente = request.get_json()
    except:
        print(request.form)
        cadastro_cliente = request.form
    return render_template('cad_view.html', dados=cadastro_cliente)