# Importação das bibliotecas necessárias
import os
import re

import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist


# Caminho dos dados
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
caminho_dados = os.path.join(BASE_DIR, "data", "atendimentos_feira.csv")
caminho_saida = os.path.join(BASE_DIR, "output", "relatorio_analise.txt")



try:
    stopwords.words('portuguese')
except LookupError:
    nltk.download('stopwords')
    
try:
    word_tokenize("teste")
except LookupError:
    nltk.download('punkt_tab')


# Caso a pasta não exista, cria a pasta "output"
if not os.path.exists(os.path.join(BASE_DIR, "output")):
    os.makedirs(os.path.join(BASE_DIR, "output"))


# Caso não consiga carregar os dados, encerra o programa
try:
    df = pd.read_csv(caminho_dados)
except FileNotFoundError:
    print("Erro: Arquivo não encontrado. Verifique o caminho.")
    exit()



def taxa_conversao():
    """Retorna o número total de vendas e calcula a taxa de conversão de vendas."""
    vendas = df["converteu_venda"].value_counts()["sim"]
    total = df["converteu_venda"].count()
    taxa = vendas / total * 100

    return total, taxa

def interesse():
    """Retorna a contagem de clientes por tipo de interesse."""
    peca = df["tipo_interesse"].value_counts()["peças"]
    curso = df["tipo_interesse"].value_counts()["curso"]
    informacoes = df["tipo_interesse"].value_counts()["informações"]
    servico = df["tipo_interesse"].value_counts()["serviço"]

    return peca, curso, informacoes, servico

def dia_movimentado():
    """Retorna o dia mais movimentado da semana."""
    dias = {
    "Monday": "Segunda-feira",
    "Tuesday": "Terça-feira",
    "Wednesday": "Quarta-feira",
    "Thursday": "Quinta-feira",
    "Friday": "Sexta-feira",
    "Saturday": "Sábado",
    "Sunday": "Domingo"
    }

    df["data_hora"] = pd.to_datetime(df["data_hora"])
    df["dia_semana"] = df["data_hora"].dt.dayofweek
    df["dia_nome_semana"] = df["data_hora"].dt.day_name()
    contagem_dias = df["dia_nome_semana"].value_counts()
    dia_pico_ingles = contagem_dias.idxmax()  
    dia_pico = dias[dia_pico_ingles]  

    return dia_pico


def horario_pico():
    """Retorna o período do dia com mais atendimentos e a quantidade."""
    df["hora"] = df["data_hora"].dt.hour
    bins = [6,12,18,24]
    label = ["Manhã", "Tarde", "Noite"]
    df["periodo"] = pd.cut(df["hora"], bins = bins, labels = label, right = False)
    contagem_periodo = df["periodo"].value_counts()
    periodo_pico = contagem_periodo.idxmax()
    atendimentos_pico = contagem_periodo[periodo_pico]

    return periodo_pico, atendimentos_pico

def palavras():
    """Retorna o top 10 das palavras mais usadas nas mensagens."""
    mensagens = " ".join(df["mensagem"])
    mensagens = mensagens.lower() 
    palavras = word_tokenize(mensagens)
    stop_words = set(stopwords.words('portuguese')) 
    palavras_filtradas = [w for w in palavras if w.isalpha() and w not in stop_words]
    frequencia = FreqDist(palavras_filtradas)
    top10 = frequencia.most_common(10)

    return top10

def relatorio():
    """Gera o relatório completo em arquivo de texto."""
    try:
        with open(caminho_saida, "w", encoding="utf-8") as f:
            total, taxa = taxa_conversao()
            peca, curso, informacoes, servico = interesse()
            dia_pico = dia_movimentado()
            periodo_pico, atendimentos_pico = horario_pico()
            top10 = palavras()

            f.write(f"Total de atendimentos: {total}\n")
            f.write(f"Taxa de conversão: {taxa:.2f}%\n\n")
            f.write(f"Clientes interessados:\n")
            f.write(f"- Peças: {peca}\n")
            f.write(f"- Cursos: {curso}\n")
            f.write(f"- Informações: {informacoes}\n")
            f.write(f"- Serviços: {servico}\n\n")
            f.write(f"Horário de pico: {periodo_pico} ({atendimentos_pico} atendimentos)\n")
            f.write(f"Dia mais movimentado: {dia_pico}\n\n")
            f.write("Top 10 palavras mais usadas:\n")
            for i, (palavra, contagem) in enumerate(top10, start=1):
                f.write(f"{i}º: '{palavra}' foi utilizada {contagem} vezes\n")
        print("Relatório gerado com sucesso!")
    except Exception as e:
        print("Erro ao gerar relatório!", e)

relatorio()
