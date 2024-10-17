from graphviz import Digraph
import os

# Crear un nuevo gráfico dirigido
dot = Digraph(comment='AMISR Processing Flow')

# Ajustes generales del gráfico
dot.attr(rankdir='TB', splines='ortho', bgcolor='lightgray', concentrate='true')

# Nodo principal
dot.node('A', 'AMISRReader\n(5 canales de lectura)', shape='box', style='filled', color='lightblue', fontcolor='black')

# Procesos
dot.node('B', 'VoltageProc\n(6 Integraciones coherentes)', shape='box', style='filled', color='lightgreen', fontcolor='black')
dot.node('C', 'SpectraProc\n(FFT de 256 puntos, Remoción de DC,\n10 Integraciones Incoherentes)', shape='box', style='filled', color='lightcoral', fontcolor='black')
dot.node('D', 'ParametersProc\n(SpectralMoments y WindsProfiler)', shape='box', style='filled', color='lightyellow', fontcolor='black')

# Nuevos nodos para las salidas de ParametersProc
dot.node('E', 'Grabado de momentos espectrales', shape='ellipse', style='filled', color='lightblue', fontcolor='black')
dot.node('F', 'Gráfico de vientos', shape='ellipse', style='filled', color='lightblue', fontcolor='black')

# Conexiones
dot.edge('A', 'B', label='Salida a', color='black')
dot.edge('B', 'C', label='Salida a', color='black')
dot.edge('C', 'D', label='Salida a', color='black')

# Conexiones para las salidas del bloque ParametersProc
dot.edge('D', 'E', label='Salida a', color='black')
dot.edge('D', 'F', label='Salida a', color='black')

# Nombre del archivo de salida (se guardará en el directorio actual)
output_filename = os.path.join(os.getcwd(), 'amisr_processing_flow_centered_colored')

# Guardar y renderizar la imagen en formato PNG
dot.render(output_filename, format='png', cleanup=True)

print(f"Diagrama centrado y coloreado guardado en: {output_filename}.png")
