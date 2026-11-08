import gspread
from google.oauth2.service_account import Credentials

# 1. Definimos o escopo de acesso que o Python precisa (Drive e Planilhas)
escopo = [
    "https://googleapis.com",
    "https://googleapis.com"
]

# 2. O cérebro carrega o crachá de segurança de trás para frente
credenciais = Credentials.from_service_account_file("chave.json", scopes=escopo)
cliente = gspread.authorize(credenciais)

# 3. Conectamos com a planilha (Coloque AQUI o nome exato da sua planilha do Google)
NOME_DA_PLANILHA = "vagas TI" 

try:
    planilha = cliente.open(NOME_DA_PLANILHA).sheet1
    print(f"Sucesso: Conectado à planilha '{NOME_DA_PLANILHA}'!")
    
    # 4. Simulando a inserção de uma vaga automatizada
    nova_vaga = ["Engenheiro de Software AI", "Itaú Unibanco", "https://itau.com.br"]
    planilha.append_row(nova_vaga)
    
    print("Engenharia ativa: Nova vaga adicionada com sucesso via Python!")

except Exception as erro:
    print(f"Erro no processo: Verifique se compartilhou a planilha com o e-mail do robô. Detalhe: {erro}")