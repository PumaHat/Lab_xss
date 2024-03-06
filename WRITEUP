# Write-up

Este laboratorio tiene dos niveles de dificultad: una versión simple y una difícil.

## Laboratorio XSS simple

El código HTML de la pantalla principal sin ningún comentario es el siguiente:

![](/docs/1.png)

Una vez que hacemos un comentario, se puede observar la estructura, la cual consiste en una etiqueta contenedora `<div>` con un id y un atributo `style` para el color, una etiqueta `<h3>` para el nombre, una etiqueta `<time>` para la hora y fecha y finalmente una etiqueta `<p> para el comentario.

![](/docs/2.png)

Al hacer un comentario con sintaxis HTML, podemos observar que los caracteres especiales no se escapan, es decir, si yo comento `<h1>Comentario grande</h1>`, el navegador lo interpreta como código HTML y lo escribe como se observa a continuación:

![](/docs/3.png)

Ya que sabemos que en la sección de comentarios podemos inyectar código HTML, generamos un script con una etiqueta `<div>` indicando con el atributo `style` todos los estilos que van a imposibilitar la página: de `width` y `height` tendrá el 100% del marco del navegador, fondo negro y el contenido “phct” con letras blancas y centrado. Con `position: fixed; top: 0; left:0;` se indica que el div estará fijado en la página y que debe empezar desde arriba en 0 y desde la izquierda en 0 para abarcar todo.

![](/docs/4.png)

De esta forma habremos cumplido con el objetivo, el resultado del comentario es el siguiente:

![](/docs/5.png)

## Laboratorio XSS difícil
En el segundo laboratorio, cuando intentamos inyectar código HTML, se puede observar que en este caso sí se escapan los caracteres especiales, por lo tanto, ya no lo tomará como una etiqueta HTML sino como texto.

![](/docs/6.png)

Las posibles entradas de datos a simple vista son el campo de nombre y comentarios, pero ninguno de estos es vulnerable a ataques XSS, por otro lado, existe otro input (el de color).

![](/docs/7.png)

Considerando que todos los inputs son de tipo “text”, envían al final sus datos como texto, y que los otros tipos se han desarrollado para adaptar la forma en la que el navegador los renderiza, podemos cambiar el tipo del input por `text` y de esta forma es más fácil observar la representación textual de los colores, que es su valor hexadecimal.

![](/docs/8.png)

Este valor en hexadecimal forma parte de cada comentario, para colorear el borde izquierdo, por lo tanto, podemos insertar el color (o no agregar nada), cerrar la etiqueta y escribir lo que sea después. En este caso, el código es casi igual al anterior a excepción del principio:

```html
#808000;"><div style="background: black; width: 100vw; height: 100vh; color: white; display: flex; justify-content: center; align-items: center; position: fixed; top: 0; left: 0; z-index: 1000">phct</div>
```

Cabe mencionar que si empezamos directamente escribiendo la etiqueta `<div>`, se escribirá todo en el atributo `style` del `<div>` del mensaje . Por lo tanto, debemos empezar cerrando la etiqueta anterior.

Finalmente, llegamos a nuestro objetivo, que era inutilizar la página.

![](/docs/9.png)
