# Импорт необходимых библиотек

from ultralytics import YOLO

# Обучение модели YOLO с включением TensorBoard
if __name__ == "__main__":
    model = YOLO("yolo11n.pt")  # Загружаем предварительно обученную модель

  # Обучение модели
results = model.train(
    data="data.yaml",  # Путь к файлу конфигурации данных (содержит пути к наборам данных, классам и их меткам).
    epochs=20,  # Количество эпох (сколько раз модель проходит через весь тренировочный набор данных).
    imgsz=420,  # Размер изображений (размер сторон входного изображения, которое подается в модель).
    batch=1,  # Размер батча (количество изображений, обрабатываемых за один шаг обучения).
    amp=True,  # Автоматическая смешанная точность (ускорение вычислений с помощью 16-битных чисел с плавающей точкой).
    
    # Параметры аугментации данных
    hsv_h=0.015,  # Диапазон изменения оттенка в цветовой модели HSV.
    hsv_s=0.7,  # Диапазон изменения насыщенности в цветовой модели HSV.
    hsv_v=0.4,  # Диапазон изменения яркости в цветовой модели HSV.
    degrees=10.0,  # Диапазон случайного вращения изображения (в градусах).
    translate=0.1,  # Диапазон случайного сдвига изображения по горизонтали и вертикали.
    scale=0.5,  # Диапазон случайного изменения масштаба изображения.
    shear=0.0,  # Диапазон случайного сдвига углов изображения (сдвиг под углом).
    perspective=0.0,  # Диапазон искажения перспективы изображения.
    flipud=0.0,  # Вероятность случайного переворота изображения по вертикали.
    fliplr=0.5,  # Вероятность случайного переворота изображения по горизонтали.
    mosaic=1.0,  # Включение mosaic-аугментации (объединение нескольких изображений в одно для создания сложных сцен).
    mixup=0.0,  # Вероятность применения mixup-аугментации (смешивание двух изображений и их меток).
    copy_paste=0.0,  # Вероятность использования copy-paste аугментации (вставка объектов из одного изображения в другое).
    auto_augment="randaugment",  # Использование автоматической аугментации (заданной схемы, например, RandAugment).
    erasing=0.4,  # Вероятность случайного удаления области изображения (Random Erasing).
    
    # Гиперпараметры оптимизатора
    momentum=0.937,  # Моментум для оптимизатора (ускоряет сходимость путем учета предыдущего шага).
    
    val=True,  # Включение валидации (проверка модели на отдельном наборе данных после каждой эпохи).
    
    name="yolo_training"  # Имя проекта в TensorBoard (для отслеживания метрик обучения и валидации).
)
