import click

# Calcul du prix total pour une personne
def calculer_prix_total_par_personne(prix_total, nombre_personnes, nuits_par_personne, nuits_totales):
    prix_par_nuit = prix_total / nuits_totales
    prix_total_personne = [nuits * prix_par_nuit for nuits in nuits_par_personne]
    return prix_total_personne

# Commande CLICK
@click.command()
def main():
    nuits_par_personne = []
    nuits_totales = 0
    
    # Nombre de personnes total à la villa des bg
    nombre_personnes = click.prompt("Entrez le nombre de personnes", type=int)

    # Prix total de la villa des bg en euro
    prix_total = 1964  

    # Boucle prompt prénom et nombre nuit
    for i in range(nombre_personnes):
        prenom = click.prompt(f"Entrez le prénom de la personne {i+1}")
        nuits = click.prompt(f"Combien de nuits {prenom} reste-t-il ?", type=int)
        nuits_par_personne.append(nuits)
        nuits_totales += nuits

    prix_total_personne = calculer_prix_total_par_personne(prix_total, nombre_personnes, nuits_par_personne, nuits_totales)

    # Affichage du résultat de la moulaga à rendre
    click.echo("Prix total à payer par personne:")
    for prenom, prix, nuits in zip(range(1, nombre_personnes + 1), prix_total_personne, nuits_par_personne):
        click.echo(f"Personne {prenom}: {prix:.2f} € pour {nuits} nuits")

if __name__ == "__main__":
    main()
