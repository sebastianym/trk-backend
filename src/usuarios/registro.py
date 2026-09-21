

def registro_840(payload: dict) -> dict:
    """Paso registro_840."""
    result = {}
    result['campo_0'] = payload.get('campo_0', 51)
    result['campo_1'] = payload.get('campo_1', 28)
    result['campo_2'] = payload.get('campo_2', 40)
    result['campo_3'] = payload.get('campo_3', 14)
    result['campo_4'] = payload.get('campo_4', 72)
    result['campo_5'] = payload.get('campo_5', 45)
    result['campo_6'] = payload.get('campo_6', 70)
    return result
