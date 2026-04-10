import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from datetime import datetime
import io

# Configuração da página
st.set_page_config(page_title="Agrometeorologia - Santa Helena", layout="wide")

st.title("📊 Monitoramento Agrometeorológico")
st.markdown("Santa Helena - PR | Fonte: **SIMEPAR**")

# --- BARRA LATERAL (Filtros) ---
st.sidebar.header("Selecione o Período")
# Convertendo para datetime para compatibilidade
data_ini_default = datetime(2025, 1, 1)
data_fim_default = datetime(2025, 12, 31)

data_inicial = st.sidebar.date_input("Data Inicial", value=data_ini_default)
data_final = st.sidebar.date_input("Data Final", value=data_fim_default)

# --- FUNÇÃO DE CARREGAMENTO DE DADOS (Baseada no seu código) ---
@st.cache_data # Isso faz o site carregar muito mais rápido
def carregar_dados():
    # Fonte 1: GitHub
    url1 = "https://raw.githubusercontent.com/fcoliveira-utfpr/agrometeorologia/refs/heads/main/SIMEPAR_dados_diario.csv"
    df1 = pd.read_csv(url1)
    df1['Data'] = pd.to_datetime(df1['Data'], dayfirst=True)
    
    # Fonte 2: Google Sheets
    url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQABQ6C2vW_WgMOWICPPwoaUNp34JcThVJiFBgCPh2P7VvDW2PyqnkAEfdUxiesAwz5Hunuzeh5IykV/pub?gid=526963453&single=true&output=csv"
    df = pd.read_csv(url)
    df['Data'] = pd.to_datetime(df['Data'], dayfirst=True)
    
    # Unindo e limpando
    df_dia = pd.concat([df, df1])
    df_dia = df_dia.replace({',': '.'}, regex=True)
    
    # Colunas para numérico (exceto Data)
    cols = df_dia.columns.drop('Data')
    df_dia[cols] = df_dia[cols].apply(pd.to_numeric, errors='coerce')
    
    return df_dia.sort_values('Data')

# Execução do carregamento
df_total = carregar_dados()

# Filtro de data
mask = (df_total['Data'].dt.date >= data_inicial) & (df_total['Data'].dt.date <= data_final)
df_inter_dia = df_total.loc[mask]

if df_inter_dia.empty:
    st.warning("Nenhum dado encontrado para o intervalo selecionado.")
else:
    # --- DASHBOARD ---
    col1, col2, col3 = st.columns(3)
    col1.metric("Chuva Acumulada", f"{df_inter_dia['Chuva (mm)'].sum():.1f} mm")
    col2.metric("Temp. Média", f"{df_inter_dia['Tmed (°C)'].mean():.1f} °C")
    col3.metric("Radiação Total", f"{df_inter_dia['Radiação solar (MJ/m²d)'].sum():.1f} MJ/m²")

    # --- GRÁFICOS INTERATIVOS (PLOTLY) ---
    
    # 1. Temperatura
    fig_temp = go.Figure()
    fig_temp.add_trace(go.Scatter(x=df_inter_dia['Data'], y=df_inter_dia['Tmax (°C)'], name="T Máx", line=dict(color='red')))
    fig_temp.add_trace(go.Scatter(x=df_inter_dia['Data'], y=df_inter_dia['Tmed (°C)'], name="T Méd", line=dict(color='green')))
    fig_temp.add_trace(go.Scatter(x=df_inter_dia['Data'], y=df_inter_dia['Tmin (°C)'], name="T Mín", line=dict(color='blue')))
    fig_temp.update_layout(title="Temperaturas do Ar (°C)", hovermode="x unified")
    st.plotly_chart(fig_temp, use_container_width=True)

    # 2. Chuva (Combinado Barras e Acumulado)
    fig_chuva = make_subplots(specs=[[{"secondary_y": True}]])
    fig_chuva.add_trace(go.Bar(x=df_inter_dia['Data'], y=df_inter_dia['Chuva (mm)'], name="Chuva Diária", marker_color='blue'), secondary_y=False)
    fig_chuva.add_trace(go.Scatter(x=df_inter_dia['Data'], y=df_inter_dia['Chuva (mm)'].cumsum(), name="Acumulada", line=dict(color='red')), secondary_y=True)
    fig_chuva.update_layout(title="Precipitação e Chuva Acumulada")
    st.plotly_chart(fig_chuva, use_container_width=True)

    # 3. Umidade e Vento
    fig_uv = make_subplots(specs=[[{"secondary_y": True}]])
    fig_uv.add_trace(go.Scatter(x=df_inter_dia['Data'], y=df_inter_dia['UR (%)'], name="Umidade (%)", line=dict(color='blue')), secondary_y=False)
    fig_uv.add_trace(go.Scatter(x=df_inter_dia['Data'], y=df_inter_dia['Vel. Vento (m/s)'], name="Vento (m/s)", line=dict(color='red')), secondary_y=True)
    fig_uv.update_layout(title="Umidade Relativa e Velocidade do Vento")
    st.plotly_chart(fig_uv, use_container_width=True)

    # --- BOTÃO DE DOWNLOAD ---
    output = io.BytesIO()
    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
        df_inter_dia.to_excel(writer, index=False, sheet_name='Dados')
    
    st.sidebar.download_button(
        label="📥 Baixar dados em Excel",
        data=output.getvalue(),
        file_name=f"dados_SH_{data_inicial}_{data_final}.xlsx",
        mime="application/vnd.ms-excel"
    )

    st.info(f"Os gráficos representam o intervalo de {data_inicial} a {data_final} para Santa Helena - PR.")
