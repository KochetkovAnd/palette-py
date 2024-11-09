from flask import Flask, request, jsonify
from PIL import Image
import numpy as np
from sklearn.cluster import KMeans

def generate_palette_from_image(image, num_colors=5):
    pixels = np.array(image)
    pixels = pixels.reshape(-1, 3)

    kmeans = KMeans(n_clusters=num_colors)
    kmeans.fit(pixels)

    cluster_centers = kmeans.cluster_centers_

    # Преобразуем цвета кластеров в HEX формат
    hex_colors = ([f"{int(c[0]):02X}{int(c[1]):02X}{int(c[2]):02X}" for c in cluster_centers])

    sorted_colors = sorted(zip(cluster_centers, hex_colors), key=lambda x: calculate_brightness(x[0]), reverse=True)

    return [color[1] for color in sorted_colors]
     
    
    
def calculate_brightness(color):
    """Вычисляет относительную светимость цвета RGB."""
    r, g, b = color
    return 0.299 * r + 0.587 * g + 0.114 * b