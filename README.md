# 📊 Análise de Atendimentos - Desafio de Estágio

Esse projeto foi feito como parte de um desafio de estágio.
A ideia é simples: analisar um arquivo CSV com registros de atendimentos em feiras e gerar um relatório com algumas informações úteis.

## 🔍 O que o script faz

* Calcula a **taxa de conversão de vendas**
* Mostra a **distribuição dos clientes por tipo de interesse** (peças, serviço, curso ou informações)
* Descobre o **dia mais movimentado da semana**
* Mostra o **horário de pico dos atendimentos** (manhã, tarde ou noite)
* Lista as **10 palavras mais usadas nas mensagens** (ignorando as palavras comuns)
* Gera tudo isso em um relatório `relatorio_analise.txt` dentro da pasta `output`

## 🧪 Testes

O projeto também tem alguns testes simples. Para rodar:

```bash
python -m unittest test_analise.py
```

## 🛠️ Feito com

* Python 3.x
* Pandas
* NLTK

---

