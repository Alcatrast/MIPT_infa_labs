import matplotlib.pyplot as plt
import numpy as np
import re
from datetime import datetime, timedelta

def parse_sensor_data(filename):
    """Парсинг данных из файла"""
    times = []
    accel_x, accel_y, accel_z = [], [], []
    
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    # Время начала (предполагаем 200мс между измерениями)
    start_time = datetime.now()
    time_delta = timedelta(milliseconds=200)
    
    for i, line in enumerate(lines):
        if 'Accel:' not in line:
            continue
            
        # Парсим данные с помощью регулярных выражений
        match = re.search(r'X=\s*([-\d]+)\s*\|\s*Y=\s*([-\d]+)\s*\|\s*Z=\s*([-\d]+)', line)
        if match:
            # Время измерения
            current_time = start_time + i * time_delta
            times.append(current_time)
            
            # Акселерометр
            accel_x.append(int(match.group(1)))
            accel_y.append(int(match.group(2)))
            accel_z.append(int(match.group(3)))
    
    return times, accel_x, accel_y, accel_z

def moving_average(data, window_size=5):
    """Фильтр скользящего среднего"""
    result = []
    for i in range(len(data)):
        start = max(0, i - window_size // 2)
        end = min(len(data), i + window_size // 2 + 1)
        window = data[start:end]
        result.append(np.mean(window))
    return result

def median_filter(data, window_size=5):
    """Медианный фильтр"""
    result = []
    for i in range(len(data)):
        start = max(0, i - window_size // 2)
        end = min(len(data), i + window_size // 2 + 1)
        window = data[start:end]
        result.append(np.median(window))
    return result

def apply_combined_filter(data, window_size=10):

    combined_filtered = data
    for i in range(50):
        """Применение медианного фильтра + скользящего среднего"""
        # Сначала медианный фильтр (убирает выбросы)
        median_filtered = median_filter(combined_filtered, window_size)
        # Потом скользящее среднее (сглаживает)
        combined_filtered = moving_average(median_filtered, window_size)
    return combined_filtered



def calculate_length(x, y, z):
    """Вычисление длины вектора ускорения"""
    return [np.sqrt(xi**2 + yi**2 + zi**2) for xi, yi, zi in zip(x, y, z)]

def plot_sensor_data(times, accel_x, accel_y, accel_z):
    """Построение графиков"""
    # Вычисляем длину вектора
    length = calculate_length(accel_x, accel_y, accel_z)
    
    # Временные метки в секундах от начала
    time_seconds = [(t - times[0]).total_seconds() for t in times]
    
    # Применяем комбинированный фильтр
    window_size = 5
    
    # Комбинированный фильтр для всех данных
    accel_x_filtered = apply_combined_filter(accel_x, window_size)
    accel_y_filtered = apply_combined_filter(accel_y, window_size)
    accel_z_filtered = apply_combined_filter(accel_z, window_size)
    length_filtered = apply_combined_filter(length, window_size)


    a = 590.5578861539504/1000000
    b = 572.3142075889061/1000000 
    c = 598.2829899163563/1000000
    d=9.8155/ np.mean(length_filtered)
    
   

    accel_x=[x*a for x in accel_x]
    accel_y=[x*b for x in accel_y]
    accel_z=[x*c for x in accel_z]
    length=[x*d for x in length]
    accel_x_filtered=[x*a for x in accel_x_filtered]
    accel_y_filtered=[x*b for x in accel_y_filtered]
    accel_z_filtered=[x*c for x in accel_z_filtered]
    length_filtered=[x*d for x in length_filtered]



    # Создаем фигуру с subplots
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 10))
    fig.suptitle('Анализ данных акселерометра с комбинированной фильтрацией', fontsize=16, fontweight='bold')
    
    # График X(t)
    ax1.plot(time_seconds, accel_x, 'r-', linewidth=1, label='Исходные данные', alpha=0.7)
    ax1.plot(time_seconds, accel_x_filtered, 'darkred', linewidth=2, label='Медианный + скользящее среднее')
    ax1.set_title('Ускорение по оси X')
    ax1.set_xlabel('Время (секунды)')
    ax1.set_ylabel('Ускорение X')
    ax1.grid(True, alpha=0.3)
    ax1.legend()
    
    # График Y(t)
    ax2.plot(time_seconds, accel_y, 'g-', linewidth=1, label='Исходные данные', alpha=0.7)
    ax2.plot(time_seconds, accel_y_filtered, 'darkgreen', linewidth=2, label='Медианный + скользящее среднее')
    ax2.set_title('Ускорение по оси Y')
    ax2.set_xlabel('Время (секунды)')
    ax2.set_ylabel('Ускорение Y')
    ax2.grid(True, alpha=0.3)
    ax2.legend()
    
    # График Z(t)
    ax3.plot(time_seconds, accel_z, 'b-', linewidth=1, label='Исходные данные', alpha=0.7)
    ax3.plot(time_seconds, accel_z_filtered, 'darkblue', linewidth=2, label='Медианный + скользящее среднее')
    ax3.set_title('Ускорение по оси Z')
    ax3.set_xlabel('Время (секунды)')
    ax3.set_ylabel('Ускорение Z')
    ax3.grid(True, alpha=0.3)
    ax3.legend()
    
    # График длины вектора
    ax4.plot(time_seconds, length, 'purple', linewidth=1, label='Исходные данные', alpha=0.7)
    ax4.plot(time_seconds, length_filtered, 'darkviolet', linewidth=2, label='Медианный + скользящее среднее')
    ax4.set_title('Длина вектора ускорения')
    ax4.set_xlabel('Время (секунды)')
    ax4.set_ylabel('√(X² + Y² + Z²)')
    ax4.grid(True, alpha=0.3)
    ax4.legend()
    
    plt.tight_layout()
    plt.show()
    
    print_statistics(accel_x_filtered, accel_y_filtered, accel_z_filtered, length_filtered)
    return length

def print_statistics(accel_x, accel_y, accel_z, length):
    """Вывод статистики"""
    print("\n=== СТАТИСТИКА ДАННЫХ ===")
    print(f"Всего измерений: {len(accel_x)}")
    print(f"Продолжительность: {len(accel_x) * 0.2:.1f} секунд")
    print(f"\nАкселерометр X:")
    print(f"  Мин: {min(accel_x)}, Макс: {max(accel_x)}, Среднее: {np.mean(accel_x):.1f}")
    print(f"Акселерометр Y:")
    print(f"  Мин: {min(accel_y)}, Макс: {max(accel_y)}, Среднее: {np.mean(accel_y):.1f}")
    print(f"Акселерометр Z:")
    print(f"  Мин: {min(accel_z)}, Макс: {max(accel_z)}, Среднее: {np.mean(accel_z):.1f}")
    print(f"Длина вектора:")
    print(f"  Мин: {min(length):.1f}, Макс: {max(length):.1f}, Среднее: {np.mean(length):.1f}")

# Основная программа
if __name__ == "__main__":
    filename = r"C:\Users\LaL\Desktop\tutu3.txt"
    
    try:
        # Чтение и парсинг данных
        times, accel_x, accel_y, accel_z = parse_sensor_data(filename)
        
        if not times:
            print("Не найдено данных в файле!")
            exit()
        
        print(f"Успешно прочитано {len(times)} измерений")
        
        # Построение графиков
        length = plot_sensor_data(times, accel_x, accel_y, accel_z)
        
        # Вывод статистики
        print_statistics(accel_x, accel_y, accel_z, length)
        
    except FileNotFoundError:
        print(f"Файл {filename} не найден!")
    except Exception as e:
        print(f"Ошибка: {e}")