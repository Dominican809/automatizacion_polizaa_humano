# 🧾 Automatizador de Emisión de Seguros - Goval API

Este proyecto permite **emitir pólizas de seguro de viaje** automáticamente utilizando la [API Goval-Web v3.7](./API%20Goval-Web%20v3.7-1.pdf). El sistema sigue el flujo oficial de emisión, tal como se describe en el documento (páginas 104–114), implementado en Python de forma modular y clara.

## 📚 Requisitos
- Python 3.9 o superior
- `requests` (para llamadas a la API)

Instalar dependencias:
```bash
pip install requests
```

## 🗂️ Estructura del Proyecto

```
emisor_goval/
├── main.py                 # Entrada principal: emite pólizas en lote
├── config.py               # Credenciales y parámetros generales
├── api/
│   ├── auth.py             # Login y token JWT
│   ├── cotizacion.py       # Cotiza y valida los datos del seguro
│   └── pago.py             # Aplica pago con línea de crédito
└── README.md               # Documentación del proyecto
```

## 🧭 Flujo de Emisión (según la documentación GAPI)

GAPI requiere un proceso transaccional en **3 pasos**, descrito en la página **104** del documento.

### 1. 🔐 Login y token JWT
- Endpoint: `POST /api/security/login`
- Devuelve un token con 5 minutos de validez.
- Obligatorio para toda solicitud posterior.

📄 Ver página 13–14 del documento `API Goval-Web v3.7-1.pdf`

---

### 2. 📥 Cotización
- Endpoint: `POST /api/issue/retail/new`
- Estructura completa del cuerpo:
  - `agency_id`, `salesman_id`, `products`, `from`, `to`, `insured`, `addresses`
- Devuelve: `id` de la cotización (requerido para el siguiente paso)

📄 Ver página 112–113 de la documentación

✔️ Esto valida que la persona pueda ser asegurada, y calcula el precio exacto.

---

### 3. 💳 Aplicación de Pago / Emisión
- Endpoint: `POST /api/issue/retail/apply/{id}/credit`
- Usa el `id` de cotización y lo convierte en un certificado emitido

📄 Ver página 122 de la documentación

✔️ Esto emite la póliza y genera el certificado de seguro.

---

## 🚀 Uso

### Procesamiento Manual

1. **Preparar Excel**: Coloca tu archivo Excel en la carpeta `Exceles/`

2. **Convertir a Emisiones**:
```bash
python -m emisor_goval.utils.excel_to_emisiones
```

3. **Procesar Emisiones**:
```bash
python main.py
```

### Automatización con N8N

El proyecto incluye configuraciones para automatización con N8N y Docker:

```yaml
# docker-compose.yml
version: '3.8'
services:
  n8n:
    image: n8nio/n8n
    ports:
      - "5678:5678"
    environment:
      - N8N_HOST=${N8N_HOST}
      - N8N_PORT=5678
      - N8N_PROTOCOL=https
    volumes:
      - n8n_data:/home/node/.n8n
    depends_on:
      - redis
      - processor

  processor:
    build: ./processor
    environment:
      - REDIS_URL=redis://redis:6379
      - GOVAL_API_URL=${GOVAL_API_URL}
    volumes:
      - ./data:/app/data
    depends_on:
      - redis

  redis:
    image: redis:alpine
    ports:
      - "6379:6379"
    volumes:
      - redis_data:/data

volumes:
  n8n_data:
  redis_data:
```

## 📊 Monitoreo y Logs

El sistema incluye:

- **Logs detallados**: En la carpeta `logs/`
- **Tracking de emisiones**: En `data/tracking/`
- **Estadísticas**: Éxitos y fallos por ejecución
- **Dashboard**: Interfaz web para monitoreo (con N8N)

## 🔧 Configuración

### Variables de Entorno

Crea un archivo `.env` con:

```env
# API Configuration
GOVAL_API_URL=https://humano.goval-tpa.com/api
USUARIO=your_username
PASSWORD=your_password

# N8N Configuration
N8N_HOST=your-domain.com
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=your-email@gmail.com
SMTP_PASS=your-app-password
```

### Configuración de API

Edita `emisor_goval/config.py` para ajustar:

- URLs de la API
- Credenciales
- IDs de agencia, vendedor, producto
- Fechas de vigencia

## 🚨 Solución de Problemas

### Error de Certificado SSL

Si encuentras errores de certificado SSL:

```
SSL: CERTIFICATE_VERIFY_FAILED certificate verify failed: certificate has expired
```

**Solución**: Contactar al equipo de Goval para renovar los certificados SSL.

### Errores de Autenticación

Verificar:
1. Credenciales correctas en `config.py`
2. Token JWT válido
3. Permisos de API

## 📈 Próximas Mejoras

- [ ] Dashboard web completo
- [ ] Notificaciones automáticas
- [ ] Escalado automático
- [ ] Backup automático de datos
- [ ] Integración con más proveedores de email

## 🤝 Contribución

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para detalles.

## 📞 Soporte

Para soporte técnico o preguntas:
- Crear un issue en GitHub
- Contactar al equipo de desarrollo

---

**Nota**: Este sistema está diseñado para uso en producción con la API de Goval. Asegúrate de tener las credenciales y permisos necesarios antes de usar en producción. 