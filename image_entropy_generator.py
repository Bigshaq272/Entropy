import numpy as np  # type: ignore
from PIL import Image  # type: ignore
import hashlib
import argparse  # Pour gérer les arguments en ligne de commande
import string


def generate_random_string_from_image(image_path, string_length, block_size, include_letters):
    """
    Génère une chaîne de caractères à partir d'une image et la divise en blocs.

    :param image_path: Chemin de l'image à utiliser.
    :param string_length: Longueur de la chaîne de caractères à générer.
    :param block_size: Taille des blocs dans lesquels la chaîne sera divisée.
    :param include_letters: Booléen pour inclure des lettres dans la chaîne générée.
    :return: Chaîne de caractères divisée en blocs.
    """
    try:
        # Charger l'image
        img = Image.open(image_path).convert('RGB')

        # Convertir l'image en tableau de pixels
        pixels = np.array(img)

        # Aplatir le tableau pour obtenir une liste de valeurs RGB
        flat_pixels = pixels.flatten()

        # Combiner les pixels en une chaîne de caractères
        pixel_data = ''.join(map(str, flat_pixels))

        # Créer un hachage SHA-256 des données des pixels
        hash_obj = hashlib.sha256(pixel_data.encode('utf-8'))
        hash_digest = hash_obj.hexdigest()

        # Préparer les caractères autorisés
        if include_letters:
            allowed_chars = string.digits + string.ascii_letters  # Chiffres + Lettres majuscules/minuscules
        else:
            allowed_chars = string.digits  # Chiffres uniquement

        # Extraire les caractères du hachage
        random_chars = [c for c in hash_digest if c in allowed_chars]

        # Si le hachage contient moins de caractères que requis, répéter
        while len(random_chars) < string_length:
            # Ré-hacher la chaîne pour ajouter plus de caractères
            hash_obj = hashlib.sha256(hash_digest.encode('utf-8'))
            hash_digest = hash_obj.hexdigest()
            random_chars.extend([c for c in hash_digest if c in allowed_chars])

        # Générer la chaîne de caractères avec la longueur spécifiée
        random_string = ''.join(random_chars[:string_length])

        # Diviser la chaîne en blocs
        blocks = [random_string[i:i + block_size] for i in range(0, len(random_string), block_size)]

        return blocks
    except FileNotFoundError:
        print(f"Erreur : Le fichier '{image_path}' est introuvable.")
        return None
    except Exception as e:
        print(f"Erreur inattendue : {e}")
        return None


def save_to_file(blocks, file_name="generated_strings.txt"):
    """
    Enregistre les blocs générés dans un fichier texte, avec chaque bloc sur une nouvelle ligne.

    :param blocks: Liste des chaînes générées (divisées en blocs).
    :param file_name: Nom du fichier où enregistrer les chaînes.
    """
    try:
        with open(file_name, "a") as file:
            for block in blocks:
                file.write(block + "\n")  # Écrit chaque ligne du bloc
            file.write("\n")  # Ajoute une ligne vide entre chaque génération
        print(f"Les chaînes ont été enregistrées dans le fichier '{file_name}'.")
    except Exception as e:
        print(f"Erreur lors de l'enregistrement : {e}")


if __name__ == "__main__":
    # Définir les arguments en ligne de commande
    parser = argparse.ArgumentParser(description="Générer une chaîne aléatoire à partir d'une image.")
    parser.add_argument("image_path", type=str, help="Chemin de l'image à utiliser.")
    parser.add_argument("string_length", type=int, help="Longueur de la chaîne à générer (doit être positive).")
    parser.add_argument("block_size", type=int, help="Taille des blocs à générer (doit être positive).")
    parser.add_argument("--include_letters", action="store_true",
                        help="Inclure des lettres (majuscules et minuscules) dans la chaîne générée.")
    parser.add_argument("--output_file", type=str, default="generated_strings.txt",
                        help="Nom du fichier pour enregistrer les chaînes générées.")

    # Lire les arguments
    args = parser.parse_args()
    image_path = args.image_path
    string_length = args.string_length
    block_size = args.block_size
    include_letters = args.include_letters
    output_file = args.output_file

    # Vérifier que les longueurs sont valides
    if string_length <= 0 or block_size <= 0:
        print("Erreur : La longueur de la chaîne et la taille des blocs doivent être supérieures à 0.")
    else:
        # Générer la chaîne et la diviser en blocs
        blocks = generate_random_string_from_image(image_path, string_length, block_size, include_letters)

        if blocks is not None:
            # Enregistrer dans le fichier
            save_to_file(blocks, output_file)
        else:
            print("Aucune chaîne générée.")
