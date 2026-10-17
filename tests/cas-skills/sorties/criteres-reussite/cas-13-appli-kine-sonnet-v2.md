<!-- Sortie brute de criteres-reussite 1.0.0 (version finale), Sonnet, 0.21 $. Cas : ../../criteres-reussite.md -->

# Critères de réussite : application de rendez-vous pour un cabinet de kinésithérapie

J'ai lu l'annexe logiciel et je m'en sers pour les lignes de tests, de charge, d'effacement et pour la partie cachée. Votre demande ne dit pas qui développe ni qui juge. J'ai donc supposé que vous commanditez l'application et que le développeur est quelqu'un d'autre (`requester: other`). J'ai écrit la partie cachée en conséquence. **Si vous développez vous-même, ne lisez pas le bloc après la ligne ✂.** Demandez alors la partie cachée à un juge (voir Questions ouvertes).

---
status: draft
skill: criteres-reussite
deliverable_kind: logiciel (application web de prise de rendez-vous et de rappels SMS)
author: non précisé (personne, équipe ou agent)
judge: quelqu'un d'autre que l'auteur, détenteur de la part cachée
---

## Synthèse / Summary
L'application livre trois choses :
- les patients réservent un créneau en ligne ;
- le kiné voit et tient son planning ;
- chaque patient reçoit un SMS de rappel la veille.

« Terminé » veut dire qu'aucun créneau ne peut être pris deux fois, que chaque RDV du lendemain donne exactement un SMS correct à la bonne heure, que les données de santé ne fuient ni à l'écran, ni dans les fichiers, ni chez un sous-traitant, et que le kiné a tenu une vraie semaine sans RDV perdu.

Le plan compte 49 lignes :
- 42 visibles : 31 mécaniques, 4 de relecture, 7 de terrain ;
- 7 cachées, toutes mécaniques.

Une boucle automatique peut en fermer environ 75 %. Le résultat réel (moins d'absences) ne se mesure qu'en conditions réelles.

La question ouverte principale est le taux d'absences actuel. Sans lui, on ne peut pas fixer le plancher de l'issue visée.

**Lignes bloquantes / Blocking lines :** 3, 11, 12, 13, 23, 25, 26

## Exigences / Requirements
| E | Exigence | Source | Livrable ou issue |
|---|---|---|---|
| E1 | Un patient réserve un RDV en ligne, seul, sans appeler | « les patients réservent en ligne » | livrable |
| E2 | Le kiné voit son planning, exact et à jour | « le kiné voit son planning » | livrable |
| E3 | Chaque patient reçoit un SMS de rappel la veille | « un rappel par SMS la veille » | livrable (l'envoi) / issue (la réception) |
| E4 | Aucune double réservation. Les créneaux respectent horaires, durée de séance et absences | [inferred] condition de E1 et E2 | livrable |
| E5 | Le patient peut annuler ou déplacer son RDV | [inferred] sinon le rappel ne sert à rien | livrable |
| E6 | Données de santé : minimisation, consentement et information, hébergement, effacement, sous-traitants (fournisseur SMS) | [inferred] thème : RGPD, données de santé | livrable |
| E7 | Cloisonnement : un patient ne voit que ses RDV, le planning exige une authentification | [inferred] thème | livrable |
| E8 | Utilisable sur mobile, par tous (accessibilité, patients âgés) | [inferred] thème | livrable |
| E9 | Les heures sont justes toute l'année, y compris au changement d'heure | [inferred] le rappel dépend de l'heure | livrable |
| E10 | Aucun trou dans ce que voit le patient (pages, e-mails, SMS) | [inferred] contenu | livrable |
| E11 | Le système tient la charge et se rétablit (pic de réservation, sauvegarde) | [inferred] | livrable |
| E12 | Le SMS en échec ou le fournisseur en panne ne casse ni la réservation ni la confiance du kiné | [inferred] | livrable |
| E13 | Le kiné peut saisir ou déplacer un RDV lui-même (téléphone, sur place), et le créneau se bloque en ligne | [inferred] le cabinet n'a pas qu'un canal | livrable |
| E14 | Moins de rendez-vous non honorés | [inferred] but du rappel | issue |
| E15 | Les patients adoptent la réservation en ligne | [inferred] but de E1 | issue |

**Limites, pas des exigences.** Je n'ai ni budget ni délai. Je suppose un seul kiné et un seul cabinet (« le kiné » au singulier), à confirmer.

## Issue visée / Outcome zone
Le plancher est fixé par le kiné avant le début du travail, après mesure de la situation actuelle. Les valeurs ci-dessous sont des propositions `[proposed]` à confirmer.

| E | Issue | Plancher (échec en dessous) | Cible (succès au-dessus) | Fixé par | Mesuré quand |
|---|---|---|---|---|---|
| E14 | Taux de RDV non honorés | pas mieux que la situation actuelle, mesurée 8 semaines avant | au moins 50 % de baisse relative `[proposed]` | le kiné | 8 semaines après la mise en service, comparées aux 8 d'avant |
| E15 | Part des RDV pris en ligne | 20 % `[proposed]` | 50 % `[proposed]` | le kiné | à 3 mois |
| E3 | SMS remis (accusé de réception de l'opérateur) sur numéros valides | 90 % `[proposed]` | 97 % `[proposed]` | le kiné | chaque mois, à partir du rapport du fournisseur |

## Critères vérifiables / Checks
| # | Élément ou situation | Vérification | Résultat attendu | Preuve | Qui vérifie |
|---|---|---|---|---|---|
| 1 | E1 : parcours complet d'un nouveau patient | Test bout en bout : choisir un créneau, saisir ses coordonnées, confirmer | Confirmation affichée, RDV visible au planning du kiné avec les mêmes date, heure et nom | mécanique | développeur, données synthétiques |
| 2 | E1, E4 : créneaux proposés | Générer l'offre sur 4 semaines avec horaires, fermetures et types de séance (bilan, séance, durée différente) | 0 créneau hors horaires, 0 sur une fermeture, 0 qui déborde sur un RDV existant ; la durée suit le type | mécanique | développeur |
| 3 | E4 : réservation simultanée | 20 requêtes API en parallèle sur le même créneau | 1 succès, 19 refus avec message clair, 1 seul RDV en base | mécanique | développeur |
| 4 | E4 : règles imposées par le serveur | Appeler l'API directement pour un créneau passé, hors horaires, sous le délai minimum (2 h `[proposed]`) | Refus à chaque fois, quel que soit l'état de l'interface | mécanique | développeur |
| 5 | E2, E4 : absence du kiné | Poser une absence sur une plage contenant des créneaux libres et 2 RDV | Créneaux libres retirés de l'offre en moins de 1 min `[proposed]` ; les 2 RDV listés pour traitement, aucun supprimé en silence | mécanique | développeur |
| 6 | E2 : planning fidèle à la base | Jeu de 50 RDV : comparer chaque ligne du planning (jour, semaine) à la base | 50 sur 50 identiques : heure, durée, nom, statut | mécanique | développeur |
| 7 | E13 : RDV saisi par le kiné | Créer un RDV manuel, puis consulter l'offre en ligne | Créneau absent de l'offre ; un second RDV en ligne sur ce créneau est refusé | mécanique | développeur |
| 8 | E2, E13 : le kiné annule ou déplace | Annuler puis déplacer un RDV | Planning à jour ; un SMS de prévenance part au patient (sauf refus de SMS) ; l'ancien créneau redevient libre | mécanique | développeur |
| 9 | E5 : le patient annule | Annuler via le lien de confirmation, avant et après le délai limite (Q5) | Avant : annulé, créneau libéré, planning à jour. Après : refus avec message qui renvoie au cabinet | mécanique | développeur |
| 10 | E5 : lien d'annulation | Essayer un lien modifié, le lien d'un autre RDV, un lien déjà utilisé, un lien après le RDV | Chaque tentative est refusée sans révéler aucune donnée | mécanique | développeur |
| 11 | E3 : un rappel, un seul | Jeu de 30 RDV pour demain, lancer la tâche d'envoi, puis la relancer | 30 SMS exactement, 0 doublon après relance | mécanique | développeur |
| 12 | E3 : moment de l'envoi | Horloge figée : RDV du mardi, du lundi matin, avant un jour férié | Envoi le jour J-1 dans la plage 17 h–19 h `[proposed]`, jamais la nuit ; pour lundi et jours fériés, appliquer la règle décidée (Q2) | mécanique | développeur |
| 13 | E3 : forme du SMS | Générer le SMS avec des noms accentués, longs et composés | Contient date, heure, nom du cabinet, moyen d'annuler ; 2 segments au plus `[proposed]` ; accents intacts ; aucun mot coupé | mécanique | développeur |
| 14 | E3 : sens du SMS | Faire lire le modèle de SMS et de confirmation par le kiné et par une personne extérieure | Aucune information de santé (motif, type de soin, pathologie) ; le message est compris sans appeler | relecture | kiné et un tiers, sans données réelles |
| 15 | E3 : cas limites de l'envoi | RDV annulé avant l'envoi ; RDV pris pour demain après l'heure d'envoi | Annulé : aucun SMS. Pris après : le comportement décidé (Q2) est appliqué, sans doublon | mécanique | développeur |
| 16 | E9 : changement d'heure | Horloge figée autour du 25 octobre 2026 et du 28 mars 2027 | Un RDV de 8 h le lundi s'affiche et est rappelé à 8 h ; le rappel du dimanche part à l'heure prévue | mécanique | développeur |
| 17 | E12 : échec d'envoi | Simuler une erreur du fournisseur SMS | 3 tentatives en 1 h `[proposed]`, 0 doublon ; l'échec final apparaît dans une liste « rappels non envoyés » vue par le kiné | mécanique | développeur |
| 18 | E12 : numéro inutilisable | Saisir un fixe, un numéro mal formé, un numéro étranger | Refusé à la saisie ou signalé avec un message ; aucun SMS à un fixe | mécanique | développeur |
| 19 | E6 : refus du SMS | Réserver en refusant le rappel | Aucun rappel envoyé ; le planning du kiné affiche « pas de rappel » | mécanique | développeur |
| 20 | E6 : information du patient | Relire le texte affiché à la réservation (SMS, données, durée de conservation, contact) | Clair, complet, case de consentement non précochée ; validé par la personne chargée de la conformité | relecture | juriste ou DPO |
| 21 | E6 : hébergement et sous-traitants | Relire le dossier d'hébergement et la liste des sous-traitants (hébergeur, fournisseur SMS) | Chaque sous-traitant listé avec contrat et lieu de traitement ; hébergement certifié HDS, ou décision écrite et motivée si Q6 conclut qu'il n'est pas requis | relecture | juriste ou DPO |
| 22 | E6 : minimisation | Lister les champs du formulaire et des tables, les comparer à la liste approuvée | 0 champ hors liste ; aucun champ « motif » obligatoire ni en texte libre | mécanique | développeur |
| 23 | E6 : effacement d'un patient | Poser une valeur témoin unique (nom, téléphone) dans un patient test, le supprimer, puis chercher la valeur dans les octets de la base et de ses fichiers annexes, les logs, les exports, les sauvegardes, les journaux du fournisseur SMS | Introuvable partout ; sinon l'endroit et la durée de conservation sont écrits | mécanique | développeur, copie des fichiers, données synthétiques |
| 24 | E6 : journaux propres | Provoquer des erreurs avec un patient test et chercher son nom, son téléphone et son motif dans les logs, le suivi d'erreurs et l'analytique | 0 occurrence | mécanique | développeur |
| 25 | E7 : cloisonnement des patients | Avec la session du patient A, appeler les RDV du patient B par identifiant, puis parcourir 1 000 identifiants consécutifs | 0 donnée d'autrui renvoyée (403 ou 404) | mécanique | développeur |
| 26 | E7 : planning protégé | Appeler chaque route du planning sans session, avec une session de patient, avec une session expirée | 401 ou 403 partout ; la session du kiné expire après inactivité (30 min `[proposed]`) | mécanique | développeur |
| 27 | E7 : ce qui reste caché | Lire l'offre de créneaux publique et le code envoyé au navigateur | Aucun nom, téléphone ou motif d'un autre patient, nulle part | mécanique | développeur |
| 28 | E7 : énumération | Réserver avec le numéro ou l'e-mail d'un patient existant | Aucun nom ni RDV de ce patient n'est révélé ; la réponse ne dit pas si le numéro est connu | mécanique | développeur |
| 29 | E8 : appareils réels | Faire le parcours de réservation sur un iPhone récent, un Android récent, un vieil Android, texte agrandi | Parcours terminé sans blocage sur les trois | terrain | le kiné ou un proche, avant la mise en service |
| 30 | E8 : accessibilité automatique | Passer un contrôle automatique (axe) sur les écrans de réservation et le planning | 0 violation critique ou sérieuse selon WCAG 2.1 AA `[proposed]` | mécanique | développeur |
| 31 | E8 : accessibilité réelle | Parcours au clavier seul, zoom à 200 %, un lecteur d'écran | Tout est faisable ; le focus est visible ; les erreurs de formulaire sont annoncées | relecture | personne formée à l'accessibilité |
| 32 | E10 : aucun trou visible | Chercher « [à compléter] », TODO, TBD, XXX, lorem, « undefined », « null », « Bonjour , » dans les pages rendues, e-mails et SMS générés, pour chaque cas (prénom manquant, sans e-mail, etc.) | 0 occurrence | mécanique | développeur |
| 33 | E10 : tout ce qui est nommé existe | Suivre chaque lien des pages, e-mails et SMS ; vérifier chaque clé et variable d'environnement utilisée | Tous répondent 200 ; le lien d'annulation pointe vers le domaine du cabinet | mécanique | développeur |
| 34 | E11 : charge | 50 patients simultanés `[proposed]` (à revoir, Q9) × 2 de marge sur un environnement proche de la production | p95 de la réservation inférieur à 1 s `[proposed]` ; erreurs inférieures à 0,5 % `[proposed]` ; 0 double réservation | mécanique | développeur |
| 35 | E11 : sauvegarde | Restaurer la dernière sauvegarde sur un environnement vierge | Tous les RDV à venir présents ; perte maximale 24 h `[proposed]` | mécanique | développeur |
| 36 | E12 : fournisseur SMS en panne | Couper l'accès au fournisseur et réserver | La réservation aboutit ; le rappel est mis en attente puis rejoué, ou signalé au kiné | mécanique | développeur |
| 37 | E2 : une vraie semaine | Le kiné utilise le planning une semaine réelle, en parallèle de son agenda actuel | 0 RDV manquant ou faux par rapport à son agenda ; il dit s'y fier | terrain | le kiné, sur 1 semaine |
| 38 | E1, E8 : vrais patients | 10 patients réels réservent, dont au moins 3 de plus de 65 ans | Au moins 9 sur 10 terminent seuls ; les échecs sont notés avec leur cause | terrain | le kiné, avant l'ouverture générale |
| 39 | E3 : SMS sur vrais téléphones | Envoyer des SMS réels vers des téléphones iOS et Android, chez les 4 opérateurs principaux | Tous reçus, accents lisibles, expéditeur reconnaissable, délai inférieur à 1 min | terrain | le kiné ou un proche |
| 40 | E14 : RDV non honorés | Compter les RDV non honorés avant et après (zone du tableau de l'issue) | Au moins au plancher ; cible si possible | terrain | le kiné, à 8 semaines |
| 41 | E15 : réservation en ligne | Calculer la part des RDV pris en ligne | Au moins au plancher | terrain | le kiné, à 3 mois |
| 42 | E3 : remise réelle | Lire le rapport mensuel du fournisseur SMS | Au moins au plancher sur numéros valides | terrain | le kiné, chaque mois |

## Ce qui passerait et serait faux / What could pass and still be wrong
- Le planning affiche tout correctement, mais deux patients peuvent prendre le même créneau au même instant. Les tests à un seul utilisateur passent → lignes 3, 7, H1.
- Les rappels sont corrects pour la date d'essai, mais faux un lundi, au changement d'heure ou au 31 décembre. Les dates du test sont codées en dur → lignes 12, 16, H2.
- Le patient « supprimé » a disparu de l'écran, mais son nom reste dans le fichier de base, dans les logs ou chez le fournisseur SMS → lignes 23, 24, H3.
- Le SMS est marqué « envoyé » dans l'application, mais n'est jamais remis, ou le texte accentué est coupé en trois messages → lignes 13, 39, 42, H5.
- Le SMS part au bon numéro saisi, mais ce numéro est celui d'un autre (faute de frappe, numéro partagé), et le rappel révèle un RDV à un tiers → lignes 14, 28, question Q7.
- Un patient ne voit que ses RDV dans l'interface, mais l'API répond à qui lui demande l'identifiant d'un autre → lignes 25, H4.
- Le kiné voit les bonnes heures chez lui, mais pas depuis un ordinateur réglé sur un autre fuseau horaire → ligne 6, H7.
- Tous les tests passent, mais aucun patient de 70 ans ne réussit à réserver → lignes 31, 38.

## Non testable en l'état / Not testable as stated
- E14, E15 : sans le taux actuel d'absences et la part actuelle de réservation en ligne, aucun plancher n'est fixable. Question : quel est le taux d'absences sur les 8 dernières semaines ?
- E6 (hébergement) : on ignore si l'obligation d'hébergement certifié HDS s'applique à ce cas. Question : le DPO ou un juriste a-t-il tranché ?
- E3 (« la veille ») : le sens exact pour un lundi, un jour férié ou un RDV pris tard n'est pas défini. Question : voir Q2.

## Couverture / Coverage
| Kind | Visible | Hidden | Who |
|---|---|---|---|
| mécanique | 31 | 7 | scripts, lancés par le juge |
| relecture | 4 | 0 | kiné, un tiers, un juriste ou DPO, une personne formée à l'accessibilité |
| terrain | 7 | 0 | le kiné, ses patients, sur 1 semaine, 8 semaines et 3 mois |

Une boucle automatique peut fermer les 38 lignes mécaniques (78 %). Elle ne décide ni le sens du SMS, ni la conformité juridique, ni l'accessibilité réelle. Elle ne dit pas non plus si les patients réservent en ligne ni si les absences baissent : cela ne se voit que sur le terrain.

## Questions ouvertes / Open questions
- Q1 : taux actuel d'absences et part actuelle de réservation en ligne ?
- Q2 : que veut dire « la veille » pour un lundi ou un lendemain férié ? Et que fait-on d'un RDV pris pour demain après l'heure d'envoi ?
- Q3 : un seul kiné et un seul cabinet, ou plusieurs ?
- Q4 : quels types de séance (bilan, suivi, domicile) et quelles durées ? Faut-il exiger l'ordonnance ou le nombre de séances prescrites ?
- Q5 : jusqu'à quand un patient peut-il annuler seul ?
- Q6 : l'hébergement certifié HDS est-il obligatoire ici ? À faire trancher par un juriste ou DPO.
- Q7 : faut-il vérifier le numéro de téléphone par un code envoyé à la réservation ?
- Q8 : qui développe (personne, équipe ou agent en boucle) et qui juge ? Si c'est un agent, ajoutez-moi la mention et j'écris le critère d'arrêt de la boucle.
- Q9 : combien de patients actifs, et à quel moment de pic ? Les 50 patients simultanés de la ligne 34 sont une proposition.
- Q10 : que fait-on des patients sans mobile ?

✂ ----- PART CACHÉE, pour le juge seul, ne pas transmettre à l'auteur / HIDDEN PART, judge only -----

## Part cachée / Hidden part
Chaque ligne reprend une exigence connue de l'auteur, avec d'autres données ou un autre angle.

| # | Élément ou situation | Vérification | Résultat attendu | Preuve | Qui vérifie |
|---|---|---|---|---|---|
| H1 | E4 : double réservation par deux canaux | Un patient en ligne et le kiné en saisie manuelle visent le même créneau à la même milliseconde ; un RDV de 30 min est placé juste avant un bilan de 45 min ; dernier créneau avant la fermeture | 1 seul RDV créé, jamais de chevauchement, jamais de débordement après la fermeture | mécanique | juge, hors de l'espace de l'auteur |
| H2 | E3, E9 : dates inédites | Rappels avec horloge figée au 31 décembre vers le 1er janvier, au 29 février 2028, au 28 mars 2027 (changement d'heure), pour un RDV à 00 h 15 et un à 23 h 30 | Un seul rappel par RDV, le bon jour, à l'heure locale du cabinet | mécanique | juge |
| H3 | E6 : effacement avec valeurs inhabituelles | Valeur témoin placée dans un champ libre, dans un numéro écrit « 06 12… » et « +33 6… », et dans une erreur provoquée ; suppression ; recherche dans la base, les fichiers annexes, les logs, les sauvegardes, les journaux du fournisseur SMS | Introuvable partout, ou lieu et durée de conservation écrits | mécanique | juge, copie des fichiers |
| H4 | E7 : modifier, pas seulement lire | Le patient A tente de modifier ou annuler le RDV de B par l'API ; réutilisation d'un jeton déjà consommé ; session patient sur les routes du kiné | Tout est refusé, rien n'est modifié en base | mécanique | juge |
| H5 | E3 : noms difficiles | SMS pour « Jean-Baptiste de la Tour-Maubourg », un nom avec émoji, un prénom de 40 caractères, un champ libre contenant « lombalgie » | Pas de coupure au milieu d'un mot, 2 segments au plus, aucun terme de santé recopié depuis un champ libre | mécanique | juge |
| H6 | E10 : champs vides | Patient sans prénom, sans e-mail, avec un motif vide : générer toutes les pages, e-mails et SMS | 0 « Bonjour , », « undefined », « null », crochet vide ou champ vide | mécanique | juge |
| H7 | E2, E9 : navigateur d'un autre fuseau | Ouvrir le planning avec un ordinateur réglé sur UTC et sur un fuseau d'outre-mer | Les heures affichées restent celles du cabinet, aussi bien pour l'affichage que pour la saisie | mécanique | juge |

Garde-fous :
- H1 garde les lignes 2, 3 et 7 ; le test visible n'essaie qu'un seul créneau.
- H2 garde les lignes 11, 12 et 16 ; des dates fixes se codent en dur.
- H3 garde les lignes 23 et 24.
- H4 garde les lignes 10 et 25.
- H5 garde la ligne 13.
- H6 garde la ligne 32.
- H7 garde les lignes 6 et 16.

La ligne 6 est faible : elle ne teste qu'un seul fuseau. H7 le montre.

Si l'auteur est un agent, ajoutez : les tests, jeux d'essai et configuration restent inchangés (somme de contrôle tenue par le juge), aucun test sauté, supprimé ou affaibli, et le code ne contient aucune valeur littérale des jeux d'essai.