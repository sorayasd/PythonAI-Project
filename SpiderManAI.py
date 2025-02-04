# Importation des modules 
import re  # Module (expressions régulières)
import datetime  # Module (dates et heures) 
# Définition des règles V2 pour les réponses du chatbot pour les exercices 4, 5 et 6
reglesV2 = [
    # Règles pour salutations
    ["regle-Bonjour","bonjour","Bonjour humain! Ravie de te voir.", 1,"enregistrement", None],
    ["regle-salut","salut","Bonjour humain", 2,"enregistrement", None],
    # Règles pour la présentation de l'utilisateur
    ["presentation1", "mon nom est .*", "Enchanté! Je peux vous quelques informations sur l'univers de spiderman adapté au cinéma. Posez moi des questions en rapport avec ces film.", 3, ],
    ["presentation2", "je m'appelle *", "Enchanté! Je peux vous quelques informations sur l'univers de spiderman adapté au cinéma. Posez moi des questions en rapport avec ces film.", 3, ],
    ["presentation3", "je suis .*", "Enchanté! Je peux vous quelques informations sur l'univers de spiderman adapté au cinéma. Posez moi des questions en rapport avec ces film.", 3, ],
    # Règles pour dire au revoir
    ["bye", "by.*", "Au revoir :/", 1, None],
    ["au revoir", "au revoir", "Au revoir :/", 1, None],
    ["fin", "fin", "Au revoir !", 1, None],
    ["mathématique", "calcul", "Essayez-moi pour les calculs simples!", 3, "calcul"], # Réponse sur les calculs mathématiques
    ["merci", "merci", "Me remerci pas, c'est toujours un plaisir pour moi!", 1, None], # Réponse aux remerciements 
    ["blague", "raconte.*blague", "Pourquoi Spiderman est-il un crack à l'école ? Parcequ'il apprend tout Parker.", 3, None], # Réponse sur blague sur Spiderman
    ["date", "quelle est la date.*", f"Aujourd'hui, nous sommes le {datetime.datetime.now().strftime('%d/%m/%Y')}.", 2, None],  # Réponse sur la date actuelle
    ["heure", "quelle heure est-il.*", f"Il est actuellement {datetime.datetime.now().strftime('%H:%M')}.", 2, None],  # Réponse sur l'heure actuelle
    
    # Règles pour les questions sur les films spiderman
    
    ["regles_film1", "Le premier spider-man","Le film Spider-Man de 2002, réalisé par Sam Raimi, met en scène Tobey Maguire dans le rôle de Peter Parker  Spider-Man, Kirsten Dunst en tant que Mary Jane Watson, et Willem Dafoe dans celui de Norman Osborn Green Goblin. Sorti en 2002, le film a été écrit par David Koepp. L'intrigue tourne autour de Peter Parker, qui acquiert des pouvoirs surhumains après avoir été mordu par une araignée génétiquement modifiée, le transformant en Spider-Man. Le film a été acclamé par la critique pour son équilibre entre action et développement de personnages. Il a également été salué pour ses effets spéciaux révolutionnaires pour l'époque, en particulier pour les scènes de balancement et les combats. La musique originale du film a été composée par Danny Elfman." ,1],
    
    ["regles_film2", "Le spider-man 1","Le film Spider-Man de 2002, réalisé par Sam Raimi, met en scène Tobey Maguire dans le rôle de Peter Parker  Spider-Man, Kirsten Dunst en tant que Mary Jane Watson, et Willem Dafoe dans celui de Norman Osborn Green Goblin. Sorti en 2002, le film a été écrit par David Koepp. L'intrigue tourne autour de Peter Parker, qui acquiert des pouvoirs surhumains après avoir été mordu par une araignée génétiquement modifiée, le transformant en Spider-Man. Le film a été acclamé par la critique pour son équilibre entre action et développement de personnages. Il a également été salué pour ses effets spéciaux révolutionnaires pour l'époque, en particulier pour les scènes de balancement et les combats. La musique originale du film a été composée par Danny Elfman."],
    
    ["regles_film3", "Le spider-man 2002","Le film Spider-Man de 2002, réalisé par Sam Raimi, met en scène Tobey Maguire dans le rôle de Peter Parker  Spider-Man, Kirsten Dunst en tant que Mary Jane Watson, et Willem Dafoe dans celui de Norman Osborn Green Goblin. Sorti en 2002, le film a été écrit par David Koepp. L'intrigue tourne autour de Peter Parker, qui acquiert des pouvoirs surhumains après avoir été mordu par une araignée génétiquement modifiée, le transformant en Spider-Man. Le film a été acclamé par la critique pour son équilibre entre action et développement de personnages. Il a également été salué pour ses effets spéciaux révolutionnaires pour l'époque, en particulier pour les scènes de balancement et les combats. La musique originale du film a été composée par Danny Elfman."],
    
    ["regles_film4", "Le spider-man avec Tobey Maguire","Le film Spider-Man de 2002, réalisé par Sam Raimi, met en scène Tobey Maguire dans le rôle de Peter Parker  Spider-Man, Kirsten Dunst en tant que Mary Jane Watson, et Willem Dafoe dans celui de Norman Osborn Green Goblin. Sorti en 2002, le film a été écrit par David Koepp. L'intrigue tourne autour de Peter Parker, qui acquiert des pouvoirs surhumains après avoir été mordu par une araignée génétiquement modifiée, le transformant en Spider-Man. Le film a été acclamé par la critique pour son équilibre entre action et développement de personnages. Il a également été salué pour ses effets spéciaux révolutionnaires pour l'époque, en particulier pour les scènes de balancement et les combats. La musique originale du film a été composée par Danny Elfman."],
#------------------------------------------------------------------

    ["regles_film5", "spider-man 2","Spider-Man 2 est un film sorti en 2004, réalisé par Sam Raimi et mettant en vedette Tobey Maguire, Kirsten Dunst et Alfred Molina. L'intrigue tourne autour de Peter Parker, alias Spider-Man, qui doit affronter le redoutable Dr. Otto Octavius, également connu sous le nom de Docteur Octopus. Le film a été acclamé comme l'un des meilleurs films de super-héros de tous les temps et utilise des effets spéciaux améliorés, en particulier pour les scènes d'action. La musique originale du film a été composée par Danny Elfman."],

    ["regles_film6", "Deuxième Spider-man","Spider-Man 2 est un film sorti en 2004, réalisé par Sam Raimi et mettant en vedette Tobey Maguire, Kirsten Dunst et Alfred Molina. L'intrigue tourne autour de Peter Parker, alias Spider-Man, qui doit affronter le redoutable Dr. Otto Octavius, également connu sous le nom de Docteur Octopus. Le film a été acclamé comme l'un des meilleurs films de super-héros de tous les temps et utilise des effets spéciaux améliorés, en particulier pour les scènes d'action. La musique originale du film a été composée par Danny Elfman."],

    ["regles_film8", "Le spider-man 2004","Spider-Man 2 est un film sorti en 2004, réalisé par Sam Raimi et mettant en vedette Tobey Maguire, Kirsten Dunst et Alfred Molina. L'intrigue tourne autour de Peter Parker, alias Spider-Man, qui doit affronter le redoutable Dr. Otto Octavius, également connu sous le nom de Docteur Octopus. Le film a été acclamé comme l'un des meilleurs films de super-héros de tous les temps et utilise des effets spéciaux améliorés, en particulier pour les scènes d'action. La musique originale du film a été composée par Danny Elfman."],
#-----------------------------------------------------------------------
    ["regles_film9", "spider-man 3","Le film Spider-Man 3 est sorti en 2007, réalisé par Sam Raimi. Il met en vedette Tobey Maguire, Kirsten Dunst et James Franco. L'intrigue tourne autour de Peter Parker, alias Spider-Man, qui doit faire face à ses propres démons tout en affrontant de nouveaux ennemis, dont le redoutable Venom. Le film a été reçu de manière mitigée par les critiques, critiqué pour sa surcharge de personnages et d'intrigues. Il utilise des effets spéciaux pour les séquences de combat, notamment pour les transformations des personnages. La musique originale du film a été composée par Christopher Young."],
    
    ["regles_film10", "Troisième spider-man ","Le film Spider-Man 3 est sorti en 2007, réalisé par Sam Raimi. Il met en vedette Tobey Maguire, Kirsten Dunst et James Franco. L'intrigue tourne autour de Peter Parker, alias Spider-Man, qui doit faire face à ses propres démons tout en affrontant de nouveaux ennemis, dont le redoutable Venom. Le film a été reçu de manière mitigée par les critiques, critiqué pour sa surcharge de personnages et d'intrigues. Il utilise des effets spéciaux pour les séquences de combat, notamment pour les transformations des personnages. La musique originale du film a été composée par Christopher Young."],

    ["regles_film11", "2007","Le film Spider-Man 3 est sorti en 2007, réalisé par Sam Raimi. Il met en vedette Tobey Maguire, Kirsten Dunst et James Franco. L'intrigue tourne autour de Peter Parker, alias Spider-Man, qui doit faire face à ses propres démons tout en affrontant de nouveaux ennemis, dont le redoutable Venom. Le film a été reçu de manière mitigée par les critiques, critiqué pour sa surcharge de personnages et d'intrigues. Il utilise des effets spéciaux pour les séquences de combat, notamment pour les transformations des personnages. La musique originale du film a été composée par Christopher Young."],
#-----------------------------------------------------------------------
    ["regles_film12", "The Amazing Spider-Man","Réalisé par Marc Webb, avec Andrew Garfield, Emma Stone, et Rhys Ifans. Ce reboot explore les origines de Spider-Man alors qu'il affronte le Lézard, un ancien collègue de son père. Le film a été salué pour ses performances et ses effets spéciaux, offrant une nouvelle perspective sur le personnage bien-aimé."],

    ["regles_film613", "amazing spider-man ","Réalisé par Marc Webb, avec Andrew Garfield, Emma Stone, et Rhys Ifans. Ce reboot explore les origines de Spider-Man alors qu'il affronte le Lézard, un ancien collègue de son père. Le film a été salué pour ses performances et ses effets spéciaux, offrant une nouvelle perspective sur le personnage bien-aimé."],

    ["regles_film14", " Spiderman 2012","Réalisé par Marc Webb, avec Andrew Garfield, Emma Stone, et Rhys Ifans. Ce reboot explore les origines de Spider-Man alors qu'il affronte le Lézard, un ancien collègue de son père. Le film a été salué pour ses performances et ses effets spéciaux, offrant une nouvelle perspective sur le personnage bien-aimé."],
#-----------------------------------------------------------------------
    ["regles_film15", "The Amazing Spider-Man : Le Destin d'un héros"," Réalisé par Marc Webb, avec Andrew Garfield, Emma Stone, et Jamie Foxx. Spider-Man affronte Electro tout en naviguant dans les complications de sa relation avec Gwen Stacy. Bien que le film ait reçu des critiques mitigées, il a continué à développer l'univers du nouveau Spider-Man."],

    ["regles_film16", "Le destin d'un héro "," Réalisé par Marc Webb, avec Andrew Garfield, Emma Stone, et Jamie Foxx. Spider-Man affronte Electro tout en naviguant dans les complications de sa relation avec Gwen Stacy. Bien que le film ait reçu des critiques mitigées, il a continué à développer l'univers du nouveau Spider-Man."],

    ["regles_film17", "2014"," Réalisé par Marc Webb, avec Andrew Garfield, Emma Stone, et Jamie Foxx. Spider-Man affronte Electro tout en naviguant dans les complications de sa relation avec Gwen Stacy. Bien que le film ait reçu des critiques mitigées, il a continué à développer l'univers du nouveau Spider-Man."],
#-----------------------------------------------------------------------
    ["regles_film18", "Spider-Man: Homecoming","Réalisé par Jon Watts, avec Tom Holland, Michael Keaton, et Zendaya. Ce film marque l'introduction de Tom Holland dans le rôle de Peter Parker/Spider-Man, alors qu'il tente de prouver sa valeur en tant que super-héros tout en étant mentoré par Iron Man."],

    ["regles_film19", "Homecoming ","Réalisé par Jon Watts, avec Tom Holland, Michael Keaton, et Zendaya. Ce film marque l'introduction de Tom Holland dans le rôle de Peter Parker/Spider-Man, alors qu'il tente de prouver sa valeur en tant que super-héros tout en étant mentoré par Iron Man."],

    ["regles_film20", "2017","Réalisé par Jon Watts, avec Tom Holland, Michael Keaton, et Zendaya. Ce film marque l'introduction de Tom Holland dans le rôle de Peter Parker/Spider-Man, alors qu'il tente de prouver sa valeur en tant que super-héros tout en étant mentoré par Iron Man."],
#-----------------------------------------------------------------------
    ["regles_film21", "Spider-Man: Far From Home","Suite de Spider-Man: Homecoming, réalisé par Jon Watts, avec Tom Holland, Zendaya, et Jake Gyllenhaal. L'histoire suit Peter Parker et ses amis lors d'un voyage scolaire en Europe, confronté aux conséquences des événements précédents et à l'émergence d'un nouvel ennemi, Mysterio."],

    ["regles_film22", "Far From Home ","Suite de Spider-Man: Homecoming, réalisé par Jon Watts, avec Tom Holland, Zendaya, et Jake Gyllenhaal. L'histoire suit Peter Parker et ses amis lors d'un voyage scolaire en Europe, confronté aux conséquences des événements précédents et à l'émergence d'un nouvel ennemi, Mysterio."],

    ["regles_film23", "2019","Suite de Spider-Man: Homecoming, réalisé par Jon Watts, avec Tom Holland, Zendaya, et Jake Gyllenhaal. L'histoire suit Peter Parker et ses amis lors d'un voyage scolaire en Europe, confronté aux conséquences des événements précédents et à l'émergence d'un nouvel ennemi, Mysterio."],
#-----------------------------------------------------------------------
    ["regles_film24", "Spider-Man: No Way Home","Réalisé par Jon Watts, avec Tom Holland, Zendaya, et Benedict Cumberbatch. Peter Parker fait appel au Docteur Strange pour inverser les conséquences de la révélation de son identité secrète, tandis que des figures du passé réapparaissent, ouvrant la porte à des dimensions alternatives."],

    ["regles_film25", "No Way Home","Réalisé par Jon Watts, avec Tom Holland, Zendaya, et Benedict Cumberbatch. Peter Parker fait appel au Docteur Strange pour inverser les conséquences de la révélation de son identité secrète, tandis que des figures du passé réapparaissent, ouvrant la porte à des dimensions alternatives."],

    ["regles_film26", "2021","Réalisé par Jon Watts, avec Tom Holland, Zendaya, et Benedict Cumberbatch. Peter Parker fait appel au Docteur Strange pour inverser les conséquences de la révélation de son identité secrète, tandis que des figures du passé réapparaissent, ouvrant la porte à des dimensions alternatives."],
#-----------------------------------------------------------------------
    ["regles_film27", "Spider-Man: Into the Spider-Verse","Réalisé par Bob Persichetti, Peter Ramsey, et Rodney Rothman, ce film d'animation présente plusieurs versions de Spider-Man provenant de dimensions différentes. L'histoire suit Miles Morales alors qu'il apprend à maîtriser ses nouveaux pouvoirs et à sauver son univers avec l'aide d'autres Spider-People."],

    ["regles_film28", "Into the Spider-Verse","Réalisé par Bob Persichetti, Peter Ramsey, et Rodney Rothman, ce film d'animation présente plusieurs versions de Spider-Man provenant de dimensions différentes. L'histoire suit Miles Morales alors qu'il apprend à maîtriser ses nouveaux pouvoirs et à sauver son univers avec l'aide d'autres Spider-People."],

    ["regles_film29", "2018","Réalisé par Bob Persichetti, Peter Ramsey, et Rodney Rothman, ce film d'animation présente plusieurs versions de Spider-Man provenant de dimensions différentes. L'histoire suit Miles Morales alors qu'il apprend à maîtriser ses nouveaux pouvoirs et à sauver son univers avec l'aide d'autres Spider-People."],
#-----------------------------------------------------------------------
    ["regles_film30", "Spider-Man : New Generation","Suite de Spider-Man: Into the Spider-Verse, toujours réalisé par Bob Persichetti, Peter Ramsey, et Rodney Rothman, explorant davantage l'univers étendu des Spider-People et introduisant de nouveaux personnages et défis pour Miles Morales."],

    ["regles_film31", "New Generation","Suite de Spider-Man: Into the Spider-Verse, toujours réalisé par Bob Persichetti, Peter Ramsey, et Rodney Rothman, explorant davantage l'univers étendu des Spider-People et introduisant de nouveaux personnages et défis pour Miles Morales."],

    ["regles_film32", "2022","Suite de Spider-Man: Into the Spider-Verse, toujours réalisé par Bob Persichetti, Peter Ramsey, et Rodney Rothman, explorant davantage l'univers étendu des Spider-People et introduisant de nouveaux personnages et défis pour Miles Morales."],
#-----------------------------------------------------------------------
    ["regles_film33", "Venom","Bien que ce ne soit pas strictement un film Spider-Man, Venom est un personnage issu de l'univers de Spider-Man. Le film met en vedette Tom Hardy dans le rôle d'Eddie Brock, un journaliste qui se lie à un symbiote extraterrestre pour devenir Venom, un anti-héros avec des pouvoirs similaires à Spider-Man."],

    ["regles_film34", "Eddie Brock","Bien que ce ne soit pas strictement un film Spider-Man, Venom est un personnage issu de l'univers de Spider-Man. Le film met en vedette Tom Hardy dans le rôle d'Eddie Brock, un journaliste qui se lie à un symbiote extraterrestre pour devenir Venom, un anti-héros avec des pouvoirs similaires à Spider-Man."],

    ["regles_film35", "2018","Bien que ce ne soit pas strictement un film Spider-Man, Venom est un personnage issu de l'univers de Spider-Man. Le film met en vedette Tom Hardy dans le rôle d'Eddie Brock, un journaliste qui se lie à un symbiote extraterrestre pour devenir Venom, un anti-héros avec des pouvoirs similaires à Spider-Man."],
#-----------------------------------------------------------------------
    ["regles_film36", "Venom: Let There Be Carnage","Suite de Venom, le film suit Eddie Brock/Venom alors qu'il affronte le redoutable Carnage, un symbiote encore plus puissant. Le film explore davantage la dualité entre Eddie et Venom, tout en introduisant de nouveaux défis pour le duo improbable."],

    ["regles_film37", "Let There Be Carnage","Suite de Venom, le film suit Eddie Brock/Venom alors qu'il affronte le redoutable Carnage, un symbiote encore plus puissant. Le film explore davantage la dualité entre Eddie et Venom, tout en introduisant de nouveaux défis pour le duo improbable."],

    ["regles_film38", "2021","Suite de Venom, le film suit Eddie Brock/Venom alors qu'il affronte le redoutable Carnage, un symbiote encore plus puissant. Le film explore davantage la dualité entre Eddie et Venom, tout en introduisant de nouveaux défis pour le duo improbable."],
]
# Dictionnaire pour stocker le nom de l'utilisateur 
memo = {}
# Fonction pour enregistrer le nom de l'utilisateur
def enregistrement(nom):
    memo["nom_utilisateur"] = nom
    return f"Enchanté {nom} Enchanté.Je suis une intelligence artificielle experte dans l'univers cinématographique de Spiderman. N'hésitez pas à me poser toutes vosquestions à ce sujet!"
# Fonction pour effectuer des calculs simples
def calcul():
    while True:
        operation = input("Entrez une opération (un exemple 2+3) ou 'fin' pour sourtir des opérations : ")
        if operation.lower() == 'fin':
            break
        match = re.match(r"(\d+)\s*\+\s*(\d+)", operation)
        if match:
            nb1 = int(match.group(1))
            nb2 = int(match.group(2))
            res = nb1 + nb2
            print(f"Le résultat de l'opération est : {res}")
        else:
            print("Je n'ai pas compris. Veuillez entrer une addition valide.")
# Boucle pour l'interaction avec l'utilisateur
user = ""
while user != "fin":
    user = input("Moi > ")  # L'entrée de l'utilisateur
    meilleure_regle = None
    max_score = 0
    # Parcour des règles 
    for r in reglesV2:
        if len(r) >= 4:  # Vérifier si la règle contient au moins 4 éléments
            motif = r[1]
            score = r[3]
            # Vérification si le motif de la règle correspond à l'entrée de l'utilisateur
            if re.search(motif, user, re.IGNORECASE):
                # Mise à jour la meilleure règle si le score est plus élevé
                if score > max_score:
                    max_score = score
                    meilleure_regle = r
    # Si une règle est trouvée
    if meilleure_regle:
        print(meilleure_regle[2])  # Affichage de la réponse associée à la règle
        if len(meilleure_regle) >= 5:  # Vérifier si la règle contient un élément associé
            associee = meilleure_regle[4]
            if associee:
                if associee == "calcul":
                    retour_fonction = calcul()
                    if retour_fonction:
                        print(retour_fonction)
            elif associee == "enregistrement":
                nom_utilisateur = input("Quel est votre nom? ")
                print(enregistrement(nom_utilisateur))
    else:
        print("Je m'excuse mais je ne sais pas...")
if "nom_utilisateur" in memo:
    print(f"Au revoir {memo['nom_utilisateur']}, ravis d'avoir pu vous aider!")
else:
    print("Au revoir !")
