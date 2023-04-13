from cx_Freeze import setup, Executable

setup(name='Nombre de la aplicación',
      version='0.1',
      description='Descripción de la aplicación',
      executables=[Executable('server.py')])