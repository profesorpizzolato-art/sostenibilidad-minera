import streamlit as st
# Importamos la lógica externa de nuestra carpeta de módulos
from modulos.evaluacion_esg import calcular_nivel_esg
from modulos.ciclo_vida import calcular_ley_corte, calcular_balance_masa, calcular_fondo_cierre
from modulos.mercado_recursos import obtener_datos_minerales, calcular_ingresos_mercado
from modulos.actores_legal import obtener_perfiles_actores, simular_riesgo_exploracion, validar_matriz_legal_mendoza


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
    "⚖️ Actores y Marco Legal"
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
# ==========================================
# ---- PESTAÑA 6: ACTORES Y MARCO LEGAL ----
# ==========================================
with tab6:
    st.header("Gobernanza del Ecosistema Minero y Marco Regulatorio")
    st.write("La minería moderna es una asociación estratégica entre capital, conocimiento técnico y estricta legalidad institucional.")
    
    col_act, col_leg = st.columns(2)
    
    with col_act:
        st.markdown("### 👥 1. Interacción de Actores y Capital")
        actores = obtener_perfiles_actores()
        actor_sel = st.selectbox("Seleccione un actor del ecosistema para ver su perfil técnico-financiero:", list(actores.keys()))
        
        info = actores[actor_sel]
        st.info(f"**Rol Central:** {info['rol']}\n\n**Estructura de Financiamiento:** {info['financiamiento']}\n\n**Ventaja Competitiva:** {info['fortaleza']}\n\n**Riesgo / Desafío:** {info['desafio']}")
        
        st.markdown("---")
        st.markdown("#### 🎲 Simulación de Riesgo Minero: El filtro de 1 en 1.000.000")
        intentos = st.number_input("Cantidad de indicios / anomalías geológicas a investigar en campaña:", value=150000, step=10000)
        
        # Simulación analítica del descarte geológico
        import numpy as np # Aseguramos la librería para el cálculo rápido
        prob_acum, exito = simular_riesgo_exploracion(intentos)
        
        st.metric("Probabilidad Estadística de Hallar una Mina", f"{prob_acum:.4f}%")
        st.caption("Recuerde: Solo 1 de cada millón de indicios explorados se consolida como un proyecto viable comercialmente.")

    with col_leg:
        st.markdown("### ⚖️ 2. Auditoría del Marco Legal (Mendoza)")
        st.write("Para liberar fondos de inversión, el operador debe demostrar conocimiento estricto del procedimiento para obtener la Declaración de Impacto Ambiental (DIA) obligatoria:")
        
        # Formulario de examen técnico para el alumno
        l_nac = st.selectbox("Código de Minería de la Nación:", ["Seleccionar...", "Ley Nacional N° 24196", "Código de Minería de la Nación (Ley N° 1919)", "Ley Nacional N° 25675"])
        l_proc = st.selectbox("Código de Procedimiento Minero de Mendoza:", ["Seleccionar...", "Ley Provincial N° 7722", "Ley Provincial N° 9529", "Ley Provincial N° 8461"])
        l_amb = st.selectbox("Ley de Preservación del Medio Ambiente (Mendoza):", ["Seleccionar...", "Ley Provincial N° 5961", "Ley Provincial N° 6045", "Ley Provincial N° 7490"])
        d_reg = st.selectbox("Decreto Reglamentario de Evaluación Ambiental Minera:", ["Seleccionar...", "Decreto N° 2100/2005", "Decreto N° 820/2006", "Decreto N° 437/1993"])
        
        if st.button("⚖️ Validar Cumplimiento Normativo de la DIA"):
            aprobado, checklist = validar_matriz_legal_mendoza(l_nac, l_proc, l_amb, d_reg)
            
            if aprobado:
                st.success("🟢 **Cumplimiento Legal Exitoso:** La matriz normativa ingresada es correcta. El trámite está habilitado para avanzar ante la autoridad ambiental de aplicación de Mendoza.")
            else:
                st.error("🔴 **Infracción de Procedimiento:** Hay errores o vacíos en la jerarquía legal seleccionada. No se puede iniciar la evaluación del Informe de Impacto Ambiental.")
                # Muestra detallada de qué falló
                for clave, valor in checklist.items():
                    if not valor: st.write(f"❌ Revisar parámetro o número de norma para: *{clave.upper()}*")
