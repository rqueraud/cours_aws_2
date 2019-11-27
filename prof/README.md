# Guide pour la création de l'environnement prof

## Création de service de distribution des tweets

* Lancer une t2.micro

```bash
chmod 400 /mnt/b383629e-82f3-42a2-af83-c6e7461db587/Inseec/2019_2020/rqueraud_inseec.pem
ssh -i /mnt/b383629e-82f3-42a2-af83-c6e7461db587/Inseec/2019_2020/rqueraud_inseec.pem ubuntu@52.213.154.80

sudo apt-get update && sudo apt-get upgrade -y
sudo apt-get install -y python3-pip

pip3 install flask flask_restful

git clone https://github.com/rqueraud/cours_aws_2
cd cours_aws_2/prof
# python3 service.py
nohup python3 service.py &  # Runs persistently even after leaving ssh
```

* Ouvrir le port 5002 sur l'instance.
