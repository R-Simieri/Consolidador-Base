from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///carteira.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    senha_hash = db.Column(db.String(200))
    
    def verificar_senha(self, senha):
        return check_password_hash(self.senha_hash, senha)

def login_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if 'usuario_id' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = Usuario.query.filter_by(email=request.form['email']).first()
        if usuario and usuario.verificar_senha(request.form['senha']):
            session['usuario_id'] = usuario.id
            session['usuario_nome'] = usuario.nome
            return redirect(url_for('dashboard'))
        return render_template('login.html', erro='Email ou senha inválidos')
    return render_template('login.html')

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        if Usuario.query.filter_by(email=request.form['email']).first():
            return render_template('cadastro.html', erro='Email já cadastrado')
        usuario = Usuario(
            nome=request.form['nome'],
            email=request.form['email'],
            senha_hash=generate_password_hash(request.form['senha'])
        )
        db.session.add(usuario)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('cadastro.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

@app.route('/')
@login_required
def dashboard():
    return render_template('dashboard.html')

@app.route('/renda-variavel')
@login_required
def renda_variavel():
    return render_template('renda-variavel.html')

@app.route('/renda-fixa')
@login_required
def renda_fixa():
    return render_template('renda-fixa.html')

@app.route('/caixa')
@login_required
def caixa():
    return render_template('caixa.html')

@app.route('/clientes')
@login_required
def clientes():
    return render_template('clientes.html')

@app.route('/movimentacoes')
@login_required
def movimentacoes():
    return render_template('movimentacoes.html')

@app.route('/proventos')
@login_required
def proventos():
    return render_template('proventos.html')

@app.route('/historico-mensal')
@login_required
def historico_mensal():
    return render_template('historico-mensal.html')

@app.route('/instituicoes')
@login_required
def instituicoes():
    return render_template('instituicoes.html')

@app.route('/relatorios')
@login_required
def relatorios():
    return render_template('relatorios.html')

@app.route('/config')
@login_required
def config():
    return render_template('config.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        print("✅ Banco criado!")
    print("🚀 Servidor em: http://localhost:5000")
    print("🔐 Cadastro: http://localhost:5000/cadastro")
    app.run(debug=True)