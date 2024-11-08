# Les IO

## Qu'est-ce que sont les IO?

IO signifie **input/output**.  
C'est le terme utilisé pour décrire, par exemple, les opérations sur des fichiers, la lecture du clavier, ou l'affichage d'éléments à l'écran. Globalement, ce sont les informations que demande un programme et celles qu'il nous rend.  

Les deux opérations possibles sur un fichier sont lire *(read)* et écrire *(write)*.  
⚠️ Ce n'est pas possible de **lire** un fichier et d'**écrire** dessus en même temps.  


## Les fichiers en Python

### Ouvrir un fichier

Pour ouvrir un fichier en Python, il faut utiliser la fonction de base `open`.
```py
file = open("file_path")
```
Cette fonction prend en paramètre le **chemin d'accès du fichier** et le **mode d'accès** *(facultatif)*.

Le **chemin d'accès du fichier** est constitué par tous les sous-dossiers du fichier suivi du nom du fichier.  
*Exemple: C:/users/username/bureau/mon_pdf.pdf*

Le **mode d'accès** est une seule lettre indiquant comment ouvrir le fichier.  
Ces modes sont:
* `r`: read *(seulement lire le fichier)*
* `w`: write *(seulement écrire le fichier)*
* `x`: create *(crée un fichier et écrit ce fichier)* ⚠️ Si le fichier existe déjà, Python met une erreur. Pour éviter d'obtenir une erreur, le mode `w` crée aussi le fichier sans mettre d'erreur.

D'autres modes sont disponibles, mais nous n'utiliseront que ces trois modes.

### Lecture

Pour **lire** un fichier, il faut utiliser la méthode `read`.
```py
file = open("file_path", "r")
file_content = file.read()
```
```py
>>> print(file_content)
# (le contenu du fichier s'affiche)
```
Erreurs possibles:
- `FileNotFoundError` : Le chemin d'accès donné est invalide
- `UnicodeDecodeError` : Le fichier à lire contient des caractères que Python ne peut pas lire. *(émojis principalement)*
- `io.UnsupportedOperation` : Le fichier à lire a été ouvert avec le mode `w` *(écrire)*

Il y a aussi d'autres méthodes pour lire un fichier:
- `read` *(décrit ci-dessus)*
- `readline` : lit seulement la première ligne
- `readlines` : retourne une liste contenant chaque ligne

*Les fonctions `read` et `readlines` acceptent un nombre comme paramètre, spécifiant le nombre de caractères à lire.*

**Point de passage: ouvrir un fichier.**

Télécharge le fichier `fichier.txt` avec ce lien: [github.com/Supertolek/club-dev/blob/main/fichier.txt](https://github.com/Supertolek/club-dev/blob/main/fichier.txt).  
Crée un fichier python dans le même dossier que `fichier.txt` et ouvre le avec n'importe quel éditeur de code *(vs code ou vs code, au choix)*.  
Ensuite, à toi de jouer! **Tu dois afficher son contenu uniquement avec python**.

### Écriture

Pour **écrire** un fichier, il faut utiliser la méthode `write`.
```py
file = open("file_path", "w")
file.write("(contenu du fichier)")
```

Erreurs possibles:
- `FileExistsError` : Apparait lorsque le mode `x` est spécifié, et que le fichier à créer existe déjà.
- `io.UnsupportedOperation` : Le fichier à écrire a été ouvert avec le mode `r` *(lire)*

Il y a aussi d'autres méthodes pour écrire un fichier:
- `write` *(décrit ci-dessus)*
- `writelines` : écrit le contenu d'une liste *(chaque élément est écrit dans une nouvelle ligne)*

**Point de passage: écrire un fichier.**

Dans le même fichier python que tout à l'heure, modifie le code pour écrire dans le fichier une autre phrase.

## Les formats de fichier

Le format d'un fichier est indiqué par son **extension**.  
Chaque format de fichier a sa propre utilité.

En voici quelques-uns:
- `*.txt` : un fichier texte classique
- `*.json` : un fichier json *(**J**ava**S**cript **O**bject **N**otation)*. Permet de représenter et d'enregistrer facilement le contenu de variables.
- `*.xml` : identique à `*.xaml` ou `*.html` etc... Permet de représenter une liste d'objets ayant chacun des propriétés et d'autres objets.
- `*.yml` : identique à `*.yaml`. Permet de représenter une liste d'éléments simples (seulement du texte) de manière compacte.

Les exemples ci-dessus sont **lisibles** par Python *(mais Python ne comprends pas leur contenu)*.  
Pour que Python puisse les comprendre, il faut utiliser des **modules**.

`json` a un module intégré dans Python *(il n'y a pas besoin de le télécharger, comme `random`).*. C'est aussi le plus simple, et c'est certainement le seul format de fichier que nous allons utiliser.

*Les formats de fichier ci-dessus sont tous des fichiers texte, donc tous lisibles par word, vs code ou bloc note.*

## json

Pour lire des fichiers `json`, il faudra en premier temps importer le module.
```py
import json
```
Le module `json` a lui aussi des fonctions pour lire et écrire.

*Le module json est un **parser**, c'est-à-dire qu'il permet de comprendre du texte.*

Le `json` s'écrit comme un dictionnaire Python. Il accepte les nombres, le texte, les booléens, les listes et les dictionnaires.
```json
{
    "nombre": 1.0,
    "texte": "texte",
    "booléen": true
}
```
⚠️ Les booléens s'écrivent entièrement en majuscule *(comme en JavaScript)*, contrairement à Python.

### Lecture

Pour lire un fichier `json`, il faut utiliser la fonction `load`.
```py
import json
file = open("file_path", "r")
data = json.load(file)
```
```py
>>> print(data)
# Le contenu du fichier json
```
La variable `data` contient le contenu du fichier `json`.

Le module `json` possède aussi la fonction `loads`, qui comprends du json sous forme de texte.
```py
import json
file = open("file_path", "r")
data = json.loads(file.read())
```
```py
>>> print(data)
# Le contenu du fichier json
```

**Point de passage: lire un fichier `json`.**

Télécharge le fichier `data.json` avec ce lien: [github.com/Supertolek/club-dev/blob/main/data.json](https://github.com/Supertolek/club-dev/blob/main/data.json).  
Crée un fichier python dans le même dossier que `data.json` et ouvre le avec n'importe quel éditeur de code *(vs code ou vs code, au choix)*.  
Ensuite, à toi de jouer! **Tu dois afficher son contenu uniquement avec python**.

### Écriture

Pour écrire un fichier `json`, il faut utiliser la fonction `dump`.
```py
import json
file = open("file_path", "w")
data = {"nombre": 1.0}
json.dump(data, file)
```
Ce code écrit le contenu de la variable `data` dans le fichier.

Le module `json` possède aussi la fonction `dumps`, qui retourne le json sous forme de texte.
```py
import json
data = {"nombre": 1.0}
json_content = json.dumps(data, file)
```
```py
>>> json_content
"{'nombre': 1.0}"
```

**Point de passage: écrire un fichier `json`.**

Dans le même fichier python que tout à l'heure, modifie ton programme pour enregistrer un autre dictionnaire dans `data.json`.

## Les IO et le texte

### Lecture

Je pense que vous connaissez déjà la fonction `input`, qui demande à l'utilisateur une valeur.  
Cette fonction est interprétée différemment selon le logiciel, mais, en général, elle affiche un message dans le terminal et permet à l'utilisateur d'écrire ce qu'il veut.
```py
valeur = input("Quel est votre nom?")
```
```py
Quel est votre nom?
>>> print(valeur)
# Affiche ce que l'utilisateur a entré
```
Cependant, cette fonction a beaucoup de limitation. Notamment, il n'est pas possible de lire en temps réel les touches préssées.

### Lecture avec pygame

Pour lire les touches pressées par l'utilisateur avec pygame, il faut tout d'abord créer une fenêtre. Pour l'instant, je vais directement donner toute cette partie du code, disponible sur Github.
```py
import pygame

pygame.init()

running = True
while running:
    for event in pygame.event.get():
        if event.type = pygame.
```

## Autre format : xml

Nous n'allons pas utiliser ce format de fichier, mais c'est toujours intéressant.  
Le `xml` est un langage de **balisage**, c'est-à-dire qu'il ordonne des données à l'aide de balises.

Les balises ont un nom, et peuvent avoir un contenu et des attributs. elles doivent commencer par des parenthèses ouvrantes et se fermer par des parenthèses fermantes.
```xml
<option valid="false">Un langage de programmation</option>
```
Dans cet exemple, il y a une balise dont le nom est `option`, dont le contenu est `Un langage de programmation` et qui possède l'attribut `valid` avec la valeur `false`.

Des éléments `xml` peuvent s'imbriquer, formant ainsi une structure d'arbre.
```xml
<quizz>
    <quizz_question type="choix_multiples" question="Qu'est-ce que HTML?">
        <option valid="false">Un langage de programmation</option>
        <option valid="true">Un langage de balisage</option>
        <option valid="false">Un plat Italien</option>
    </quizz_question>
</quizz>
```

## Lecture

Le module `xml` inclus dans python de base permet de comprendre ce langage (c'est un **parser**).  
Il faut premièrement l'importer. Le module possède 
```py
```