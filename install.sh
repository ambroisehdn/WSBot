clear
echo '[!] Installation des outils...'
echo "[!] Mise à jour de L'environnement ..."
apt-get update > install.log
echo
echo '[!] Installation de Package  ...'
echo '    Python'
apt-get -y install python &>> install.log
echo '[!] Installation Terminée '
echo '[!] Autorisation du programme  '
chmod +x WSBot.py
echo '[!] Démarrage de WSBot '
python3 WSBot.py

