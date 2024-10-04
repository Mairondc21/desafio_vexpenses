from desafio_funcs import *

if __name__ == "__main__":
    url = "./dados/netflix_titles.csv"
    df = ler_csv(url)

    q01 = questao_01_count_colunas(df)
    q02 = questao_02_count_filmes(df)
    q03 = questao_03_maiores_diretores(df)
    q04 = questao_04_diretores_que_sao_atores(df)
    q05 = questao_05_quantidade_de_lancamento_por_ano(df)

    print(f'questão 01:\n Colunas:\n{q01}\n\n'
          f'questão 02:\n Total de filmes = {q02}\n\n'
          f'questão 03:\n Top 5 diretores:\n{q03}\n\n'
          f'questão 04:\n Diretores que são atores:\n{q04}\n\n'
          f'questão 05:\n Top 5 filmes e series lançado por ano:\n{q05}\n\n'
          )
