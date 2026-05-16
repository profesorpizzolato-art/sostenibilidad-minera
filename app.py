import streamlit as st
# Importamos la lógica externa de nuestra carpeta de módulos
from modulos.evaluacion_esg import calcular_nivel_esg
from modulos.ciclo_vida import calcular_ley_corte, calcular_balance_masa, calcular_fondo_cierre

st.set_page_config(page_title="Simulador Industrial MENFA", page_icon="🌍", layout="wide")

st.title("🌍 Evaluador y Simulador Minero Industrial")
st.caption("Ecosistema Modular de Capacitación — Autor: Fabricio Pizzolato | IPCL MENFA")

# Registro del alumno en la barra lateral
st.sidebar.header("📋 Registro del Operador")
dni = st.sidebar.text_input("DNI / Legajo del Alumno")

# Pestañas principales
tab1, tab2, tab3, tab4 = st.tabs([
    "📊 Matriz ESG (Video 1)", 
    "🔍 Geología y Factibilidad", 
    "⛏️ Planta y Operación", 
    "🍃 Cierre de Mina"
])

# ---- PESTAÑA 1: EVALUACIÓN ESG ----
with tab1:
    st.header("Autoevaluación de Proveedores ESG")
    with st.form("esg_form"):
        st.subheader("🌱 Pilar Ambiental")
        e1 = st.checkbox("¿Registra huella de carbono (Alcance 1 y 2)?")
        e2 = st.checkbox("¿Implementa ecoeficiencia hídrica en base?")
        e3 = st.checkbox("¿Posee plan certificado de residuos peligrosos?")
        # (Se pueden listar las variables sociales y de gobernanza de igual manera...)
        s1, s2, s3, g1, g2, g3 = True, True, False, False, True, False # Mock de ejemplo
        
        if st.form_submit_button("Calcular Diagnóstico ESG"):
            respuestas = [e1, e2, e3, s1, s2, s3, g1, g2, g3]
            # Llamada al módulo externo
            score, estado, msg, tipo = calcular_nivel_esg(respuestas)
            
            st.metric("Puntaje de Alineación", f"{score}%", help=f"Estado: {estado}")
            if tipo == "success": st.success(msg)
            elif tipo == "warning": st.warning(msg)
            else: st.error(msg)

# ---- PESTAÑA 2: GEOLOGÍA (CICLO DE VIDA 01-03) ----
with tab2:
    st.header("Fase de Exploración: Viabilidad de Ley de Corte")
    col1, col2 = st.columns(2)
    with col1:
        tonelaje = st.number_input("Toneladas cubicadas (Mt)", value=50.0)
        ley = st.slider("Ley de Cobre (%)", 0.1, 3.0, 0.65)
    with col2:
        precio = st.number_input("Precio Cu (USD/Tn)", value=8500)
        costo = st.number_input("Costo Operativo (USD/Tn)", value=35)
        
    # Usamos el motor de cálculo del ciclo de vida
    v_ton, margen, rentable = calcular_ley_corte(tonelaje, ley, precio, costo)
    st.metric("Valor Recuperable por Tonelada", f"USD {v_ton:.2f}", delta=f"Margen: USD {margen:.2f}")
    if rentable: st.success("Proyecto viable para avanzar a etapa de Factibilidad.")
    else: st.error("Proyecto paralizado por margen negativo.")

# ---- PESTAÑA 3: PLANTA (CICLO DE VIDA 04-06) ----
with tab3:
    st.header("Fase de Extracción y Procesamiento Metalúrgico")
    ingreso = st.slider("Alimentación de Planta (Tn/Hora)", 100, 2000, 500)
    eficiencia = st.slider("Eficiencia de Recuperación (%)", 50, 99, 85)
    
    util, esteril = calcular_balance_masa(ingreso, ley, eficiencia)
    st.info(f"⚙️ **Balance:** Se recuperan {util:.2f} Tn/h de metal puro. Se disponen {esteril:.2f} Tn/h de material estéril en diques de colas.")

# ---- PESTAÑA 4: CIERRE (CICLO DE VIDA 07) ----
with tab4:
    st.header("Fase de Cierre y Remediación Ambiental")
    remediacion = st.number_input("Presupuesto de Remediación (USD)", value=25000000)
    vida_util = st.slider("Vida útil (Años)", 5, 30, 15)
    
    reserva_anual = calcular_fondo_cierre(remediacion, vida_util)
    st.warning(f"⚖️ Fondo de Garantía Obligatorio: Se deben provisionar **USD {reserva_anual:,.2f} anuales**.")
