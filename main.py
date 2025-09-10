import pandas as pd

def substituir_valores_csv(arquivo_entrada, arquivo_saida):
    """
    Lê um CSV, substitui valores específicos por números e salva o resultado.

    Parâmetros:
    - arquivo_entrada (str): Caminho do arquivo CSV original.
    - arquivo_saida (str): Caminho do novo arquivo CSV com os valores substituídos.
    """
    # Lendo o CSV com separador ";" e garantindo que não haja espaços extras nas colunas
    df = pd.read_csv(arquivo_entrada, encoding="utf-8", sep=",")

    # Dicionário de substituição
    substituicoes = {
        "Plena Noite": 0.7,
        "Amanhecer": 0.5,
        "Pleno dia": 0.9,
        "Anoitecer": 0.3,
        "Céu Claro": 0.8,
        "Ignorado": 0.0,
        "Garoa/Chuvisco": 0.6,
        "Nublado": 0.7,
        "Sol": 0.5,
        "Chuva": 0.9,
        "Nevoeiro/Neblina": 0.4,
        "Vento": 0.3,
        "Granizo": 0.2,
        "Neve": 0.1,
        "Reta": 0.8,
        "Curva": 0.9,
        "Declive": 0.8,
        "Aclive": 0.8,
        "Interseção de Vias": 0.7,
        "Retorno Regulamentado": 0.4,
        "Viaduto": 0.2,
        "Rotatória": 0.5,
        "Ponte": 0.3,
        "Desvio Temporário": 0.6,
        "Em Obras": 0.6,
        "Túnel": 0.1,
        "Caminhão": 0.5,
        "Caminhão-trator": 0.5,
        "Reboque": 0.1,
        "Semireboque": 0.1,
        "Automóvel": 0.7,
        "Caminhonete": 0.7,
        "Motocicleta": 0.9,
        "Camioneta": 0.7,
        "Outros": 0.1,
        "Bicicleta": 0.9,
        "Motoneta": 0.9,
        "Utilitário": 0.7,
        "Trator de esteira": 0.2,
        "Ônibus": 0.5,
        "Trator de rodas": 0.2,
        "Carroça-charrete": 0.2,
        "Trator misto": 0.2,
        "Micro-ônibus": 0.5,
        "Ciclomotor": 0.9,
        "Motor-casa": 0.2,
        "Carro de mão": 0.2,
        "Trem-bonde": 0.2,
        "Triciclo": 0.9,
        "Chassi-plataforma": 0.2,
        "Quadriciclo": 0.9,
        "Com Vítimas Fatais": "[1,1]",
        "Com Vítimas Feridas": "[1,0]",
        "Sem Vítimas": "[0,0]"
    }

    # Limpar os valores: Remover espaços extras
    df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)

    # Substituir valores
    df.replace(substituicoes, inplace=True)

    # Corrigir números decimais que usam vírgula em vez de ponto
    df = df.applymap(lambda x: str(x).replace(",", ".") if isinstance(x, str) and "," in x else x)

    # Salvar o novo CSV
    df.to_csv(arquivo_saida, index=False, sep=";", encoding="utf-8")

    print(f"Arquivo salvo como {arquivo_saida}")

def normalize(value, Xmax=753, Xmin=420.1):
    return ((Xmax - Xmin) * value) + Xmin

def calculate_accuracy(csv_file):
    # Carregar CSV
    df = pd.read_csv(csv_file)
    
    # Normalizar os valores
    df['actual_km'] = df['actual'].apply(normalize)
    df['predicted_km'] = df['predicted'].apply(normalize)
    
    # Calcular erro absoluto
    df['error'] = abs(df['actual_km'] - df['predicted_km'])
    
    # Definir margens
    margins = [5, 10, 15, 20, 25, 30]
    results = {}
    total = len(df)
    
    for margin in margins:
        correct = (df['error'] <= margin).sum()
        results[f"Acerto {margin}km"] = (correct / total) * 100
    
    # Exibir resultados
    for key, value in results.items():
        print(f"{key}: {value:.2f}%")

# Exemplo de uso



if __name__ == '__main__':
    calculate_accuracy('resultado3.csv')
    #substituir_valores_csv("dados.csv", "data_normalizado.csv")
