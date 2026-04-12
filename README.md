# 🌱 Agrometeorologia Aplicada com Python

Este repositório reúne notebooks didáticos utilizados na área de **Agrometeorologia**, com foco na análise de dados climáticos, caracterização clima–solo–cultura e aplicação em balanço hídrico agrícola, utilizando **Python no Google Colab** [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/fcoliveira-utfpr/agrometeorologia/blob/main/exemplo_notebook.ipynb)

Os notebooks foram desenvolvidos com abordagem prática, utilizando dados reais e exemplos aplicados à agricultura brasileira.

---
[![DOI](https://zenodo.org/badge/1137750656.svg)](https://doi.org/10.5281/zenodo.19342886)

Como citar?
---
<p style="font-size: 12px;">
OLIVEIRA, Fabricio Correia de. Agrometeorologia: v. 1.0. Zenodo, 2026. DOI: 10.5281/zenodo.1934288. Disponível em: https://doi.org/10.5281/zenodo.1934288. Acesso em: 30 mar. 2026.
</p>


## 🎯 Objetivos da disciplina

Ao final do Curso, discentes são capazes de avaliar o efeito de elementos climáticos e meteorológicos sobre o planejamento de uso da terra e das operações agrícolas e pecuárias, relacionando informações de tempo e clima com os sistemas de produção agropecuária, com decisões sustentáveis e inovadoras. 

---

## 🚀 Como utilizar os notebooks

1. Abra o notebook desejado diretamente no GitHub  
2. Clique em **“Open in Colab”**
3. Faça uma cópia para seu Drive ou Execute as células **na ordem**  
5. Leia atentamente os textos explicativos (Markdown) e comentários no código
6. Para baixar arquivos retire o # e execute o bloco de código
7. Os arquivos com final .csv são dados brutos, não precisar ser abertos

---

## 📚 Organização dos notebooks

### 🔹 1. Dados climáticos

#### `01_dados_nasapower.ipynb`

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/fcoliveira-utfpr/agrometeorologia/blob/main/01_dados_nasapower.ipynb)

**Objetivo:**  
Obter dados meteorológicos da base [**NASA/POWER**](https://power.larc.nasa.gov/) por município.

**Conteúdos abordados:**
- Permite visualizar todos os ESTADOS e MUNICÍPIOS
- Baixa dados meteorológicos do NASA/POWER em escala diária, mensal e de uma Normal Climatológica

---

### 🔹 2. Caracterização climática e climogramas

#### `02_climogramas_br.ipynb`

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/fcoliveira-utfpr/agrometeorologia/blob/main/02_climogramas_br.ipynb)

**Objetivo:**  
Analisar o regime climático e construir **climogramas**.

**Conteúdos abordados:**
- Permite visualizar todos os ESTADOS e MUNICÍPIOS
- Gera tabela com Tmed - dados do [Alvares et al. (2013)](https://www.schweizerbart.de/papers/metz/detail/22/82078/Koppen_s_climate_classification_map_for_Brazil?af=crossref) e chuva mensal - dados do TerraClimate
- Constrói gráfico climograma (temperatura média mensal e precipitação acumulada mensal) - Análises temporal
- Constrói mapa da chuva por estado - Análises espacial de dados anuais
- Constrói mapa da temperatura por estado - Análises espacial de dados anuais
- Constrói mapa de Classificação Climática de Köppen-Geiger

---

### 🔹 3. Informações de solo e clima

#### `03_infos_clima_solo.ipynb`

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/fcoliveira-utfpr/agrometeorologia/blob/main/03_infos_clima_solo.ipynb)

**Objetivo:**  
Integrar informações climáticas e propriedades do solo relevantes ao manejo agrícola.

**Conteúdos abordados:**
- Permite visualizar todos os ESTADOS e MUNICÍPIOS
- Gera Tabela de informações do município: **Altitude (m)**,	**DTA (mm/m)**,	**clima KöppenGeiger**,	**latitude e longitude** do centroide do município
- Permite visualizar por Estado no mapa: município, latitude, longitude
- Permite visualizar por Estado no mapa: município, DTA [Atlas Irrigação, 2021](https://metadados.snirh.gov.br/geonetwork/srv/api/records/1b19cbb4-10fa-4be4-96db-b3dcd8975db0)
- Permite visualizar por Estado no mapa: município, clima Köppen-Geiger
- Município e estado pela latitude e longitude
- Informações do solo pela lat e lon

---

### 🔹 4. Informações de cultura agrícola

#### `04_infos_cultura.ipynb`

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/fcoliveira-utfpr/agrometeorologia/blob/main/04_infos_cultura.ipynb)

**Objetivo:**  
Organizar parâmetros fenológicos e fisiológicos das culturas agrícolas.

**Conteúdos abordados:**
- Permite visualizar todas as CULTURAS do banco de dados
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

### 🔹 5. Balanço climatológico

#### `05_bh_climatologico.ipynb`

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/fcoliveira-utfpr/agrometeorologia/blob/main/05_bh_climatologico.ipynb)

**Objetivo:**  
Calcular e analisar o **balanço hídrico climatológico** integrando clima e solo.

**Conteúdos abordados:**
- Permite visualizar todos os ESTADOS e MUNICÍPIOS
- Baixa dados da Normal Climatológica do TerraClimate (1991-2020)
- Calcula o balanço hídrico climatológico de Thothwaite-Mather em escala mensal
- Constrói gráfico do Extrato do Balanço Hídrico
- Constrói gráfico de água no solo
- Constrói gráfico de retiradas e reposições de água
- Constrói gráfico do balanço hídrico
 
---
### 🔹 6. Balanço hídrico da cultura

#### `06_bh_cultura.ipynb`

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/fcoliveira-utfpr/agrometeorologia/blob/main/06_bh_cultura.ipynb)

**Objetivo:**  
Calcular e analisar o **balanço hídrico agrícola** integrando clima, solo e cultura.

**Conteúdos abordados:**
- Permite visualizar todos os ESTADOS e MUNICÍPIOS
- Para cada município, cultura, ano e data de semeadura, calcula o balanço hídrico de cultura
- calcula o ISNA diário para o ciclo da cultura
- calcula o ISNA para cada fase da cultura 

---
### 🔹 7. NoteBook para gráficos gerais

#### `07_graficos_gerais.ipynb`

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/fcoliveira-utfpr/agrometeorologia/blob/main/06_bh_cultura.ipynb)

**Objetivo:**  
Construção de gráficos gerais, barra, linhas, heatmap, boxplot.

**Conteúdos abordados:**
- Construir gráficos
---
---
### 🔹 EXTRA 1. baixar dados de SANTA HELENA - PR

#### `GAMBITEC_DADOS_SH.ipynb`

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/fcoliveira-utfpr/agrometeorologia/blob/main/GAMBITEC_DADOS_SH.ipynb)

**Objetivo:**  
Baixar dados meteorológicos para Santa Helena - PR.

**Conteúdos abordados:**
- Baixa dados do SIMEPAR para Santa Helena - PR


**👨‍🏫 Autor**

Prof. Fabrício Correia de Oliveira 

Universidade Tecnológica Federal do Paraná (UTFPR)

[Currículo Lattes](http://lattes.cnpq.br/9528194038713972)
