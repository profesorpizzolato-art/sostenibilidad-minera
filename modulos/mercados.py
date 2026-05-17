# Módulo de Clasificación de Recursos y Simulación de Mercados (LME)

def obtener_datos_minerales():
    """Retorna las categorías estratégicas de minerales y sus valores base de cotización."""
    return {
        "Metales Base (Cobre, Aluminio, Zinc)": {
            "tipo": "Commodity (LME)",
            "precio_base": 8500.0,
            "unidad": "USD / Tonelada",
            "mecanismo": "Cotización pública internacional regulada en el London Metal Exchange.",
            "descripcion": "Columna vertebral de la infraestructura moderna y la electrificación global."
        },
        "Metales Preciosos (Oro, Plata)": {
            "tipo": "Reserva de Valor",
            "precio_base": 2300.0,
            "unidad": "USD / Onza Troy",
            "mecanismo": "Fijación diaria en mercados globales (LBMA) y refugio financiero.",
            "descripcion": "Usos en electrónica avanzada, transacciones e instrumentos de inversión."
        },
        "Minerales Críticos (Litio, Cobalto, Tierras Raras)": {
            "tipo": "Estratégico Tecnológico",
            "precio_base": 14500.0,
            "unidad": "USD / Tonelada LCE",
            "mecanismo": "Contratos directos a mediano plazo y mercados spot de especialidad.",
            "descripcion": "Insumos indispensables para la transición energética y almacenamiento de energía."
        },
        "Minerales Industriales (Potasio, Yeso, Cal)": {
            "tipo": "Insumo Industrial / Agro",
            "precio_base": 350.0,
            "unidad": "USD / Tonelada",
            "mecanismo": "Contratos directos privados (Off-take) altamente dependientes de la logística.",
            "descripcion": "Minerales de aplicación directa esenciales para la construcción civil y el agro."
        }
    }

def calcular_ingresos_mercado(mineral_seleccionado, volumen_anual, fluctuacion_mercado):
    """Aplica las variaciones macroeconómicas globales a la rentabilidad del proyecto local."""
    minerales = obtener_datos_minerales()
    datos = minerales[mineral_seleccionado]
    
    # Cálculo indexado por fluctuación
    precio_ajustado = datos["precio_base"] * (1 + (fluctuacion_mercado / 100))
    ingreso_total = volumen_anual * precio_ajustado
    return precio_ajustado, ingreso_total, datos["tipo"], datos["mecanismo"], datos["unidad"]
