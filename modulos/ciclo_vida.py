# Módulo de Ingeniería del Ciclo de Vida de la Mina
def calcular_ley_corte(tonelaje, ley_promedio, precio_cu, costo_op):
    valor_por_tonelada = (ley_promedio / 100) * precio_cu
    margen = valor_por_tonelada - costo_op
    es_rentable = margen > 0
    return valor_por_tonelada, margen, es_rentable

def calcular_balance_masa(mineral_ingreso, ley_promedio, eficiencia):
    toneladas_utiles = (mineral_ingreso * (ley_promedio / 100)) * (eficiencia / 100)
    toneladas_esteril = mineral_ingreso - toneladas_utiles
    return toneladas_utiles, toneladas_esteril

def calcular_fondo_cierre(costo_remediacion, anos_operacion):
    return costo_remediacion / anos_operacion
