import numpy as np
from tensorflow.keras.models import load_model

from functions import luminance_distribution_score, luminance_range_score, luminance_contrast_score, hue_range_score

input_dim = 20

#Загрузка модели
# model = load_model('_1_simple_model.h5') #Здесь указать тестируемую модель

model = load_model('test_model_5.h5') #Здесь указать тестируемую модель


def test():
    

    n = 1000

    lum_dist_score = 0
    lum_range_score = 0
    lum_contrast_score = 0
    h_range_score = 0

    for i in range(n):
        random_input = np.random.rand(1, input_dim)
        # Предсказание цветов
        predicted_colors = model.predict(random_input).reshape(5, 3) * 255    
        # Округление значений до целых чисел
        predicted_colors = np.round(predicted_colors).astype(int)

        lum_dist_score += luminance_distribution_score(predicted_colors)       
        lum_range_score += luminance_range_score(predicted_colors)
        lum_contrast_score += luminance_contrast_score(predicted_colors)
        h_range_score += hue_range_score(predicted_colors)

    lum_dist_score /= n  
    lum_range_score /= n  
    lum_contrast_score /= n  
    h_range_score /= n  

    print("Luminance Distribution -", round(lum_dist_score * 100, 2))
    print("Luminance Range -", round(lum_range_score* 100, 2))
    print("Luminance Contrast -", round(lum_contrast_score * 100, 2))
    print("Hue range -", round(h_range_score * 100, 2))

test()




