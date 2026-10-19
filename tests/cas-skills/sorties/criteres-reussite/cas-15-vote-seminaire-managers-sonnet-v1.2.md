<!-- Sortie brute de criteres-reussite 1.2.0, Sonnet, 0.59 $, 7 min. Cas : ../../criteres-reussite.md -->

---
status: draft
skill: criteres-reussite
deliverable_kind: logiciel (petite application web de vote en séance, plus textes et chiffres qu'elle porte)
author: l'agence Pixelia (équipe, pas un agent en boucle, à confirmer)
judge: la DRH et la responsable formation. Elles lisent les résultats mais n'exécutent pas les contrôles. Un vérificateur technique indépendant de Pixelia les exécute (à désigner, voir questions).
requester: judge (vous êtes DRH, vous recevez le module et vous jugez). Plan visible et part cachée sont donc tous deux écrits.
---

# Critères de réussite : module de vote des séminaires managers

## Synthèse / Summary

On livre une application web hébergée chez Pixelia. Trois dilemmes y existent chacun en deux versions tirées au sort, avec une échelle de 1 à 5, et leurs résultats agrégés par version sont projetés. Les engagements sont l'anonymat total y compris vis-à-vis de la DRH, aucun résultat individuel et la suppression des réponses à la fin de chaque session. Le module est « fini » quand l'anonymat et la suppression sont prouvés dans les fichiers, pas seulement à l'écran. Il l'est aussi quand les élus du CSE ont vu le dispositif et la preuve avant le 14 novembre, et que la répétition dans la salle réelle réussit.

- **Cahier visible :** 58 lignes (41 mécanique, 7 relecture, 10 terrain). Un script peut en clore environ 70 %, et ce sont celles qui portent l'anonymat, la suppression et le tirage. Ni l'effet du débrief, ni la confiance des managers, ni l'acceptation par le CSE ne se règlent par script.
- **Sources datées (étape 2) :** le compte rendu du 18 septembre l'emporte sur la note de juin. Il y a trois dilemmes et non quatre, le temps partiel est retiré et le chiffre Cadremploi est abandonné. Aucune ligne n'est donc écrite sur le contenu de ces trois points.
- **Hypothèses `[inférées]` :**
  - Pixelia est une équipe humaine.
  - Les textes des dilemmes ne figurent dans aucun des deux documents ; je teste donc leur forme, pas leur fond.
  - Les seuils `[proposé]` sont à confirmer par vous.
- **Calendrier :** nous sommes le 17 octobre et la livraison est prévue le 20. Le vérificateur doit être désigné et les scripts gelés avant la livraison. Le 14 novembre 2026 tombe un samedi.
- **Règle des scripts :** les scripts des lignes mécaniques sont écrits par le vérificateur, ou écrits par Pixelia et relus ligne à ligne par lui, puis gelés avant la livraison. Sinon la ligne compte comme relecture.

**Lignes bloquantes :** 2, 12, 17, 20, 27, 29, 30, 32, 33, 38, 39, 45, 50.
**Noyau (rejouable en séance courte, sans terrain ni ligne cachée) :** 1, 2, 3, 4, 6, 7, 8, 9, 11, 12, 15, 17, 20, 25, 27, 28, 29, 30, 32, 33, 34, 35, 36, 37, 38, 39, 40, 42, 47, 48.

Dans les tableaux, **V** désigne le vérificateur technique : un développeur indépendant de Pixelia, désigné par la DRH, qui travaille sur des données synthétiques uniquement. **Jury** désigne la DRH et la responsable formation.

## Exigences / Requirements

| E | Exigence | Source | Livrable ou issue |
|---|---|---|---|
| E1 | Faire voir aux managers que leurs décisions varient selon des détails sans importance, sans les mettre en cause personnellement | note juin : « Objectif » | issue |
| E2 | 40 à 60 managers par session, 4 sessions de novembre à février, vote sur téléphone | note juin : « Dispositif » | livrable (la participation est une issue) |
| E3 | Trois dilemmes, chacun en deux versions qui ne diffèrent que par un détail, échelle de 1 à 5 | note juin + CR : « Trois dilemmes et non quatre » | livrable |
| E4 | Le temps partiel est retiré, car il est trop proche d'un cas réel en cours | CR : décisions | livrable |
| E5 | Les versions sont tirées au sort | note juin | livrable |
| E6 | Résultats agrégés par version projetés, puis débrief par l'animatrice | note juin | livrable |
| E7 | Chiffre Cadremploi abandonné, remplacé par ceux de l'Observatoire des inégalités, sourcés précisément | CR : décisions | livrable |
| E8 | Anonymat total, y compris vis-à-vis de la DRH | note juin : « Engagements » | livrable |
| E9 | Aucun résultat individuel | note juin | livrable |
| E10 | Réponses supprimées à la fin de chaque session | note juin | livrable |
| E11 | Les élus du CSE voient le dispositif avant la première session | CR | livrable |
| E12 | Les élus reçoivent la preuve que les réponses sont réellement supprimées | CR | livrable |
| E13 | Accès par lien et code affichés, sans connexion au compte d'entreprise | CR | livrable |
| E14 | Application web hébergée chez Pixelia, livrée le 20 octobre, première session le 14 novembre | CR | livrable |
| E15 | Un manager qui ne veut pas voter peut le faire sans trace (point ouvert, version minimale) | CR : points ouverts `[inféré]` | livrable |
| E16 | La salle en sous-sol au siège est utilisable, et il est dit ce qui tient sans réseau (point ouvert) | CR : points ouverts `[inféré]` | livrable |
| E17 | Rôles étanches côté serveur, code de session protégé contre les essais en série | `[inféré]` thème | livrable |
| E18 | Fonctionne sur les téléphones réels des managers, accessible | `[inféré]` thème | livrable |
| E19 | Les managers sont informés des engagements avant de répondre, et c'est vrai | `[inféré]` thème | livrable |
| E20 | Les résultats projetés se lisent honnêtement (effectifs, rien d'interprété automatiquement) | `[inféré]` thème : 20 à 30 personnes par version, le bruit peut passer pour un effet | livrable |

## Issue visée / Outcome zone

Ces seuils sont fixés par vous avant le début du travail. Je les propose, vous les confirmez. Il n'y a volontairement aucune cible sur l'écart entre les deux versions : ce n'est pas une mesure de réussite, et une cible pousserait à truquer.

| E | Issue | Plancher (échec en dessous) | Cible (succès au-dessus) | Fixé par | Mesuré quand |
|---|---|---|---|---|---|
| E1 | Les managers disent avoir vu qu'un détail peut peser sur leurs décisions | 60 % d'accord `[proposé]` | 80 % d'accord `[proposé]` | DRH | fiche papier anonyme en fin de session |
| E1 | Les managers ne se sont pas sentis visés personnellement | au plus 20 % se sentent visés `[proposé]` | au plus 5 % `[proposé]` | DRH | idem |
| E8 | « J'ai répondu franchement parce que c'était anonyme » | 75 % d'accord `[proposé]` | 90 % d'accord `[proposé]` | DRH | idem |
| E2 | Part des présents qui répondent aux 3 dilemmes | 60 % `[proposé]` | 85 % `[proposé]` | DRH | effectifs affichés par le module, chaque session |
| E11, E12 | Le CSE a vu le dispositif et reçu la preuve, sans réserve non traitée | pas vu 7 jours avant le 14/11 | vu, aucune réserve ouverte | DRH avec le CSE | avant la 1re session |

## Critères vérifiables / Checks

| # | Élément ou situation | Vérification | Résultat attendu | Preuve | Qui vérifie |
|---|---|---|---|---|---|
| 1 | E3 : dilemmes servis | Dérouler une session test complète et lister tout ce que l'application contient (données, admin, API) | Exactement 3 dilemmes, chacun avec exactement 2 versions ; aucun 4e dilemme ni version résiduelle | mécanique | V |
| 2 | E3 : écart entre les deux versions | Comparer mot à mot les deux versions de chaque dilemme dans la page servie | Seuls diffèrent le détail testé (prénom, âge, 3e détail) et les accords grammaticaux qu'il impose, listés dans un tableau validé par le jury avant le gel ; zéro autre écart (ponctuation, ordre, mot) | mécanique | V ; tableau fixé par le jury |
| 3 | E3 : aucun autre indice | Lire chaque paire en aveugle et dire ce qui change | Le lecteur ne nomme que le détail prévu ; aucun métier genré, ton ou adjectif ne différencie autrement ; la question posée est identique | relecture | responsable formation + lecteur sans enjeu, qui n'ont pas rédigé les textes |
| 4 | E4 : temps partiel absent | Chercher `temps partiel\|mi-temps\|partiel` dans les pages rendues (toutes versions), les réponses d'API, les données initiales et l'admin | 0 occurrence | mécanique | V |
| 5 | E4 : aucun cas réel | Lire les 3 dilemmes en 2 versions | Aucun ne permet de reconnaître la situation en cours ni une personne réelle | relecture | DRH (seule à connaître le cas) ; le cas n'est pas transmis à Pixelia |
| 6 | E3, E7 : aucune lacune visible | Produire toutes les pages et messages de chaque rôle, état et version ; chercher `[à compléter]\|TODO\|TBD\|XXX\|lorem\|{{\|}}\|undefined\|null\|NaN\|projet X` et les blocs requis vides | 0 occurrence ; chaque dilemme décrit une situation précise (l'exemple de juin dit « le projet X ») | mécanique | V |
| 7 | E3 : échelle 1 à 5 | Afficher chaque question ; appeler l'API directement avec 0, 6, 3.5, « abc », vide, deux valeurs | Échelle identique et étiquetée aux deux extrémités dans les deux versions ; seuls les entiers 1 à 5 sont acceptés ; le reste est refusé sans rien enregistrer | mécanique | V |
| 8 | E5 : répartition globale | 10 000 participants simulés × 3 dilemmes, graine fixe, puis 100 graines | Chaque version à 50 % ± 2 points `[proposé]` | mécanique | V |
| 9 | E5 : équilibre dans une session | Simuler des sessions de 40 à 60 participants (arrivées groupées, tardives, départs) | Par dilemme, écart entre versions servies ≤ 2 à tout moment `[proposé]` | mécanique | V |
| 10 | E5 : indépendance entre dilemmes `[inféré]` | 10 000 participants simulés | Chacune des 8 combinaisons de versions à 12,5 % ± 2 points `[proposé]` | mécanique | V |
| 11 | E5 : stabilité | Recharger, revenir en arrière, rouvrir le lien dans le même navigateur, à chaque état | Même version, même état ; aucun nouveau tirage | mécanique | V |
| 12 | E5, E8 : l'autre version reste cachée | Pendant une étape ouverte, capturer tout ce que reçoit le navigateur d'un participant (HTML, JSON, scripts, fichiers statiques) ; chercher les mots propres à l'autre version et toute étiquette de version | 0 occurrence : le participant ne peut pas savoir qu'une autre version existe | mécanique | V |
| 13 | E13 : accès sans compte | Depuis un téléphone sans compte d'entreprise, ouvrir le lien et saisir le code | Première question atteinte ; aucun champ nom, e-mail, téléphone ou identifiant ; seul champ de saisie : le code | mécanique | V |
| 14 | E13, E17 : essais de code | Depuis une même adresse, 15 codes faux en 1 minute | Au-delà de 10 faux par minute `[proposé]`, les essais faux sont refusés ≥ 60 s ; même message pour code faux et code expiré | mécanique | V |
| 15 | E13, E2 : toute la salle derrière une adresse | 60 participants simulés derrière une seule adresse publique, après 20 essais faux depuis cette adresse | Les 60 rejoignent avec le bon code en ≤ 2 min ; aucun blocage collectif | mécanique | V |
| 16 | E13 : vie du code | Utiliser le code avant l'ouverture, pendant, après la fin, 4 h après l'ouverture ; lire un échantillon de 200 codes | Refusé avant, après la fin et après 4 h `[proposé]` ; accepté pendant ; aucun caractère ambigu (0/O, 1/I/l) ; saisie insensible à la casse | mécanique | V |
| 17 | E17 : droits par rôle, côté serveur | Avec le jeton d'un participant, appeler directement chaque fonction de l'animatrice (ouvrir, clore, publier, terminer, verrouiller, lire les effectifs) | Refus 401/403 pour chacune ; aucun état modifié | mécanique | V |
| 18 | E17 : console de l'animatrice | Ouvrir la console sans son identifiant secret ; essayer des adresses voisines | Refusé ; l'identifiant n'est pas le code de session | mécanique | V |
| 19 | E17 : fermer les arrivées `[inféré]` | L'animatrice verrouille ; un nouvel arrivant saisit le code | Refusé avec message ; les participants déjà entrés continuent | mécanique | V |
| 20 | E2 : états côté participant | Pour chaque état (avant début, étape ouverte, étape close, après fin, après suppression), noter ce que le participant voit et peut faire | Avant début : « pas commencé », aucune question. Ouverte : question et réponse possible. Close : réponse impossible, y compris par appel direct. Après fin et suppression : « session terminée », aucune donnée | mécanique | V |
| 21 | E2 : reprise | Recharger l'écran participant et la console animatrice dans chaque état | Même état retrouvé, réponses déjà données conservées | mécanique | V |
| 22 | E2 : réponse changée ou doublée | Changer sa réponse pendant l'étape ; double-clic ; renvoi | Une seule réponse comptée par participant et par étape (la dernière) ; effectif inchangé | mécanique | V |
| 23 | E2 : arrivée tardive | Rejoindre pendant la 2e étape | Arrive sur l'étape courante, jamais sur une étape close ; version tirée respectant la ligne 9 | mécanique | V |
| 24 | E15 : ne pas voter `[inféré]` | Suivre la projection sans ouvrir le lien ; ouvrir le lien sans répondre | Suivre la projection n'exige rien sur le téléphone ; ne pas répondre ne crée aucune réponse ; l'animatrice ne voit que des effectifs (connectés, ayant répondu), jamais de liste | mécanique | V |
| 25 | E2 : pic de réponses | 120 participants simulés `[proposé : 2 × 60]` rejoignent et répondent à la même question en 60 s, sur l'hébergement réel | 100 % des réponses comptées une fois ; 95e centile de confirmation ≤ 2 s `[proposé]` ; 0 erreur | mécanique | V |
| 26 | E16 : coupure d'un téléphone | Couper le réseau 30 s pendant une étape ouverte, puis le rétablir | Réponse déjà envoyée conservée ; réponse non envoyée soit envoyée une seule fois au retour, soit la personne est prévenue ; jamais de doublon | mécanique | V |
| 27 | E6 : exactitude des agrégats | Jeu synthétique connu (dont des participants qui sautent un dilemme) ; comparer la projection à un recalcul indépendant | Moyenne, répartition 1 à 5 et effectif de chaque version identiques au recalcul à la précision affichée ; le dénominateur est le nombre de réponses reçues, pas de connectés | mécanique | V |
| 28 | E6, E8 : pas de chiffre avant publication | Appeler les résultats pendant une étape ouverte (participant, appel non authentifié) ; tenter une réponse après publication | Refus avant publication ; après publication les réponses sont refusées, donc les chiffres projetés sont figés | mécanique | V |
| 29 | E8 : petites cellules | Jeux synthétiques à (0, 40), (4, 36), (5, 35) réponses par version | Si une version a moins de 5 réponses `[proposé]`, aucun agrégat de ce dilemme n'est affiché (ni l'une ni l'autre version), avec un message neutre ; à 5 ou plus, affiché | mécanique | V |
| 30 | E8 : recalcul par soustraction | À partir de tous les chiffres affichés dans toutes les vues et tous les états (totaux, par version, avant/après l'arrivée d'une personne), tenter de retrouver une valeur masquée | Aucune valeur masquée récupérable ; aucun total ne la livre | mécanique | V |
| 31 | E20, E1 : lecture honnête | Lire les écrans projetés | Effectif affiché par version ; aucun libellé calculé qui interprète un écart (« biais », « discrimination ») ; aucune ventilation par équipe, direction, sexe ou âge de manager | relecture | jury |
| 32 | E8, E9 : le stockage ne relie à personne | Lire le schéma ; lancer une session test avec valeurs repères (nom fictif, IP et user-agent de test, identifiant d'appareil) ; les chercher dans la base et ses fichiers annexes | Aucune table ou colonne ne contient nom, e-mail, téléphone, IP, user-agent, identifiant d'appareil durable ou compte ; valeurs repères introuvables à côté d'une réponse | mécanique | V, sur copie des fichiers |
| 33 | E8 : journaux et rapports d'erreur | Après la session test (et des erreurs provoquées), chercher dans journaux d'accès et applicatifs, outil de suivi d'erreurs et caches | Aucune ligne ne relie une adresse, un appareil ou un jeton à une valeur de réponse ou à une version ; aucune réponse dans une URL ni un corps journalisé | mécanique | V |
| 34 | E8 : heure et ordre | Voter dans un ordre et à des heures connus, puis lire le stockage | Aucun horodatage de réponse plus fin que l'étape ; l'ordre de stockage ne restitue pas l'ordre d'arrivée | mécanique | V |
| 35 | E8 : services tiers | Capturer toutes les requêtes réseau des pages participant, console et projection | Toutes vers le domaine du module ; 0 analytique, police, script ou pixel tiers ; seul stockage navigateur : celui de la session | mécanique | V |
| 36 | E8, E9 : aucune sortie individuelle | Lister toutes les routes et fonctions ; tenter chaque export, liste, tableau de bord | Aucune ne restitue une réponse individuelle ; la DRH n'a aucun compte ni accès ; les seules sorties sont la projection et ce qui est listé à la ligne 43 | mécanique | V |
| 37 | E19 : information des managers | Lire le texte affiché avant la 1re réponse et le confronter aux résultats des lignes 32 à 34 et 38 à 42 | Il existe, est atteint avant toute réponse, sans lacune ; il dit : anonyme y compris vis-à-vis de la DRH, aucun résultat individuel, suppression en fin de session ; chaque phrase est vraie d'après les mesures (délai de sauvegarde mentionné s'il en subsiste) | relecture | jury, V pour les mesures |
| 38 | E10 : suppression dans le stockage actif | Planter une valeur repère dans réponses, jetons, version tirée et code de session ; l'animatrice termine la session ; chercher les octets bruts dans la base et ses annexes (journal d'écriture, WAL), journaux archivés, caches, fichiers temporaires, exports. Si la base est SQLite, vérifier par recherche d'octets, pas par le réglage | Valeur introuvable partout | mécanique | V, sur copie des fichiers |
| 39 | E10 : sauvegardes et instantanés | Même valeur repère ; chercher dans la dernière sauvegarde, le dernier instantané de l'hébergeur pris après la fin, et chez tout service tiers ayant reçu des données | Valeur introuvable. Si un délai est inévitable : durée écrite, acceptée par la DRH avant la réunion CSE, et reprise dans le texte de la ligne 37 | mécanique | V ; Pixelia donne accès (voir questions) |
| 40 | E10 : fin oubliée | Ouvrir une session sans la terminer ; accélérer l'horloge | Suppression automatique ≤ 2 h après la dernière activité `[proposé]` ; valeur repère introuvable | mécanique | V |
| 41 | E10 : échec de suppression | Provoquer une erreur pendant la suppression | L'animatrice et Pixelia sont alertées ; la suppression est rejouée jusqu'à réussite ; aucune réponse lisible via le module entre-temps | mécanique | V |
| 42 | E10 : côté téléphone | Après fin puis suppression, inspecter stockage local, cookies et cache du téléphone test ; rouvrir le lien | Aucune réponse ni version ; l'écran dit « session terminée » | mécanique | V |
| 43 | E10 : ce qui reste | Lister tout ce qui subsiste après suppression et le comparer à la liste arrêtée par la DRH avant livraison | Identique à la liste. Par défaut : rien d'autre qu'une trace technique sans contenu de réponse. Si des agrégats sont conservés, les lignes 29 et 30 s'y appliquent | mécanique | V |
| 44 | E12 : rapport de preuve | Relire le rapport de suppression remis au CSE | Il couvre chaque lieu de stockage du schéma d'architecture fourni par Pixelia (base, annexes, journaux, caches, sauvegardes, instantanés, tiers) avec méthode, commande, sortie brute et date ; aucun lieu de l'architecture n'est absent | relecture | responsable formation, V ; Pixelia fournit l'architecture |
| 45 | E11, E12 : démonstration au CSE | Séance où les élus voient les 3 dilemmes en 2 versions et le déroulé, puis la suppression d'une valeur repère ; ils peuvent désigner un lieu à fouiller | Tenue au plus tard le 7 novembre `[proposé]` ; la recherche demandée par les élus est faite en séance ; aucune réserve laissée sans réponse | terrain | DRH organise, V exécute, élus du CSE observent |
| 46 | E10 : vérification en réel | Le jour de la 1re session réelle, puis après la dernière : compter les lignes des tables de réponses et chercher des fichiers de session en production | 0 ligne, 0 fichier de réponses ; sauvegardes selon la ligne 39 | terrain | V, sans lire de contenu |
| 47 | E7 : ancien chiffre absent | Chercher `38 %\|Cadremploi\|écarté une candidature` dans les pages rendues et tous les supports livrés (présentations, notes, PDF, courriels) | 0 occurrence | mécanique | V |
| 48 | E7 : chiffres de remplacement | Pour chaque chiffre présent, ouvrir la source citée | Source précise (titre du rapport, année, page ou tableau) ; valeur, population et année identiques à la source ; chiffres dérivés recalculés (`calc-check`) | relecture | responsable formation, qui n'a pas inséré les chiffres |
| 49 | E7 : dernier rapport | Chercher sur le site de l'Observatoire au jour du contrôle | Le rapport cité est le plus récent publié | relecture | responsable formation |
| 50 | E18, E2 : téléphones réels, salle réelle | Répétition dans la salle en sous-sol avec ≥ 10 téléphones personnels (≥ 2 Android anciens, ≥ 2 iPhone Safari, un en grand texte, un en mode sombre), via lien et code projetés | Tous rejoignent et répondent aux 3 dilemmes ; du code lu à la 1re question ≤ 60 s `[proposé]` | terrain | responsable formation + V, avant le 14/11 |
| 51 | E16 : réseau de la salle | Même répétition : wifi du siège seul, puis données mobiles seules ; places devant, au fond, sur les côtés | À chaque place testée, au moins un des deux réseaux permet de rejoindre et de répondre ; sinon la part touchée est mesurée et rapportée | terrain | idem |
| 52 | E18 : lisibilité à la projection | Depuis le fond de la salle, sur le projecteur réel | Lien et code lisibles et recopiables ; graphiques lisibles sans dépendre de la couleur seule | terrain | responsable formation |
| 53 | E18 : audit automatique | Outil d'audit d'accessibilité sur les écrans participant et projection | 0 erreur grave ou critique (ne règle pas la ligne 54) | mécanique | V |
| 54 | E18 : lecteur d'écran et grand texte | VoiceOver ou TalkBack : rejoindre, lire le dilemme, donner 1 à 5 ; texte à 200 % | Accompli sans aide ; zones de réponse ≥ 44 px `[proposé]` ; aucun texte tronqué | terrain | responsable formation, avec une personne usagère de lecteur d'écran si possible |
| 55 | E6 : animatrice autonome | Répétition complète avec 10 collègues non managers : ouvrir, clore, publier, verrouiller, terminer ; panne de la console en cours d'étape | Elle y arrive sans le développeur ; liste des gestes qu'elle ne sait pas faire seule : vide | terrain | animatrice + responsable formation |
| 56 | E1 : issue ressentie | Fiche papier anonyme en urne en fin de session, 2 questions (compris, visé) | Voir la zone de l'issue visée | terrain | responsable formation, sans lien avec le module |
| 57 | E8 : confiance dans l'anonymat | Même fiche, 1 question | Voir la zone de l'issue visée | terrain | idem |
| 58 | E2 : participation | Effectifs (ayant répondu / présents) relevés sur le compteur du module à chaque session | Voir la zone de l'issue visée | terrain | animatrice |

## Ce qui passerait et serait faux / What could pass and still be wrong

- La suppression est constatée à l'écran et dans la table principale, mais la valeur survit dans le journal d'écriture, les journaux archivés ou une sauvegarde → lignes 38, 39.
- Une petite cellule est masquée mais recalculable par un total affiché ailleurs, ou par deux affichages successifs → lignes 28, 29, 30.
- Les deux versions « ne diffèrent que par un détail » à l'œil nu, mais un accord ou un métier genré trahit un autre indice, ou les deux versions sont envoyées au téléphone et choisies côté client → lignes 2, 3, 12.
- Le limiteur d'essais passe son test unitaire mais bloque toute la salle derrière une seule adresse → ligne 15.
- Le texte d'information promet la suppression alors qu'une sauvegarde garde les réponses : le document existe, la promesse est fausse → lignes 37, 39.
- La moyenne est juste quand tous répondent, fausse quand certains sautent un dilemme → ligne 27.
- Le chiffre Cadremploi a disparu de l'écran mais reste dans une note d'animation ou un PDF → ligne 47.
- Tout passe sur ordinateur, mais pas sur de vieux téléphones ni sous terre → lignes 50, 51.
- L'anonymat tient à l'écran, mais l'ordre ou l'heure d'arrivée permettent de reconnaître qui a voté quoi → ligne 34.
- La « preuve de suppression » est un document qui affirme, sans recherche dans les fichiers → lignes 44, 45.

## Non testable en l'état / Not testable as stated

- **E1 :** « faire voir sans mettre en cause » dépend du débrief de l'animatrice, que le module ne contrôle pas. On mesure seulement l'effet ressenti (lignes 56 et 57). Quelle part de la réussite attendez-vous du module, et quelle part du débrief ?
- **E3 :** les textes des trois dilemmes, et le 3e détail testé, ne figurent dans aucun des deux documents. La note de juin cite trois détails pour quatre dilemmes. Quels sont les trois dilemmes retenus, qui les rédige, et quel est le tableau des écarts autorisés (ligne 2) ?
- **E7 :** les chiffres de remplacement ne sont pas choisis. Quels chiffres, où affichés, et avant ou après le vote ? Un chiffre sur l'accès des femmes à l'encadrement montré avant le vote peut influencer les réponses au dilemme du prénom, et brouiller la mesure.
- **E15 :** la décision est en suspens. Rien demandé au manager ? Un bouton « je ne réponds pas » ? Le vote à main levée est à éviter, car il lève l'anonymat. La ligne 24 couvre le minimum.
- **E16 :** hors réseau, le module ne fonctionne pas. Faut-il un mode sans réseau, ou seulement une répétition réussie dans la salle (lignes 50 et 51) ? Si la salle n'a aucun réseau le jour J, que doit-il rester vrai (séance menée jusqu'au bout, anonymat, suppression) ?

## Couverture / Coverage

| Kind | Visible | Who |
|---|---|---|
| mécanique | 41 | scripts de V, gelés avant livraison |
| relecture | 7 | jury, V pour les mesures |
| terrain | 10 | répétitions avant le 14/11, 1re session réelle, fiches de fin de session |

Un script peut clore près de 70 % des lignes, et ce sont celles qui engagent la DRH devant le CSE : anonymat, suppression, tirage, résultats. Il ne dit rien de l'effet du séminaire ni de la confiance des managers, qui relèvent de l'issue visée et du terrain.

## Questions ouvertes / Open questions

1. **Qui est V ?** C'est urgent, puisque la livraison est le 20 octobre. V a besoin d'un accès contractuel à une copie des fichiers, des journaux et de la liste des sauvegardes et instantanés chez Pixelia. Où le module est-il hébergé, et avec quels sous-traitants ?
2. **Que livre Pixelia le 20 :** une adresse en ligne, ou aussi le code et un accès de déploiement ?
3. **Après la session :** les agrégats sont-ils conservés ou détruits (ligne 43) ? Quel délai de sauvegarde acceptez-vous, le cas échéant ?
4. **Seuils `[proposé]` :** les confirmez-vous (5 réponses minimum, 2 h, 4 h, 7 jours, 120 simultanés, zones de l'issue visée) ?
5. **Preuve pour le CSE :** quel format satisfait les élus ? Veulent-ils leur propre expert ?
6. **Double vote :** rouvrir le lien dans un autre navigateur crée un second participant. Sans identité, c'est une limite acceptée, que l'animatrice repère par l'écart entre connectés et présents. L'acceptez-vous ?
7. **Date :** le 14 novembre 2026 est un samedi. Est-ce voulu ?
8. **Pixelia et les agents de code :** Pixelia fait-elle itérer un agent de code jusqu'à ce que les tests passent ? Si oui, je rédige le critère d'arrêt de la boucle.
9. **Lignes 5 et 48 :** si vous avez rédigé les dilemmes ou inséré les chiffres, quelqu'un d'autre doit les relire à votre place.

✂ ----- PART CACHÉE — pour le juge seul, ne pas transmettre à l'auteur / HIDDEN PART — judge only -----

## Part cachée / Hidden part

Chaque ligne teste une exigence que Pixelia connaît déjà (E dans le cahier visible), par d'autres entrées ou sous un autre angle. Elles sont exécutées par V, hors de l'espace de Pixelia. Si une ligne échoue, on dit à Pixelia l'exigence ou la famille d'exigences, jamais le test ni son entrée. Une ligne qui a échoué puis été corrigée est « brûlée » et remplacée.

| # | Élément ou situation | Vérification | Résultat attendu | Preuve | Qui vérifie |
|---|---|---|---|---|---|
| H1 | E10 : octets bruts, au-delà des requêtes | Valeur repère glissée aussi dans les en-têtes (User-Agent, langue), le code de session et le nom de l'animatrice. Après la fin, recherche d'octets sur l'image disque entière : journaux compressés (.gz) et tournés, swap, fichiers temporaires, couches de conteneur, rapports de plantage | Valeur introuvable | mécanique | V |
| H2 | E10 : redémarrage | Tuer le processus ou redéployer en pleine session, session abandonnée sans fin ; attendre l'échéance de la ligne 40 | La suppression a bien lieu après redémarrage ; la planification n'est pas perdue avec la mémoire ; données absentes | mécanique | V |
| H3 | E10 : restauration d'une sauvegarde | Restaurer la dernière sauvegarde dans un environnement vierge et y chercher la session test | Aucune réponse ; durée de conservation des sauvegardes conforme à ce que dit le texte de la ligne 37 | mécanique | V |
| H4 | E10 : contrôle inopiné | Après une session réelle choisie par le jury (ni la 1re ni annoncée), chercher dans la production et la liste des instantanés des lignes ou fichiers de cette session | 0 ligne, 0 fichier, sans lire de contenu | terrain | V |
| H5 | E8, E9 : ré-identification par recoupement | V observe une session synthétique (liste des présents, ordre et heures approximatives des votes). Avec la base entière, les journaux et les sauvegardes, il tente de rattacher chaque réponse à une personne (jetons, ordre, heures, groupes d'adresses, user-agent) | Aucune réponse attribuable mieux qu'au hasard | mécanique | V |
| H6 | E8 : erreurs provoquées | Provoquer erreurs serveur, code faux, hors-ligne et mauvaise requête en capturant ce qui part vers l'outil de suivi d'erreurs ou une page d'erreur | Aucun jeton, réponse, version ni identifiant de participant dans les rapports | mécanique | V |
| H7 | E8 : accès de l'exploitant | Lister les comptes d'administration et d'exploitation de Pixelia et ce qu'ils peuvent ouvrir en production, hors module | Aucun accès à des réponses identifiables ; ce qu'un exploitant peut lire ne relie pas une réponse à une personne | relecture | V ; DRH pour la portée contractuelle |
| H8 | E5 : imposer sa version | Appeler l'API avec un paramètre de version (`v=B`, corps, en-tête, cookie modifié) | Ignoré par le serveur ; la version servie ne change pas | mécanique | V |
| H9 | E5, E3 : téléchargement intégral côté client | Tout récupérer comme un navigateur (chunks, cartes de source, JSON aux adresses prévisibles, commentaires HTML) et chercher les deux prénoms et âges | Une seule version par dilemme est présente | mécanique | V |
| H10 | E5 : équilibre sous contrainte | 30 sessions simulées de 40 à 60 avec arrivées groupées, départs, reconnexions avec stockage effacé, second navigateur | Équilibre ≤ 2 tenu parmi les participants servis ; l'effectif de connectés de l'animatrice augmente (le doublon est visible) | mécanique | V |
| H11 | E3 : lecture en aveugle | 10 lecteurs reçoivent chacun une version, sans savoir qu'il y en a deux, et expliquent ce qui leur paraît compter dans la décision ; deux autres reçoivent la paire et nomment ce qui change | Un seul écart nommé ; les explications ne ciblent pas le détail testé comme évidence | relecture | jury, lecteurs sans enjeu |
| H12 | E8, E6 : soustraction à grande échelle | 1 000 sessions synthétiques générées (une version à 0 à 4 réponses, réponses toutes identiques, arrivée d'une personne entre deux affichages) ; résolution de toutes les valeurs masquées à partir de toutes les vues | Aucune cellule masquée récupérable | mécanique | V |
| H13 | E6 : agrégats par un autre calcul | 50 sessions aléatoires avec réponses sautées, comparées à un recalcul écrit par V | Identiques, y compris les arrondis | mécanique | V |
| H14 | E6, E8 : résultats appelés par la porte de service | Interroger les points d'accès de résultats avec identifiants devinés, jeton de participant, sans jeton, pendant et après étape | Rien avant publication ; rien hors de l'animatrice | mécanique | V |
| H15 | E7, E4 : restes dans les recoins | Chercher l'ancien chiffre et « temps partiel » dans l'historique du dépôt, les données initiales, notes d'animation, PDF exportés, commentaires HTML, balises `title` et `meta`, page 404, textes alternatifs | 0 occurrence dans les livrables ; l'historique est tracé s'il en reste | mécanique | V |
| H16 | E7 : tous les chiffres de tous les supports | Relever chaque chiffre de chaque support livré (pas seulement les écrans) et vérifier source, population et année | Tous sourcés et identiques à la source | relecture | responsable formation |
| H17 | E19 : promesse contre mesure | Confronter chaque phrase du texte d'information aux résultats de H1, H3 et H5 | Aucune phrase contredite par les mesures | relecture | jury, V |

**Pièges gardés seulement ici :**
- H2 : la planification de suppression perdue au redémarrage.
- H6 : les jetons dans les rapports d'erreur.
- H8 : la version imposée par un appel direct.
- H3 : la restauration d'une sauvegarde.
- H5 : le recoupement que ne ferait pas un test de schéma.
- H14 : les résultats lus par une porte de service.

**Exigences gardées, deux lignes au moins chacune :**
- E10 : H1, H2, H3, H4.
- E8 et E9 : H5, H6, H7.
- E5 et E3 : H8, H9, H10, H11.
- E6 : H12, H13, H14.
- E7 et E4 : H15, H16.
- E19 : H17, appuyée sur H1, H3 et H5.

### Couverture complète / Full coverage

| Kind | Visible | Hidden | Who |
|---|---|---|---|
| mécanique | 41 | 12 | scripts de V, hors de l'espace de Pixelia pour les cachés |
| relecture | 7 | 4 | jury, V |
| terrain | 10 | 1 | répétitions, 1re session réelle, contrôle inopiné |

Au total, 53 lignes mécaniques sur 75 : une boucle ou un pipeline peut les clore, et elles pèsent lourd. Les lignes de relecture et de terrain, moins nombreuses, décident de l'acceptation par le CSE et de la confiance des managers.