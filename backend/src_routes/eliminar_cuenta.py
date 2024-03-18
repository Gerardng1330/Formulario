import sqlite3
from datetime import datetime, timedelta

# Conectar a la base de datos
conn = sqlite3.connect('tu_base_de_datos.db')
cursor = conn.cursor()

# Definir el tiempo límite para la inactividad (12 horas)
limite_inactividad = datetime.now() - timedelta(hours=12)

# Consulta SQL para seleccionar cuentas que cumplen las condiciones
sql = "DELETE FROM cuentas WHERE (estado = 'inactiva' AND token IS NULL) OR (estado = 'inactiva' AND token IS NOT NULL AND fecha_creacion < ?)"

# Ejecutar la consulta SQL
cursor.execute(sql, (limite_inactividad,))

# Guardar los cambios
conn.commit()

# Cerrar la conexión
conn.close()
