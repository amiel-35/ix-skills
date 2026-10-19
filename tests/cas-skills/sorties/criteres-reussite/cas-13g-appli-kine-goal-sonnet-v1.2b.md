<!-- Sortie brute de criteres-reussite 1.2.0 (après les retouches du juge : énoncé goal complet, plancher inversé, synthèse relue), Sonnet, 0.22 $. Cas : ../../criteres-reussite.md -->

---
status: draft
skill: criteres-reussite
deliverable_kind: logiciel (application web de prise de rendez-vous avec rappels SMS)
author: Claude Code, agent en boucle via /goal
judge: vous (acceptation finale), avec un relecteur technique indépendant à désigner. Vous n'exécutez pas les scripts vous-même.
requester: judge, déduit de « c'est moi qui accepterai ». Ce plan est cependant écrit dans une session qui peut être celle de l'agent, donc traité comme `author` pour la part cachée (étape 9).
---

# Critères de réussite — Application de rendez-vous du cabinet de kinésithérapie

## Synthèse / Summary
On livre une application où les patients réservent en ligne, où chacun des 2 kinés voit son planning (environ 120 RDV par semaine), et où chaque patient reçoit un SMS de rappel la veille. « Terminé » veut dire que les 44 lignes ci-dessous sont passées, que de vrais SMS arrivent sur de vrais téléphones trois soirs de suite, et que les résultats d'usage atteignent le plancher fixé par vous avant le début des travaux.

**Décompte :** 44 lignes visibles, soit 34 mécanique, 6 relecture et 4 terrain. La part cachée n'est pas écrite ici (voir plus bas).

**Part de la boucle :** elle peut clore les 34 lignes mécaniques, à condition que leurs scripts soient revus par un tiers (voir « Critère d'arrêt »). Elle ne peut pas décider de l'hébergement des données de santé, des textes légaux ni des essais réels. Une boucle « verte » prouve donc surtout que la mécanique tient. Elle ne prouve pas que l'application convient à votre cabinet.

**Hypothèses [inferred] :**
- Les patients ne créent pas de compte. Ils réservent avec nom et téléphone.
- Les kinés ont un accès protégé par mot de passe.
- Le cabinet doit pouvoir gérer lui-même ses horaires, ses absences et les RDV pris par téléphone. Le brief ne le dit pas, mais 120 RDV par semaine l'imposent presque.

**Alerte calendrier :** le changement d'heure a lieu dans la nuit du 24 au 25 octobre 2026, c'est-à-dire bientôt. La ligne 19 le teste.

Lignes bloquantes / Blocking lines : 1, 2, 12, 13, 16, 17, 20, 23, 24, 28, 32, 36.
Noyau : non applicable (moins de 45 lignes).

## Exigences / Requirements
| E | Exigence | Source | Livrable ou issue |
|---|---|---|---|
| E1 | Les patients réservent un créneau en ligne | « Les patients réservent en ligne » | livrable |
| E2 | Chaque kiné voit son propre planning | « chaque kiné voit son planning » | livrable |
| E3 | Rappel SMS la veille du RDV | « reçoivent un rappel par SMS la veille » | livrable (envoi), issue (réception) |
| E4 | 2 kinés, environ 120 RDV par semaine tiennent sans lenteur | « deux kinés, environ 120 rendez-vous par semaine » | livrable |
| E5 | Acceptable par un non-développeur, construit en boucle | « Je ne suis pas développeur ; c'est moi qui accepterai » | livrable |
| E6 | Jamais deux patients sur le même créneau, aucun créneau absurde (passé, hors horaires, chevauchant) | [inferred] | livrable |
| E7 | Données de santé protégées : hébergement, accès, chiffrement, secrets | [inferred] (RGPD, hébergeur de données de santé) | livrable |
| E8 | Droits des patients : information, effacement, opposition aux SMS, durée de conservation | [inferred] | livrable |
| E9 | Annulation, absences et congés, RDV pris par le cabinet | [inferred] | livrable |
| E10 | Exploitation : sauvegarde restaurable, alerte si les rappels ne partent pas, installation reproductible, tâches courantes faisables sans développeur | [inferred] | livrable |
| E11 | Utilisable sur téléphone, accessible | [inferred] | livrable |
| E12 | Heures correctes en Europe/Paris, y compris au changement d'heure | [inferred] | livrable |
| E13 | Aucun trou de contenu visible par l'utilisateur final | [inferred] | livrable |
| E14 | Les patients prennent réellement RDV en ligne et honorent davantage leurs RDV | [inferred] (but du rappel) | issue |

Limites, qui ne sont pas des exigences :
- le budget SMS (environ 500 SMS par mois au volume annoncé) ;
- aucune donnée médicale (motif, pathologie) n'est nécessaire à la prise de RDV.

## Issue visée / Outcome zone
Les seuils ci-dessous sont **proposés** [proposed]. C'est à vous de les fixer avant le début des travaux, pas après avoir vu le résultat. Je n'ai aucune donnée de départ sur votre cabinet.

| E | Issue | Plancher (échec en dessous, ou au-dessus quand « moins » vaut mieux) | Cible | Fixé par | Mesuré quand |
|---|---|---|---|---|---|
| E14 | Part des nouveaux RDV pris en ligne | 40 % [proposed] | 70 % [proposed] | vous | 8 semaines après la mise en service |
| E14 | Taux de RDV non honorés | échec au-dessus de votre taux actuel, à mesurer sur les 4 semaines précédentes | baisse d'un tiers [proposed] | vous | 8 semaines après la mise en service |
| E3 | SMS remis (rapport du fournisseur) | 90 % [proposed] | 97 % [proposed] | vous | sur les 8 premières semaines |
| E4 | Appels au cabinet « je n'arrive pas à réserver » | échec au-dessus de 1 patient sur 10 [proposed] | moins de 1 sur 20 [proposed] | vous | sur les 4 premières semaines |

## Critères vérifiables / Checks
Une ligne « mécanique » dont le script a été écrit par l'agent et non revu par un tiers compte comme « relecture » (étape 12).

| # | Élément ou situation | Vérification | Résultat attendu | Preuve | Qui vérifie |
|---|---|---|---|---|---|
| 1 | E1 Réservation nominale | Test de bout en bout : un patient choisit un kiné, un créneau, saisit nom et téléphone | Confirmation affichée, RDV visible dans le planning du bon kiné, un seul enregistrement | mécanique | Script ; développeur autre que l'auteur ; données fictives |
| 2 | E6 Réservation simultanée | 20 requêtes simultanées sur le même créneau (pas des requêtes à la suite) | Exactement 1 réussite, 19 refus avec message clair, 1 seul RDV en base | mécanique | Script ; développeur autre que l'auteur |
| 3 | E6 Chevauchement, côté serveur | Pour un RDV de 30 min, envoyer directement à l'interface serveur un créneau qui chevauche | Refus, même si l'écran ne le propose pas | mécanique | Script ; développeur autre que l'auteur |
| 4 | E6 Créneau passé, hors horaires, jour fermé, kiné absent | Envoi direct de chacun de ces 4 cas | 4 refus, aucun RDV créé | mécanique | Script ; développeur autre que l'auteur |
| 5 | E9 Absence ou congé d'un kiné | Poser une absence sur une plage où 3 RDV existent | Les créneaux disparaissent de l'offre en ligne ; l'application liste les 3 patients à prévenir | mécanique | Script ; développeur autre que l'auteur |
| 6 | E9 Annulation par le patient | Utiliser le lien d'annulation (confirmation ou SMS) ; l'utiliser une 2e fois | Créneau à nouveau réservable, disparu du planning du kiné ; 2e usage = message clair, pas d'erreur technique | mécanique | Script ; développeur autre que l'auteur |
| 7 | E1 Saisies invalides | Téléphone avec lettres, numéro trop court, nom vide, formats 06…, +33 6… | Invalides refusés avec message ; valides enregistrés sous un même format | mécanique | Script ; développeur autre que l'auteur |
| 8 | E6 Abus | Un même poste tente 30 réservations en 10 minutes | Limité à 5 par heure [proposed] ; l'agenda n'est pas vidé | mécanique | Script ; développeur autre que l'auteur |
| 9 | E11 Parcours sur vrais téléphones | 3 patients réels (dont 1 de plus de 65 ans) réservent seuls sur leur téléphone | Les 3 réussissent en moins de 3 minutes [proposed], sans aide | terrain | Vous, au cabinet, avant la mise en service |
| 10 | E11 Accessibilité | Audit automatique + parcours au clavier seul | Aucune anomalie « critique » dans l'audit ; réservation possible sans souris | mécanique | Outil d'audit, qui ne mesure que ce qu'il sait mesurer ; développeur autre que l'auteur |
| 11 | E2 Contenu du planning | Créer 10 RDV via l'application ; comparer au planning jour et semaine du kiné | Les 10 apparaissent, avec heure, nom et téléphone, sur le bon jour | mécanique | Script ; développeur autre que l'auteur |
| 12 | E2/E7 Isolation entre kinés | Kiné A connecté demande directement les RDV et patients de B | Refus, aucune donnée de B (règle à confirmer, voir questions ouvertes) | mécanique | Script ; développeur autre que l'auteur |
| 13 | E7 Accès non connecté | Appeler les pages et données du planning sans connexion ; 10 mauvais mots de passe d'affilée | Refus ; compte verrouillé ou ralenti ; aucun mot de passe par défaut dans le code ni la configuration | mécanique | Script + recherche dans le code ; développeur autre que l'auteur |
| 14 | E2 Mise à jour du planning | Un patient réserve ; le kiné a son planning ouvert | RDV visible en moins de 60 s [proposed] avec ou sans rechargement | mécanique | Script ; développeur autre que l'auteur |
| 15 | E9 RDV saisi par le kiné ou le cabinet | Créer un RDV (appel téléphonique) | Le créneau disparaît de l'offre en ligne ; la ligne 2 s'applique à ce cas | mécanique | Script ; développeur autre que l'auteur |
| 16 | E3 Sélection des destinataires | Jeu de 30 RDV (lendemain, surlendemain, passés, annulés), horloge simulée à l'heure d'envoi | SMS envoyés à tous les RDV non annulés du lendemain, et à eux seuls | mécanique | Script ; développeur autre que l'auteur ; numéros fictifs |
| 17 | E3 Un seul SMS par RDV | Lancer la tâche d'envoi 3 fois de suite | 1 SMS par RDV, pas 3 | mécanique | Script ; développeur autre que l'auteur |
| 18 | E3 Contenu du SMS | Lire les SMS produits pour 5 cas (accents, apostrophes, nom long) | Contient cabinet, kiné, date, heure, moyen d'annuler ; aucun motif ni terme médical ; 2 segments au plus [proposed] | mécanique | Script ; développeur autre que l'auteur |
| 19 | E12 Heure et changement d'heure | RDV les 24, 25 et 26 octobre 2026 ; vérifier l'heure affichée, l'heure du SMS et l'heure d'envoi | Partout la même heure locale Europe/Paris ; envoi la veille entre 17 h et 19 h [proposed] | mécanique | Script ; développeur autre que l'auteur |
| 20 | E3 Panne du fournisseur SMS, 4 pannes distinctes simulées | Chacune simulée : délai dépassé, numéro refusé, crédit épuisé, panne totale | Nouvelles tentatives ; en échec définitif, liste « rappels non envoyés » visible au cabinet avant 20 h [proposed] ; aucun doublon au retour du service | mécanique | Script avec faux fournisseur ; développeur autre que l'auteur |
| 21 | E8 Opposition aux SMS | Un patient refuse les SMS ou répond STOP | Plus aucun SMS pour ce numéro ; le RDV reste valide | mécanique | Script ; développeur autre que l'auteur |
| 22 | E3 RDV modifié ou annulé après le rappel | Annuler ou déplacer un RDV déjà notifié | Le patient reçoit une information qui corrige la précédente, ou la règle écrite est appliquée | mécanique | Script ; développeur autre que l'auteur |
| 23 | E3 SMS réels | Envoyer de vrais SMS à 3 téléphones d'opérateurs différents (Orange, SFR, Bouygues ou Free) | Reçus en moins de 5 minutes, lisibles, accents corrects | terrain | Vous, avec 3 numéros de proches ou de collègues consentants |
| 24 | E3 Planificateur réel | Après mise en service, 3 soirs de suite, un RDV de test le lendemain | Le vrai SMS part chaque soir à l'heure prévue, sans intervention | terrain | Vous, 3 soirs consécutifs |
| 25 | E10 Alerte si la tâche ne tourne pas | Couper la tâche d'envoi un soir | Une alerte (courriel ou SMS) vous parvient en moins d'une heure après l'heure prévue | mécanique | Script ; développeur autre que l'auteur |
| 26 | E4 Volume | Jeu de 4 semaines (environ 480 RDV, 2 kinés) ; 10 réservations simultanées | Affichage du planning en moins de 2 s ; réservation en moins de 3 s [proposed] | mécanique | Script ; développeur autre que l'auteur |
| 27 | E4 Pic de rappels | 40 RDV le même lendemain [proposed] | Tous les SMS envoyés en moins de 15 minutes | mécanique | Script avec faux fournisseur ; développeur autre que l'auteur |
| 28 | E7 Hébergement de données de santé | Relever l'hébergeur retenu, son certificat HDS (consultable au registre public de l'ANS), sa localisation, le contrat du fournisseur SMS | Hébergeur certifié ; pièces présentes ; la mention « non conforme » ne suffit pas. L'applicabilité de HDS à ce service est à confirmer. | relecture | Juriste ou DPO ; indépendant de l'auteur |
| 29 | E7/E8 Minimisation | Lister tous les champs enregistrés | Aucun motif de consultation ni donnée de santé ; chaque champ a une raison écrite | relecture | Développeur ou DPO ; indépendant de l'auteur |
| 30 | E7 Transport et stockage | Audit TLS du site ; accès en http ; contrôle du chiffrement au repos | Redirection vers https ; TLS à jour ; base chiffrée | mécanique | Outil d'audit ; développeur autre que l'auteur |
| 31 | E7 Secrets et journaux | Recherche de clés et mots de passe dans le code et l'historique ; recherche de noms et téléphones dans les journaux | Aucune clé ni donnée patient en clair | mécanique | Script ; développeur autre que l'auteur |
| 32 | E8 Effacement jusqu'aux fichiers | Créer un patient fictif aux nom et numéro uniques, puis demander l'effacement. Chercher ces valeurs dans la base, les journaux, les exports et les copies de test. | Zéro occurrence hors sauvegardes ; durée de conservation des sauvegardes écrite | mécanique | Script ; développeur autre que l'auteur |
| 33 | E8 Durée de conservation | RDV plus vieux que la durée retenue | Purge ou anonymisation automatique, vérifiée sur jeu de test (durée à fixer par vous) | mécanique | Script ; développeur autre que l'auteur |
| 34 | E8 Information du patient | Lire la page affichée avant la réservation | Responsable, finalité, durée, droits, contact : présents et compréhensibles | relecture | Juriste ou DPO ; indépendant de l'auteur |
| 35 | E10 Sauvegarde restaurable [costly] | Restaurer la dernière sauvegarde sur un environnement vide | Les RDV de test sont retrouvés ; sauvegarde au moins quotidienne [proposed] | mécanique | Script ; développeur autre que l'auteur |
| 36 | E7 Accès aux RDV d'autrui | Changer l'identifiant dans une adresse ; deviner un lien d'annulation | Accès refusé ; liens d'au moins 128 bits aléatoires | mécanique | Script ; développeur autre que l'auteur |
| 37 | E7 Dépendances | Audit des vulnérabilités connues | Aucune « haute » ni « critique » non traitée | mécanique | Outil d'audit ; développeur autre que l'auteur |
| 38 | E10 Installation reproductible | Une personne qui n'est pas l'auteur installe depuis la notice, sur une machine vierge | Application fonctionnelle sans demander l'agent ; notice sans étape manquante | relecture | Développeur autre que l'auteur |
| 39 | E5/E9 Tâches courantes sans développeur | Sans aide : ajouter un congé, changer un horaire, créer un RDV téléphonique, annuler un RDV, voir les rappels non envoyés | Les 5 tâches réussies en moins de 10 minutes chacune [proposed] | terrain | Vous, ou la personne qui tiendra l'agenda |
| 40 | E13 Aucun trou dans le rendu | Chercher dans toutes les pages et messages rendus (confirmation, erreur, annulation, SMS, courriel, vue kiné) : TODO, TBD, XXX, lorem, [à compléter], undefined, null, {{ | Zéro occurrence | mécanique | Script sur le rendu réel ; développeur autre que l'auteur |
| 41 | E13 Éléments nommés existants | Suivre chaque lien et bouton ; vérifier chaque commande et variable citée dans la notice | Aucun lien mort ; tout élément cité existe | mécanique | Script ; développeur autre que l'auteur |
| 42 | E13 Cohérence | Comparer adresse, téléphone et horaires du cabinet sur le site, le SMS et les courriels | Une seule valeur partout, lue d'une seule source | mécanique | Script ; développeur autre que l'auteur |
| 43 | E13 Chaque acteur, chaque état | Le patient sans créneau libre, créneau pris entre-temps, RDV passé, annulation deux fois ; le kiné avec journée vide | Un message compréhensible dans chaque cas, jamais une erreur technique | relecture | Relecteur autre que l'auteur ; vous pouvez la faire à la main |
| 44 | E5 Les tests attrapent les pannes | Le relecteur injecte 5 défauts de son choix (verrou de réservation retiré, rappel doublé, planning d'autrui visible…) | Au moins 5 sur 5 font échouer la suite | relecture | Développeur autre que l'auteur, dans un environnement séparé |

## Ce qui passerait et serait faux / What could pass and still be wrong
- Tout est vert avec un faux fournisseur SMS qui réussit toujours, alors que le vrai refuse (identifiants, nom d'expéditeur, crédit) → lignes 20, 23, 24.
- L'écran cache le planning de l'autre kiné, mais l'accès direct aux données le donne → ligne 12.
- Le planificateur est simulé dans les tests et ne tourne jamais en production → ligne 24 (3 soirs réels) et ligne 25.
- La double réservation n'est testée que séquentiellement, jamais en parallèle → ligne 2.
- L'effacement retire le patient à l'écran, mais son nom reste dans les journaux ou les exports → ligne 32.
- L'hébergement est « documenté » comme non certifié, et la ligne se contente de dire qu'il est documenté → ligne 28.
- Les tests ont été affaiblis, supprimés ou rendus triviaux pour passer → ligne 44 et règles de gel dans le critère d'arrêt.
- Les rappels sont corrects sauf autour du changement d'heure du 25 octobre → ligne 19.
- Un texte « à compléter » existe seulement dans un message d'erreur rarement vu → ligne 40.

## Non testable en l'état / Not testable as stated
- **E14 (adoption et non-présentation)** : seul le terrain tranche, après 8 semaines. Question : quel est votre taux actuel de RDV non honorés ?
- **« Confortable pour les patients »** : seule la ligne 9 s'en approche, sur 3 personnes. Question : quelles personnes représentent vos patients ?

## Couverture / Coverage
| Kind | Visible | Hidden | Who |
|---|---|---|---|
| mécanique | 34 | non écrites ici | scripts, rejoués par le juge hors du poste de l'agent |
| relecture | 6 | non écrites ici | développeur indépendant, juriste ou DPO |
| terrain | 4 | non écrites ici | vous, au cabinet, avant puis après la mise en service |

La boucle peut clore les 34 lignes mécaniques, soit environ trois quarts des lignes. Elle ne tranche ni l'hébergement des données de santé, ni les textes légaux, ni la réception réelle des SMS, ni l'adoption par les patients, qui sont les points qui comptent le plus. Un « tout vert » ne veut donc pas dire « accepté ».

## Critère d'arrêt de la boucle / Loop stopping criterion

**Deux niveaux s'appliquent** (étapes 12 et 13), car /goal fait juger par un évaluateur qui ne lit que la conversation, et vous acceptez ensuite.

**Un point à régler avant de lancer la boucle.** Vous n'êtes pas développeur et vous ne pouvez pas relire les scripts de test. Faites revoir ligne à ligne ceux des 34 lignes mécaniques par un développeur indépendant, ou à défaut par une session distincte d'un autre modèle que celui de l'agent. Cette revue doit être faite avant le tour 1. Les tests sont ensuite gelés. Sans cette revue, ces lignes comptent comme « relecture » et la boucle ne peut en clore aucune.

**Règles de l'instrument.**
- Les tests, jeux de données, scripts de mesure et leur configuration sont gelés avant le tour 1. Le relecteur garde l'empreinte (checksum).
- Aucun test n'est supprimé, ignoré ou marqué « échec attendu ».
- Le nombre de tests ne baisse pas.

**Limite de l'évaluateur.** Il ne lit que la conversation. Il ne peut pas distinguer une sortie fabriquée d'une vraie. Son verdict n'est pas une acceptation.

**Après la boucle,** hors de la session de l'agent :
- un juge qui exécute rejoue les lignes mécaniques ;
- puis viennent les lignes de relecture ;
- puis les lignes de terrain 9, 23, 24 et 39, que vous faites.

En cas d'échec, l'agent reçoit l'exigence et le symptôme visible, jamais une entrée cachée ni une valeur attendue.

**Énoncé du but à donner à /goal :**

```
BUT : l'application de rendez-vous du cabinet est prête pour la recette.
Lignes couvertes : mécaniques 1-8, 10-22, 25-27, 30-33, 35-37, 40-42
(le plan numérote 44 lignes ; 9, 23, 24, 28, 29, 34, 38, 39, 43, 44 sont
hors de ce but : relecture ou terrain, jugés après la boucle).
Règles :
1. Les tests sont ceux gelés par le relecteur. Aucun test n'est modifié,
   supprimé, ignoré ni affaibli. Aucune ligne n'est traitée comme optionnelle.
2. À chaque tour, afficher la commande exacte et la sortie brute complète :
   (a) l'empreinte de tous les fichiers de test
       (ex. find tests -type f | sort | xargs shasum -a 256 | shasum -a 256),
   (b) le nombre de tests,
   (c) la sortie complète de la suite.
   L'empreinte doit rester identique à celle du tour 1 ; le nombre de tests
   ne doit pas baisser.
3. Une ligne compte comme passée seulement si sa commande et sa sortie brute
   complète sont affichées dans la conversation, pas un résumé.
Le but est atteint quand toutes les lignes ci-dessus passent sur le même
tour avec l'empreinte inchangée. Ce n'est pas une acceptation : le juge rejouera
tout hors session, puis passera aux lignes de relecture et de terrain.
```

## Questions ouvertes / Open questions
1. Un kiné voit-il uniquement ses propres patients (hypothèse de la ligne 12) ou ceux du cabinet ?
2. Qui prend les RDV par téléphone : un secrétariat, ou les kinés eux-mêmes ? Faut-il un compte « cabinet » ?
3. Durée des séances : fixe (30 min ?) ou variable ? Le premier RDV est-il plus long ? Une ordonnance doit-elle être mentionnée ?
4. Délai limite d'annulation par le patient ?
5. Rappel d'un RDV du lundi : envoyé le dimanche ? Quelle règle pour un RDV pris le jour même ou après l'heure d'envoi ? (La ligne 22 en dépend.)
6. HDS : l'hébergement de simples RDV de kiné relève-t-il de l'obligation HDS ? À confirmer par un juriste ou la CNIL avant de choisir l'hébergeur.
7. Durée de conservation des RDV passés, qu'il vous appartient de fixer (ligne 33).
8. Qui assurera la maintenance après livraison, et qui reçoit les alertes (ligne 25) ?
9. Qui est le relecteur technique indépendant ? C'est le point qui conditionne la boucle.
10. Les seuils de l'issue visée sont à confirmer par vous avant le démarrage.

✂ ----- À TRANSMETTRE AU JjUGE / FOR THE JUDGE -----

## Demande de part cachée / Hidden part request
Environ 14 lignes cachées, au moins deux par exigence gardée. Le juge choisit les exigences à garder.

Juge : lancez `criteres-reussite` avec `requester: judge`, ce brief et le plan visible ci-dessus, dans une session que l'agent ne peut pas lire, et gardez pour vous ce qu'elle écrit. La part cachée ne doit jamais entrer dans le contexte de l'agent ni dans la condition d'arrêt de /goal. Elle sera rejouée après la boucle.