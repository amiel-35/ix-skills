# Notation criteres-reussite 1.2.0 (sorties Sonnet), juge indépendant

Critères : `tests/cas-skills/criteres-reussite.md`, sections « Version 1.2.0 », « Cas 7 » et « Cas 3 ». Sorties : `tests/cas-skills/sorties/criteres-reussite/*-sonnet-v1.2.md`. Les numéros de ligne renvoient aux fichiers de sortie. Barème : 1 tenu, 0,5 en partie, 0 non.

Contrôles mécaniques faits sur les cinq sorties :
- Lignes H citées avant le « ✂ » (recherche `H[0-9]+` avant la ligne de coupe) : aucune, dans les cinq sorties.
- Décompte des lignes par type, refait par script : il correspond aux totaux annoncés partout (15 : 41/7/10 visibles + 12/4/1 cachées ; 13n : 34/3/7 ; 13g : 30/5/9 ; 7 : 19/13/31 + 3/4/11 ; 3 : 36/21/8 + 9/5/2). Les pourcentages annoncés (70 %, environ trois quarts, deux tiers, 30 %, 55 %) sont justes.
- Dates : le 14/11/2026 est bien un samedi (cas 15, l. 24) ; le 25/10/2026 est bien le dimanche du passage à l'heure d'hiver (13n l. 75, 13g l. 78).

## Cas 15 : module de vote anonyme

| # | Critère | Note | Preuve |
|---|---|---|---|
| 1 | Rien de mécanique sur « 38 % » ni sur le 4e dilemme ; le chiffre retenu en question ouverte ou testé comme sourcé | 1 | l. 19 : le CR l'emporte, aucune ligne sur le contenu abandonné ; l. 119 et l. 73 (lignes 47 et 1 du cahier) ne testent que l'**absence** (« 0 occurrence », « aucun 4e dilemme ») ; chiffre de remplacement en l. 48-49 (sourcé, le plus récent) et l. 149 (question). Réserve : lu à la lettre, la l. 119 est une ligne mécanique « sur » le 38 %. Je la compte comme conforme parce qu'elle applique la décision de septembre. |
| 2 | Équilibre du tirage testé sur la distribution, dans chaque session | 1 | l. 80 (global, 100 graines), l. 81 « Par dilemme, écart entre versions servies ≤ 2 à tout moment » sur des sessions de 40 à 60 ; l. 82 (indépendance), H10 |
| 3 | Anonymat vérifié dans fichiers et journaux, y compris vis-à-vis de la DRH ; petites cases masquées, sans recalcul par soustraction | 1 | l. 104-105 (stockage, journaux) ; l. 108 « la DRH n'a aucun compte ni accès » ; l. 101 (seuil de 5) ; l. 102 « Aucune valeur masquée récupérable » |
| 4 | Suppression vérifiée dans les octets (canari) ; preuve demandée par le CSE | 1 | l. 110 « Planter une valeur repère… chercher les octets bruts » ; l. 116 (rapport de preuve), l. 117 (démonstration aux élus) |
| 5 | Mode sans réseau écrit comme un résultat, vérifié par un essai à blanc | 0,5 | Essai à blanc dans la salle réelle : l. 122-123. Mais le comportement hors réseau reste une question, pas un résultat attendu : l. 151 « hors réseau, le module ne fonctionne pas. Faut-il un mode sans réseau… ? » |
| 6 | Manager qui ne vote pas : aucune donnée, il suit la séance | 1 | l. 96 « Suivre la projection n'exige rien… ne pas répondre ne crée aucune réponse » |
| 7 | Le bloc visible ne cite aucune ligne cachée | 1 | aucune référence `H*` avant la l. 175 (vérifié par script) |
| 8 | « Qui vérifie » nomme une indépendance vis-à-vis de l'agence | 1 | l. 30 « un développeur indépendant de Pixelia, désigné par la DRH » |
| 9 | Code de session jugé sur la limite d'essais et la durée de vie, pas sur l'entropie | 1 | l. 86 (≤ 10 faux/min, refus ≥ 60 s), l. 87 (salle derrière une seule adresse), l. 88 (vie du code : avant, pendant, après, 4 h) |

**Total cas 15 : 8,5/9**

## Cas 13n : appli kiné, demandeur inconnu

| # | Critère | Note | Preuve |
|---|---|---|---|
| 1 | Demandeur inféré ou traité comme auteur, donc demande scellée au lieu de lignes cachées | 1 | l. 9 « traité comme auteur ; aucune part cachée n'est écrite » ; l. 140-144 : demande scellée seulement, aucune ligne H |
| 2 | Aucune ligne H citée dans le bloc visible | 1 | aucune référence `H*` dans le fichier |
| 3 | Pas de profil de charge de séance importé | 0,5 | l. 24 dit bien « quelques patients en même temps, pas un pic de masse », mais l. 94 teste quand même « 20 réservations simultanées », p95 < 2 s. C'est un profil de charge que rien dans la demande ne justifie, et il contredit l. 24. (l. 63 est un test de concurrence sur un même créneau, ce qui est légitime.) |
| 4 | Hébergement des données de santé testé comme conforme, pas seulement documenté | 1 | l. 84 « conforme… pas seulement “documenté” », avec certificat et périmètre ; l. 112. Réserve : la règle (certification HDS) n'est pas nommée ; « ce que la règle exige » oblige le vérificateur à la connaître. |
| 5 | Audit automatique d'accessibilité `mécanique`, doublé d'une ligne d'usage réel | 1 | l. 91 (audit, mécanique) ; l. 92 (clavier et lecteur d'écran, terrain) ; l. 90 (5 personnes sur téléphone) |

**Total cas 13n : 4,5/5**

## Cas 13g : appli kiné construite en boucle `/goal`

| # | Critère | Note | Preuve |
|---|---|---|---|
| 1 | Deux réglages distingués : évaluateur qui lit la conversation, juge qui exécute | 1 | l. 136-139 (évaluateur, étape 13) et l. 141-145 (juge qui exécute, étape 12) |
| 2 | L'agent montre la commande exacte et la sortie brute, plus somme de contrôle et nombre de tests à chaque tour | 1 | l. 150 « la commande exacte et sa sortie brute complète » ; l. 154 « somme de contrôle… et le nombre de tests » |
| 3 | Qui écrit et fige les tests (le juge, ou relus ligne à ligne avant le premier tour), le demandeur n'étant pas développeur | 1 | l. 8, l. 28 ; l. 142 « écrits ou relus ligne à ligne par une personne indépendante, puis gelés avant le premier tour » ; l. 153 |
| 4 | Part cachée hors de la session de l'agent | 1 | l. 9 (aucune part cachée écrite ici) ; l. 175 « dans une session que l'agent… ne peut pas lire » |
| 5 | Énoncé `/goal` de 10 à 15 lignes | 0,5 | l. 149-157 : 9 lignes, une de moins que le minimum |
| 6 | Aveu que l'évaluateur ne distingue pas une sortie fabriquée | 1 | l. 138 « Il ne peut pas distinguer une sortie fabriquée d'une sortie réelle » ; l. 28 |

**Total cas 13g : 5,5/6**

## Cas 7 : rénovation énergétique

| # | Critère | Note | Preuve |
|---|---|---|---|
| 1 | Test de réception par lot écrit avant signature (R ou épaisseur, fenêtres, puissance et rendement de la PAC, débits VMC) | 0,5 | l. 87 (test de réception de chaque lot écrit au contrat) ; l. 81, 105, 109, 111, 122. Ni la puissance ni le rendement de la PAC (COP/SCOP) n'apparaissent. l. 81 dit seulement « performance PAC », et l. 118 ne mesure que des températures départ/retour. |
| 2 | Points d'arrêt avant recouvrement (ITE avant l'enduit, épaisseur soufflée, fenêtres avant l'habillage) | 1 | l. 105-106 (« Avant la sous-couche », « Avant l'enduit ») ; l. 108-109 ; l. 111 (« Avant la finition ») |
| 3 | Interfaces sans maître d'œuvre : fenêtres/ITE, VMC/étanchéité à l'air, PAC/radiateurs | 0,5 | Fenêtres/ITE : l. 85. PAC/radiateurs : l. 114 (« chaque radiateur couvre sa pièce »). VMC/étanchéité à l'air : absente du plan, renvoyée en l. 197 (« Il n'est pas dans le plan actuel ») |
| 4 | Réception par lot, réserves écrites, ce qui bloque le paiement | 1 | l. 136 (réserves datées, assignées, bloquantes) ; l. 137 (5 % retenus jusqu'à la levée) ; l. 89, l. 128 |
| 5 | Pièces exigées pour les aides présentes avant de payer ; reste à charge recalculé (78 − 31 k€) | 0,5 | Pièces : l. 90, l. 138-139. Le reste à charge de 47 k€ n'apparaît nulle part (vérifié par recherche) ; l. 71 et l. 193 renvoient la trésorerie au demandeur |
| 6 | DPE après travaux en zone (C visé, deux classes comme plancher) | 1 | l. 68 « D (2 classes, condition des aides) \| C » ; l. 142 |
| 7 | Durabilité : premier hiver, facture comparée aux 2 600 €, défauts à un an | 1 | l. 150-153 (hiver, DJU), l. 69 (zone rapportée aux 2 600 €), l. 155-156 (garantie, contrôle à 12 mois) |
| 8 | Parties non représentées : voisin (état des lieux avant l'échafaudage), enfants | 1 | l. 96 « accord écrit… état contradictoire du mur » ; l. 102-103 (enfants), l. 112 |
| 9 | Qui vérifie : le propriétaire n'est pas du métier, l'accompagnateur ou un tiers prend les mesures | 0,5 | Bien traité pour les points d'arrêt (l. 105-109, l. 190). Mais des mesures de réception restent au propriétaire : l. 122 débits VMC « Vous, avec un débitmètre », l. 123 bruit VMC « Vous ou l'accompagnateur », H7 |
| 10 | Aucune ligne H citée dans le bloc visible | 1 | aucune référence `H*` avant la l. 200 |
| 11 | Seuils réglementaires (DPE) gardés tels quels | 1 | l. 68, l. 142 ; l. 80 marge `[proposed]` sous la limite C/D, sans toucher à la limite ; l. 116 émergence 5/3 dB(A), « à confirmer » |
| 12 | Vérification destructive ou intrusive marquée `[costly]` | 0,5 | H4 (carottage) est marqué, l. 211, ainsi que l. 149 et H16. Mais H3 « ouvrir 3 des 9 tableaux et 2 traversées » (l. 210), elle aussi intrusive, ne l'est pas, et l. 236 la propose même comme repli moins cher que H4 |

**Total cas 7 : 9,5/12**

## Cas 3 : revue d'une grille de salaires

| # | Critère | Note | Preuve |
|---|---|---|---|
| 1 | Lignes mécaniques : min < médiane < max, recouvrement borné, compression 3-5 par règle chiffrée, **chaque salarié** au moins au minimum conventionnel | 0,5 | l. 88, l. 90, l. 94-95 tenus. Le minimum conventionnel n'est testé que par cellule (l. 93 « min de chaque cellule ≥ minimum conventionnel »), jamais salarié par salarié. Or l. 100 admet « ou exception datée et écrite » sous le minimum de cellule, et l. 102 tolère 5 % de salariés hors fourchette |
| 2 | Enveloppe recalculée (284,8 k€) et coût total qui tient dedans | 1 | l. 16 et l. 49 « 3,2 % de 8,9 M€ chargés = 284 800 € » (juste) ; l. 117 |
| 3 | Les 19 et les 6 traités par une règle écrite, coût compté | 0,5 | Les 19 : règle écrite en l. 97-98. Les 6 : une comparaison (l. 100), pas de règle. Coût compté pour les 6 (l. 120), pas pour la règle des 19 |
| 4 | Écart F/H recalculé à niveau égal, par famille, avec seuil cible | 1 | l. 84, l. 104-105 (4 familles et par niveau) ; l. 72 (≤ 5 % plancher, ≤ 2 % cible) |
| 5 | Temps plein et définition constante du variable, en « passerait et serait faux » | 0,5 | Tenu pour l'écart F/H : l. 103 (ETP, fixe ou total, figés avant calcul) et l. 151. Pas pour les autres comparaisons de grille (l. 94, 95, 100, 102 ne disent pas ETP), et l. 195 pose encore la question de l'ETP |
| 6 | Chaque fourchette rattachée à un percentile de l'étude du cabinet | 0,5 | l. 86 vérifie source, n et date de chaque cellule ; l. 101 un écart à la « référence marché ». Le percentile reste une question (l. 161), aucune ligne ne l'exige |
| 7 | Critères de passage testés : deux personnes, même dossier, même niveau | 1 | l. 109 « Deux lecteurs classent 12 profils… ≥ 80 % d'accord » ; H7 |
| 8 | Confidentialité : trois personnes, agrégats pour le CSE, petites cases masquées | 1 | l. 126 (droits : RRH, analyste, DRH) ; l. 125 (cellule < 5, aucun matricule ni nom) ; H9-H10 |
| 9 | NAO lue comme une issue (zone fixée d'avance), avec l'annexe négociation | 1 | l. 71 (zone NAO), l. 135-137 (mandat, gabarit), l. 20 (annexe lue) |
| 10 | Part cachée qui vise l'agent du tableur (second calcul indépendant, quelques salariés vérifiés à la main) ; couverture forte pour la grille, faible pour la NAO | 0,5 | Second calcul : H1, H2, H3 (l. 206-208). Aucune vérification à la main de quelques salariés (H12 est un script). Couverture dite en l. 174 |
| 11 | Aucune ligne H citée dans le bloc visible | 1 | aucune référence `H*` avant la l. 198 |
| 12 | Seuils réglementaires (minimum conventionnel) gardés tels quels | 1 | l. 92 (texte officiel en vigueur, avenant cité), l. 93 (≥ minimum, prorata du temps partiel) |
| 13 | « Qui vérifie » écarte l'auteur (analyste, agent du tableur) | 1 | l. 30 « la RRH et l'analyste ne vérifient aucune ligne » ; l. 31 script écrit sans accès aux salaires, lancé hors de l'espace de l'agent |

**Total cas 3 : 10,5/13**

## Récapitulatif

| Cas | Total |
|---|---|
| 15 | 8,5/9 |
| 13n | 4,5/5 |
| 13g | 5,5/6 |
| 7 | 9,5/12 |
| 3 | 10,5/13 |

## Erreurs relevées

**Cas 15**
- Contradiction interne mineure : l. 19 dit qu'aucune ligne n'est écrite sur les trois points abandonnés, alors que les l. 73, 76 et 119 testent leur absence. La méthode est bonne ; c'est la formulation de la synthèse qui est inexacte.
- Pas d'erreur de calcul ni de date (le 14/11/2026 est un samedi, 41/58 ≈ 70 %, 53/75).

**Cas 13n**
- l. 24 contre l. 94 : la synthèse annonce « quelques patients en même temps », et la ligne 34 teste 20 réservations simultanées.
- Un DPO est supposé partout (l. 22, 77, 82, 84, 121) alors qu'un cabinet libéral n'est en principe pas tenu d'en désigner un. Il faut parler de juriste ou de conseil RGPD, sinon la ligne n'a pas de vérificateur.
- l. 84 ne nomme pas la certification HDS (« ce que la règle exige »).

**Cas 13g**
- **Incohérence du critère d'arrêt** : l. 143 dit que la boucle s'arrête « quand toutes les lignes mécaniques visibles passent ». Pourtant la liste de l'énoncé `/goal` (l. 151, reprise l. 137) n'en retient que 20 sur 30 et omet les lignes 6, 8, 11, 12, 25, 31, 32, 33, 36 et 41. Le but peut donc être déclaré atteint avec dix lignes mécaniques en échec, et rien ne dit pourquoi l'évaluateur ne pourrait pas les fermer.
- l. 139 (« la part cachée [est jouée] après la boucle ») contredit l. 143 (les cachées font partie du critère d'arrêt).
- **Erreur factuelle** l. 77 : « 2 segments au plus (320 caractères) » est faux. En SMS concaténé, un segment GSM-7 fait 153 caractères, soit 306 pour deux, et un segment UCS-2 en fait 67, soit 134 pour deux. Or les accents hors jeu GSM (ê, â, ô…), que la même ligne exige « corrects », font passer le message en UCS-2.
- Énoncé `/goal` de 9 lignes (l. 149-157).
- l. 23 : l'annexe logiciel n'a pas été lue (« n'était pas disponible »), alors qu'elle l'a été en 13n (l. 23 de 13n). Le résultat dépend de l'environnement d'exécution.

**Cas 7**
- **Reste à charge non calculé** : 78 − 31 = 47 k€ n'apparaît nulle part.
- l. 30 dit qu'aucune ligne mécanique n'est tirée des seuils réglementaires ou des aides tant qu'ils ne sont pas confirmés. Pourtant l. 80 (classe C avec une marge sous la limite C/D) et l. 81 (« ≥ au seuil du guide des aides ») sont des lignes mécaniques sur ces seuils.
- l. 69 : le plancher de coût (« prévision de l'audit + 25 % ») est accompagné d'un ordre de grandeur, 1 300 €/an, qui ne repose sur aucune prévision donnée. En plus, la colonne « Plancher (échec en dessous) » est inversée pour un coût, où l'échec est au-dessus.
- H3 (l. 210), qui consiste à ouvrir des tableaux, est intrusive sans être marquée `[costly]`, et elle est présentée en l. 236 comme le repli économique de H4.
- PAC : ni puissance ni COP/SCOP dans les tests de réception.

**Cas 3**
- **Minimum conventionnel non garanti par salarié** : l. 93 teste les cellules, l. 100 admet une « exception » sous le minimum de cellule, et l. 102 tolère 5 % de salariés hors fourchette. Aucune ligne ne vérifie que chacun des 140 est au moins au minimum Syntec de sa position. Les exigences propres à Syntec (salaire minimal majoré pour les modalités 2 et 3 du temps de travail des cadres) ne sont pas mentionnées non plus.
- l. 71 : « Accord ou avis recueilli » mélange deux procédures. Une NAO se conclut par un accord ou par un procès-verbal de désaccord ; l'avis relève de la consultation du CSE.
- l. 72 : seuil de 5 % présenté comme « seuil de la directive ». La directive 2023/970 fait de 5 % le déclencheur d'une évaluation conjointe des rémunérations, pas une cible de conformité. Le renvoi au juriste est prudent, mais le libellé peut induire en erreur.
- l. 75 : « 4 dimensions du questionnaire de valeur subjective », jargon importé de l'annexe négociation et jamais défini, ce qui rend la ligne inapplicable.
- Calculs justes : 284 800 €, 108 valeurs (36 × 3), 45/81 ≈ 55 %.

## Faiblesses communes

- Les synthèses contredisent leurs propres tableaux (15 l. 19 ; 13n l. 24/34 ; 13g l. 143/151 ; 7 l. 30/80-81) : le texte de cadrage n'est pas relu contre les lignes.
- Les zones d'issue gardent l'en-tête « Plancher (échec en dessous) » même quand moins vaut mieux (coût, écart, part de personnes visées : 15 l. 64, 7 l. 69, 3 l. 72), et les règles précises sont souvent renvoyées à « la règle » ou au juriste au lieu d'être nommées (HDS, minima Syntec, seuils des aides).
- Plusieurs mesures restent confiées à des non-spécialistes ou à des vérificateurs dont on ne dispose peut-être pas (le propriétaire avec un débitmètre, un DPO supposé, le juge « à désigner »), si bien que des lignes notées vérifiables n'ont pas encore quelqu'un capable de les vérifier.

## Cas 13g, nouvelle passe (`cas-13g-appli-kine-goal-sonnet-v1.2b.md`)

Contrôles mécaniques : coupe à la l. 193, aucune référence `H*` avant ; décompte refait par script, 34 mécanique, 6 relecture, 4 terrain, ce qui correspond aux l. 17, 131-133 et 135 (34/44 ≈ trois quarts).

| # | Critère | Note | Preuve |
|---|---|---|---|
| 1 | Deux réglages distingués (évaluateur qui lit la conversation, juge qui exécute) | 1 | l. 139 « Deux niveaux s'appliquent (étapes 12 et 13) » ; l. 148 (évaluateur) ; l. 150-151 (juge qui exécute, après la boucle) |
| 2 | Commande exacte et sortie brute complète, somme de contrôle et nombre de tests à chaque tour | 1 | l. 167-175 (empreinte avec commande d'exemple, nombre de tests, sortie complète, « pas un résumé ») |
| 3 | Qui écrit et fige les tests, le demandeur n'étant pas développeur | 1 | l. 141 « revoir ligne à ligne… par un développeur indépendant… avant le tour 1. Les tests sont ensuite gelés » ; l. 144 (le relecteur garde l'empreinte) ; l. 8. Réserve : le repli « une session distincte d'un autre modèle » (l. 141) est plus faible qu'un juge humain |
| 4 | Part cachée hors de la session de l'agent | 1 | l. 9, l. 198 « dans une session que l'agent ne peut pas lire » |
| 5 | Énoncé `/goal` de 10 à 15 lignes | 0,5 | l. 160-178 : 19 lignes physiques dans le bloc. Sans les retours à la ligne, on compte à peu près 12 énoncés. Le texte dépasse donc la borne lue à la lettre, et c'est une ligne vérifiable qui doit être notée strictement |
| 6 | Aveu que l'évaluateur ne distingue pas une sortie fabriquée | 1 | l. 148 « Il ne peut pas distinguer une sortie fabriquée d'une vraie » |

**Total cas 13g, nouvelle passe : 5,5/6** (la première passe avait aussi 5,5/6, mais le seul point perdu a changé de nature : énoncé trop long au lieu de trop court, alors que les défauts de fond sont corrigés).

Vérifications demandées :
- (a) **Tenu.** La l. 161 couvre les 34 lignes mécaniques visibles (1-8, 10-22, 25-27, 30-33, 35-37, 40-42, comparées par script à la colonne Preuve). Les l. 162-163 nomment les 10 autres (9, 23, 24, 28, 29, 34, 38, 39, 43, 44) et disent pourquoi elles sont écartées (relecture ou terrain), soit 34 + 10 = 44.
- (b) **Tenu.** L'évaluateur s'arrête sur les seules lignes listées (l. 176-178). La part cachée est rejouée après la boucle (l. 150-151) et la l. 198 dit qu'elle « ne doit jamais entrer… dans la condition d'arrêt de /goal ». La contradiction de la première passe (l. 139 contre l. 143) a disparu.
- (c) **Tenu.** Aucune contradiction entre la synthèse et les tableaux : le décompte de la l. 17, les « 34 lignes mécaniques » de la l. 19, les « trois soirs de suite » de la l. 15 (l. 91) et les lignes de terrain 9, 23, 24 et 39 de la l. 153 concordent tous. L'en-tête de la zone d'issue est corrigé (l. 56 « ou au-dessus quand “moins” vaut mieux »).
- (d) Erreurs factuelles : aucune erreur de fond. Les chiffres sont justes (environ 500 SMS par mois pour 520, 480 RDV sur 4 semaines), la date aussi (changement d'heure dans la nuit du 24 au 25/10/2026), et la référence au registre HDS de l'ANS est correcte. L'erreur « 320 caractères » de la première passe a disparu (l. 85). Points mineurs :
  - renvoi faux en l. 186 : la question 5 (RDV du lundi, RDV pris après l'heure d'envoi) dit que « la ligne 22 en dépend », alors que la ligne 22 traite d'un RDV modifié après le rappel ;
  - coquille en l. 193 : « JjUGE » ;
  - la l. 77 met l'audit automatique et le parcours au clavier dans une seule ligne `mécanique`, et aucune ligne ne teste un lecteur d'écran ou l'usage réel de l'accessibilité (la l. 76 ne teste que la réservation sur téléphone).
