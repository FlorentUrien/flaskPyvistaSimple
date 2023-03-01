# Mode d'emploi
## 1. But

C'est de réaliser une application très simple utilisant Pyvista au niveau d'un serveur pour calculer des objets simples. Ces derniers seront ensuite "pris en photo" par pyvista puis transmis au client dans une page html.

Cela marche sans problème en lançant la ligne de code :

```batch
(venv) PS C:\Users\florent.urien\PycharmProjects\flaskPyvistaSimple> python -m main
```

![Alt text](./static/images/capture.PNG?raw=true "Lancement IHM")

Il va falloir lui rajouter la possibilité de fonctionner dans un conteneur docker, ce qui n'est pas forcément si trivial qu'il y parait.
