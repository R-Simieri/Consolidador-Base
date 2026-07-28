from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Ativo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    codigo = db.Column(db.String(10), nullable=False)
    tipo = db.Column(db.String(20), nullable=False)  # Ação, FII, ETF, BDR
    empresa = db.Column(db.String(100))
    quantidade = db.Column(db.Integer, default=0)
    preco_medio = db.Column(db.Float, default=0.0)
    
    def __repr__(self):
        return f'<Ativo {self.codigo}>'

class HistoricoMensal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mes = db.Column(db.String(20))
    entrada = db.Column(db.Float)
    aporte = db.Column(db.Float)
    tx_mes = db.Column(db.Float)
    total = db.Column(db.Float)
    tx_adm = db.Column(db.Float)
    ir = db.Column(db.Float)
    liquido = db.Column(db.Float)
    tx_nominal = db.Column(db.Float)
    
    def __repr__(self):
        return f'<Historico {self.mes}>'

# Para criar as tabelas no banco (roda uma vez)
def criar_banco(app):
    with app.app_context():
        db.create_all()
        print("✅ Banco de dados criado com sucesso!")