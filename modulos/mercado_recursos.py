# Módulo de Clasificación de Recursos y Simulación de Mercados
def obtener_datos_minerales():
    """Retorna los grupos estratégicos de minerales y sus datos base de mercado."""
    return {
        "Metales Base (Cobre, Aluminio, Zinc)": {
            "tipo": "Commodity (LME)",
            "precio_base": 8500,
            "unidad": "USD / Tonelada",
            "descripcion": "Columna vertebral de la infraestructura moderna y la electrificación.",
            "mecanismo": "Cotización pública internacional en tiempo real."
        },
        "Metales Preciosos (Oro, Plata)": {
            "tipo": "Reserva de Valor",
            "precio_base": 2300,
            "unidad": "USD / Onza Troy",
            "descripcion": "Usos industriales de alta tecnología y refugio financiero global.",
            "mecanismo": "Fijación diaria en mercados globales (LBMA)."
        },
        "Minerales Críticos (Litio, Cobalto, Tierras Raras)": {
            "tipo": "Estratégico Tecnológico",
            "precio_base": 14500,
            "unidad": "USD / Tonelada LCE",
            "descripcion": "Esenciales para la transición energética. Objeto de disputas geopolíticas.",
            "mecanismo": "Contratos a mediano plazo y mercados spot de especialidad."
        },
        "Minerales Industriales (Potasio, Yeso, Cal)": {
            "tipo": "Insumo Industrial / Agro",
            "precio_base": 350,
            "unidad": "USD / Tonelada",
            "descripcion": "Fundamentales para la construcción y fertilizantes en el agro.",
            "mecanismo": "Contratos directos Off-take donde la logística de transporte es clave."
        }
    }

def calcular_ingresos_mercado(mineral_seleccionado, volumen_anual, fluctuacion_mercado):
    """Calcula el impacto de las fluctuaciones macroeconómicas en la facturación del proyecto."""
    minerales = obtener_datos_minerales()
    datos = minerales[mineral_seleccionado]
    
    # Aplicamos el porcentaje de fluctuación macro (crecimiento de China, conflictos, etc.)
    precio_ajustado = datos["precio_base"] * (1 + (fluctuacion_mercado / 100))
    ingreso_estimado = volumen_anual * precio_ajustado
    
    return precio_ajustado, ingreso_estimado, datos["tipo"], datos["mecanismo"]
