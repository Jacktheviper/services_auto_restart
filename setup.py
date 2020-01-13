from cx_Freeze import setup, Executable
base = None

executables = [Executable("services_auto_restart.py", base=base)]

setup(
    name = "Services Auto Restarter",
    version = "1.0",
    description = 'Permet de redémarrer les services en auto qui sont arrêtés.',
    executables = executables
)