from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/process_login', methods=['GET', 'POST'])
def process_login():
    if request.method == 'POST':
        # Lógica para processar o formulário de login
        # Exemplo: obter os dados do formulário
        name = request.form.get('name')
        email = request.form.get('email')
        institution = request.form.get('institution')
        subject = request.form.get('subject')

        # Redirecionar para a rota de informações e passar os dados do formulário
        return redirect(url_for('show_info', name=name, email=email, institution=institution, subject=subject))
    else:
        # Se o método for GET, redirecione de volta para a página de login
        return redirect(url_for('login'))

@app.route('/info')
def show_info():
    # Lógica para exibir as informações na página info.html
    # Exemplo: obter os dados passados pela rota
    name = request.args.get('name')
    email = request.args.get('email')
    institution = request.args.get('institution')
    subject = request.args.get('subject')

    return render_template('info.html', name=name, email=email, institution=institution, subject=subject)

if __name__ == '__main__':
    app.run(debug=True)
