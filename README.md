# Previsão da Extração de Ouro / Gold Purification Prediction

![GitHub](https://img.shields.io/github/license/willianadb/gold_purification_prediction)

## Português

### Introdução
Este projeto tem como objetivo prever a pureza da extração de ouro a partir do minério utilizando modelos de machine learning. Ele visa melhorar a eficiência do processo de extração de ouro fornecendo previsões mais precisas sobre a pureza final.

### Conjunto de Dados
O conjunto de dados inclui vários atributos relacionados ao minério e ao processo de extração de ouro, como:
- Composição do minério
- Condições do processo (temperatura, pressão, etc.)
- Rendimento histórico da extração

### Metodologia
1. **Pré-processamento de dados**: Tratamento de valores ausentes, normalização e seleção de variáveis.
2. **Análise Exploratória de Dados (EDA)**: Visualização dos principais atributos para entender correlações e padrões.
3. **Modelagem**: Diversos modelos de machine learning foram testados, como:
   - Regressão Linear
   - Árvores de Decisão
   - Random Forest
   - XGBoost

   Os modelos foram avaliados usando validação cruzada e métricas como RMSE (Erro Quadrático Médio) e R².

### Resultados
O modelo que apresentou melhor desempenho alcançou uma acurácia superior a 90% na previsão da pureza do ouro extraído do minério.

### Como Executar o Projeto

1. Clone o repositório:
   git clone https://github.com/yourusername/gold_purification_prediction.git

2. Instale as dependências:
   pip install -r requirements.txt

3. Execute o Jupyter Notebook para ver a análise e os resultados do modelo:
   jupyter notebook Projeto_Sprint_10.ipynb

### Tecnologias Utilizadas
- Python
- Jupyter Notebook
- Scikit-learn
- XGBoost
- Pandas
- Matplotlib / Seaborn para visualização

### Conclusão
Este projeto oferece uma solução robusta de machine learning para prever a pureza do ouro extraído do minério. Ao implementar e comparar diferentes modelos, podemos melhorar significativamente o processo de purificação do ouro.

---

## English

### Introduction
This project aims to predict the purity of gold extracted from ore using machine learning models. It seeks to improve the efficiency of the gold extraction process by providing better predictions of the final purity.

### Dataset
The dataset includes various attributes related to the ore and the gold extraction process, such as:
- Ore composition
- Process conditions (temperature, pressure, etc.)
- Historical extraction yields

### Methodology
1. **Data Preprocessing**: Handling missing values, normalization, and feature selection.
2. **Exploratory Data Analysis (EDA)**: Visualizing key attributes to understand correlations and patterns.
3. **Modeling**: Several machine learning models were tested, including:
   - Linear Regression
   - Decision Trees
   - Random Forest
   - XGBoost

   Models were evaluated using cross-validation and metrics such as RMSE (Root Mean Squared Error) and R².

### Results
The best-performing model achieved an accuracy of over 90% in predicting the purity of gold extracted from ore.

### How to Run the Project

1. Clone the repository:
   git clone https://github.com/yourusername/gold_purification_prediction.git

2. Install the required dependencies:
   pip install -r requirements.txt

3. Run the Jupyter Notebook to see the analysis and model results:
   jupyter notebook Projeto_Sprint_10.ipynb

### Technologies Used
- Python
- Jupyter Notebook
- Scikit-learn
- XGBoost
- Pandas
- Matplotlib / Seaborn for visualization

### Conclusion
This project provides a robust machine learning solution to predict the purity of gold extracted from ore. By implementing and comparing different models, we can significantly enhance the gold purification process.

