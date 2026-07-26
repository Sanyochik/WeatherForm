## 📖 О проекте

**WeatherForm** — это простое и элегантное десктопное приложение для получения актуальной температуры в любом городе мира. Проект построен по архитектурному паттерну **MVC (Model-View-Controller)** и демонстрирует:

- 🖥️ Работу с графическим интерфейсом на **CustomTkinter**
- 🌐 Интеграцию с **OpenWeatherMap API**
- 🏗️ Чистую архитектуру с разделением ответственности

## 📦 Установка и запуск

### 1. Клонирование репозитория

```bash
git clone https://github.com/Sanyochik/WeatherForm.git
cd WeatherForm
```
### 2. Установка зависимостей
```bash
pip install customtkinter requests
```
### 3. Настройка API ключа
Откройте файл models/weather.py и замените 'openweathermapkey' на ваш ключ
```python
API_key = 'ваш_реальный_ключ_OpenWeatherMap'
```
Ключ можно получить зарегистрировавшись на сайте <a href="https://openweathermap.org/api">Openweathermap</a>
### 4. Запуск приложения
```python
python index.py
```
