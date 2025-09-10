
# 🚦 Previsão de Acidentes Viários com Redes Neurais Artificiais  

## 📌 Descrição do Projeto  
Este projeto tem como objetivo **prever acidentes viários** utilizando **redes neurais artificiais** treinadas a partir de dados históricos.  
A motivação do trabalho está em apoiar órgãos de trânsito e pesquisadores a identificar padrões de risco e propor medidas preventivas.  

Os dados coletados incluem informações sobre:  
- **Luminosidade** (ex.: plena noite, amanhecer, pleno dia, anoitecer)  
- **Condições climáticas** (ex.: chuva, neblina, céu claro)  
- **Tipos de via** (reta, curva, túnel, interseção de vias etc.)  
- **Tipos de veículos envolvidos** (automóveis, motocicletas, ônibus, caminhões etc.)  
- **Severidade do acidente** (sem vítimas, com feridos, com vítimas fatais)  

A partir desses dados, o sistema realiza pré-processamento, normalização e treinamento de um modelo de rede neural artificial.

---

## 🛠️ Funcionalidades  
- **Pré-processamento dos dados:**  
  - Substituição de valores categóricos por representações numéricas.  
  - Normalização de variáveis contínuas.  
  - Tratamento de inconsistências (ex.: vírgula vs ponto decimal).  

- **Treinamento da Rede Neural:**  
  - Modelo supervisionado para previsão da gravidade de acidentes.  
  - Aprendizado a partir de dados já normalizados.  
  - Ajuste de pesos por backpropagation.  

- **Avaliação do Modelo:**  
  - Cálculo da acurácia considerando margens de erro (5km, 10km, 15km, etc.).  
  - Geração de métricas de desempenho para análise dos resultados.  

- **Exportação dos Dados Processados:**  
  - Geração de arquivos CSV já normalizados, prontos para uso no modelo de machine learning.  

---

## 🧠 Arquitetura da Rede Neural  
A rede neural artificial utilizada segue a seguinte estrutura:  

- **Camada de Entrada:**  
  - Recebe os atributos pré-processados (luminosidade, clima, via, veículo, etc.).  
- **Camadas Ocultas:**  
  - 2 a 3 camadas densas (fully connected).  
  - Função de ativação: **ReLU**.  
- **Camada de Saída:**  
  - Saída binária ou categórica representando a severidade do acidente:  
    - `[0,0]` → Sem vítimas  
    - `[1,0]` → Com vítimas feridas  
    - `[1,1]` → Com vítimas fatais  
  - Função de ativação: **Softmax** (para classificação multiclasse).  

- **Função de Perda:** *Categorical Crossentropy*  
- **Otimização:** *Adam Optimizer*  
- **Métrica:** *Accuracy*  

---

## 📂 Estrutura do Código  
- `main.py` → Contém funções principais:  
  - `substituir_valores_csv` → converte dados categóricos em valores numéricos.  
  - `normalize` → aplica normalização em valores contínuos.  
  - `calculate_accuracy` → calcula métricas de acurácia da rede neural com base em um CSV de resultados.  

---

## 📊 Exemplo de Resultados  
O modelo gera estatísticas como:  

```
Acerto 5km: 62.35%  
Acerto 10km: 78.42%  
Acerto 15km: 85.67%  
Acerto 20km: 91.23%  
Acerto 25km: 94.10%  
Acerto 30km: 96.85%  
```

*(valores ilustrativos)*  

---

## 🚀 Como Executar  
1. Clone este repositório:  
   ```bash
   git clone https://github.com/seuusuario/seuprojeto.git
   cd seuprojeto
   ```

2. Instale as dependências:  
   ```bash
   pip install pandas
   ```

3. Execute o script principal:  
   ```bash
   python main.py
   ```

4. Funções disponíveis:  
   - **Normalizar dados:**  
     ```python
     substituir_valores_csv("dados.csv", "data_normalizado.csv")
     ```
   - **Calcular acurácia:**  
     ```python
     calculate_accuracy("resultado3.csv")
     ```

---

## 📖 Tecnologias Utilizadas  
- **Python 3**  
- **Pandas** → manipulação e tratamento de dados  
- **NumPy** → operações matemáticas  
- **TensorFlow/Keras** → construção e treinamento da rede neural  
- **Matplotlib/Seaborn** → visualização de resultados (quando aplicável)  

---

## 👨‍💻 Autores 
- Nome: Victor Hugo Nunes Alves, Rafael Borges Morais, Gabriel Nicholas Pires de Moraes
 
- Projeto desenvolvido para fins acadêmicos e de pesquisa.  
