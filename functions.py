import numpy as np
from itertools import combinations

# Вспомогательная функция для расчета яркости (luminance)
def luminance(color):
    r, g, b = color
    return 0.2126 * r + 0.7152 * g + 0.0722 * b

# Функции для оценки палитры
def clamp(value, min_val, max_val):
    return max(min(value, max_val), min_val)

def gradients(values):
    return [values[i + 1] - values[i] for i in range(len(values) - 1)]

def luminance_distribution_score(palette):
    lum_pal = sorted(map(luminance, palette))
    lum_grd = gradients(lum_pal)
    lum_grd_target = (lum_pal[-1] - lum_pal[0]) / len(palette)
    ok = [g for g in lum_grd if abs(g - lum_grd_target) / lum_grd_target <= 0.25]
    return len(ok) / len(palette)

def luminance_range_score(palette):
    lum_pal = sorted(map(luminance, palette))
    return (lum_pal[-1] - lum_pal[0]) / 255



def partition(iterable, condition):
    true_part = [item for item in iterable if condition(item)]
    false_part = [item for item in iterable if not condition(item)]
    return true_part, false_part


def luminance_contrast_score(palette):
    

    threshold = 0.05
    lum = list(map(luminance, palette))

    # Комбинации яркостей для всех пар
    lum_differences = [abs(b - a) for a, b in combinations(lum, 2)]
    
    # Разделяем пары на удовлетворяющие и не удовлетворяющие пороговому значению
    ok, notok = partition(lum_differences, lambda diff: diff >= threshold)

    # Идеальное различие яркости
    ideal = max(threshold, (max(lum) - min(lum)) / len(lum))

    # Разделяем удовлетворяющие пары на превышающие или недостающие идеального значения
    above, below = partition(ok, lambda diff: (diff - ideal) >= 0)
    
    # Если есть элементы, не удовлетворяющие минимальному порогу, возвращаем 0
    if len(notok):
        return 0

    # Возвращаем отношение пар с различием выше идеального к общему числу пар
    return len(above) / len(ok) if len(ok) > 0 else 0




def saturation(color):
    r, g, b = [c / 255 for c in color]  # Нормализуем значения в диапазон [0, 1]
    max_c = max(r, g, b)
    min_c = min(r, g, b)
    return 0 if max_c == 0 else (max_c - min_c) / max_c

def hue(color):
    r, g, b = [c / 255 for c in color]  # Нормализуем значения в диапазон [0, 1]
    max_c = max(r, g, b)
    min_c = min(r, g, b)
    if max_c == min_c:
        return 0
    elif max_c == r:
        h = (g - b) / (max_c - min_c)
    elif max_c == g:
        h = 2 + (b - r) / (max_c - min_c)
    else:
        h = 4 + (r - g) / (max_c - min_c)
    h = (h * 60) % 360
    return h

def circdist(a, b):
    # Циклическое расстояние между двумя углами в градусах
    diff = abs(a - b) % 360
    return min(diff, 360 - diff)

def hue_range_score(palette):
    # Фильтруем цвета с низкой насыщенностью
    filtered_palette = [color for color in palette if saturation(color) >= 0.05]
    
    # Если после фильтрации палитра пуста, возвращаем 0
    if not filtered_palette:
        return 0
    
    # Вычисляем оттенки оставшихся цветов
    hues = list(map(hue, filtered_palette))
    
    # Находим максимальное циклическое расстояние между парами оттенков
    max_hue_distance = max(
        circdist(a, b) for a, b in combinations(hues, 2)
    ) if len(hues) > 1 else 0
    



    return (360 - max_hue_distance) / 360