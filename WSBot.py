#!/usr/bin/env python
#coding:utf-8

#       ....Importation des modules ....

import os, sys, shutil, glob, time


#Vérification de systeme d'exploitation pour l'assignation de couleur et l'utilisation de WstatutsBot

if sys.platform in ["linux", "linux2"] :
    R = "\033[31;1m"
    V = "\033[32;1m"
    B = "\033[0m"
    C = "\033[36;1m"
else :
    R = ""
    V = ""
    B = ""
    c = ""
#Redéfinition d'encodage par défaut 

"""
    Les afficharges des Menus et sous Menus de SocialBot
"""
def whatbot() :
    print(C+"""
                               
        ------------WstatutsBot------------
        Coding by Hackylu'x :::-:::
        _________________________
                  Fondateur of InformaTutos
        -----------------------------------
        Contact us: informatutos7@gmail.com
        |||-----------------------------|||
        [1] - Statuts Check
        [2] - Statuts pic get
        [3] - Statuts video get
        [4] - Quit
         
         """+B)
#   ------Construction de WhatBot---------  #

def whatsAppBot() : 
    sourceSdcard = "/sdcard/WhatsApp/Media/.Statuses/"
    sourceStorage = "/storage/emulated/legacy/WhatsApp/Media/.Statuses/"
    def Sdcard() :
        sourceSdcard = "/sdcard/WhatsApp/Media/.Statuses/"
        destinationSdcard = "/sdcard/WhatsBot"
        print(C+"[!]-Vérification de la carte_Mémoire")
        time.sleep(1)
        if os.path.exists(sourceSdcard) :
            time.sleep(1)
            print("[!]-Obtention d'accès vers votre Carte_Memoire")
            time.sleep(3)
            try :
                os.mkdir(destinationSdcard)
            except :
                pass
            if os.path.exists(destinationSdcard) :
                time.sleep(2)
                print(V+"[!]-Accès obtenir.......")
                time.sleep(1)
                print(V+"[!]-Statuts Check successful")
            else :
                effacer()
                time.sleep(1)
                print(R+"[!]-Statuts Check failure")
        else :
            effacer()
            print(R+"[!]-Votre Mémoire de Stockage est définie sur la Mémoire Interne")
            time.sleep(0.5)
            print(R+"[!]-Repondez 'N' à la demande ")
            time.sleep(1)
            Statuts_check()
    def Storage() :
        sourceStorage = "/storage/emulated/legacy/WhatsApp/Media/.Statuses/"
        destinationStorage = "/storage/emulated/legacy/WhatsBot"
        print("[!]-Vérification de la Mémoire_Storage")
        time.sleep(1)
        if os.path.exists(sourceStorage) :
            time.sleep(1)
            print("[!]-Obtention d'accès vers votre Storage_Mémoire")
            time.sleep(3)
            try :
                os.mkdir(destinationStorage)
            except :
                pass 
            if os.path.exists(destinationStorage) :
                time.sleep(2)
                print(V+"[!]-Accès obtenir........")
                time.sleep(1)
                print(V+"[!]-Statuts Check successful")
            else :
                effacer()
                time.sleep(1)
                print(R+"[!]-Statuts Check failure")
        else :
            effacer()
            print(R+"[!]-Votre Mémoire de Stockage est définir sur la Carte_Mémoire")
            time.sleep(0.5)
            print(R+"[!]-Répondez 'Y' à la demande ")
            time.sleep(1)
            Statuts_check()
    def Statuts_check():
        print(B+"[?]-Avez vous une carte memoire dans votre Smartphone 'Y'or'N' ")
        check_input = input(C+" <•> WhatBot <•> "+B)
        try :
            check_input = str(check_input)            
        except:
            effacer()
            print(R+"\n[!]-Entrer une réponse valide")
            Statuts_check()
        if check_input == "Y":
            time.sleep(1)
            Sdcard()
            whatbot_choix_sdcard()
        elif check_input == "N":
            Storage()
            time.sleep(1)
            whatbot_choix_storage()
        else :
            effacer()
            print(R+"[!]-Veuillez répondre par 'Y/N'")
            Statuts_check()
    def whatbot_choix_sdcard():
        time.sleep(1)
        print(C+"""
        [2] - Statuts pic get
        [3] - Statuts video get
        [4] - Acceuil
       \n""")
        whatbot_input = input(B+" <•> WhatBot <•> ")
        try :
            whatbot_input = int(whatbot_input)
        except:
            print(R+"[!]-Entrer invalide !")
            time.sleep(3)
            effacer()
            whatbot_choix_sdcard()
        if whatbot_input == 2 :
            print(C+"[!]-Bot en marche initialisation du Système ........")
            time.sleep(3)
            print("[!]-Création du Dossier 'whatBot_img'")
            fichier_jpg = "/sdcard/WhatsBot/whatBot_img"
            try :
                os.mkdir(fichier_jpg)
            except:
                pass
            time.sleep(1)
            print(V+"[!]-Dossier 'whatBot_img créer avec succès'")
            deplacer = glob.glob(sourceSdcard + "*.jpg")
            time.sleep(3)
            print(C+"[!]-Vérification de fichier en cours ")
            time.sleep(3)
            print("[!]- [{}] fichier(s) Photo(s) Trouvé(s)".format(len(deplacer)))
            time.sleep(2)
            print("Consulter le Dossier WhatsBot pour retrouver vos fchiers après le Téléchargement")
            try :
                for i in range(len(deplacer)) :
                    time.sleep(3)
                    shutil.move(deplacer[i], fichier_jpg)
                    time.sleep(2)
                    print(C+"[!]-Téléchargement de la Photo Nº {} vers le dossier whatBot_img".format(i))
                    print(B+"[!]-Téléchargement Total de {} fichier(s)".format(i))
            except:
                pass
            whatbot_choix_sdcard()
        elif whatbot_input == 3 :
            print(C+"[!]-Bot en marche initialisation du Système ........")
            time.sleep(3)
            print("[!]-Création du Dossier 'whatBot_vid'")
            fichier_mp4 = "/sdcard/WhatsBot/whatBot_vid"
            try :
                os.mkdir(fichier_mp4)
            except:
                pass
            time.sleep(2)
            print(V+"[!]-Dossier 'whatBot_vid' créer avec succès")
            deplacer = glob.glob(sourceSdcard+ "*.mp4")
            time.sleep(3)
            print(C+"[!]-Vérification de fichier en cours ")
            time.sleep(3)
            print("[!]- [{}] fichier(s) Vidéo(s) trouvé(s)".format(len(deplacer)))
            time.sleep(2)
            print("Consulter le Dossier WhatsBot pour retrouver vos fchiers après le Téléchargement")
            try :
                for i in range(len(deplacer)) :
                    time.sleep(2)
                    shutil.move(deplacer[i], fichier_mp4)
                    time.sleep(2)
                    print(C+"[!]-Téléchargement de la vidéos Nº {} vers le dossier whatBot_vid".format(i))  
                    print(B+"[!]-Téléchargement Total de {} fichier(s)".format(i))
            except :
                pass
            whatbot_choix_sdcard() 
        elif whatbot_input == 4 :
            _quit()
        else :
            effacer()
            print(R+"[!]-Saisir invalide "+B)
            time.sleep(1)
            whatbot_choix_sdcard()
    def whatbot_choix_storage():
        print(C+"""
        [2] - Statuts pic get
        [3] - Statuts video get
        [4] - Acceuil
       \n""")
        whatbot_input = input(B+" <•> WhatBot <•> ")
        try :
            whatbot_input = int(whatbot_input)
        except :
            print(R+"[!]-Entrer invalide !")
            time.sleep(1.5)
            effacer()
            whatbot_choix_storage()
        if whatbot_input == 2 :
            print(C+"[!]-Bot en marche initialisation du Système ........")
            time.sleep(3)
            print("[!]-Création du Dossier 'whatBot_img'")
            fichier_jpg = "/storage/emulated/legacy/WhatsBot/whatBot_img"
            try :
                os.mkdir(fichier_jpg)
            except :
                pass
            time.sleep(2)
            print(V+"[!]-Dossier 'whatBot_img créer avec succès'")
            deplacer = glob.glob(sourceStorage + "*.jpg")
            time.sleep(3)
            print(C+"[!]-Vérification de fichier en cours ")
            time.sleep(3)
            print("[!]- [{}] fichier(s) photo(s) trouvé(s)".format(len(deplacer)))
            time.sleep(2)
            print("Consulter le Dossier WhatsBot pour retrouver vos fchiers après le Téléchargement")
            try :
                for i in range(len(deplacer)) :
                    time.sleep(2)
                    shutil.move(deplacer[i], fichier_jpg)
                    time.sleep(2)
                    print(C+"[!]-Téléchargement de la Photo Nº {} vers le dossier whatBot_img".format(i))
                    time.sleep(2) 
                    print(V+"[!]-Téléchargement Total de {} fichier(s)".format(i))
            except :
                pass
            whatbot_choix_storage()
        elif whatbot_input == 3 :
            print(C+"[!]-Bot en marche initialisation du Système ........")
            time.sleep(3)
            print("[!]-Création du Dossier 'whatBot_vid'")
            fichier_mp4 = "/storage/emulated/legacy/WhatsBot/whatBot_vid"
            try :
                os.mkdir(fichier_mp4)
            except :
                pass
            time.sleep(1)
            print(V+"[!]-Dossier 'whatBot_vid' créer avec succès")
            deplacer = glob.glob(sourceStorage+ "*.mp4")
            time.sleep(3)
            print(C+"[!]-Vérification de fichier en cours ")
            time.sleep(3)
            print("[!]- [{}] fichier(s) Vidéo(s)".format(len(deplacer)))
            time.sleep(2)
            print("Consulter le Dossier WhatsBot pour retrouver vos fchiers après le Téléchargement")
            try :
                for i in range(len(deplacer)) :
                    time.sleep(2)
                    shutil.move(deplacer[i], fichier_mp4)
                    time.sleep(2)
                    print(C+"[!]-Téléchargement de la vidéo Nº {} vers le dossier whatBot_vid".format(i))
                    time.sleep(2)
                    print(B+"[!]-Téléchargement Total de {} fichier(s)".format(i))
            except :
                pass
            whatbot_choix_storage()
        elif whatbot_input == 4 :
            _quit()
        else :
            effacer()
            print(R+"[!]-Saisir invalide "+B)
            time.sleep(1)
            whatbot_choix_sdcard()
    def _quit():
        print(R+"[!]-Fermerture de la session actuelle")
        time.sleep(1)
        os.system("clear")
        main_whatsAppBot()
    def effacer():
        os.system("clear")
    def main_whatsAppBot():
        whatbot()
        main_whatsApBot = input(C+" <•> WhatBot <•> ")
        try :
            main_whatsApBot = int(main_whatsApBot)
        except:
            print(R+"[!]-Entrer invalide ")
            time.sleep(2)
            effacer()
            main_whatsAppBot()
        if main_whatsApBot == 1:
            effacer()
            time.sleep(2)
            print(B+"[!]-Status Check en cours .....")
            time.sleep(2)
            Statuts_check()                
        elif main_whatsApBot == 2:
            effacer()
            print(R+"[!]-Veuillez faire le Statuts Check d'abord")
            time.sleep(2)
            main_whatsAppBot()
        elif main_whatsApBot == 3:
            effacer()
            print(R+"[!]-Veuillez faire le Statuts Check d'abord")
            time.sleep(2)
            main_whatsAppBot()
        elif main_whatsApBot == 4:
            print(R+"[*] Fermerture du Programme "+B)
            time.sleep(2)
            sys.exit()
        else:
            print(R+"[!]-Aucun choix ne corresponde à votre demande")
            time.sleep(3)
            effacer()
            main_whatsAppBot()
    main_whatsAppBot()
whatsAppBot()
#Création de whatsAppBot terminé
# Ce projet est une partie de SocialBot mais suite à des problemes de version j'ai découpé le projet SocialBot en sous Projets différents