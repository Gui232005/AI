import math

cidades = {
    'Aveiro': {'Porto': 68, 'Viseu': 95, 'Coimbra': 68, 'Leiria': 115},
    'Braga': {'Viana do Castelo': 48, 'Vila Real': 106, 'Porto': 53},
    'Bragança': {'Vila Real': 137, 'Guarda': 202},
    'Beja': {'Évora': 78, 'Faro': 152, 'Setúbal': 142},
    'Castelo Branco': {'Coimbra': 159, 'Guarda': 106, 'Portalegre': 80, 'Évora': 203},
    'Coimbra': {'Aveiro': 68, 'Viseu': 96, 'Leiria': 67, 'Castelo Branco': 159},
    'Évora': {'Beja': 78, 'Castelo Branco': 203, 'Lisboa': 150, 'Santarém': 117, 'Portalegre': 131, 'Setúbal': 103},
    'Faro': {'Beja': 152, 'Setúbal': 249, 'Lisboa': 299},
    'Guarda': {'Bragança': 202, 'Castelo Branco': 106, 'Vila Real': 157, 'Viseu': 85},
    'Leiria': {'Aveiro': 115, 'Coimbra': 67, 'Lisboa': 129, 'Santarém': 70},
    'Lisboa': {'Évora': 150, 'Faro': 299, 'Leiria': 129, 'Santarém': 78, 'Setúbal': 50},
    'Portalegre': {'Castelo Branco': 80, 'Évora': 131},
    'Porto': {'Aveiro': 68, 'Braga': 53, 'Viana do Castelo': 71, 'Vila Real': 116, 'Viseu': 133},
    'Santarém': {'Évora': 117, 'Leiria': 70, 'Lisboa': 78},
    'Setúbal': {'Beja': 142, 'Évora': 103, 'Faro': 249, 'Lisboa': 50},
    'Viana do Castelo': {'Braga': 48, 'Porto': 71},
    'Vila Real': {'Braga': 106, 'Bragança': 137, 'Guarda': 157, 'Porto': 116, 'Viseu': 110},
    'Viseu': {'Aveiro': 95, 'Coimbra': 96, 'Guarda': 85, 'Porto': 133, 'Vila Real': 110}
}

origem_faro = {
    'Aveiro': 366,
    'Braga': 454,
    'Bragança': 487,
    'Beja': 99,
    'Castelo Branco': 280,
    'Coimbra': 319,
    'Évora': 157,
    'Faro': 0,
    'Guarda': 352,
    'Leiria': 278,
    'Lisboa': 195,
    'Portalegre': 228,
    'Porto': 418,
    'Santarém': 231,
    'Setúbal': 168,
    'Viana do Castelo': 473,
    'Vila Real': 429,
    'Viseu': 363
}


# Tabela 3: Coordenadas geográficas (Latitude, Longitude) das cidades do projeto
coordenadas = {
    'Aveiro': (40.6443, -8.6455),
    'Beja': (38.0151, -7.8632),
    'Braga': (41.5454, -8.4265),
    'Bragança': (41.8058, -6.7572),
    'Castelo Branco': (39.8222, -7.4909),
    'Coimbra': (40.2056, -8.4195),
    'Évora': (38.5667, -7.9000),
    'Faro': (37.0194, -7.9322),
    'Guarda': (40.5373, -7.2658),
    'Leiria': (39.7436, -8.8071),
    'Lisboa': (38.7223, -9.1393),
    'Portalegre': (39.2938, -7.4312),
    'Porto': (41.1579, -8.6291),
    'Santarém': (39.2333, -8.6833),
    'Setúbal': (38.5243, -8.8926),
    'Viana do Castelo': (41.6932, -8.8329),
    'Vila Real': (41.3006, -7.7441),
    'Viseu': (40.6566, -7.9125)
}

def linha_reta(origem, destino):
    """
    Calcula a distância em linha reta (Haversine) entre duas cidades em km.
    """
    if origem not in coordenadas or destino not in coordenadas:
        return None  # Prevenção de erros caso a cidade não exista
    
    lat1, lon1 = coordenadas[origem]
    lat2, lon2 = coordenadas[destino]
    
    R = 6371.0 # Raio médio da Terra em quilómetros
    
    # Conversão de graus para radianos
    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)
    delta_phi = math.radians(lat2 - lat1)
    delta_lambda = math.radians(lon2 - lon1)
    
    # Aplicação da fórmula de Haversine
    a = math.sin(delta_phi / 2.0)**2 + math.cos(phi1) * math.cos(phi2) * math.sin(delta_lambda / 2.0)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    
    distancia = R * c
    
    return round(distancia) # Devolve o valor arredondado (inteiro)

