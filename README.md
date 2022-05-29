# Sistema de recomendaciones Life

El target de este proyecto fue construir un modelo de recomendaciones enfocado a Cursos Extracurriculares de una Universidad para que los alumnos puedan tener una mejor idea de las actividades que les podrían gustar basado en sus elecciones anteriores. 
Para este modelo se usaron las herramientas de Microsoft Azure Machine Learning Studio, el cuál nos permitió construir un pipeline para limpieza de datos, entrenamiento y deployment de todo el sistema.

Pasos para obtener el set de datos final:

--- Cargar los datasets necesarios en el datastore de Azureml studio. (Los nombres de los archivos vienen especificados en la documentación.
--- Guardar el notebook limpieza.ipynb y el script helper_functions.py en la sección Notebooks de Azureml Studio.
--- Correr el notebook y esperar a que se genere el dataset final.

Para correr el modelo es necesario seguir los pasos de la documentación 'Sistema de recomendaciones 2022.pdf', donde podremos encontrar la forma de configurar el espacio de trabajo de Azureml, construir el modelo y el deployment del mismo.
