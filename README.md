# INSEEC - TP2: AWS

Objectifs de ce cours : 
* S'exercer à python avec une suite d'exercices sur un notebook jupyter
* Utiliser les services AWS pour créer une chaîne de traitement de l'information

## Partie 0 : Rallumer son instance et accéder au notebook jupyter

Le notebook jupyter sera executé sur une instance EC2 sur AWS. Suivant votre avancée au dernier TP, vous pouvez :

* Si vous aviez un environnement fonctionnel : 
    * Redémarrez votre instance EC2. Pour rappel, allez sur http://console.aws.amazon.com, dans le service EC2, puis faites un clic-droit sur votre instance et *Instance State -> Start*.
* Si vous n'aviez pas d'environnement fonctionnel :
    * Allez sur http://console.aws.amazon.com puis choisissez le service EC2.
    * Selectionnez AMIs dans le menu de gauche. Les AMIs sont des images d'instances, c'est à dire que l'on a conservé uniquement le disque dur et qu'il n'est pour le moment rattaché à aucune instance.
    * Clic-droit sur l'AMI `rqueraud-jupyter-notebook` et *Launch*.
    * Selectionnez le type `t2.micro` puis *Review and Launch*.
    * Prenez le temps d'observer ce qui a été selectionné  dans le recapitulatif et cliquez sur *Launch*.
    * Selectionnez votre *key-pair* existant et cliquez sur *Launch Instances*.
    * Vous pouvez retrouver votre instance en train de démarrer en cliquant dans le menu de gauche *Instances*.
    * Suivez la Partie 5 du TP précédent (https://github.com/rqueraud/cours_aws_1#partie-2--ssh-avec-bitvise) pour autoriser l'accès à l'interface web de jupyter.

Connectez-vous en SSH à votre instance :
* Pour windows, voir la partie 2 du TP précédent : https://github.com/rqueraud/cours_aws_1#partie-2--ssh-avec-bitvise
* Pour mac, entrez la commande suivante dans votre terminal

```bash
# Commande pour se connecter en SSH depuis un Mac
ssh -i /chemin/vers/votre/cle ubuntu@IP-DE-VOTRE-INSTANCE
```

Une fois sur l'instance, récupérez le sujet de TP à l'url https://raw.githubusercontent.com/rqueraud/cours_aws_2/master/python-training-cours-2.ipynb grâce à la commande `wget` :

```bash
# Commande pour télécharger un fichier depuis une url
wget URL-DU-FICHIER-A-TELECHARGER
```

Relancez le service jupyter-notebook avec la commande :

```bash
# Commande pour lancer le service jupyter-notebook
jupyter-notebook
```

Vous pouvez maintenant accéder à l'interface web de jupyter depuis votre navigateur à l'adresse : http://IP-DE-VOTRE-INSTANCE:8888, mot de passe `a`. Puis ouvrir le fichier *python-training-cours-2.ipynb* depuis l'interface jupyter. 

*Note: Si vous avez un warning à l'ouverture du notebook indiquant des problèmes d'incompatibilité, vous pouvez l'ignorer. Ceci provient du fait que j'ai utilisé un outil différent pour créer ce notebook.*

## Partie 1 : Exercices de Python

Jupyter propose une interface où le code s'execute dans des cellules. Vous pouvez executer les cellules une à une ou tout executer en même temps.  
Attention cependant, car l'environnement python est conservé entre les différentes cellules. Une variable définie dans une cellule est donc accessible depuis une autre cellule.

Résolvez les problèmes du notebook en vous aidant des notions vues dans le *Problème 0*.

## Partie 2 : Création du Bucket S3

S3 est le service de stockage d'AWS.

Allez sur la page du service S3 et créez un nouveau bucket à votre nom en laissant tous les autres paramètres par défaut.

## Partie 3 : Le service Lambda

Lambda est un service de functions (FaaS), permettant d'executer du code court sans se soucier de l'environnement.

Nous disposons déjà d'un service sur une autre instance EC2 qui expose un nouveau tweet toutes les secondes. L'objectif de cette étape va être de récupérer ces tweets à intervalles réguliers et de les enregistrer sur S3.

Les étapes initiales sont :
* Depuis la console AWS, allez sur la page du service Lambda et créez une nouvelle fonction.
* Selectionnez Author from scratch, puis entrez un nom pour votre fonction (contenant votre prénom pour vous différencier des autres) et choisissez le langage Python 3.7.

Vous arrivez sur la page de développement de votre fonction lambda où vous pourrez écrire votre code.  
A noter: Vous pouvez simuler une execution en cliquant sur *Test* en haut de la fenêtre. Vous aurez besoin pour tester de créer un *test event* vide car nous n'aurons pas d'inputs à notre fonction.