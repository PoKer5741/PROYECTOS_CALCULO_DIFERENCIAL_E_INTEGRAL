# -*- coding: utf-8 -*-
"""
Proyecto 10: Ruido de embarcaciones y ballenas jorobadas en el Golfo Dulce
Cálculo Diferencial e Integral (MA-0321)
Estudiante: Isaac Alexander Vega Orozco (C-08)
"""

import os
import sys
from pathlib import Path
import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

# Configuración de página
st.set_page_config(
    page_title="Proyecto 10 - Ruido y Ballenas en Golfo Dulce",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Estilo sobrio y limpio con texto en blanco de alto contraste
st.markdown("""
<style>
    body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; }
    .titulo-principal { font-size: 28px; font-weight: 800; color: #ffffff !important; margin-bottom: 6px; }
    .subtitulo { font-size: 16px; color: #e2e8f0 !important; margin-bottom: 22px; font-weight: 500; }
    .caja-resumen { background-color: #1e293b; border: 1px solid #475569; border-radius: 8px; padding: 18px; margin-bottom: 20px; color: #ffffff !important; }
    .ganadora { background-color: #064e3b; border: 2px solid #10b981; border-radius: 8px; padding: 20px; margin-bottom: 22px; color: #ffffff !important; }
</style>
""", unsafe_allow_html=True)

# Encabezado en blanco
st.markdown('<div class="titulo-principal">Proyecto 10: Ruido de Embarcaciones y Ballenas en el Golfo Dulce</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitulo">Estudiante: Isaac Alexander Vega Orozco (C-08) | Curso: Cálculo Diferencial e Integral</div>', unsafe_allow_html=True)

# Resumen directo en 3 puntos
st.markdown("""
<div class="ganadora">
    <h3 style="margin-top:0; color:#34d399; font-size:20px;">Resumen del Proyecto en 3 puntos:</h3>
    <ol style="margin-bottom:0; font-size:15.5px; line-height:1.65; color:#ffffff;">
        <li><b style="color:#ffffff;">El problema:</b> En el Golfo Dulce pasan 1,100 embarcaciones por la zona donde las ballenas cuidan a sus crías. El ruido de los motores tapa sus llamados acústicos. El refugio pide <b>reducir el ruido al menos un 50%</b> con el menor costo posible.</li>
        <li><b style="color:#ffffff;">La solución (Opción A):</b> Poner un <b>límite de velocidad de 10 nudos</b> en los 6 km de la zona sensible. Reduce el ruido un <b>71.4%</b> (supera de sobra la meta) y cuesta <b>₡5.85 millones</b> (es la más barata de todas). Solo agrega 8 minutos por viaje.</li>
        <li><b style="color:#ffffff;">¿Y si piden el 60%?:</b> Como la Opción A ya reduce el <b>71.4%</b>, sigue cumpliendo sin tener que gastar ni un solo colón adicional.</li>
    </ol>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# =============================================================================
# SECCIÓN 1: COMPARACIÓN DE LAS 4 OPCIONES
# =============================================================================
st.subheader("1. Comparación de las 4 Opciones de Manejo")
st.write("El refugio planteó 4 propuestas oficiales. Aquí podés ver claramente cuánto ruido quita cada una y cuánto cuesta en total:")

datos_opciones = [
    {
        "Opción": "Opción A (Elegida)",
        "Regla que se aplica": "Límite de 10 nudos",
        "Ruido que elimina": "71.4% (-5.4 dB)",
        "Tiempo extra de toda la flota": "145.5 horas (~8 min por viaje)",
        "Costo total en colones": "₡5,847,362",
        "¿Cumple la meta?": "SÍ CUMPLE (La más barata)"
    },
    {
        "Opción": "Opción B",
        "Regla que se aplica": "Límite de 6 nudos",
        "Ruido que elimina": "88.4% (-9.4 dB)",
        "Tiempo extra de toda la flota": "360.8 horas (~20 min por viaje)",
        "Costo total en colones": "₡10,599,122",
        "¿Cumple la meta?": "Sí, pero cuesta casi el doble"
    },
    {
        "Opción": "Opción C (Descartada)",
        "Regla que se aplica": "Distancia mínima de 300 metros",
        "Ruido que elimina": "35.9% (-1.9 dB)",
        "Tiempo extra de toda la flota": "0.0 horas (0 min por viaje)",
        "Costo total en colones": "₡6,800,000",
        "¿Cumple la meta?": "NO CUMPLE (No llega al 50%)"
    },
    {
        "Opción": "Opción D",
        "Regla que se aplica": "10 nudos + 300 metros",
        "Ruido que elimina": "81.7% (-7.4 dB)",
        "Tiempo extra de toda la flota": "145.5 horas (~8 min por viaje)",
        "Costo total en colones": "₡11,247,362",
        "¿Cumple la meta?": "Sí, pero es la más cara de todas"
    }
]

df_tabla = pd.DataFrame(datos_opciones)
st.dataframe(df_tabla, hide_index=True, width="stretch")

col_g1, col_g2 = st.columns(2)

opcs = ["Opción A\n(10 nudos)", "Opción B\n(6 nudos)", "Opción C\n(300 metros)", "Opción D\n(10 kts + 300m)"]
reds = [71.43, 88.42, 35.89, 81.68]
costos = [5.85, 10.60, 6.80, 11.25]
colores_red = ['#10b981', '#f59e0b', '#ef4444', '#64748b']

with col_g1:
    fig1 = go.Figure()
    fig1.add_trace(go.Bar(
        x=opcs,
        y=reds,
        marker_color=colores_red,
        text=[f"{r:.1f}%" for r in reds],
        textposition='outside'
    ))
    fig1.add_hline(y=50, line_dash="dash", line_color="#ef4444", annotation_text="Meta mínima (50%)")
    fig1.add_hline(y=60, line_dash="dot", line_color="#8b5cf6", annotation_text="Meta más estricta (60%)")
    fig1.update_layout(
        title="<b>Ruido eliminado por cada opción</b>",
        yaxis_title="Porcentaje de reducción (%)",
        yaxis=dict(range=[0, 108]),
        template="plotly_white",
        height=360
    )
    st.plotly_chart(fig1, width="stretch")

with col_g2:
    fig2 = go.Figure()
    fig2.add_trace(go.Bar(
        x=opcs,
        y=costos,
        marker_color='#38bdf8',
        text=[f"₡{c:.2f}M" for c in costos],
        textposition='outside'
    ))
    fig2.update_layout(
        title="<b>Costo total de cada opción (en millones de colones)</b>",
        yaxis_title="Millones de colones (₡)",
        yaxis=dict(range=[0, 14]),
        template="plotly_white",
        height=360
    )
    st.plotly_chart(fig2, width="stretch")

st.markdown("---")

# =============================================================================
# SECCIÓN 2: LA INTEGRAL EXPLICADA EN SIMPLE
# =============================================================================
st.subheader("2. ¿Qué significa la Integral en este proyecto?")
st.write(
    "Cuando un bote pasa cerca de una ballena, el sonido sube al acercarse, llega a un máximo cuando pasa justo al frente (t = 0), "
    "y luego vuelve a bajar al alejarse. **La integral es simplemente sumar todo ese sonido segundo a segundo (el área bajo la curva)**."
)

col_curva1, col_curva2 = st.columns([1, 2])
with col_curva1:
    st.write("**Mirá la diferencia entre ir rápido y bajar a 10 nudos:**")
    st.write("- **Línea roja (sin regla):** Una lancha a 23 nudos mete un pico de ruido altísimo.")
    st.write("- **Línea verde (Opción A):** Al bajar a 10 nudos, el ruido del motor cae en picada y la curva casi se aplana contra el suelo.")
    st.write("Por eso, en un solo viaje, **el ruido baja un 79%**.")
    st.caption("Fórmula teórica de la presión: p²(t) = S / (d² + v²·t²). Área total = (π · S) / (d · v).")

with col_curva2:
    # Simulación de la curva teórica con los parámetros calibrados del hidrófono
    t_vals = np.linspace(-120, 120, 300)
    S0_ref = 10150.04
    n_exp = 2.8641
    d_ej = 200.0

    v_rapida_ms = 22.8 * (1852.0 / 3600.0)
    v_lenta_ms = 10.0 * (1852.0 / 3600.0)

    S_rapida = S0_ref * ((22.8 / 10.0) ** n_exp)
    S_lenta = S0_ref * ((10.0 / 10.0) ** n_exp)

    p2_rapida = S_rapida / (d_ej**2 + (v_rapida_ms * t_vals)**2)
    p2_lenta = S_lenta / (d_ej**2 + (v_lenta_ms * t_vals)**2)

    fig3 = go.Figure()
    fig3.add_trace(go.Scatter(
        x=t_vals,
        y=p2_rapida,
        mode='lines',
        line=dict(color='#ef4444', width=2.8),
        name="Lancha rápida (23 nudos)"
    ))
    fig3.add_trace(go.Scatter(
        x=t_vals,
        y=p2_lenta,
        mode='lines',
        line=dict(color='#10b981', width=2.8),
        name="Con límite de 10 nudos (Opción A)"
    ))
    fig3.update_layout(
        title="<b>Curva de sonido: Rápido vs. 10 nudos</b>",
        xaxis_title="Segundos antes y después de pasar",
        yaxis_title="Sonido recibido (Pa²)",
        template="plotly_white",
        height=320,
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="left", x=0)
    )
    st.plotly_chart(fig3, width="stretch")

st.markdown("---")

# =============================================================================
# SECCIÓN 3: QUIÉN GENERA EL RUIDO
# =============================================================================
st.subheader("3. ¿Quién genera el ruido en el Golfo Dulce?")
st.write("De los 1,100 viajes registrados en la temporada, casi todo el ruido viene de las lanchas y las pangas por ir rápido:")

datos_flota = [
    {"Tipo de embarcación": "Lancha turística", "Viajes en la temporada": 471, "Velocidad típica": "22.8 nudos", "Porcentaje del ruido total": "62.1%", "Nivel (dB)": "168.0 dB"},
    {"Tipo de embarcación": "Panga de pesca", "Viajes en la temporada": 324, "Velocidad típica": "17.0 nudos", "Porcentaje del ruido total": "25.8%", "Nivel (dB)": "164.2 dB"},
    {"Tipo de embarcación": "Yate", "Viajes en la temporada": 196, "Velocidad típica": "15.0 nudos", "Porcentaje del ruido total": "11.1%", "Nivel (dB)": "160.5 dB"},
    {"Tipo de embarcación": "Velero", "Viajes en la temporada": 109, "Velocidad típica": "5.5 nudos", "Porcentaje del ruido total": "1.0%", "Nivel (dB)": "149.9 dB"},
]

df_flota = pd.DataFrame(datos_flota)
st.dataframe(df_flota, hide_index=True, width="stretch")

st.caption("Nota: Los veleros viajan a 5.5 nudos y solo producen el 1% del ruido, por lo que la regla de 10 nudos no los afecta en nada.")
