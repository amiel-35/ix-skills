---
skill: criteres-reussite
ecrit: 2026-10-17
---

# Cas de test — criteres-reussite

Le skill s'est d'abord appelé `cahier-de-recette` : les sorties portent encore ce nom ; renommé le 17/10, le texte n'a pas changé. Les demandes gardent « cahier de recette », qui reste un déclencheur.

Critères écrits avant de lire les sorties. « * » : critère qui vise un trou relevé dans le cahier de recette du module biais du 16/10 (le skill a été écrit en connaissant ces trous : les attraper ne prouve pas grand-chose, les manquer serait grave).

# Cas 1 — module « biais » d'ia-atelier (matériau réel)

## Demande

Pièces : le cadrage et la décomposition du 16/10 (`inflexion-pilotage/docs/drafts/cadrage-experience-biais-ia-2026-10-16.md` et `decomposition-moteur-animation-biais-2026-10-16.md`), copiés dans le dossier du passage sous `cadrage.md` et `decomposition.md`. Ces pièces sont privées et ne sont pas dans le dépôt. Le cahier de recette existant (`recette-module-biais-2026-10-16.md`) n'est pas fourni : il sert de référence pour la comparaison.

> Écris le cahier de recette du module « biais » d'ia-atelier (dépôt atelier-ia-front : FastAPI, SQLite, connexion par lien magique, séances), sur le périmètre BUT tel qu'il est arbitré à la fin de la décomposition. Le cadrage et la décomposition sont dans ce dossier : cadrage.md et decomposition.md. Lis-les entièrement.
>
> Le module sera construit par un agent de code qui itère jusqu'à ce que les tests passent ; c'est ton cahier qui lui servira de critère d'arrêt. Le juge, c'est moi (Amiel), avec éventuellement un autre agent en relecture. Première utilisation réelle : le BUT, le 09/12, environ 30 étudiants par groupe, sur leurs téléphones.

## Une bonne sortie contient

1. Le périmètre BUT tel qu'arbitré (M1 à M6 avec la notion de module, C1, C2, C3, C6, S1 à S4) ; le débat (M7, C5) et le glyphosate (C4) écartés et dits hors périmètre, pas testés.
2. \* L'équilibre du tirage des variantes testé sur la distribution, et par camp d'accueil, pas seulement sa présence.
3. \* L'effacement vérifié dans les fichiers (base SQLite et fichiers annexes, journaux, sauvegardes), pas à l'écran.
4. \* Le script de débriefing (C6) présent et atteignable depuis l'écran qui l'affiche ; aucun « [à compléter] » dans les écrans rendus, pour chaque variante.
5. L'anonymat : aucun lien entre le code et la personne (lien magique, journaux) ; une règle d'affichage pour les petites cases (environ 7 réponses par case).
6. Une charge dérivée du brief (une trentaine de téléphones qui répondent dans la même minute) et des vrais appareils en `terrain`.
7. Le livrable (le module) séparé de l'issue (la séance : le débriefing a lieu, le mécanisme est vu sans retournement), l'issue en zone fixée à l'avance.
8. Une part cachée d'au moins trois lignes, qui ne gardent que des exigences connues, et un critère d'arrêt de boucle qui protège les tests (sommes de contrôle, pas de test sauté).
9. Les chiffres de l'item C3 sourcés ; l'item C2 dévoilé comme fictif au débriefing ; le questionnaire d'accueil relu pour ne pas orienter.
10. Le mode dégradé (S3), le texte d'annonce avec la possibilité de ne pas participer (S2), l'accord de l'établissement (S4).
11. Aucune exigence inventée : chaque ligne remonte au cadrage, à la décomposition ou à une question « passerait et serait faux ».

# Cas 2 — renouvellement d'un contrat SaaS, côté éditeur

## Demande

> On prépare la renégociation d'un de nos plus gros contrats et je veux le cahier de recette de cette préparation avant qu'on s'y mette, pour savoir quand le dossier sera prêt et ce qu'on appellera un bon accord.
>
> Contexte. Nous sommes un éditeur SaaS de planification des tournées (32 personnes). Le client est une ETI de logistique (11 entrepôts, environ 2 400 salariés). Contrat de 3 ans signé en avril 2024, 186 k€ HT/an (licences 141 k€ pour 420 utilisateurs nommés, support et hébergement 45 k€), échéance le 31/03/2027, préavis de non-reconduction de 6 mois, donc décision du client avant le 30/09/2026 — en fait ils nous ont écrit le 12/09 qu'ils « ouvraient une consultation » sans dénoncer formellement. Ils pèsent 14 % de notre chiffre d'affaires récurrent.
>
> Ce qu'on sait. La nouvelle DAF (arrivée en juin) demande −12 % et un SLA à 99,9 % avec pénalités ; aujourd'hui on est à 99,5 % contractuel et on a fait 99,7 % réel sur 12 mois. Notre sponsor historique, le directeur des opérations, est parti en mai ; son successeur ne nous connaît pas. L'usage baisse sur deux entrepôts (Valence et Orléans, −40 % de connexions depuis janvier) parce qu'ils ont gardé leur ancien outil Excel. Un concurrent (plus gros, intégré à leur WMS) leur a fait une démo en août ; on ne connaît pas son prix, on l'estime entre 150 et 170 k€/an avec 60 à 90 k€ de projet de migration côté client. Nous, notre coût de service sur ce compte est d'environ 72 k€/an. Notre direction veut au minimum garder 170 k€/an, idéalement passer à 3 ans de plus avec l'indexation Syntec, et vendre le module d'optimisation dynamique (38 k€/an) qu'ils avaient testé en pilote à Lyon avec −9 % de kilomètres.
>
> Ce qu'on livre en interne : un dossier de préparation (mandat signé par notre CEO, analyse des intérêts des deux côtés, solutions de repli, plan de concessions, scénarios), puis on négocie en novembre. Je veux aussi qu'on sache, dans six mois et dans un an, si l'accord était bon, pas seulement s'il a été signé. L'auteur du dossier, c'est notre directeur commercial avec moi ; le juge, c'est notre CEO, qui n'a pas participé au compte.

## Une bonne sortie contient

1. Le dossier de préparation (livrable) séparé de l'accord (issue) ; l'issue en zone : plancher 170 k€/an fixé par la direction, objectif nommé (durée, indexation, module), signés dans le mandat avant la première offre.
2. Notre solution de repli chiffrée (perte de 186 k€/an et de 14 % du récurrent, coût de service de 72 k€) et celle du client estimée (concurrent 150 à 170 k€/an plus 60 à 90 k€ de migration), marquée comme estimation.
3. Un tableau de score par sujet (prix, SLA, pénalités, durée, module, adoption des deux entrepôts) avec des poids pour chaque partie.
4. Un contrôle de Pareto sur les paquets et un seuil pour la partie la moins bien servie, choisis à l'avance.
5. La satisfaction ressentie mesurée après coup (quatre dimensions) et la durabilité à 6 et 12 mois (usage à Valence et Orléans, pas de résiliation, module adopté).
6. Une ligne « parties non représentées » : utilisateurs des entrepôts, notre équipe support (coût d'un SLA à 99,9 %), nos autres clients.
7. Une contre-partie simulée (la nouvelle DAF, ou le concurrent) en part cachée.
8. Le SLA à 99,9 % vérifié comme tenable par l'exploitation, et son coût ; chaque chiffre du dossier sourcé (le 99,7 % réel, le −40 % d'usage).
9. Le statut juridique du courrier du 12/09 (consultation sans dénonciation formelle) soumis à un juriste.
10. Une couverture automatique dite faible.

# Cas 3 — revue d'une grille de salaires

## Demande

> Il me faut le cahier de recette de notre revue de grille de salaires 2027, avant qu'on la lance.
>
> Nous sommes une entreprise de services numériques de 140 salariés (convention Syntec), 9 niveaux de classification internes rattachés aux positions de la convention, une grille de fourchettes (minimum, médiane, maximum) par niveau et par famille de métiers (développement, conseil, support, fonctions centrales). La grille n'a pas été revue depuis 2022. Constats remontés : compression entre les niveaux 3 et 5 (des confirmés embauchés en 2025 gagnent autant que des seniors présents depuis six ans), 19 salariés au-dessus du maximum de leur fourchette, 6 sous le minimum, un écart de rémunération femmes-hommes de 7,2 % à niveau égal sur la famille conseil d'après notre dernier calcul interne, et une demande des élus du CSE d'avoir enfin des critères écrits de passage d'un niveau à l'autre. On doit aussi se préparer aux obligations de transparence salariale de la directive européenne de 2023 (fourchettes dans les offres, droit à l'information, rapport sur les écarts).
>
> Budget : la direction a fixé une enveloppe de 3,2 % de la masse salariale annuelle chargée (masse de 8,9 M€ brut chargé), qui doit couvrir à la fois les mises en grille et les augmentations individuelles. Les données viennent de l'export de paie au 30/09 (un fichier avec matricule, niveau, famille, sexe, ancienneté, temps de travail, fixe, variable) et d'une étude de rémunération d'un cabinet achetée en septembre.
>
> Le livrable : la nouvelle grille (fourchettes par niveau et famille), les règles de positionnement et de passage, le coût de mise en grille et sa répartition, et une note de présentation au CODIR puis au CSE. La NAO commence en janvier ; les élus voudront discuter de la grille et de l'enveloppe. Le travail est fait par notre RRH avec un analyste qui s'appuie sur un agent pour les calculs dans le tableur ; je suis le DRH et je jugerai. Les salaires individuels ne doivent être vus que par la RRH, l'analyste et moi.

## Une bonne sortie contient

1. Des lignes mécaniques sur la grille : minimum < médiane < maximum, recouvrement entre niveaux borné, compression 3-5 traitée par une règle chiffrée, chaque salarié au moins au minimum conventionnel.
2. L'enveloppe recalculée (3,2 % de 8,9 M€ = 284,8 k€) et le coût total (mises en grille plus augmentations) qui tient dedans.
3. Les 19 au-dessus du maximum et les 6 sous le minimum traités par une règle écrite, et leur coût compté.
4. L'écart femmes-hommes recalculé à niveau égal, par famille, avec un seuil cible après révision.
5. Les comparaisons ramenées au temps plein, et une définition constante du variable (inclus ou non) : « passerait et serait faux ».
6. Chaque fourchette rattachée à un percentile de l'étude du cabinet.
7. Des critères de passage écrits et testés : deux personnes qui les appliquent au même dossier arrivent au même niveau.
8. La confidentialité : salaires individuels vus par trois personnes, le CSE n'a que des agrégats, petites cases masquées.
9. La NAO lue comme une issue (zone fixée à l'avance), avec l'annexe négociation.
10. Une part cachée qui vise l'agent du tableur (contrôle par un second calcul indépendant, quelques salariés vérifiés à la main) ; couverture forte pour la grille, faible pour la NAO.

# Cas 4 — proposition de loi négociée

## Demande

> Je suis collaborateur d'une sénatrice, rapporteure d'une proposition de loi transpartisane qui assouplit l'objectif de « zéro artificialisation nette » pour les communes rurales de moins de 2 000 habitants : une enveloppe garantie d'un hectare par commune sur 2021-2031, mutualisable à l'échelle de l'intercommunalité, la possibilité de décompter hors enveloppe les projets d'intérêt communal (école, maison de santé, logements sociaux), et un report de deux ans de l'intégration des objectifs dans les SCoT. Je veux le cahier de recette de notre travail, du texte de la commission jusqu'à la commission mixte paritaire.
>
> Les parties : notre groupe et deux autres groupes cosignataires au Sénat, qui veulent une victoire visible pour les maires ruraux avant les sénatoriales ; l'Association des maires ruraux, qui pousse pour aller plus loin (pas de plafond sur les projets d'intérêt communal) ; le gouvernement, qui accepte l'enveloppe mais refuse le report des SCoT et veut un décompte strict ; les associations environnementales et une partie des députés, qui y voient un détricotage de la loi Climat et résilience de 2021 ; les régions, qui ont déjà intégré l'objectif dans leurs SRADDET et craignent de devoir les réviser. À l'Assemblée, aucune majorité n'est assurée ; le texte peut être adopté conforme, modifié puis renvoyé en CMP, ou enterré.
>
> Ce que nous produisons : le texte de la commission et le rapport, les amendements de séance, une étude d'impact maison (le gouvernement n'en fera pas, c'est une proposition de loi) avec le nombre de communes concernées et les hectares en jeu, et la stratégie de négociation avec le gouvernement et les députés pour la CMP. La sénatrice veut savoir à l'avance ce qu'elle appellera un succès et ce qu'elle refusera de signer, et elle veut qu'on vérifie ensuite, à un an, si le texte est appliqué et s'il a tenu ses promesses aux maires sans faire exploser l'artificialisation. Le travail est fait par moi et une collègue ; le juge sera le directeur de cabinet du groupe, qui n'a pas suivi le dossier.

## Une bonne sortie contient

1. Le livrable (texte, rapport, amendements, étude d'impact, stratégie) séparé de l'issue (adoption, CMP, application) ; ce que la sénatrice refuse de signer écrit comme plancher avant la CMP.
2. Des lignes de légistique : chaque article modifie une disposition qui existe dans sa version en vigueur, les renvois existent, pas de contradiction entre articles.
3. L'étude d'impact chiffrée et sourcée (communes concernées, hectares en jeu), recalculable.
4. Les intérêts et solutions de repli de chaque partie (groupes, maires ruraux, gouvernement, associations environnementales, régions), estimés et marqués comme tels.
5. Une ligne « parties non représentées » : communes urbaines et périurbaines, futurs habitants, biodiversité et sols, générations suivantes — avec ce que le texte leur coûte (hectares ajoutés à l'échelle nationale).
6. La durabilité à un an : textes d'application, artificialisation mesurée, contentieux, éventuel contrôle de constitutionnalité.
7. Un risque constitutionnel (égalité devant la loi, seuil de 2 000 habitants) relu par un juriste.
8. Une contre-partie simulée (gouvernement ou associations) en part cachée.
9. Une couverture automatique dite très faible, et la satisfaction ressentie limitée aux négociateurs, pas aux électeurs.

# Cas 5 — réponse à un appel d'offres privé (annexe documents)

## Demande

> On répond à un appel d'offres privé et je veux les critères de réussite de notre offre avant qu'on commence à l'écrire.
>
> Le client : une mutuelle santé régionale (620 salariés, 14 agences), qui lance une consultation pour « un accompagnement à la transformation de la relation adhérent » : 40 à 60 jours de conseil sur 9 mois, diagnostic, ateliers avec les conseillers d'agence et le centre d'appels, feuille de route, puis appui au pilotage des trois premiers chantiers. Remise des offres le 14/11 à midi, sur leur plateforme, en PDF, 25 pages maximum hors annexes, avec le bordereau de prix à leur format Excel, les CV des intervenants et trois références de moins de trois ans. Critères annoncés : valeur technique et méthodologie 40 %, équipe et références 30 %, prix 30 %. Une soutenance de 45 minutes est prévue pour les trois premiers.
>
> Nous sommes un cabinet de deux associés et trois consultants. On a deux références en assurance, mais une seule de moins de trois ans ; la troisième serait un groupe de protection sociale, en 2021. On sait par un contact que deux gros cabinets sont consultés et que le directeur de la relation adhérent « ne veut plus de PowerPoint ». Notre taux journalier moyen est de 1 150 € HT ; en dessous de 950 € on perd de l'argent avec la sous-traitance d'un des consultants. On réutilise une partie d'une offre faite en juin pour une caisse de retraite.
>
> C'est moi et mon associé qui écrivons l'offre ; le juge sera notre troisième associé, qui n'a pas suivi le dossier. Je veux aussi savoir ce qu'on appellera un bon résultat, au-delà de gagner ou perdre.

## Une bonne sortie contient

1. Le demandeur est co-auteur : pas de lignes cachées, une demande scellée au troisième associé.
2. Une matrice de conformité tirée de la consultation : 25 pages hors annexes, PDF, bordereau Excel au format du client, CV, trois références de moins de trois ans, dépôt le 14/11 avant midi sur la plateforme.
3. La référence de 2021 relevée comme risque (plus de trois ans selon la date de remise), avec une question ou une parade.
4. La recherche des restes de l'offre de juin (nom de la caisse de retraite, exemples, chiffres) dans le PDF envoyé.
5. Le prix : jours × taux recalculés, taux au-dessus de 950 € HT, mêmes chiffres dans le texte et le bordereau.
6. Chaque élément du besoin traité : diagnostic, ateliers agences et centre d'appels, feuille de route, pilotage des trois chantiers.
7. La remarque « plus de PowerPoint » traduite en ligne vérifiable sur la forme de l'offre et de la soutenance.
8. L'issue en zone : soutenance obtenue, marché gagné à un taux au-dessus du plancher, et un « bon résultat » au-delà (retour d'analyse demandé au client en cas d'échec, par exemple).
9. La soutenance en `terrain`, et une contre-partie (acheteur simulé avec la grille annoncée) proposée au juge.

# Cas 6 — dissertation de classe préparatoire, grille annoncée (annexe documents)

## Demande

> J'enseigne la culture générale en classe préparatoire (concours des écoles de commerce). Je donne en novembre une dissertation de quatre heures sur table, sans document, huit pages au plus, sur le sujet : « Faut-il se fier aux experts ? ». Je veux écrire les critères de réussite de cette copie : je les donnerai aux étudiants avant l'épreuve, et je m'en servirai pour corriger, avec un collègue qui corrigera en double un tiers des copies.
>
> Ce que j'attends, en vrac : une introduction qui définit les termes (« se fier », « experts ») et pose une vraie tension, pas une question rhétorique ; un plan qui répond au sujet et pas à « les experts ont-ils raison ? » ; des références précises (pas « comme le dit un philosophe ») et pas seulement des philosophes : sociologie, histoire des sciences, un cas d'actualité traité sérieusement ; une conclusion qui tranche. J'ai 42 étudiants ; l'an dernier, beaucoup ont plaqué un cours appris par cœur sur « la science », et quelques copies de devoirs à la maison étaient manifestement écrites avec une IA. Cette fois c'est sur table, mais je referai le même sujet en devoir maison pour ceux qui étaient absents.
>
> Le barème du concours n'est pas publié en détail. Je veux une grille juste, que je puisse défendre devant un étudiant qui conteste sa note, et je veux savoir si cet exercice améliore vraiment leurs copies au concours de mai.

## Une bonne sortie contient

1. Les critères seront donnés aux étudiants : aucun critère caché sur les copies ; la part cachée teste la grille (une copie fictive de « cours plaqué » ou de remplissage ne doit pas obtenir une bonne note).
2. Le demandeur est le juge : la part cachée peut être écrite.
3. Chaque attente traduite en observable : termes définis, tension posée en question, plan qui répond au sujet et pas à un sujet voisin, références précises et de plusieurs disciplines, cas d'actualité traité, conclusion qui tranche.
4. Une ligne contre le cours plaqué (une partie qui ne sert pas la question posée).
5. La double correction : accord entre les deux correcteurs sur un tiers des copies, avec un seuil et une règle en cas d'écart.
6. Le devoir maison : la règle sur l'IA écrite, et une vérification orale sur un passage choisi par le juge.
7. Une note défendable : chaque critère pèse un nombre de points, et le correcteur peut montrer le passage qui justifie chacun.
8. L'issue (copies au concours de mai) en zone, avec ce qu'on compare et la limite de la mesure.
9. Une couverture mécanique quasi nulle (longueur seulement).

# Cas 7 — rénovation énergétique d'une maison (annexe travaux)

## Demande

> On rénove notre maison et je veux écrire, avant de signer les devis, ce que j'appellerai des travaux réussis, pour pouvoir les vérifier à la réception et après.
>
> La maison : 1975, 120 m² sur deux niveaux, chauffage au fioul, simple vitrage à l'étage, combles perdus isolés en 1990 avec 10 cm de laine de verre tassée. Diagnostic de performance énergétique en F. Les travaux prévus : isolation des murs par l'extérieur (ITE, 14 cm), isolation des combles par soufflage (40 cm), remplacement de 9 fenêtres, pompe à chaleur air-eau sur les radiateurs existants, VMC hygroréglable, dépose de la cuve à fioul. Budget total 78 k€ TTC, dont environ 31 k€ d'aides attendues si on atteint un gain d'au moins deux classes ; l'accompagnateur Rénov' nous suit. Objectif : passer en C, et sortir d'un chauffage à 2 600 € par an.
>
> Quatre entreprises : une pour l'ITE et les combles, un menuisier, un chauffagiste pour la PAC et la VMC, une pour la cuve. Pas de maître d'œuvre ; c'est moi qui coordonne. Les travaux doivent se faire entre mars et juin, en habitant la maison. On a un voisin mitoyen côté nord dont le mur sera touché par l'échafaudage, et on garde nos deux enfants à la maison pendant les travaux. Je ne suis pas du métier ; je jugerai, avec l'aide de l'accompagnateur.

## Une bonne sortie contient

1. Un test de réception par lot, écrit avant la signature des devis : épaisseur ou résistance thermique, performance des fenêtres, puissance et rendement de la pompe à chaleur, débits de la VMC.
2. Des points d'arrêt avant recouvrement : isolant de l'ITE avant l'enduit, épaisseur soufflée dans les combles, pose et étanchéité des fenêtres avant habillage.
3. Les interfaces entre lots, sans maître d'œuvre : fenêtres et ITE, VMC et étanchéité à l'air, PAC et radiateurs existants.
4. La réception par lot, réserves écrites, et ce qui bloque le paiement.
5. Les pièces exigées pour les aides présentes avant de payer ; le reste à charge recalculé (78 − 31 k€).
6. Le DPE après travaux en zone (C visé, deux classes de gain comme plancher, puisque les aides en dépendent).
7. La durabilité : première saison de chauffe, facture comparée aux 2 600 € par an, défauts à un an.
8. Les parties non représentées : le voisin mitoyen (état des lieux avant l'échafaudage), les enfants (sécurité du chantier habité).
9. Qui vérifie : le propriétaire n'est pas du métier, l'accompagnateur ou un tiers pour les mesures.

# Cas 8 — partie technique d'un cahier des charges de marché public (annexe documents)

## Demande

> Je suis chargée de mission numérique dans une communauté de communes (22 communes, 31 000 habitants). J'écris la partie technique du cahier des charges d'un marché à procédure adaptée : refonte du site internet et création d'un portail de démarches en ligne (inscriptions périscolaires, réservation de salles, demandes de bacs à ordures). Budget estimé : 60 k€ HT, plus la maintenance sur trois ans. Critères d'attribution prévus : valeur technique 60 %, prix 40 %. Publication prévue le 2 décembre.
>
> Contraintes connues : obligation d'accessibilité (RGAA), hébergement des données en France, reprise des 400 pages actuelles, interfaçage avec notre logiciel de facturation de la cantine (un éditeur qui fournit une API mal documentée), connexion par FranceConnect souhaitée, et des agents qui mettront à jour le site eux-mêmes après une formation. Les élus veulent « un site moderne et simple » et que « les habitants trouvent en trois clics ». La dernière refonte, en 2019, a été un échec : le prestataire a livré un site conforme sur le papier, mais les agents ne savaient pas l'administrer et les formulaires n'étaient pas accessibles sur téléphone.
>
> Je veux les critères de réussite de ma partie du cahier des charges : ce qui fera qu'elle est prête à publier, et ce qui permettra de choisir le bon prestataire puis de recevoir le site. Je l'écris seule ; le juge sera notre directeur général des services.

## Une bonne sortie contient

1. Les critères seront publiés : aucune part cachée sur les offres ; la part cachée teste le cahier des charges (une offre fictive qui coche tout sans servir le besoin ne doit pas gagner).
2. La demandeuse est l'auteure : demande scellée au DGS au lieu des lignes cachées.
3. « Moderne et simple » et « trois clics » traduits en observables (tâches réalisées par des habitants en test, nombre d'étapes mesuré).
4. Les deux échecs de 2019 transformés en exigences avec leur test de réception : administration par les agents après formation, formulaires accessibles sur téléphone.
5. Chaque exigence dit comment elle sera vérifiée à la réception (accessibilité auditée, reprise des pages et redirections, API de la cantine testée).
6. Le risque de l'API mal documentée traité dans le cahier (ce que le candidat doit chiffrer, ce que la collectivité fournit).
7. Les sous-critères de la valeur technique et leur pondération annoncés ; aucune solution ni éditeur nommé sans justification.
8. FranceConnect « souhaitée » tranché : exigence, option ou variante.
9. L'issue en zone : nombre d'offres conformes reçues, puis usage des démarches en ligne après mise en service.

# Cas 9 — cahier des charges d'une campagne publicitaire (aucune annexe dédiée)

## Demande

> Je suis responsable communication d'un réseau de 38 boulangeries artisanales franchisées en Bretagne et Pays de la Loire. On lance un appel d'offres auprès d'agences pour une campagne de printemps (mars à mai) : faire connaître la nouvelle gamme de pains au levain et ramener en boutique les 25-40 ans, qui achètent de plus en plus en grande surface. Budget : 90 k€ HT, création et achat d'espace compris (affichage local, réseaux sociaux, radio locale peut-être). Les franchisés paient la moitié via la cotisation marketing, et ils sont méfiants : la dernière campagne, en 2024, a eu des visuels primés mais aucun effet mesurable sur les ventes, et deux franchisés se sont plaints que leurs boutiques n'étaient même pas sur la carte du site.
>
> Je dois écrire le cahier des charges de la consultation, et je veux d'abord ses critères de réussite : ce qui fera que le CDC est prêt à envoyer à cinq agences, ce qui permettra de choisir la bonne, et ce qui dira en juin si la campagne a marché. On a les tickets de caisse par boutique et par semaine depuis 2022, et une carte de fidélité utilisée par environ 30 % des clients. Je l'écris avec notre directrice marketing ; c'est le comité des franchisés qui jugera.

## Une bonne sortie contient

1. Trois temps séparés : le CDC prêt à envoyer, le choix de l'agence, l'effet de la campagne en juin.
2. L'échec de 2024 traduit en exigence : un effet sur les ventes mesuré, pas des visuels primés ; et chaque boutique présente sur la carte et les supports.
3. Une mesure d'effet définie avant la campagne, à partir des tickets de caisse : période de référence, boutiques ou semaines de comparaison, part des 25-40 ans via la carte de fidélité (limite : 30 % des clients seulement).
4. L'issue en zone (plancher et objectif d'effet sur les ventes de la gamme), fixée par le comité avant la consultation.
5. Les franchisés comme partie : ceux qui paient la moitié jugent ; leur satisfaction et leur adhésion mesurées.
6. Une grille d'attribution annoncée aux agences, testée par une réponse fictive « belle mais sans mesure » qui ne doit pas gagner.
7. Les demandeuses sont auteures : demande scellée au comité.
8. Le budget de 90 k€ ventilé (création, espace) et tenu.

# Cas 10 — un mariage (aucune annexe dédiée)

## Demande

> On se marie le 13 juin prochain, dans une longère louée près de Vannes, 110 invités, cérémonie laïque dans le jardin puis dîner et soirée. Budget 24 k€, dont 9 k€ donnés par nos parents (les siens et les miens, pas à parts égales, et ça fait des histoires). Un traiteur, un DJ, une officiante, une photographe ; on gère tout le reste nous-mêmes avec des amis. Ma future belle-mère voudrait une messe le matin, ce qu'on ne veut pas ; ma grand-mère de 91 ans vient en fauteuil ; une dizaine d'enfants ; deux amis végans et une allergie aux fruits à coque. Mon compagnon veut surtout « que les gens s'amusent » ; moi je veux qu'on ne passe pas la journée à gérer des problèmes.
>
> Je voudrais qu'on écrive, avant de tout réserver, ce qu'on appellera un mariage réussi, et comment on saura si c'est le cas, le jour même et après. C'est nous deux qui organisons et nous deux qui jugerons.

## Une bonne sortie contient

1. Pas de juge séparé : pas de part cachée, mais des critères écrits par chacun seul, puis comparés.
2. Le livrable (l'organisation : réservations, plan, budget, logistique) séparé de l'issue (la journée vécue, les invités, la relation avec les familles).
3. Les besoins concrets testés : accès en fauteuil de la grand-mère, repas végans et sans fruits à coque vérifiés avec le traiteur, enfants.
4. Le budget : 24 k€ tenu, et la contribution inégale des parents traitée (qui paie quoi, ce que ça donne comme droit de regard).
5. La messe voulue par la belle-mère traitée comme une partie non représentée ou un désaccord à régler avant, sans en faire un critère imposé.
6. Les deux souhaits du couple traduits en signes observables (« que les gens s'amusent », « ne pas passer la journée à gérer »), dont un responsable du jour désigné qui n'est pas le couple.
7. Un plan de repli (pluie, cérémonie dans le jardin).
8. Une couverture automatique nulle, dite comme telle, sans rendre la chose ridicule.

# Cas 11 — une vie commune (aucune annexe dédiée)

## Demande

> Mon compagnon et moi sommes ensemble depuis six ans, sans enfant. On a décidé d'emménager ensemble en janvier, après quatre ans à vivre chacun chez soi à 40 km l'un de l'autre. On se dispute régulièrement sur les mêmes sujets : le partage des tâches, l'argent (je gagne 40 % de plus que lui), le temps passé avec nos amis respectifs, et le fait que je travaille souvent le soir. On s'aime et on veut que ça marche ; on a même pensé à voir une conseillère conjugale pour préparer ce passage, sans l'avoir encore fait.
>
> Je sais que c'est un drôle d'usage, mais j'aimerais qu'on se fixe, avant l'emménagement, des critères de réussite de notre vie commune : à quoi on verra dans trois mois, puis dans un an, que c'est une réussite, et ce qui devrait nous alerter. Je ne veux pas transformer notre couple en tableau Excel, mais je veux qu'on évite de découvrir dans deux ans qu'on n'avait pas la même idée de ce qu'on voulait. C'est nous deux qui jugerons.

## Une bonne sortie contient

1. Pas de juge séparé : critères écrits par chacun seul avant l'emménagement, comparés à une date convenue ; aucune part cachée.
2. Presque tout est issue, rien n'est mécanique ; dit sobrement.
3. Les quatre sujets de dispute traduits en signes observables, sans fixer d'avance la bonne réponse à la place du couple (partage des tâches, argent, amis, soirées de travail).
4. Des rendez-vous datés (trois mois, un an) et des signaux d'alerte.
5. La conseillère conjugale proposée comme regard extérieur, pas imposée.
6. Le ton : pas de tableau de pilotage du couple, pas de seuils chiffrés artificiels ; des critères que les deux reconnaissent.
7. Ce que le skill ne fait pas : pas de conseil conjugal, pas de jugement sur qui a raison.

# Cas 12 à 14 — demandes nues : le skill apporte-t-il ce que le thème exige ?

Test proposé par Amiel : un logiciel dont le cahier des charges ne parle pas de sécurité doit quand même recevoir des lignes de sécurité. Même question pour tout thème. Demandes d'une phrase, sans aucune exigence.

## Demandes

- Cas 12 : « Fais le document de critères de réussite d'un couple. » Le skill pose sa question (à quoi sert le livrable) ; cas 12b : la même demande, plus « C'est nous deux, ensemble depuis trois ans. On veut que notre couple aille bien dans la durée. »
- Cas 13 : « Écris les critères de réussite d'une application de prise de rendez-vous pour un cabinet de kinésithérapie : les patients réservent en ligne, le kiné voit son planning, les patients reçoivent un rappel par SMS la veille. »
- Cas 14 (témoin, absent des exemples du skill) : « Fais le document de critères de réussite d'une colocation à quatre étudiants. On est les quatre colocataires, on emménage en septembre pour l'année scolaire. »

## Une bonne sortie contient

1. Les exigences du thème, marquées `[inferred]`, que la demande ne cite pas : sécurité et données de santé pour l'application ; désir et sexualité, sécurité face à la violence ou à l'emprise, argent, projets pour le couple ; cadre légal, argent, vie privée, sécurité, départ en cours d'année pour la colocation.
2. Pour une dimension intime, la dimension nommée et ses signes laissés aux parties.
3. Aucune exigence de goût personnel ajoutée.

# Version 1.1.0 — corrections tirées d'un essai réel sur le module biais

Un agent Opus à contexte neuf a appliqué la 1.0.0 au cadrage, à la décomposition et au topo du 16/10 du module biais ; sa sortie a été comparée au cahier de recette écrit à la main et aux défauts de sept versions construites (session de comparaison, hors dépôt). Sept corrections génériques en sortent (CHANGELOG, 1.1.0). Rejoué : le cas 1 avec le topo (cas 1b, Opus), et deux cas sans rapport pour la non-régression (cas 2 et 13, Sonnet).

## Cas 1b, une bonne sortie 1.1.0 contient

1. Aucune ligne mécanique tirée d'un chiffre du topo que la décomposition a pu remplacer (le « 0,26 mL ») ; le point est en question ouverte.
2. Le code anonyme jugé sur la limite d'essais et sa durée de vie, pas sur 64 bits d'entropie.
3. Une ligne sur le recalcul d'une case masquée par soustraction (totaux, autre vue, avant/après), et sa version cachée.
4. Le mode dégradé écrit comme un résultat, par type de panne (réseau, appareil absent, service injoignable), vérifié par un essai à blanc et par la présence du matériel.
5. La personne qui ne participe pas suit ce que voient les autres.
6. Une passe « états » : reprise du questionnaire sans les réponses d'avant, écran « terminé » après effacement.
7. Un noyau de vingt à trente lignes marqué.
8. Toujours attrapés : l'équilibre par camp, l'effacement jusqu'au `-wal`, les trous de contenu.

## Cas 2 et 13, non-régression

Les critères de leur première passe tiennent toujours ; un noyau est marqué s'ils dépassent trente lignes ; le cas 13 écrit la panne du fournisseur de SMS comme un résultat.

# Version 1.2.0 — corrections de la relecture indépendante (Fable)

Vingt-trois constats sur 1.1.0 (A1 à A5, B1 à B10, C1 à C8 ; rapport hors dépôt, session de comparaison du module biais). Essais : un cas synthétique équivalent au cas biais, versionné (cas 15, B9), et quatre cas sans rapport avec lui. **Notation par un agent Opus à contexte neuf, qui n'a pas écrit le skill**, critère par critère, sur les sorties brutes.

## Cas 15 — module de vote anonyme d'un séminaire managers (synthétique)

Pièces : [`pieces/criteres-reussite/cas-15/`](pieces/criteres-reussite/cas-15/) (note d'intention de juin, compte rendu de septembre qui la corrige).

> Je suis la DRH. Écris les critères de réussite du module de vote de nos séminaires managers, que l'agence Pixelia va développer. Les deux documents sont dans ce dossier : note-intention-juin.md et compte-rendu-septembre.md. Lis-les entièrement. C'est moi qui recevrai le module et qui jugerai, avec la responsable formation.

Une bonne sortie contient :
1. Aucune ligne mécanique sur le chiffre de « 38 % » ni sur le quatrième dilemme, abandonnés en septembre ; le chiffre retenu demandé en question ouverte ou testé comme « sourcé et retenu ».
2. L'équilibre du tirage des versions testé sur la distribution, dans chaque session.
3. Un anonymat vérifié dans les fichiers et les journaux, y compris vis-à-vis de la DRH ; les petites cases masquées et non recalculables par soustraction.
4. La suppression vérifiée dans les octets (canari), et la preuve demandée par le CSE.
5. Le mode sans réseau écrit comme un résultat, vérifié par un essai à blanc.
6. Le manager qui ne vote pas : pas de donnée, et il suit la séance.
7. Le bloc visible ne cite aucune ligne cachée.
8. « Qui vérifie » nomme une indépendance vis-à-vis de l'agence, pas seulement une compétence.
9. Le code de session jugé sur la limite d'essais et la durée de vie, pas sur l'entropie.

## Cas 13n — appli kiné, demande nue, demandeur non précisé

La demande du cas 13. Une bonne sortie contient : 1. le demandeur déclaré inféré ou traité comme auteur, et donc une demande scellée au lieu de lignes cachées ; 2. aucune ligne H citée dans le bloc visible ; 3. pas de profil de charge de séance importé (des dizaines d'utilisateurs simultanés) ; 4. le choix d'hébergement des données de santé testé comme conforme, pas seulement documenté ; 5. un audit automatique d'accessibilité étiqueté `mécanique` et doublé d'une ligne qui juge l'usage réel.

## Cas 13g — appli kiné construite en boucle avec `/goal`

> Je vais faire construire une application de prise de rendez-vous pour mon cabinet de kinésithérapie (deux kinés, environ 120 rendez-vous par semaine) par Claude Code, qui travaillera en boucle avec /goal jusqu'à ce que le but soit atteint. Les patients réservent en ligne, chaque kiné voit son planning, les patients reçoivent un rappel par SMS la veille. Écris les critères de réussite, y compris le critère d'arrêt de la boucle. Je ne suis pas développeur ; c'est moi qui accepterai l'application.

Une bonne sortie contient : 1. les deux réglages distingués (évaluateur qui lit la conversation pendant la boucle, juge qui exécute avant l'acceptation) ; 2. ce que l'agent doit montrer : commande exacte et sortie brute complète, somme de contrôle des tests et nombre de tests à chaque tour ; 3. qui écrit et qui fige les tests (le juge, ou relus ligne à ligne par lui avant le premier tour), alors que le demandeur n'est pas développeur ; 4. la part cachée hors de la session de l'agent ; 5. un énoncé pour `/goal` de dix à quinze lignes ; 6. l'aveu que cet évaluateur ne distingue pas une sortie fabriquée.

## Cas 7 et cas 3, non-régression

Les critères de leur première passe, plus : aucune ligne H citée dans le bloc visible ; les seuils réglementaires (DPE, minimum conventionnel) gardés tels quels ; une vérification destructive ou intrusive marquée `[costly]` (cas 7) ; « qui vérifie » qui écarte l'auteur (cas 3, l'analyste et l'agent du tableur).

# Résultats

| Date | Cas | Modèle | Critères tenus | Sortie | Note |
|---|---|---|---|---|---|
| 2026-10-17 | 1 | Opus | 11/11 | hors dépôt (matériau privé) | 84 lignes visibles + 16 cachées ; 0,84 $, 5 min |
| 2026-10-17 | 1 | Sonnet | 11/11 | hors dépôt (matériau privé) | 80 + 15 ; attrape aussi le refus sans donnée créée, le passage wifi → 4G, l'horodatage qui permet de recouper ; 0,50 $, 6 min |
| 2026-10-17 | 2 | Sonnet | 10/10 | [v1](sorties/criteres-reussite/cas-2-renouvellement-saas-sonnet.md) | voit seul que le préavis du 30/09 est passé et que le plancher de 170 k€ est une préférence, pas un repli ; mais livre la part cachée à un demandeur co-auteur ; 0,36 $ |
| 2026-10-17 | 3 | Sonnet | 10/10 | [v1](sorties/criteres-reussite/cas-3-grille-salaires-sonnet.md) | 85 lignes ; enveloppe 284,8 k€ juste, temps partiel en ETP, valeurs collées dans le tableur en part cachée ; 0,33 $ |
| 2026-10-17 | 4 | Sonnet | 8/9 | [v1](sorties/criteres-reussite/cas-4-loi-negociee-sonnet.md) | manque la relecture constitutionnelle avant le vote (7) et ne limite pas la satisfaction ressentie aux négociateurs (9) ; part cachée livrée à l'auteur avec un simple avertissement ; 0,24 $ |
| 2026-10-17 | 2 | Sonnet, gabarit ajusté | 10/10 | [v2](sorties/criteres-reussite/cas-2-renouvellement-saas-sonnet-v2.md) | demande scellée au juge au lieu de la part cachée ; lignes bloquantes ; 0,29 $ |
| 2026-10-17 | 4 | Sonnet, gabarit ajusté | 9/9 | [v2](sorties/criteres-reussite/cas-4-loi-negociee-sonnet-v2.md) | ligne 12 : avis écrit sur l'égalité devant la loi (seuil de 2 000 habitants) avant le vote ; demande scellée au juge ; 0,25 $ |
| 2026-10-17 | 2, juge | Sonnet, `requester: judge` | — | [juge](sorties/criteres-reussite/cas-2-renouvellement-saas-juge-sonnet.md) | à partir du seul plan visible v2 : 13 lignes cachées sur les exigences demandées, couverture mise à jour, et une faiblesse de la ligne 14 visible relevée ; 0,19 $ |

| 2026-10-17 | 5 | Sonnet | 9/9 | [sortie](sorties/criteres-reussite/cas-5-offre-appel-offres-sonnet.md) | référence de 2021 interdite de passer pour récente, taux moyen sous 950 € par effet de mix, « perdre utilement » (notes par critère obtenues) en issue ; demande scellée ; 0,30 $ |
| 2026-10-17 | 6 | Sonnet | 9/9 | [sortie](sorties/criteres-reussite/cas-6-dissertation-sonnet.md) | grille publiée : la part cachée teste la grille par quatre copies fictives (cases cochées, sujet voisin, plan inhabituel, références inventées) ; refuse les détecteurs d'IA comme preuve ; en-tête manquant |
| 2026-10-17 | 7 | Sonnet | 9/9 | [sortie](sorties/criteres-reussite/cas-7-renovation-maison-sonnet.md) | 77 lignes ; acomptes liés aux points d'arrêt, dimensionnement de la PAC sur les radiateurs existants, signature des devis après accord pour les aides ; 0,42 $ |
| 2026-10-17 | 8 | Sonnet | 9/9 | [sortie](sorties/criteres-reussite/cas-8-cdc-marche-public-sonnet.md) | échecs de 2019 en tests de réception ; le portail qui affiche « enregistré » sans écrire dans le logiciel de la cantine ; avis du service marchés sur les critères ; demande scellée |
| 2026-10-17 | 9 | Sonnet | 8/8 | [sortie](sorties/criteres-reussite/cas-9-cdc-campagne-pub-sonnet.md) | effet mesuré contre Pâques et la saison, cannibalisation des autres pains, boutique la moins bien servie ; n'a pas lu l'annexe documents ; laisse les seuils « à fixer » par le comité plutôt que d'en proposer |
| 2026-10-17 | 10 | Sonnet | 8/8 | [sortie](sorties/criteres-reussite/cas-10-mariage-sonnet.md) | critères aveugles au lieu de la part cachée ; rappelle que la cérémonie laïque n'a pas de valeur légale ; coordinateur du jour qui n'est pas le couple ; amis aidants épuisés en « passerait et serait faux » |
| 2026-10-17 | 11 | Sonnet | 5,5/7 | [sortie](sorties/criteres-reussite/cas-11-vie-commune-sonnet.md) | critères aveugles, règle « la lecture la plus sévère l'emporte » ; mais des écarts en points et des virements à ±5 % alors que la demandeuse refuse le tableau Excel (6), et 11 lignes dites « mécaniques » (2) |
| 2026-10-17 | 9 | Sonnet, version finale | 8/8 | [v2](sorties/criteres-reussite/cas-9-cdc-campagne-pub-sonnet-v2.md) | lit l'annexe documents ; la grille note les références sur un effet avant/après, pas sur un prix créatif ; demande scellée en français ; 0,23 $ |
| 2026-10-17 | 11 | Sonnet, version finale | 7/7 | [v2](sorties/criteres-reussite/cas-11-vie-commune-sonnet-v2.md) | plus de points ni de pourcentages : des signes (« l'un des deux évite d'inviter par gêne »), les seuils de fréquence « à fixer ensemble », la relecture qui doit se faire dans une conversation, pas dans un tableur ; 0,10 $ |
| 2026-10-17 | 12 | Sonnet | — | [sortie](sorties/criteres-reussite/cas-12-couple-demande-nue-sonnet.md) | pose une seule question avant d'écrire, comme prévu ; 0,01 $ |
| 2026-10-17 | 12b | Sonnet, avant | 1/3 | [sortie](sorties/criteres-reussite/cas-12b-couple-sonnet.md) | que de la procédure (bilans, rituels, voix égale) ; l'intimité en une ligne euphémisée ; ni désir, ni sexualité, ni violence |
| 2026-10-17 | 13 | Sonnet, avant | 3/3 | [sortie](sorties/criteres-reussite/cas-13-appli-kine-sonnet.md) | RGPD, HDS, consentement SMS et STOP, HTTPS, accessibilité, accès au rendez-vous d'un autre par l'URL : le thème logiciel est déjà couvert |
| 2026-10-17 | 12b | Sonnet, exigences du thème | 3/3 | [v2](sorties/criteres-reussite/cas-12b-couple-sonnet-v2.md) | sécurité et respect (plancher « non négociable »), désir et sexualité nommés et laissés à chacun, argent et charge mentale, projets, épreuves ; « je n'ai ajouté ni sport ni vacances » |
| 2026-10-17 | 13 | Sonnet, exigences du thème | 3/3 | [v2](sorties/criteres-reussite/cas-13-appli-kine-sonnet-v2.md) | pas de régression ; ajoute le changement d'heure, le rendez-vous pris par téléphone, les absences comme issue |
| 2026-10-17 | 14 | Sonnet, exigences du thème | 3/3 | [sortie](sorties/criteres-reussite/cas-14-colocation-sonnet.md) | témoin : bail, assurance, caution, examens, partenaires, « aucune pression, aucun contrôle », départ en cours d'année, isolement |
| 2026-10-17 | 1b | Opus, 1.1.0 | 8/8 | hors dépôt (matériau privé) | topo signalé antérieur aux arbitrages, aucune ligne mécanique sur « 0,26 mL » ; plus de seuil d'entropie ; soustraction (ligne et version cachée dans le temps) ; panne par type ; le refus suit la séance ; reprise vierge, « séance terminée » ; noyau de 30 lignes (2 h contre une journée) ; 1,03 $ |
| 2026-10-17 | 13 | Sonnet, 1.1.0 | non-régression tenue | [v1.1](sorties/criteres-reussite/cas-13-appli-kine-sonnet-v1.1.md) | données de santé, consentement et STOP, accès croisés gardés ; panne du fournisseur de SMS écrite comme un résultat ; noyau de 24 lignes ; 0,20 $ |
| 2026-10-17 | 2 | Sonnet, 1.1.0 | non-régression tenue | [v1.1](sorties/criteres-reussite/cas-2-renouvellement-saas-sonnet-v1.1.md) | plancher contre repli, préavis, demande scellée gardés ; noyau de 25 lignes ; 0,29 $ |
| 2026-10-17 | 15 | Sonnet, 1.2.0 | 8,5/9 (juge indépendant) | [v1.2](sorties/criteres-reussite/cas-15-vote-seminaire-managers-sonnet-v1.2.md) | sources abandonnées sans ligne mécanique ; mode sans réseau resté en question plutôt qu'en résultat ; 0,59 $ |
| 2026-10-17 | 13n | Sonnet, 1.2.0 | 4,5/5 (juge indépendant) | [v1.2](sorties/criteres-reussite/cas-13n-appli-kine-demandeur-inconnu-sonnet-v1.2.md) | demandeur inconnu traité comme auteur, demande scellée ; un test de 20 réservations simultanées que rien ne justifie ; 0,21 $ |
| 2026-10-17 | 13g | Sonnet, 1.2.0 | 5,5/6 (juge indépendant) | [v1.2](sorties/criteres-reussite/cas-13g-appli-kine-goal-sonnet-v1.2.md) | énoncé `/goal` qui omettait dix lignes mécaniques ; erreur sur la longueur des SMS concaténés ; 0,18 $ |
| 2026-10-17 | 13g | Sonnet, 1.2.0 retouché | 5,5/6 (juge indépendant) | [v1.2b](sorties/criteres-reussite/cas-13g-appli-kine-goal-sonnet-v1.2b.md) | l'énoncé liste les 34 lignes mécaniques et dit pourquoi il écarte les autres ; part cachée hors de la condition d'arrêt ; énoncé un peu long (19 lignes) ; 0,22 $ |
| 2026-10-17 | 7 | Sonnet, 1.2.0 | 9,5/12 (juge indépendant) | [v1.2](sorties/criteres-reussite/cas-7-renovation-maison-sonnet-v1.2.md) | aucun renvoi H dans le visible, carottage marqué `[costly]` ; reste à charge non recalculé, une vérification intrusive non marquée, plancher de coût inversé ; 0,49 $ |
| 2026-10-17 | 3 | Sonnet, 1.2.0 | 10,5/13 (juge indépendant) | [v1.2](sorties/criteres-reussite/cas-3-grille-salaires-sonnet-v1.2.md) | aucun renvoi H dans le visible ; minimum conventionnel vérifié par cellule, pas par salarié ; 0,46 $ |
Rapport de la notation indépendante de 1.2.0 : [notation-independante-1.2.0.md](sorties/criteres-reussite/notation-independante-1.2.0.md). Les retouches faites après lui (plancher inversé quand moins vaut mieux, synthèse relue contre les tableaux, énoncé `/goal` complet) n'ont été rejouées que sur le cas 13g.

Jusqu'à 1.1.0 : notation par l'auteur du skill, pas par un juge indépendant : à rejouer avec `banc.py` d'ix-recipes et des juges d'autres fournisseurs avant de s'y fier.

## Ce qui a demandé d'ajuster le gabarit

1. **Le demandeur est l'auteur** (cas 2 et 4) : la part cachée lui était remise, précédée d'un « ne lisez pas ». Le skill prend maintenant un champ `requester` ; quand c'est l'auteur, il n'écrit pas la part cachée mais une demande scellée au juge (les exigences à garder, le nombre de lignes, relancer le skill avec `requester: judge`).
2. **Longueur** : 51 à 95 lignes par cahier. La synthèse nomme maintenant les **lignes bloquantes** (Sonnet l'avait inventé seul sur le cas 1).
3. **En-tête** : deux sorties commençaient par un préambule ou mettaient l'en-tête dans un bloc de code ; l'en-tête vient maintenant en premier, l'alerte dans la synthèse.
4. **Annexe négociation** : un plancher au-dessus du repli est une préférence, pas un point de retrait (trouvé par le cas 2, désormais demandé) ; la compatibilité avec les normes supérieures relue avant le vote (manquée au cas 4) ; le questionnaire de satisfaction mesure les négociateurs, pas ceux qu'ils représentent.
5. **Annexe logiciel** : les situations que le cahier de référence du cas 1 avait et que les sorties ont manquées (changer sa réponse tant que l'étape est ouverte, autre navigateur, mode sombre), plus les règles appliquées par le serveur et pas seulement par l'interface, et le contenu caché absent de tout ce que le client reçoit.

6. **Sujets sans annexe** (cas 9 à 11, après la remarque d'Amiel : le skill doit servir à n'importe quel appel d'offres, une campagne de publicité, un mariage, une relation) : le rôle dit maintenant que le geste vaut pour tout sujet et que la méthode tient seule ; quand il n'y a pas de juge séparé, la part cachée devient des **critères aveugles** (chacun écrit seul ses signes de réussite, comparés à une date convenue) ; pour un sujet personnel, des signes que les parties reconnaissent plutôt que des notes et des pourcentages (cas 11) ; le cahier des charges de n'importe quel appel d'offres renvoie à l'annexe documents (cas 9 ne l'avait pas lue) ; les libellés de la demande scellée sont bilingues (ils restaient en anglais dans des sorties en français).
7. **Critères publiés** (cas 6 et 8) : quand les auteurs connaîtront la grille (appel d'offres, grille annoncée aux élèves), pas de critère caché sur leur travail ; la part cachée teste la grille par des réponses fictives qui cochent tout sans servir le besoin.

8. **Exigences du thème** (cas 12 à 14) : le modèle apportait de lui-même les exigences d'un thème à normes fortes (la sécurité d'un logiciel) mais se rabattait sur la procédure pour un couple. L'étape 1 demande maintenant ce que tout spécialiste du thème vérifierait sans qu'on le demande, surtout ce que la demande tait parce que c'est intime, gênant ou tenu pour acquis, et l'étape 5 ajoute la famille « le plan couvre les problèmes déjà nommés et manque la dimension que personne n'a nommée ». L'exemple « couple » figurant dans le skill, la colocation sert de témoin.

## Cas 1 face au cahier de recette existant (16/10, 33 tests)

Lu après les passages, comme convenu.

**Ce que les sorties attrapent et que le cahier existant manquait :**
- l'équilibre du tirage par camp, et non seulement au global (le cahier existant : « écart d'au plus 2 » sur 30) ;
- l'effacement vérifié dans les octets du fichier SQLite et de ses fichiers `-wal` / `-shm` par une valeur canari (le cahier existant : « inspecter la base », que `DELETE` suffit à satisfaire) ;
- l'absence de trou dans chaque écran rendu, variante par variante, et la présence du script de débriefing avec ses messages clés (le cahier existant : « relire le script », pas de test sur ce qui s'affiche) ;
- le moteur générique jamais testé : jouer un autre sujet sans toucher au code, aucun texte du contenu dans le code ;
- les garde-fous côté serveur (étape fermée, accueil avant l'item, accueil figé « à froid ») appelés directement par l'API, et l'autre variante absente du JSON et du JS avant le dévoilement ;
- l'anonymat jusque dans les journaux (code à côté d'une IP), les URL et l'horodatage ;
- une charge doublée avec le piège `database is locked`, la non-régression d'ia-atelier, l'indépendance des deux tirages, les chiffres identiques entre les deux cadrages de C3 ;
- l'issue en zone (participation, mécanisme vu, pas de retournement, pas de poussée vers un camp), que le cahier existant ne mesurait pas du tout ;
- l'intégrité de la boucle (sommes de contrôle, tests non affaiblis, mutants) et une part cachée de 15 à 16 lignes ;
- pour chaque ligne, le type de preuve et qui vérifie.

**Ce que le cahier existant avait et que les sorties ont manqué ou laissé en question :**
- modifier son vote tant que l'item est ouvert, compté une fois (R11) ;
- rescanner le QR dans un autre navigateur (R4) ;
- le mode sombre (R29) ;
- un plan B papier décrit concrètement (R28) : les sorties demandent qu'il soit écrit et répété, sans le décrire ;
- les questions d'accueil reposées en fin de séance (R16, R20) : les sorties ne l'inventent pas et le posent en question ouverte ; le cahier existant reposait sur un choix de conception absent du cadrage ;
- Opus manque aussi le refus sans donnée créée (R6) et le passage wifi → 4G (R27), que Sonnet attrape.

**Prix** : 80 à 100 lignes contre 33. Le cahier existant se lit en dix minutes ; les sorties demandent un tri, d'où les lignes bloquantes ajoutées au gabarit.

**Limite de la preuve** : le skill a été écrit en connaissant les trois trous du cahier existant. Les attraper ne prouve pas grand-chose ; les cas 2 à 4 et ce que les sorties ajoutent au-delà de ces trois points mesurent mieux le skill.
