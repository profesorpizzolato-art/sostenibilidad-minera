# Módulo de Autoevaluación para Proveedores - ESG
def calcular_nivel_esg(respuestas):
    total_checks = sum(respuestas)
    score = int((total_checks / 9) * 100)
    
    if score == 100:
        estado = "Avanzado / Certificable"
        msg = "Su empresa cumple con la totalidad de los estándares exigidos por las operadoras internacionales (Apto para financiamiento IFC)."
        tipo = "success"
    elif score >= 70:
        estado = "Intermedio / En Desarrollo"
        msg = "Buen nivel en campo. Falta formalizar o documentar procesos para calificar como proveedor estratégico."
        tipo = "warning"
    else:
        estado = "Inicial / Crítico"
        msg = "Se requiere reingeniería urgente. Riesgo de descalificación en matrices técnicas de compras."
        tipo = "error"
        
    return score, estado, msg, tipo
