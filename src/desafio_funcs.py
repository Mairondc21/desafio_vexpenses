from pathlib import Path

import pandas as pd


def ler_csv(path: Path) -> pd.DataFrame:
    # pega o caminho do arquvio netflix.csv e transforma em dataframe
    df = pd.read_csv(path)

    return df


def questao_01_count_colunas(df: pd.DataFrame) -> pd.DataFrame:
    # .colums retorna todas as colunas existentes no DF
    return df.columns


def questao_02_count_filmes(df: pd.DataFrame):
    """
    faço uma condição que retorna um valor booleano,
    esse valor eu somo e me dara a quantidade total de filmes
    """
    df = (df["type"] == "Movie").sum()

    return df


def questao_03_maiores_diretores(df: pd.DataFrame) -> pd.DataFrame:
    # armazeno as duas colunas que vou usar na variavel abaixo
    diretor_count = df[["type", "director"]]
    """
    agrupo pela coluna diretor os resultados, 
    coloco em ordem decrescentee mostro os 5 primeiros
    """
    diretor_count = df.groupby("director").size().sort_values(ascending=False).head(5)

    return diretor_count


def questao_04_diretores_que_sao_atores(df: pd.DataFrame) -> list:
    # retiro os valores nulos das colunas que serão usadas
    df_clean = df.dropna(subset=["director", "cast", "show_id"])
    """
    transformo os valores da coluna "cast" em string para não dar erro com
    nomes que tenham numeros do tipo int
    """
    # usar .loc para modificar a coluna 'cast' com segurança
    df_clean.loc[:, "cast"] = df_clean["cast"].astype(str)  

    lista_atores = []  # Lista para armazenar os diretores que também atuaram

    for index, row in df_clean.iterrows():
        # percorro cada linha das colunas e armazeno cada uma em uma variavel propria
        director = row["director"]
        cast = row["cast"]
        id = row["show_id"]

        # Separar diretores e elenco por vírgula e remover espaços extras
        lista_director = director.split(",")  # Lista de diretores
        lista_cast = cast.split(",")  # Lista de elenco

        # Verificar se algum diretor está presente no elenco
        for diretor in lista_director:
            # faz a comparação se algum diretor está contido na coluna "cast"
            if diretor in lista_cast:
                lista_atores.append([id, director])  # Armazenar o diretor na lista

    # lista para remover duplicatas
    lista_atores_unicos = []
    for ator in lista_atores:
        if ator not in lista_atores_unicos:
            lista_atores_unicos.append(ator)

    return lista_atores_unicos


def questao_05_quantidade_de_lancamento_por_ano(df: pd.DataFrame) -> pd.DataFrame:
    # extraio e retiro os valores nulos das colunas abaixo
    df_clean = df.dropna(subset=["title", "release_year"])
    """
    agrupo pela coluna release_year os resultados, 
    coloco em ordem decrescentee mostro os 5 primeiros
    """
    df_filtrado = (
        df_clean.groupby("release_year").size().sort_values(ascending=False).head(5)
    )

    return df_filtrado


if __name__ == "__main__":
   pass