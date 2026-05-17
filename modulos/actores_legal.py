# Módulo de Actores del Ecosistema Minero y Marco Legal de Mendoza

def obtener_perfiles_actores():
    """Retorna los roles estratégicos y su interacción financiera."""
    return {
        "Compañía Junior": {
            "rol": "Descubrimiento y Exploración Inicial",
            "financiamiento": "Mercado de Capitales (Acciones/Equity) de Alto Riesgo",
            "fortaleza": "Gran agilidad y capacidad técnica de campo",
            "desafio": "Sin flujo de caja propio. Dependencia absoluta del éxito geológico."
        },
        "Compañía Major": {
            "rol": "Construcción, Operación y Cierre a Gran Escala",
            "financiamiento": "Ingresos Operativos Propios y Sindicación de Deuda Internacional",
            "fortaleza": "Enorme espalda financiera y capacidad de infraestructura",
            "desafio": "Estructuras burocráticas pesadas. Requieren yacimientos World-Class."
        },
        "Proveedor Industrial / Local": {
            "rol": "Soporte de Servicios, Logística, Ingeniería y Tecnología",
            "financiamiento": "Contratos comerciales por servicios prestados (OPEX/CAPEX de operadoras)",
            "fortaleza": "Generación de empleo indirecto multiplicado en la región",
            "desafio": "Cumplimiento estricto de matrices de riesgo y estándares ESG."
        }
    }

def simular_riesgo_exploracion(intentos_prospeccion):
    """Simula la estadística real minera: solo 1 de cada 1.000.000 de indicios llega a ser mina."""
    probabilidad_exito = 1 / 1000000
    # Cálculo probabilístico acumulado para el volumen de intentos del alumno
    prob_acumulada = 1 - ((1 - probabilidad_exito) ** intentos_prospeccion)
    exito_conseguido = np.random.random() < prob_acumulada if 'np' in globals() else False
    
    return prob_acumulada * 100, exito_conseguido

def validar_matriz_legal_mendoza(ley_nacional, ley_procedimiento, ley_ambiental, decreto_reg):
    """Valida si el operador conoce la jerarquía de leyes para obtener la DIA en Mendoza."""
    # Respuestas correctas esperadas
    checklist = {
        "nacional": ley_nacional == "Código de Minería de la Nación (Ley N° 1919)",
        "procedimiento": ley_procedimiento == "Ley Provincial N° 9529",
        "ambiental": ley_ambiental == "Ley Provincial N° 5961",
        "decreto": decreto_reg == "Decreto N° 820/2006"
    }
    
    aprobado = all(checklist.values())
    return aprobado, checklist
# Módulo de Dinámica de Actores y Validación Normativa de Mendoza
import random

def obtener_perfiles_actores():
    return {
        "Compañía Junior": {
            "rol": "Descubrimiento y Exploración Inicial",
            "financiamiento": "Mercado de Capitales (Venta de Acciones / Equity de alto riesgo)",
            "foco": "Agilidad técnica en geología y perforación minera preliminar."
        },
        "Compañía Major": {
            "rol": "Construcción, Operación Comercial y Cierre Complejo",
            "financiamiento": "Reinversión de Ingresos Operativos y Sindicación de Deuda Global",
            "foco": "Capacidad de infraestructura para proyectos de miles de millones de dólares (World Class)."
        },
        "Proveedores y Servicios Locales": {
            "rol": "Soporte de Ingeniería, Logística, Mantenimiento y Tecnología",
            "financiamiento": "Contratos comerciales (Adjudicación por licitaciones OPEX/CAPEX)",
            "foco": "Multiplicación de empleo indirecto y desarrollo del entramado PyME regional."
        }
    }

def simular_probabilidad_exploracion(anomalías_investigadas):
    """Aplica la estadística real de la industria: solo 1 de cada 1.000.000 de indicios llega a ser mina."""
    prob_base = 1 / 1000000
    # Cálculo probabilístico acumulado binomial
    prob_acumulada = (1 - ((1 - prob_base) ** anomalías_investigadas)) * 100
    exito = random.random() < (prob_acumulada / 100)
    return prob_acumulada, exito

def verificar_marco_dia_mendoza(nacional, provincial, ambiental, decreto):
    """Valida el conocimiento del orden jerárquico normativo para operar en Mendoza."""
    checks = {
        "nacional": nacional == "Código de Minería de la Nación (Ley N° 1919)",
        "provincial": provincial == "Ley N° 9529 (Procedimiento Minero)",
        "ambiental": ambiental == "Ley N° 5961 (Preservación del Medio Ambiente)",
        "decreto": decreto == "Decreto N° 820/2006 (Reglamento Ambiental)"
    }
    es_valido = all(checks.values())
    return es_valido, checks
