# AI Skills Hub

Biblioteca abierta de Agent Skills propias y catálogo curado de fuentes externas.

## Principios
- Formato estándar `SKILL.md` (https://agentskills.io/specification).
- Las skills externas se enlazan, no se copian ni ejecutan automáticamente.
- Toda incorporación requiere revisión de licencia, instrucciones, scripts y procedencia.
- La instalación de terceros se hace de manera explícita con el CLI de Vercel: https://github.com/vercel-labs/skills.

## Primeros pasos (PowerShell)

```powershell
python .\scripts\validate.py
Get-Content .\catalog.json
npx skills add . --list
```

Para instalar una skill local en el proyecto actual, consultar primero qué detecta la herramienta:

```powershell
npx skills add . --skill code-review
```

> Ejecutá la instalación en el directorio adecuado. El gestor solicita agente y destino; revisá lo seleccionado. No uses flags de instalación indiscriminada.

## Instalar desde fuentes externas (ejemplo)

```powershell
npx skills add coreyhaines31/marketingskills --list
```

Antes de instalar, revisá licencia y contenido del repositorio upstream. Ninguna entrada del catálogo debe considerarse auditada.

## Organización
- `skills/` skills mantenidas aquí.
- `catalog.json` fuentes externas candidatas para evaluación, **no aprobadas automáticamente**.
- `scripts/validate.py` verificador básico sin dependencias externas.
- `docs/ARCHITECTURE.md` decisiones y próximos pasos.
- `.github/workflows/validate.yml` verificación en pull requests.

## Estado
Versión 0.1: base local. Sin servidor, sincronización automática, búsqueda semántica ni ejecución remota.

## Licencias
Las skills propias de este starter se ofrecen bajo MIT (ver `LICENSE`). Cada repositorio externo conserva su licencia y autoría respectivas.
