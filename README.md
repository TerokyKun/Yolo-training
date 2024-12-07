# Yolo-training

Для тренировки используйте data.yaml и самостоятельно сделанные labels

Вот пример data 

train: C:\Users\maxkl\Downloads\crash\images\trains
val: C:\Users\maxkl\Downloads\crash\images\trains

nc: 1
names: 
  - none


Результаты будут в папке runs, а сам файл модели в папке runs/detect/train(последний номер)/weights/best.pt