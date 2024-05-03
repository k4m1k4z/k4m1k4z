# Welcome to github repository of Fran Ruiz - k4m1K4z3!

![Captura2](https://github.com/k4m1k4z/k4m1k4z/assets/153621827/05cb33b3-aee4-4beb-b4de-7582e4315b05)


### Hola Mundo! Hello everyone! 👋

# RETO - PRIMEROS PASOS CON GIT

## **1.-Crea un repositorio nuevo que se llame retogit.**

<p> Accedemos a www.github.com, hacemos login con nuestra cuenta de usuario y una vez estamos en la página principal, hacemos clic en “NEW”. Después, tendremos que rellenar “repository name” y demás campos que reflejan las características que va a tener nuestro nuevo repositorio. Va a ser privado, y añadimos el “Readme”.</p>

![cap1](IMG/retogit-1.jpg)

## **2.-Realiza la subida de la carpeta src de un proyecto en java.**

<p>Para ello accedemos a nuestro repositorio y hacemos clic en ADD FILE y luego a “upload files”.Arrastramos la carpeta y añadimos una descripción corta en “Commit changes” , dejamos cliqueada la opción “  Commit directly to the main branch. “ y le damos a “Commit”</p>

![cap2](IMG/retogit-2.jpg)

## **3.-Crea una nueva rama que se llame desarrolloPersona.**

<p>Hacemos clic en “Branch” y damos a “Create New Branch”. Ponemos el nombre y dejamos como “source” la rama principal que es “main”. Despues, damos a Create New Branch</p>

![cap3](IMG/retogit-3.jpg)

## **4.-Descarga el contenido de la rama a tu repositorio local.**

<p>Para descargarlo, puedes clonarlo con “clone” y obtendrás los mismos archivos en tu carpeta de GitHub del PC o en el directorio indicado por defecto. Luego puedes ver si el contenido es idéntico viendo el Preview Pull Request, y de haber actualizaciones, se podría hacer un pull para traernos las nuevas actualizaciones.</p>

![cap4](IMG/retogit-4.jpg)

## **5.-Crea una clase nueva y realiza la actualización de la rama en el repositorio, documenta este proceso con el comentario “Nueva clase – nombre de la clase”.**

<p>Creo una nueva clase “puesto” dentro del proyecto retogit y dentro creo el atributo “nombre”.Después, cliqueo en “commit” que es como mi declaración de intenciones de que yo quiero actualizar algo.</p>

![cap5-a](IMG/retogit-5-A.jpg)

<p>Por ultimo, para “lanzar” los cambios a nuestro repositorio de GitHub, tenemos que darle a Push: ( push commits to the origin remote )</p>

![cap5-b](IMG/retogit-5-B.jpg)

<p>Y ahora, al acceder a nuestro nuevo repositorio, encontramos ya la nueva clase creada y en el titulo el nombre que hemos puesto antes de lanzar el commit:</p>

![cap5-c](IMG/retogit-5-C.jpg)

## **6.-Modifica algún atributo de la clase nueva y realiza la actualización de la rama en el repositorio, documenta este proceso con el comentario “Edición clase – nombre de la clase”.**

<p>Accedemos al Intellij y modificamos el atributo. Cambio el valor del atributo de  “Administrativo” a “Enfermero” y  hacemos el Commit y después el Push origin</p>

![cap6](IMG/retogit-6.jpg)

<p> Al acceder al repositorio en GitHub ya vemos que hay un push reciente realizado y para confirmar que está guardado el cambio accedemos a la clase nueva y vemos que el valor del atributo se ha cambiado, verificando que está Enfermero:</p>

![cap6-b](IMG/retogit-6-B.jpg)

## **7.-Realiza una comprobación de los cambios.**

<p>Este punto lo he ido haciendo mientras hacia los ejercicios para comprobar los cambios. Sin embargo, también si hacemos clic en pull request, aquí vemos los cambios realizados, los commits hechos e incluso el tiempo en el que se ha lanzado el commit con el cambio:</p>

![cap7](IMG/retogit-7.jpg)

<p>Y si lo queremos ver desde GitHub Desktop podemos verlo en el histórico:</p>

![cap7-c](IMG/retogit-7-B.jpg)

<p>Y si lo queremos ver directamente en el archivo afectado, accedemos directamente a él en Github y en Code y Blame podemos ver los cambios que han tenido:</p>

![cap7-c](IMG/retogit-7-C.jpg)

## **8.-Fusiona la rama “desarrolloPersona” con la rama principal “main”.**

<p>Hacemos un “Create Push Request” y luego damos a “Merge pull request”</p>

![cap8](IMG/retogit-8-A.jpg)

![cap8](IMG/retogit-8-B.jpg)

<p>Y ya tendría en mi rama Main el proyecto principal con todas las modificaciones que he hecho</p>

![cap8](IMG/retogit-8-C.jpg)

# **Ayuda con los terminos de operaciones básicas con GitHub**

Las funciones más importantes de GD son:

#### **1.	Clone (Clonar):**

<p>Clona un repositorio remoto en tu máquina local. Este comando crea una copia exacta del repositorio, incluyendo todas las ramas y el historial de commits. Puedes clonar un repositorio desde la interfaz web de GitHub o usando la URL del repositorio en tu terminal.</p>

#### **2.	Pull (Tirar):**

<p>Descarga los cambios desde un repositorio remoto y los incorpora en tu rama local. Puedes hacer un pull desde la interfaz web de GitHub o utilizando el comando git pull en tu terminal.</p>

### **3.	Push (Empujar):**

<p>Sube tus cambios locales al repositorio remoto. Puedes hacer un push desde la interfaz web de GitHub o utilizando el comando git push en tu terminal.</p>

### **4.	Commit:**

<p>Guarda los cambios realizados en los archivos de tu repositorio. Cada commit tiene un mensaje asociado que describe los cambios realizados. Puedes realizar commits desde la interfaz web de GitHub o utilizando el comando git commit en tu terminal.</p>

### **5.	Fetch (Recuperar):**

<p>Descarga todos los cambios del repositorio remoto a tu repositorio local, pero no los incorpora automáticamente en tu rama actual. Se puede hacer un fetch desde la interfaz web de GitHub o utilizando el comando git fetch en tu terminal.</p>

### **6.	Merge (Fusionar):**

<p>Combina los cambios de una rama en otra rama. Por ejemplo, puedes fusionar una rama de desarrollo en una rama principal como main o master. Se puede hacer un merge desde la interfaz web de GitHub o utilizando el comando git merge en tu terminal.</p>

### **7.	Branch (Rama):**

<p>Permite trabajar en paralelo en diferentes líneas de desarrollo. Cada rama puede contener cambios independientes.Puedes crear, eliminar y administrar ramas desde la interfaz web de GitHub o utilizando el comando git branch en tu terminal.</p>

### **8.	Pull Request (Solicitud de extracción):**

<p< Una solicitud de extracción es una forma de proponer cambios en un repositorio. Permite a otros revisar los cambios antes de fusionarlos en la rama principal. Se puede crear desde la interfaz web de GitHub.</p>








<!--
**k4m1k4z/k4m1k4z** is a ✨ _special_ ✨ repository because its `README.md` (this file) appears on your GitHub profile.

Here are some ideas to get you started:

- 🔭 I’m currently working on ...
- 🌱 I’m currently learning ...
- 👯 I’m looking to collaborate on ...
- 🤔 I’m looking for help with ...
- 💬 Ask me about ...
- 📫 How to reach me: ...
- 😄 Pronouns: ...
- ⚡ Fun fact: ...
-->
