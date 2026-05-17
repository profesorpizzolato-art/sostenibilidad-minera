import streamlit as st
# Importamos la lógica externa de nuestra carpeta de módulos
from modulos.evaluacion_esg import calcular_nivel_esg
from modulos.ciclo_vida import calcular_ley_corte, calcular_balance_masa, calcular_fondo_cierre
from modulos.mercado_recursos import obtener_datos_minerales, calcular_ingresos_mercado


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
    "📈 Mercados y Commodities"
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
# ==========================================
# ---- PESTAÑA 5: MERCADOS Y COMMODITIES ----
# ==========================================
with tab5:
    st.header("Análisis de Mercados Mundiales y Comercialización")
    st.write("El precio de los recursos mineros está atado a dinámicas geopolíticas y macroeconómicas externas. Simule su impacto:")

    # Traemos las clasificaciones del módulo backend
    lista_minerales = obtener_datos_minerales()
    
    col_ui1, col_ui2 = st.columns(2)
    with col_ui1:
        mineral_sel = st.selectbox("Seleccione el Grupo Estratégico de Recurso:", list(lista_minerales.keys()))
        volumen = st.number_input("Volumen de producción anual estimado (en unidades comerciales):", value=12000, step=500)
    
    with col_ui2:
        st.markdown("**Simulación de Eventos Macroeconómicos (Gobernanza de Mercado):**")
        evento = st.radio("Seleccione un escenario geopolítico global:", [
            "Estabilidad de Mercado (Sin cambios)",
            "Aceleración Industrial de China (+15% en demanda)",
            "Tensión Geopolítica / Conflictos Internacionales (-10% en logística)",
            "Disrupción por Recesión Global o Cambio Tecnológico (-25% en commodities)"
        ])
        
        # Mapeo del evento macro a porcentaje de fluctuación real de precios
        dict_eventos = {
            "Estabilidad de Mercado (Sin cambios)": 0.0,
            "Aceleración Industrial de China (+15% en demanda)": 15.0,
            "Tensión Geopolítica / Conflictos Internacionales (-10% en logística)": -10.0,
            "Disrupción por Recesión Global o Cambio Tecnológico (-25% en commodities)": -25.0
        }
        fluctuacion = dict_eventos[evento]

    # Invocamos la lógica matemática del backend
    pr_ajustado, ingreso_total, tipo_mercado, mecanismo_venta = calcular_ingresos_mercado(mineral_sel, volumen, fluctuacion)
    
    # Despliegue de Resultados e Inteligencia de Negocio
    st.markdown("---")
    st.markdown(f"### 📊 Informe Ejecutivo de Comercialización: {mineral_sel}")
    st.caption(f"**Clasificación del Activo:** {tipo_mercado} | **Modelo de Contrato:** {mecanismo_venta}")
    
    col_m1, col_m2 = st.columns(2)
    with col_m1:
        st.metric(
            label="Precio de Venta Ajustado", 
            value=f"USD {pr_ajustado:,.2f}", 
            delta=f"{fluctuacion}% por condiciones externas" if fluctuacion != 0 else "Estable"
        )
    with col_m2:
        st.metric(label="Facturación Bruta Proyectada Anual", value=f"USD {ingreso_total:,.2f}")
        
    # Mensaje educativo contextual para el alumno
    if fluctuacion < 0:
        st.error("🚨 **Riesgo de Viabilidad:** Las caídas en el mercado internacional impactan directo en el VAN/TIR local. Las operaciones deben optimizar su OPEX para resistir el ciclo bajo.")
    elif fluctuacion > 0:
        st.success("🚀 **Ciclo de Alta (Boom):** Ventana de oportunidad para acelerar inversiones, optimizar exploración y consolidar contratos de provisión de largo plazo.")
