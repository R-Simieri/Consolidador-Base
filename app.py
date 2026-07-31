from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__, static_folder='static')

# ============================================================
# ROTAS PRINCIPAIS
# ============================================================

@app.route('/')
def dashboard():
    return render_template('dashboard.html')

@app.route('/dashboard.html')
def dashboard_html():
    return render_template('dashboard.html')

@app.route('/renda-variavel')
@app.route('/renda-variavel.html')
def renda_variavel():
    return render_template('renda-variavel.html')

@app.route('/renda-fixa')
@app.route('/renda-fixa.html')
def renda_fixa():
    return render_template('renda-fixa.html')

@app.route('/caixa')
@app.route('/caixa.html')
def caixa():
    return render_template('caixa.html')

# ============================================================
# ROTAS DE GESTÃO
# ============================================================

@app.route('/clientes')
@app.route('/clientes.html')
def clientes():
    return render_template('clientes.html')

@app.route('/movimentacoes')
@app.route('/movimentacoes.html')
def movimentacoes():
    return render_template('movimentacoes.html')

@app.route('/proventos')
@app.route('/proventos.html')
def proventos():
    return render_template('proventos.html')

@app.route('/historico-mensal')
@app.route('/historico-mensal.html')
def historico_mensal():
    return render_template('historico-mensal.html')

@app.route('/instituicoes')
@app.route('/instituicoes.html')
def instituicoes():
    return render_template('instituicoes.html')

@app.route('/relatorios')
@app.route('/relatorios.html')
def relatorios():
    return render_template('relatorios.html')

@app.route('/config')
@app.route('/config.html')
def config():
    return render_template('config.html')

# ============================================================
# ROTA PARA ARQUIVOS ESTÁTICOS (CSS, JS, IMAGENS)
# ============================================================

@app.route('/static/<path:path>')
def serve_static(path):
    return send_from_directory('static', path)

# ============================================================
# ROTA PARA SERVIR O ARQUIVO Carteira Teórica - Simieri - Página85.pdf
# ============================================================

@app.route('/pdf/<path:filename>')
def serve_pdf(filename):
    return send_from_directory('pdf', filename)

# ============================================================
# INICIALIZAÇÃO
# ============================================================

if __name__ == '__main__':
    # Criar pastas necessárias se não existirem
    if not os.path.exists('templates'):
        os.makedirs('templates')
    if not os.path.exists('static'):
        os.makedirs('static')
    if not os.path.exists('pdf'):
        os.makedirs('pdf')
    
    print("=" * 60)
    print("🚀 CARTEIRA PESSOAL - SERVIDOR FLASK")
    print("=" * 60)
    print("📁 Módulos disponíveis:")
    print("   📊 Dashboard:        http://localhost:5000/")
    print("   📈 Renda Variável:   http://localhost:5000/renda-variavel")
    print("   🏦 Renda Fixa:       http://localhost:5000/renda-fixa")
    print("   💳 Caixa:            http://localhost:5000/caixa")
    print("   👥 Clientes:         http://localhost:5000/clientes")
    print("   💵 Movimentações:    http://localhost:5000/movimentacoes")
    print("   📊 Proventos:        http://localhost:5000/proventos")
    print("   📅 Histórico Mensal: http://localhost:5000/historico-mensal")
    print("   🏛️ Instituições:     http://localhost:5000/instituicoes")
    print("   📄 Relatórios:       http://localhost:5000/relatorios")
    print("   ⚙️ Configurações:    http://localhost:5000/config")
    print("=" * 60)
    print("🔄 Servidor rodando em modo DEBUG")
    print("📍 Acesse: http://localhost:5000")
    print("=" * 60)
    
    app.run(debug=True, host='0.0.0.0', port=5000)