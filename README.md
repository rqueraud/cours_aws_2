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

```

Vous pouvez maintenant accéder à l'interface web de jupyter depuis votre navigateur à l'adresse : http://IP-DE-VOTRE-INSTANCE:8888. Puis ouvrir le fichier *python-training-cours-2.ipynb* depuis l'interface jupyter.

## Partie 1 : Exercices de Python

Jupyter propose une interface où le code s'execute dans des cellules. Vous pouvez executer les cellules une à une ou tout executer en même temps.  
Attention cependant, car l'environnement python est conservé entre les différentes cellules. Une variable définie dans une cellule est donc accessible depuis une autre cellule.

Résolvez les problèmes du notebook en vous aidant des notions vues dans le *Problème 0*.

** Partie 2 : 