# poo_python
lesson #9 - Herencia:
El comportamiento de las Superclases se lo podemos heredar a las subclases, e ir generando mayor especialización(gererar jerarquias).

lesson #10 - Polimorfismo:
Es la habilidad de tomar varias formas.

En Python, nos permite cambiar el comportamiento o método de una superclase para adaptarlo a la subclase.

lesson #11 - Introducción a la complejidad algorítmica:
Nos permite comparar la eficiencia en dos diferentes algoritmos. y predecir el tiempo que nos vamos a tardar en resolver un problema.

.-Complejidad temporal vs complejidad espacial
  .- cronometar el tiempo en el que corre un algoritmo.

  .- Contar los pasos con una medida abstracta de operación.

  .- Contar los pasos conforme nos aproximamos al infinito.

lesson #13 - Notación Asintótica:

  .- Conforme se va al infinito.
    .-No Importan las variaciones pequeñas.
    .- Mejor de los casos, promedio, pero de los casos
    .- Big O
    .- Nada mas importa el término de mayor tamaño
    .- Si vemos un Loop: tenemos un crecimiento lineal.
    .- Si tenemos un loop dentro de otro loop: podemos decir que su crecimiento es cuadrático.
    .- Si tenemos una funcion recursiva que genera mas de una llamada recursiva, podemos pensar que tenemos un crecimiento exponencial.

lesson #14 - Clases de complejidad algorítmica:

  .-O(1) Constante. No importa cuanto crece nuestro input se va a tardar lo mismo
  .-O(n) Lineal. Nosotros vamos a Crecer de manera proporcional conforme a crezca el input.
  .-O(log n) Logarítmica: nuestra función crecerá de forma logarítmica con respecto al input. Esto significa que en un inicio crecerá rápido, pero luego se estabilizara.
  .-O(n log n) Log lineal: crecerá de forma logarítmica pero junto con una constante.
  .-O(n²) Polinomial: crecen de forma cuadrática. No son recomendables a menos que el input de datos en pequeño.
  .-O(2^n) Exponencial: crecerá de forma exponencial, por lo que la carga es muy alta. Para nada recomendable en ningún caso, solo para análisis conceptual.
  .-O(n!) Factorial: crece de forma factorial, por lo que al igual que el exponencial su carga es muy alta, por lo que jamas utilizar algoritmos de este tipo.

lesson #15 - Búsqueda Lineal:
  .- Buscar en todos los elementos de manera secuencial.
  .-¿Cuál es el peor caso?
