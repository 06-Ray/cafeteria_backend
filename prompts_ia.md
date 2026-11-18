# para base.html
rol: actua como desarrollador front-end experto en django y bootstrap 5

tarea: crea la primera plantilla base en base.html de este proyecto, con un nav bar, un bloque para mostrar las alertas y otro para el titulo y el contenido del proyecto

contexto: Es una proyecto en django sobre una cafeteria, los modelos padre e hijo son Categoria y Productos, el nav bar debe contener un inicio de sesion por si el usuario no esta autenticado y poder añadir un nuevo producto y tambien cerrar sesion, los estilos propios iran en un archivo estatico, cargando con {% load static %}, no uses javascript, solo bootstrap 5

formato: un unico archivo html completo, si hay comentarios, que sean en español indicando que sirve cada bloque

** asistente utilizado: Claude**
** resultado: la plantilla base para el proyecto **
** modifique: la estructura para que se acople a la estetica de una pagina de cafeteria real **


# para lista_productos.html y producto_eliminado.html
rol: actua como desarrollador front-end experto en django y bootstrap 5

tarea: crearas dos plantillas, lista_productos.html que sirve para ver la lista de los productos en tipo tarjeta y producto_eliminado.html que sirva para confirmar antes de eliminar un producto

contexto: Es una proyecto en django sobre una cafeteria, los modelos padre e hijo son Categoria y Productos, ambas plantillas heredan de base.html
En lista_productos.html obtiene ListView de vista, cada tarjeta muestra la categoria, el nombre, el precio y si se encuentra disponible o no, ademas, solo si el usuario esta autenticado debe verse los botones de editar y eliminar, ademas habra un filtro que permite ver los productos dependiendo lo que diga
En producto_eliminado obtiene DeleteView de vista, debe mostrar el nombre del producto, ademas de pedir la confirmacion con un formulario tipo POST y tener un boton para cancelar en caso de equivocación y poder volver al catagolo que seria lista_productos

formato: Son dos bloques de codigo HTML, uno por archivo, si hay comentarios, que sean en español para entender que realiza cada apartado

** asistente utilizado: Claude**
** resultado: una plantilla para cada archivo simplificados**
** modifique: nada **

# para form_productos.html y detalle_producto.html
rol: actua como desarrollador front-end experto en django y bootstrap 5

tarea: crearas dos plantillas, la de form_productos.html que servira para crear y editar los productos de la cafeteria con los errores de validacion en cada campo, y detalle_producto.html que muestra la ficha completa de cada producto

contexto: Es una proyecto en django sobre una cafeteria, los modelos padre e hijo son Categoria y Productos, ambas plantillas heredan de base.html 
En producto_form obtiene CreateView y UpdateView de vista el titulo debe cambiar entre si es un nuevo producto o se esta editando con "nuevo producto" y "editar producto", debe tener un boton de cancelar en caso de haber error y volver a catalogo que seria lista_productos, los campos que son booleanos debe verse como una checkbox siguiendo el modelo bootstrap para que no se vea muy acoplado en la pantalla
En detalle_producto.html obtiene DetailView y debe mostrar la categoria, el nombre, descripcion, el sku, el precio, estado, el stock disponible y la fecha en que se ingreso, de preferencia con formato (dd/mm/aaaa), ademas solo si el usuario esta autenticado deben poder verse los botones de editar y eliminar y un enlace para volver al catalogo

formato: Son dos bloques de codigo HTML, uno por archivo, si hay comentarios, que sean en español para entender que realiza cada apartado

** asistente utilizado: Claude**
** resultado: una plantilla para cada archivo **
** modifique: nada**

# para el login y registro
rol: actua como desarrollador front-end experto en django y bootstrap 5

tarea: crearas dos plantillas login.html con un formato de inicio de sesion que muestre un mensaje cuando el usuario o la contraseña no sean correctos y registro.html que permita crear a un nuevo usuario

contexto: Es una proyecto en django sobre una cafeteria, los modelos padre e hijo son Categoria y Productos, la plantilla que hereda es base.html, 
El formulario de login.html debe usar el metodo POST tener los campos de usuario y contraseña, los estilos propios estan en un archivo estatico, ademas debe tener estetica acorde a una cafeteria.
El formulario de registro.html obtiene CreateView para utilizar RegistroForm y usar UserCreationForm, asi trae los campos de usuario y contraseña, igual utilizara el metodo POST, tendra boton para registrar y la estetica seguira acorde a la cafeteria

formato: dos bloques de codigo html , si hay comentarios, que sean en español

** asistente utilizado: Claude**
** resultado: plantilla para el login acorde a estetica y rgistro**
** modifique: nada **

# al final borre la plantilla de registro, porque se me dificulto realizarlo, pero ese es el prompt original, ya que solo utilice la de login