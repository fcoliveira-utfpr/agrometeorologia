# 🌱 Agrometeorologia Aplicada com Python

Este repositório reúne notebooks didáticos utilizados na disciplina de **Agrometeorologia**, com foco na análise de dados climáticos, caracterização clima–solo–cultura e aplicação em balanço hídrico agrícola, utilizando **Python no Google Colab**.

Os notebooks foram desenvolvidos com abordagem prática, utilizando dados reais e exemplos aplicados à agricultura brasileira.

---

## 🎯 Objetivos da disciplina

Ao final do uso destes notebooks, o estudante será capaz de:

- Obter e organizar dados meteorológicos de bases públicas  
- Analisar variáveis climáticas aplicadas à agricultura  
- Construir climogramas  
- Integrar informações de clima, solo e cultura  
- Calcular e interpretar o balanço hídrico agrícola  

---

## 🚀 Como utilizar os notebooks

1. Abra o notebook desejado diretamente no GitHub  
2. Clique em **“Open in Colab”**  
3. Execute as células **na ordem**  
4. Leia atentamente os textos explicativos (Markdown) e comentários no código  

> 📌 Recomenda-se seguir a **ordem sugerida** dos notebooks.

---

## 📚 Organização dos notebooks

### 🔹 1. Dados climáticos

#### `dados_nasapower.ipynb`
**Objetivo:**  
Obter dados meteorológicos da base **NASA/POWER** para localidades específicas.

**Conteúdos abordados:**
- Extração de dados climáticos  
- Organização em DataFrame  
- Variáveis meteorológicas aplicadas à agrometeorologia  

---

### 🔹 2. Caracterização climática e climogramas

#### `climogramas_br.ipynb`
**Objetivo:**  
Analisar o regime climático e construir **climogramas**.

**Conteúdos abordados:**
- Precipitação mensal  
- Temperatura média mensal  
- Construção e interpretação de climogramas  
- Aplicação na caracterização climática regional  

---

### 🔹 3. Informações de solo e clima

#### `infos_clima_solo.ipynb`
**Objetivo:**  
Integrar informações climáticas e propriedades do solo relevantes ao manejo agrícola.

**Conteúdos abordados:**
- Parâmetros físicos do solo  
- Relação solo–água–clima  
- Conceitos aplicados ao balanço hídrico  

---

### 🔹 4. Informações de cultura agrícola

#### `infos_cultura.ipynb`
**Objetivo:**  
Organizar parâmetros fenológicos e fisiológicos das culturas agrícolas.

**Conteúdos abordados:**
- Profundidade efetiva do sistema radicular  
- Coeficientes de cultura (Kc)  
- Duração das fases fenológicas  
- Aplicação em estudos agrometeorológicos  

---

### 🔹 5. Balanço hídrico da cultura

#### `bh_cultura.ipynb`
**Objetivo:**  
Calcular e analisar o **balanço hídrico agrícola** integrando clima, solo e cultura.

**Conteúdos abordados:**
- Evapotranspiração  
- Armazenamento de água no solo  
- Déficit e excedente hídrico  
- Interpretação para planejamento agrícola  

---

## 🧭 Ordem recomendada de execução

```text
1 → dados_nasapower.ipynb  
2 → climogramas_br.ipynb  
3 → infos_clima_solo.ipynb  
4 → infos_cultura.ipynb  
5 → bh_cultura.ipynb  

