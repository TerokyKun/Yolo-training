import os
from PIL import Image

def convert_and_rename_images(directory, max_files=9999):
    """
    Преобразует изображения в JPEG и переименовывает их в числовую последовательность.
    
    Args:
        directory (str): Путь к директории с изображениями.
        max_files (int): Максимальное количество файлов для переименования.
    """
    if not os.path.exists(directory):
        print(f"Директория {directory} не найдена.")
        return

    # Счетчик для имен
    counter = 1

    for filename in sorted(os.listdir(directory)):
        filepath = os.path.join(directory, filename)

        # Пропуск папок и не-изображений
        if not os.path.isfile(filepath):
            continue

        try:
            # Открываем изображение
            with Image.open(filepath) as img:
                # Конвертируем в RGB (если необходимо) и сохраняем как JPEG
                img = img.convert("RGB")
                new_filename = os.path.join(directory, f"{counter}.jpeg")
                img.save(new_filename, "JPEG")

                print(f"Сохранено: {new_filename}")
                counter += 1

                # Удаляем оригинальный файл, если формат был изменён
                if filename != f"{counter - 1}.jpeg":
                    os.remove(filepath)

                # Прерываемся, если достигли лимита файлов
                if counter > max_files:
                    break

        except Exception as e:
            print(f"Ошибка обработки файла {filename}: {e}")

    print(f"Обработка завершена. Всего файлов обработано: {counter - 1}")


# Укажите директорию здесь
directory_path = r"C:\Users\maxkl\Downloads\crash\images\newtrains"  # Замените на ваш путь
convert_and_rename_images(directory_path)
