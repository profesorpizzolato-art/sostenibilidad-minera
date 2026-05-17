import streamlit as st
import sys

# Aseguramos la importación correcta de módulos locales
from modulos.evaluacion_esg import calcular_nivel_esg
from modulos.ciclo_vida import calcular_ley_corte, calcular_balance_masa, calcular_fondo_cierre
from modulos.mercados import obtener_datos_minerales, calcular_ingresos_mercado
from modulos.actores_legal import obtener_perfiles_actores, simular_probabilidad_exploracion, verificar_marco_dia_mendoza

# Configuración del contenedor web
st.set_page_config(page_title="Simulador Industrial MENFA", page_icon="🏗️", layout="wide")

st.title("🏗️ Ecosistema de Simulación Minera Industrial — MENFA v6")
st.caption("Plataforma Modular de Capacitación | Autor y Desarrollador: Fabricio Pizzolato — Mendoza, Argentina")

# Sidebar - Persistencia de datos del operador
st.sidebar.header("📋 Registro del Operador")
dni = st.sidebar.text_input("DNI / Legajo del Alumno")
if dni:
    st.sidebar.success(f"Sesión Activa: {dni}")

# Definición de la botonera de navegación (Pestañas de Videos 01 a 05)
tabs = st.tabs([
    "📊 Matriz ESG (V1)", 
    "🔍 Geología y Factibilidad (V2-3)", 
    "⛏️ Planta y Operación (V2-3)", 
    "🍃 Cierre de Mina (V2-3)",
    "📈 Mercados y Commodities (V4)",
    "⚖️ Actores y Marco Legal (V5)"
])

# ---- PESTAÑA 1: EVALUACIÓN ESG ----
with tabs[0]:
    st.header("Autoevaluación de Proveedores Industriales (ESG)")
    with st.form("esg_form"):
        col_e, col_s, col_g = st.columns(3)
        with col_e:
            st.markdown("### 🌱 Pilar Ambiental (E)")
            e1 = st.checkbox("Registro de Huella de Carbono (Alcance 1 y 2)")
            e2 = st.checkbox("Ecoeficiencia e Indicadores de Huella Hídrica")
            e3 = st.checkbox("Plan Certificado de Gestión de Residuos Peligrosos")
        with col_s:
            st.markdown("### 🤝 Pilar Social (S)")
            s1 = st.checkbox("Matrices IPERC vigentes / Cumplimiento ISO 45001")
            s2 = st.checkbox("Priorización de Contratación y Compre Local")
            s3 = st.checkbox("Programas Activos de Capacitación Técnica en Campo")
        with col_g:
            st.markdown("### ⚖️ Gobernanza Corporativa (G)")
            g1 = st.checkbox("Código de Conducta y Compliance formalizado")
            g2 = st.checkbox("Estados Financieros Transparentes y Auditables")
            g3 = st.checkbox("Auditoría Socioambiental de Subproveedores")
            
        if st.form_submit_button("Calcular Diagnóstico ESG"):
            respuestas = [e1, e2, e3, s1, s2, s3, g1, g2, g3]
            score, estado, msg, tipo = calcular_nivel_esg(respuestas)
            st.markdown("---")
            st.metric("Puntaje de Alineación", f"{score}%")
            if tipo == "success": st.success(f"🏆 {estado}: {msg}")
            elif tipo == "warning": st.warning(f"⚡ {estado}: {msg}")
            else: st.error(f"🚨 {estado}: {msg}")

# ---- PESTAÑA 2: GEOLOGÍA Y FACTIBILIDAD ----
with tabs[1]:
    st.header("Fase de Exploración: Viabilidad de Ley de Corte")
    col1, col2 = st.columns(2)
    with col1:
        tonelaje = st.number_input("Toneladas cubicadas (Mt)", value=50.0, key="k_ton")
        ley = st.slider("Ley de Cobre en la Roca (%)", 0.1, 3.0, 0.65, key="k_ley")
    with col2:
        precio = st.number_input("Precio Cu de Referencia (USD/Tn)", value=8500, key="k_prec")
        costo = st.number_input("Costo Operativo de Extracción/Planta (USD/Tn)", value=35, key="k_cost")
        
    v_ton, margen, rentable = calcular_ley_corte(tonelaje, ley, precio, costo)
    st.metric("Valor Neto Recuperable por Tonelada", f"USD {v_ton:.2f}", delta=f"Margen: USD {margen:.2f}")
    if rentable: st.success("Proyecto viable para avanzar a etapa de Factibilidad.")
    else: st.error("Proyecto paralizado por margen operativo insuficiente.")

# ---- PESTAÑA 3: PLANTA Y OPERACIÓN ----
with tabs[2]:
    st.header("Fase de Extracción y Procesamiento Metalúrgico")
    ingreso = st.slider("Alimentación de Planta (Tn/Hora)", 100, 2000, 500, key="k_ing")
    eficiencia = st.slider("Eficiencia de Recuperación Planta (%)", 50, 99, 85, key="k_ef")
    
    util, esteril = calcular_balance_masa(ingreso, ley, eficiencia)
    st.info(f"⚙️ **Balance de Masa:** Se recuperan {util:.2f} Tn/h de metal puro. Se disponen {esteril:.2f} Tn/h de material estéril (Ganga) en diques de colas seguros.")

# ---- PESTAÑA 4: CIERRE DE MINA ----
with tabs[3]:
    st.header("Fase de Cierre y Remediación Ambiental Mandatoria")
    remediacion = st.number_input("Presupuesto de Remediación Estimado (USD)", value=25000000, key="k_rem")
    vida_util = st.slider("Vida útil del Yacimiento (Años)", 5, 30, 15, key="k_vida")
    
    reserva_anual = calcular_fondo_cierre(remediacion, vida_util)
    st.warning(f"⚖️ **Fondo de Garantía Requerido:** Se deben previsionar **USD {reserva_anual:,.2f} anuales** desde el inicio operativo.")

# ---- PESTAÑA 5: MERCADOS Y COMMODITIES (Video 4) ----
with tabs[4]:
    st.header("Dinámica de Mercados Globales y Commodities")
    st.write("Simule cómo las variables geopolíticas afectan el valor de comercialización internacional:")
    
    dict_minerales = obtener_datos_minerales()
    col_v1, col_v2 = st.columns(2)
    
    with col_v1:
        mineral_sel = st.selectbox("Seleccione el Tipo de Recurso:", list(dict_minerales.keys()))
        vol_anual = st.number_input("Volumen de venta anual proyectado:", value=15000, step=1000)
    with col_v2:
        evento_macro = st.radio("Escenario Macroeconómico Global:", [
            "Estabilidad Financiera Internacional (LME Base)",
            "Aceleración Económica e Industrial de China (+15% Demanda)",
            "Conflictos Geopolíticos y Restricciones Logísticas (-10% Valor)",
            "Disrupción por Recesión Global o Transición Tecnológica Agresiva (-25% Ciclo)"
        ])
        mapeo_fluct = {
            "Estabilidad Financiera Internacional (LME Base)": 0.0,
            "Aceleración Económica e Industrial de China (+15% Demanda)": 15.0,
            "Conflictos Geopolíticos y Restricciones Logísticas (-10% Valor)": -10.0,
            "Disrupción por Recesión Global o Transición Tecnológica Agresiva (-25% Ciclo)": -25.0
        }
        fluctuacion = mapeo_fluct[evento_macro]

    pr_ajustado, ingreso_total, tipo_m, mecano_v, unidad_m = calcular_ingresos_mercado(mineral_sel, vol_anual, fluctuacion)
    
    st.markdown("---")
    st.subheader(f"📊 Reporte de Comercialización Spot: {mineral_sel}")
    st.write(f"**Tipo de Activo:** {tipo_m} | **Canal de Venta:** {mecano_v}")
    
    col_res1, col_res2 = st.columns(2)
    with col_res1:
        st.metric("Precio Unitario de Venta Ajustado", f"USD {pr_ajustado:,.2f} / {unidad_m}", delta=f"{fluctuacion}%" if fluctuacion != 0 else None)
    with col_res2:
        st.metric("Facturación Bruta Anual Estimada", f"USD {ingreso_total:,.2f}")

# ---- PESTAÑA 6: ACTORES Y MARCO LEGAL (Video 5) ----
with tabs[5]:
    st.header("Gobernanza del Ecosistema y Regulación de Mendoza")
    col_l1, col_l2 = st.columns(2)
    
    with col_l1:
        st.markdown("### 👥 Roles del Ecosistema")
        dict_actores = obtener_perfiles_actores()
        actor_sel = st.selectbox("Seleccione un actor institucional:", list(dict_actores.keys()))
        st.info(f"**Rol Operativo:** {dict_actores[actor_sel]['rol']}\n\n**Mecanismo de Capital:** {dict_actores[actor_sel]['financiamiento']}\n\n**Foco Estratégico:** {dict_actores[actor_sel]['foco']}")
        
        st.markdown("---")
        st.markdown("#### 🎲 El Embudo de la Exploración: Filtro de 1 en 1.000.000")
        anomalias = st.number_input("Cantidad de indicios/anomalías geológicas registradas en campaña:", value=250000, step=10000)
        p_acum, exito_h = simular_probabilidad_exploracion(anomalias)
        st.metric("Probabilidad de Descubrir una Mina Viable", f"{p_acum:.5f}%")
        if exito_h: st.success("🎯 ¡Éxito Estadístico! Se detectó un yacimiento comercializable.")
        else: st.warning("🔍 Campaña Finalizada. Los indicios fueron descartados por falta de ley de corte (Proceso estándar).")

    with col_l2:
        st.markdown("### ⚖️ Auditoría Normativa para la obtención de la DIA")
        st.write("Determine el marco de leyes obligatorio para habilitar la Declaración de Impacto Ambiental en Mendoza:")
        
        in_nac = st.selectbox("Código de Minería de la Nación:", ["Seleccione...", "Decreto N° 437/1993", "Código de Minería de la Nación (Ley N° 1919)"])
        in_prov = st.selectbox("Código de Procedimiento Minero Provincial:", ["Seleccione...", "Ley N° 7722", "Ley N° 9529 (Procedimiento Minero)"])
        in_amb = st.selectbox("Ley de Preservación Ambiental de Mendoza:", ["Seleccione...", "Ley N° 5961 (Preservación del Medio Ambiente)", "Ley N° 8461"])
        in_dec = st.selectbox("Decreto Reglamentario de Evaluación Minera:", ["Seleccione...", "Decreto N° 820/2006 (Reglamento Ambiental)", "Decreto N° 2100/2005"])
        
        if st.button("⚖️ Evaluar Consistencia Legal ante Autoridad"):
            es_ok, checklist = verificar_marco_dia_mendoza(in_nac, in_prov, in_amb, in_dec)
            if es_ok: st.success("🟢 Matriz Legal Correcta. Trámite de evaluación de DIA formalmente iniciado en Mendoza.")
            else:
                st.error("🔴 Rechazo de Expediente. Existen inconsistencias en las normativas citadas.")
                for k, v in checklist.items():
                    if not v: st.markdown(f"❌ *Error crítico de referenciación en parámetro:* **{k.upper()}**")
