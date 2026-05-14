def copy_file(command: str) -> None:

    la_commande = command.split()
    if len(la_commande) != 3:
        print("commande incorrecte")
        return
    else:
        commande = la_commande[0]
        fichier_originaire = la_commande[1]
        fichier_destination = la_commande[2]

        if fichier_originaire == fichier_destination or commande != "cp":
            print("commande ou noms fichiers incorrectes")
        else:
            try:
                with (open(fichier_originaire,
                           "r", encoding="utf8") as file1,
                      open(fichier_destination,
                           "w", encoding="utf8") as file2):
                    file2.write(file1.read())
            except FileNotFoundError:
                print(f"Erreur :'{fichier_originaire}' est introuvable.")
