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

#### `01_dados_nasapower.ipynb`

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/fcoliveira-utfpr/agrometeorologia/blob/main/01_dados_nasapower.ipynb)

**Objetivo:**  
Obter dados meteorológicos da base [**NASA/POWER**](https://power.larc.nasa.gov/) por Município.

**Conteúdos abordados:**
- Baixa dados meteorológicos do NASA/POWER em escala diária, mensal e de uma Normal Climatológica

---

### 🔹 2. Caracterização climática e climogramas

#### `02_climogramas_br.ipynb`

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/fcoliveira-utfpr/agrometeorologia/blob/main/02_climogramas_br.ipynb)

**Objetivo:**  
Analisar o regime climático e construir **climogramas**.

**Conteúdos abordados:**
- Constroi gráfico climograma (temperatura média mensal e precipitação acumulada mensal
- Gera tabela com Tmed e chuva mensal - dados do [Alvaes et al. (2013)](https://www.schweizerbart.de/papers/metz/detail/22/82078/Koppen_s_climate_classification_map_for_Brazil?af=crossref) 

---

### 🔹 3. Informações de solo e clima

#### `03_infos_clima_solo.ipynb`

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/fcoliveira-utfpr/agrometeorologia/blob/main/03_infos_clima_solo.ipynb)

**Objetivo:**  
Integrar informações climáticas e propriedades do solo relevantes ao manejo agrícola.

**Conteúdos abordados:**
- Gera Tabela de informações do município: **Altitude (m)**,	**DTA (mm/m)**,	**clima KöppenGeiger**,	**latitude e longitude** do centroide do município
- Permite visualizar por Estado no mapa: município, latitude, longitude
- Permite visualizar por Estado no mapa: município, DTA [Atlas Irrigação, 2021](https://metadados.snirh.gov.br/geonetwork/srv/api/records/1b19cbb4-10fa-4be4-96db-b3dcd8975db0)
- Permite visualizar por Estado no mapa: município, clima Koppen-Geiger
- Município e estado pela latitude e longitude

---

### 🔹 4. Informações de cultura agrícola

#### `04_infos_cultura.ipynb`

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/fcoliveira-utfpr/agrometeorologia/blob/main/04_infos_cultura.ipynb)

**Objetivo:**  
Organizar parâmetros fenológicos e fisiológicos das culturas agrícolas.

**Conteúdos abordados:**
- *São obtidos os seguintes dados das culturas* [Allen et al. (1998)](https://www.fao.org/4/x0490e/x0490e00.htm):
- **F1 (%)** – Fase inicial do ciclo da cultura  
- **F2 (%)** – Fase de desenvolvimento da cultura  
- **F3 (%)** – Fase média (máximo desenvolvimento) da cultura  
- **F4 (%)** – Fase final (maturação/senescência) da cultura  

- **f** – Fator de depleção da água disponível no solo  

- **Kc ini** – Coeficiente de cultura na fase inicial  
- **Kc méd** – Coeficiente de cultura na fase média  
- **Kc fin** – Coeficiente de cultura na fase final  

- **Z efetivo (m)** – Profundidade efetiva do sistema radicular  

- **Ky₁** – Fator de resposta da cultura ao déficit hídrico na fase 1  
- **Ky₂** – Fator de resposta da cultura ao déficit hídrico na fase 2  
- **Ky₃** – Fator de resposta da cultura ao déficit hídrico na fase 3  
- **Ky₄** – Fator de resposta da cultura ao déficit hídrico na fase 4  

- **Ky total** – Fator de resposta global da cultura ao déficit hídrico  


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

