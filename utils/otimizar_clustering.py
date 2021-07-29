def numero_otimo_clusters(wcss):
    x1, y1 = 2, wcss[0]
    x2, y2 = 20, wcss[len(wcss)-1]

    distancias = []
    for i in range(len(wcss)):
        x0 = i+2
        y0 = wcss[i]
        numerador = abs((y2-y1)*x0 - (x2-x1)*y0 + x2*y1 - y2*x1)
        denominador = ((y2 - y1)**2 + (x2 - x1)**2)**(-1)
        distancias.append(numerador/denominador)
    
    return distancias.index(max(distancias)) + 2