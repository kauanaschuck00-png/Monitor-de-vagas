# Automação de Planilhas de Vagas (LinkedIn ➔ Google Sheets)

Uma solução automatizada em nuvem desenvolvida para otimizar o acompanhamento de processos seletivos. O sistema extrai e centraliza oportunidades de emprego diretamente do LinkedIn em um banco de dados no Google Sheets, eliminando o trabalho manual de busca e catalogação.

## 🚀 Como Funciona a Arquitetura
O fluxo de dados foi projetado para ser totalmente independente de execução local (Serverless), operando de forma 100% automatizada na nuvem:

1. *Captura de Dados:* Monitoramento de novas vagas postadas e recomendadas no LinkedIn conectadas ao perfil.
2. *Integração (API):* Consumo seguro dos dados e tratamento das informações estruturadas (Cargo, Empresa, Link da Vaga, Data de Publicação).
3. *Persistência:* Atualização automática do banco de dados relacional criado dentro do *Google Sheets*.
4. *Agendamento (Trigger):* Um gatilho temporal está configurado para disparar o script diariamente às *07:00 AM*, garantindo dados frescos logo no início do dia.

## 🛠️ Tecnologias Utilizadas
* *Python:* Linguagem base para engenharia, paginação e tratamento dos dados.
* *Google Sheets API:* Integração e manipulação automatizada de planilhas.
* *Cloud Environment:* Hospedagem em ambiente de nuvem para execução em segundo plano.

## 🔒 Segurança e Boas Práticas
* *Variáveis de Ambiente:* O projeto foi configurado para ocultar tokens de acesso, IDs de planilhas e credenciais confidenciais, utilizando boas práticas de segurança de dados (evitando hardcoded credentials no repositório público).
