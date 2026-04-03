# Clínica Médica - Sistema de Gestión de Pacientes

Una aplicación web desarrollada con Django para gestion de pacientes y médicos en una clínica médica.

## 📋 Descripción

Sistema integral de gestión de información clínica que permite:
- Registrar y gestionar médicos de la clínica
- Registrar y gestionar pacientes
- Asignar pacientes a médicos
- Buscar pacientes por nombre
- Editar información de pacientes y médicos

## 🚀 Características

- **CRUD Completo** para pacientes y médicos
- **Búsqueda funcional** de pacientes por nombre
- **Interfaz responsiva** con Bootstrap
- **Validación de datos** en formularios
- **Base de datos PostgreSQL** integrada
- **Panel administrativo** de Django

## 📦 Requisitos

- Python 3.8+
- Django 6.0.3

## 🔧 Instalación

1. **Clonar el repositorio:**
```bash
git clone <URL_DEL_REPOSITORIO>
cd tarea_clinica
```

2. **Crear entorno virtual (opcional pero recomendado):**
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

3. **Instalar dependencias:**
```bash
pip install -r requirements.txt
```

4. **Aplicar migraciones:**
```bash
python manage.py migrate
```

5. **Crear superusuario (opcional, para acceder al admin):**
```bash
python manage.py createsuperuser
```

6. **Ejecutar servidor de desarrollo:**
```bash
python manage.py runserver
```

La aplicación estará disponible en `http://127.0.0.1:8000/`

## 📖 Uso

### Rutas Disponibles

| Ruta | Descripción |
|------|-------------|
| `/pacientes/` | Lista de todos los pacientes |
| `/pacientes/?nombre=<busqueda>` | Buscar pacientes por nombre |
| `/pacientes/nuevo/` | Crear nuevo paciente |
| `/pacientes/editar/<id>/` | Editar información de paciente |
| `/medicos/nuevo/` | Crear nuevo médico |
| `/medicos/editar/<id>/` | Editar información de médico |


## 📁 Estructura del Proyecto

```
tarea_clinica/
├── clinica_medica/          # Configuración principal del proyecto
│   ├── settings.py          # Configuración de Django
│   ├── urls.py              # URLs principales
│   ├── asgi.py
│   └── wsgi.py
├── gestion_pacientes/       # Aplicación principal
│   ├── models.py            # Modelos (Medico, Paciente)
│   ├── views.py             # Vistas (lógica de negocio)
│   ├── forms.py             # Formularios
│   ├── urls.py              # URLs de la app
│   ├── admin.py
│   ├── templates/           # Plantillas HTML
│   │   └── gestion_pacientes/
│   │       ├── lista_pacientes.html
│   │       ├── formulario_paciente.html
│   │       └── formulario_medico.html
│   ├── static/              # Archivos estáticos (CSS, JS)
│   └── migrations/          # Migraciones de base de datos
├── manage.py                # Script de gestión de Django
├── db.sqlite3               # Base de datos
└── requirements.txt         # Dependencias del proyecto
```

## 🗄️ Modelos de Datos

### Médico
```
- nombre (CharField): Nombre completo del médico
- especialidad (CharField): Especialidad médica
- registro_medico (CharField): Número de registro único
```

### Paciente
```
- nombre (CharField): Nombre completo del paciente
- rut (CharField): Identificación única
- fecha_nacimiento (DateField): Fecha de nacimiento
- medico_asignado (ForeignKey): Médico asignado
```

## 🛠️ Tecnologías Utilizadas

- **Django 6.0.3**: Framework web Python
- **Bootstrap**: Estilos responsivos
- **SQLite**: Base de datos
- **HTML5/CSS3**: Interfaz

## 📝 Notas de Desarrollo

- Los formularios incluyen clases Bootstrap para mejor presentación
- La búsqueda es case-insensitive utilizando `icontains`
- Todos los pacientes deben tener un médico asignado
- El campo RUT debe ser único para cada paciente
- El número de registro médico debe ser único para cada médico

Creadores: Alfoso Basterrechea, Viviana Canales, Cristofer Henríquez, Sebastián Toledo.

