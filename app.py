import streamlit as st
import pandas as pd

# Configuración de página
st.set_page_config(
    page_title="Simulador ESG - IPCL MENFA",
    page_icon="🌍",
    layout="wide"
)

# Estilos personalizados
st.markdown("""
    <style>
    .main-title { font-size:28px; font-weight:bold; color:#002D62; margin-bottom:5px; }
    .subtitle { font-size:16px; color:#4682B4; font-style:italic; margin-bottom:20px; }
    .section-box { padding: 15px; background-color: #F4F6F9; border-radius: 8px; margin-bottom: 15px; }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">🌍 Evaluador de Sostenibilidad Industrial (ESG)</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Módulo de Autoevaluación para Proveedores - IPCL MENFA (Mendoza)</div>', unsafe_allow_html=True)

st.write("Esta herramienta interactiva permite a las empresas y contratistas del sector minero e industrial evaluar su nivel de alineación con las exigencias ESG globales analizadas en la capacitación.")

# Pestañas de la aplicación
tab1, tab2, tab3 = st.tabs(["📊 Autoevaluación Operativa", "📚 Compendio Teórico", "📋 Guía de Respuestas"])

with tab1:
    st.header("Matriz de Ponderación ESG")
    st.write("Responda con honestidad el estado de su organización respecto a cada indicador:")

    with st.form("esg_form"):
        st.subheader("🌱 Pilar Ambiental (E)")
        e1 = st.checkbox("¿La empresa cuenta con un registro/inventario de su huella de carbono o emisiones de GEI (Scope 1 y 2)?")
        e2 = st.checkbox("¿Se implementan medidas de ecoeficiencia hídrica y reciclaje de efluentes en talleres o base operativa?")
        e3 = st.checkbox("¿Existe un plan formal de gestión, clasificación y disposición certificada de residuos peligrosos (aceites, chatarra)?")

        st.subheader("🤝 Pilar Social (S)")
        s1 = st.checkbox("¿Se cuenta con matrices IPERC vigentes y certificación o alineación con la norma ISO 45001 (Salud y Seguridad)?")
        s2 = st.checkbox("¿La empresa prioriza la contratación de mano de obra local y el desarrollo de subproveedores de la comunidad?")
        s3 = st.checkbox("¿Se registran de forma sistemática las horas de capacitación dictadas al personal técnico en campo?")

        st.subheader("⚖️ Pilar de Gobernanza y Ética (G)")
        g1 = st.checkbox("¿La empresa cuenta con un Código de Conducta escrito y políticas explícitas de Compliance / Anticorrupción?")
        g2 = st.checkbox("¿Los estados financieros, registros fiscales y laborales están abiertos a auditorías externas de tercera parte?")
        g3 = st.checkbox("¿Se evalúa el cumplimiento socioambiental y legal de su propia cadena de subproveedores (Abastecimiento Responsable)?")

        submitted = st.form_submit_form_button("📊 Calcular Nivel de Cumplimiento")

    if submitted:
        # Cálculo de puntaje
        total_checks = sum([e1, e2, e3, s1, s2, s3, g1, g2, g3])
        score = int((total_checks / 9) * 100)
        
        st.metric(label="Puntaje de Alineación ESG", value=f"{score}%")
        
        if score == 100:
            st.success("🏆 **Nivel Avanzado / Certificable:** Su empresa cumple con la totalidad de los estándares exigidos por las operadoras internacionales de primer nivel (Apto para licitaciones con financiamiento IFC).")
        elif score >= 70:
            st.warning("⚡ **Nivel Intermedio / En Desarrollo:** Buen nivel de cumplimiento en campo. Falta formalizar o documentar algunos procesos para calificar como proveedor estratégico prioritario.")
        else:
            st.error("🚨 **Nivel Inicial / Crítico:** Se requiere una reingeniería urgente de sus procesos. Su estado actual representa un riesgo de descalificación en las matrices técnicas de compras mineras.")

with tab2:
    st.header("Compendio de Estudio Modular")
    st.markdown("""
    <div class="section-box">
        <h4>Módulo 1: Fundamentos y Evolución</h4>
        <p>La minería moderna ha migrado del paradigma tradicional (enfoque puramente reactivo y extractivo) hacia el modelo del <b>Triple Bottom Line</b>, donde la licencia social para operar y las exigencias de financiamiento internacional (Principios del Ecuador) determinan la viabilidad del proyecto.</p>
    </div>
    <div class="section-box">
        <h4>Módulo 2: Cadena de Valor y Expectativas</h4>
        <p>Las grandes operadoras evalúan de manera mandatoria a su cadena de suministro. La transparencia, el cumplimiento de convenios de la OIT y la gestión demostrable de emisiones indirectas (Alcance 3) ya no son opcionales.</p>
    </div>
    <div class="section-box">
        <h4>Módulo 3: Herramientas para la Acción</h4>
        <p>El uso de tecnologías de la Industria 4.0 como <b>Blockchain</b> para el pasaporte digital de minerales, <b>Inteligencia Artificial</b> para la predicción de fallas operacionales y el análisis de <b>Big Data</b> permiten combinar sustentabilidad con eficiencia de costos.</p>
    </div>
    """, unsafe_allow_html=True)

with tab3:
    st.header("Cuestionario de Autoevaluación y Guía Didáctica")
    st.write("A continuación se presentan las preguntas clave extraídas del manual con sus ejes de respuesta esperados para el debate técnico:")
    
    st.markdown("""
    1. **¿Qué hitos históricos marcaron el camino hacia la sostenibilidad y qué ideas principales aportaron?**
       * *Eje de respuesta:* Estocolmo 1972 (concienciación global), Informe Brundtland 1987 (definición formal de desarrollo sostenible) y Río 1992 (Agenda 21 y convenios marco).
    
    2. **¿Cuáles son las diferencias clave entre la minería tradicional y la minería moderna?**
       * *Eje de respuesta:* La minería tradicional es puramente económica, lineal y reactiva. La minería moderna equilibra el vector social y ambiental de manera preventiva, implementando esquemas de debida diligencia y economía circular.
    
    3. **¿Por qué la sostenibilidad es crítica para la supervivencia de las empresas mineras hoy?**
       * *Eje de respuesta:* Por la interdependencia con la Licencia Social comunitaria, los condicionamientos de los bancos internacionales para liberar capital y la necesidad de eficiencia ante la baja en las leyes de mineral.
    """, unsafe_allow_html=True)
