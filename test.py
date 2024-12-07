from ultralytics import YOLO

# Загрузка обученной модели (например, best.pt)
model = YOLO("name_model.pt")

# Пример предсказания на изображении
results = model.predict("имя_изображения.jpg")

# Обработка результатов (results — это список)
for result in results:
    # Покажет изображение с аннотациями
    result.show()

    # Сохранит изображение с аннотациями в папку 'runs/detect/predict'
    result.save()

    # Выведет результаты предсказания в формате pandas DataFrame
    print(result.pandas())  # Печать результатов предсказания
