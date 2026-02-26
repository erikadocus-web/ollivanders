# 🪄 Ollivanders shop

Bienvenido a **Ollivanders**, un sistema de gestión de inventario para la legendaria tienda de varitas mágicas. Este proyecto implementa un kata tipo *Gilded Rose* con temática de Harry Potter.

## 📋 Descripción

Ollivanders es un sistema que mantiene y actualiza la calidad de las varitas mágicas en inventario según reglas para cada tipo de varita. Cada varita tiene propiedades como nombre, días para vender (*sellIn*) y calidad (*quality*).

## 🏗️ Estructura

```
ollivanders/
├── main.py                 # Punto de entrada de la aplicación
├── src/
│   ├── __init__.py
│   ├── ollivanders.py      # Clases principales del sistema
│   └── __pycache__/
├── test/
│   ├── test_gilded_rose.py # Tests para la clase GildedRose
│   ├── test_aged_brie.py   # Tests para varitas Aged Brie
│   ├── test_backstage.py   # Tests para entradas Backstage
│   ├── test_conjured.py    # Tests para varitas Conjured
│   ├── test_item.py        # Tests para items genéricos
│   ├── test_normal_item.py # Tests para items normales
│   ├── test_sulfuras.py    # Tests para Sulfuras
│   └── __pycache__/
└── README.md               # Este archivo
```

## 🎯 Componentes Principales

### Clases Base

- **`Item`**: Clase base que representa una varita mágica con atributos:
  - `name`: Nombre de la varita
  - `sellIn`: Días hasta que debe venderse
  - `quality`: Calidad del item (rango 0-50)

- **`NormalItem`**: Varita de calidad normal que decrece con el tiempo

- **`Ollivanders`**: Tienda que gestiona la colección de varitas y actualiza sus propiedades

### Tipos Especiales de Varitas

- **`AgedBrie`**: Aumenta de calidad con el tiempo
- **`Conjured`**: Decrece el doble de rápido que un item normal
- **`Backstage`**: Aumenta de calidad conforme se acerca la fecha de venta
- **`Sulfuras`**: Varita legendaria que nunca disminuye en calidad

## 🚀 Uso

### Ejecutar la aplicación:

```bash
python main.py
```

### Ejecutar los tests:

```bash
pytest
```

### Ejecutar un test específico:

```bash
pytest test/test_aged_brie.py -v
```

## 📝 Ejemplo de Uso

```python
from src.ollivanders import NormalItem, AgedBrie, Ollivanders

# Crear un inventario
shop = Ollivanders([])

# Agregar varitas
normal = NormalItem("+5 Dexterity Vest", 10, 20)
brie = AgedBrie("Aged Brie", 2, 0)

shop.items.append(normal)
shop.items.append(brie)

# Actualizar calidad
shop.updateQuality()
```

## 🧪 Tests

El proyecto incluye una suite completa de tests unitarios para validar el comportamiento de cada tipo de varita:

- **test_normal_item.py**: Validar el comportamiento de items normales
- **test_aged_brie.py**: Validar que Aged Brie aumenta de calidad
- **test_conjured.py**: Validar que Conjured decrece más rápido
- **test_backstage.py**: Validar el comportamiento de Backstage
- **test_sulfuras.py**: Validar que Sulfuras es legendaria
- **test_gilded_rose.py**: Tests integrales de la tienda

## ⚙️ Requisitos

- Python 3.7+
- pytest (para ejecutar los tests)

## 👨‍💻 Desarrollo

Este proyecto es un kata de programación basado en el famoso *Gilded Rose Kata*. El objetivo es implementar correctamente las reglas de actualización de calidad para diferentes tipos de items.
