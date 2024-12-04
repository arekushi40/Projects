
import socket
import os
from _thread import *
ClientSocket = None
host = '127.0.0.1'
port = 9090
myNumber = 0
def main():
    ClientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ClientSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    try:
        ClientSocket.connect((host, port))
    except socket.error as e:
        print(str(e))
    finally:
        print("connected to Server !")
        myNumber = int(ClientSocket.recv(1024))
        print("myNumber client received : ", myNumber)
    start_new_thread(threaded_server, (ClientSocket, myNumber))

    a=1

    while a == 1:

        login=input("Entre le nom d'utilisateur|le mot de passe (ex: azerty|uiop) : ")
        ClientSocket.send(login.encode())
        reponse = ClientSocket.recv(1024)
        print(reponse)
        if reponse == "nok":
            break
        else:
            a=0

    while True:
        print("Requêtes possibles : \n1. Créer une promotion \n2. Créer un étudiant \n3. Ajouter une note \n4. Calculer la moyenne d'un élève \n5. Calculer la moyenne d'une promotion \n6. Afficher une promotion \n9. Quitter")
        requete=input("entrez la requete : ")


        if requete== "1":
            
            nom_prom = input("Nom de la promo : ")
            # Créer une commande d'ajout d'étudiant
            commande = f"Promo|{nom_prom}"

            # Envoyer la commande au serveur
            ClientSocket.send(commande.encode())
            # Attendre la réponse du serveur (vous devrez implémenter cette partie)
            reponse = ClientSocket.recv(1024)
            print(reponse.decode())
        

        elif requete== "2":
            
            nom_prom = input("Nom de la promo : ")
            nom_etud = input("Nom de l'étudiant : ")
            prenom_etud = input("Prénom de l'étudiant : ")
            notes = input("rentrez les notes,coef puis espacées(ex : 17/8;19/6):")

            # Créer une commande d'ajout d'étudiant
            commande = f"AjoutEtud|{nom_prom}|{nom_etud}|{prenom_etud}|{notes}"

            # Envoyer la commande au serveur
            ClientSocket.send(commande.encode())
            # Attendre la réponse du serveur (vous devrez implémenter cette partie)
            reponse = ClientSocket.recv(1024)
            print(reponse.decode())

        elif requete== "3":
            
            nom_prom = input("Nom de la promo : ")
            nom_etud = input("Nom de l'étudiant : ")
            notes = input("rentrez les notes,coef puis espacées(ex : 17/8;19/6):")

            # Créer une commande d'ajout d'étudiant
            commande = f"AjoutNotesProm|{nom_prom}|{nom_etud}|{notes}"

            # Envoyer la commande au serveur
            ClientSocket.send(commande.encode())
            # Attendre la réponse du serveur (vous devrez implémenter cette partie)
            reponse = ClientSocket.recv(1024)
            print(reponse.decode())

        elif requete== "4":
            
            nom_prom = input("Nom de la promo : ")
            nom_etud = input("Nom de l'étudiant : ")

            # Créer une commande d'ajout d'étudiant
            commande = f"Moyenneetudprom|{nom_prom}|{nom_etud}"

            # Envoyer la commande au serveur
            ClientSocket.send(commande.encode())
            # Attendre la réponse du serveur (vous devrez implémenter cette partie)
            reponse = ClientSocket.recv(1024)
            print(reponse.decode())


        elif requete== "5":
            
            nom_prom = input("Nom de la promo : ")

            # Créer une commande d'ajout d'étudiant
            commande = f"Moyenneprom|{nom_prom}"

            # Envoyer la commande au serveur
            ClientSocket.send(commande.encode())
            # Attendre la réponse du serveur (vous devrez implémenter cette partie)
            reponse = ClientSocket.recv(1024)
            print(reponse.decode())

        elif requete== "6":
            
            nom_prom = input("Nom de la promo : ")

            # Créer une commande d'ajout d'étudiant
            commande = f"AffichageProm|{nom_prom}"

            # Envoyer la commande au serveur
            ClientSocket.send(commande.encode())
            # Attendre la réponse du serveur (vous devrez implémenter cette partie)
            reponse = ClientSocket.recv(1024)
            print(reponse.decode())


        elif requete=="9":
            break

        else :
            break


"""        if requete== "1":
            
            nom_etud = input("Nom de l'étudiant : ")
            prenom_etud = input("Prénom de l'étudiant : ")
            notes = input("rentrez les notes,coef puis espacées(ex : 17/8;19/6):")

            # Créer une commande d'ajout d'étudiant
            commande = f"Etudiant|{nom_etud}|{prenom_etud}|{notes}"

            # Envoyer la commande au serveur
            ClientSocket.send(commande.encode())
            # Attendre la réponse du serveur (vous devrez implémenter cette partie)
            reponse = ClientSocket.recv(1024)
            print(reponse.decode())

        elif requete== "2":
            
            nom_etud = input("Nom de l'étudiant : ")
            notes = input("rentrez les notes,coef puis espacées(ex : 17/8;19/6):")

            # Créer une commande d'ajout d'étudiant
            commande = f"Ajout|{nom_etud}|{notes}"

            # Envoyer la commande au serveur
            ClientSocket.send(commande.encode())
            # Attendre la réponse du serveur (vous devrez implémenter cette partie)
            reponse = ClientSocket.recv(1024)
            print(reponse.decode())

        elif requete== "3":
            
            nom_etud = input("Nom de l'étudiant : ")
            # Créer une commande d'ajout d'étudiant
            commande = f"Moyenne|{nom_etud}"

            # Envoyer la commande au serveur
            ClientSocket.send(commande.encode())
            # Attendre la réponse du serveur (vous devrez implémenter cette partie)
            reponse = ClientSocket.recv(1024)
            print(reponse.decode())

        elif requete== "4":
            
            nom_prom = input("Nom de la promo : ")
            # Créer une commande d'ajout d'étudiant
            commande = f"Promo|{nom_prom}"

            # Envoyer la commande au serveur
            ClientSocket.send(commande.encode())
            # Attendre la réponse du serveur (vous devrez implémenter cette partie)
            reponse = ClientSocket.recv(1024)
            print(reponse.decode())
"""

 
def threaded_server(connection, num):
    while True:
        response = connection.recv(1024)
        print(response.decode('utf-8'))

if __name__== "__main__":
    main()
