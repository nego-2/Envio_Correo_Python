# Envio_Correo_Python


Servidor SMTP: Se cambió de smtp.gmail.com a smtp.office365.com que es el servidor SMTP de Outlook.
Puerto SMTP: El puerto sigue siendo 587, que es el adecuado para Outlook y otros proveedores que usan TLS.
Credenciales de Outlook: Cambié la variable mi_correo para usar tu correo de Outlook y dejé un comentario para que pongas tu contraseña en mi_pass.

Sí aparece error: SMTPAuthenticationError: (535, b'5.7.139 Authentication unsuccessful, basic authentication is disabled), indica que la autenticación básica está deshabilitada en tu cuenta de Outlook.

Este es un mecanismo de seguridad de Microsoft, que bloquea los intentos de inicio de sesión usando autenticación básica, es decir, solo con la dirección de correo y contraseña. Microsoft requiere una autenticación moderna que generalmente usa OAuth o contraseñas de aplicación.

Pasos a seguir para solucionar el problema:
1. Generar una contraseña de aplicación (si tienes activada la autenticación en dos pasos)
Si tienes habilitada la autenticación en dos pasos, necesitarás una contraseña de aplicación especial para usarla en el script en lugar de tu contraseña habitual. Aquí están los pasos para obtenerla:

Iniciar sesión en tu cuenta de Outlook:
Ve a https://account.microsoft.com e inicia sesión.

Activar la autenticación en dos pasos (si no lo has hecho ya):
Si no la has activado, ve a la sección Seguridad y activa la autenticación en dos pasos.

Generar una contraseña de aplicación:
Una vez activada la autenticación en dos pasos, ve a Contraseñas de aplicación y genera una contraseña de aplicación específica.

Usar esta contraseña en el código:
En lugar de usar tu contraseña normal (mi_pass), usa la contraseña de aplicación que generaste.

2. Habilitar el acceso a aplicaciones menos seguras
Si no tienes habilitada la autenticación en dos pasos o prefieres no usar contraseñas de aplicación, puede que debas habilitar el acceso a aplicaciones menos seguras (aunque Microsoft está limitando esta opción). Si decides ir por este camino, sigue estos pasos:

Accede a la configuración de seguridad de tu cuenta de Microsoft:
Ve a https://account.microsoft.com/security y, en la sección de Seguridad avanzada, busca una opción que te permita habilitar el acceso a aplicaciones menos seguras.
3. Usar una biblioteca que maneje la autenticación moderna (OAuth)
Otra opción, si los métodos anteriores no funcionan, es utilizar una biblioteca como MSAL (Microsoft Authentication Library) para manejar la autenticación moderna con OAuth. Este enfoque es más complejo, pero es más seguro y recomendado para acceder a los servicios de Microsoft de forma programática.
