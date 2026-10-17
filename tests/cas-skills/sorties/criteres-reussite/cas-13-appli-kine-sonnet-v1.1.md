<!-- Sortie brute de criteres-reussite 1.1.0, Sonnet, 0.20 $, 2 min. -->

---
status: draft
skill: criteres-reussite
deliverable_kind: software (application web de prise de rendez-vous, avec envoi de SMS)
author: non précisé (personne, équipe ou agent en boucle)
judge: quelqu'un d'autre que l'auteur (non précisé)
---

# Critères de réussite : prise de rendez-vous du cabinet de kinésithérapie

## Synthèse / Summary
On livre une application où les patients réservent en ligne, où le kiné consulte son planning et où chaque patient reçoit un SMS la veille de son rendez-vous. « Terminé » veut dire qu'aucun créneau ne peut être pris deux fois, que chaque rendez-vous actif reçoit exactement un rappel lisible sans révéler de donnée de santé, et que le planning du kiné est toujours exact. Le plan compte 43 lignes visibles (34 mécanique, 3 relecture, 6 terrain) et 8 lignes cachées (7 mécanique, 1 relecture). Une boucle automatique peut en fermer environ 80 %. Le résultat réel (moins de rendez-vous non honorés) ne se voit que sur le terrain, après trois mois.

Je n'ai pas pu savoir qui demande ce plan ni qui développe. J'ai supposé que le demandeur est le juge ou le cabinet, donc la partie cachée est écrite. **Si vous êtes aussi l'auteur, ne lisez pas le bloc après la coupure.** Relancez-moi avec `requester: author` et je le remplace par une demande scellée.

Lignes bloquantes / Blocking lines : 3, 12, 17, 20, 22, 24, 29.

Noyau / Core : 1, 3, 4, 5, 7, 11, 12, 13, 17, 18, 19, 20, 21, 22, 24, 25, 26, 28, 29, 30, 31, 35, 38, 40. Je compte environ 1 h pour rejouer le noyau, dont 20 min de script, et environ une demi-journée pour le plan complet, hors lignes terrain.

Annexe logiciel appliquée. Les annexes document, négociation et travaux ne s'appliquent pas.

## Exigences / Requirements
| E | Exigence | Source | Livrable ou issue |
|---|---|---|---|
| E1 | Les patients réservent un rendez-vous en ligne | « les patients réservent en ligne » | livrable |
| E2 | Le kiné voit son planning | « le kiné voit son planning » | livrable |
| E3 | Chaque patient reçoit un rappel SMS la veille | « rappel par SMS la veille » | livrable (la réception réelle dépend de l'opérateur) |
| E4 | Aucun créneau n'est attribué deux fois et seuls des créneaux réellement libres sont proposés | [inferred] | livrable |
| E5 | Les données de santé et personnelles sont protégées : accès, journaux, SMS discret, suppression, hébergement | [inferred] | livrable |
| E6 | La réservation est utilisable sur téléphone et accessible | [inferred] | livrable |
| E7 | Le patient peut annuler ou déplacer son rendez-vous | [inferred] | livrable |
| E8 | La continuité tient quand une dépendance tombe (fournisseur SMS, application) | [inferred] | livrable |
| E9 | L'application résiste à l'abus (réservations en masse, devinette de liens, énumération) | [inferred] | livrable |
| E10 | Le kiné gère ses disponibilités, absences et rendez-vous pris par téléphone | [inferred] | livrable |
| E11 | Moins de rendez-vous non honorés et un cabinet allégé du téléphone | [inferred] | issue |

## Issue visée / Outcome zone
Les seuils sont fixés par le cabinet avant le démarrage, pas après avoir vu les résultats. Mes valeurs sont des propositions `[proposed]`.

| E | Issue | Plancher (échec en dessous) | Cible (succès au-dessus) | Fixé par | Mesuré quand |
|---|---|---|---|---|---|
| E11 | Taux de rendez-vous non honorés | pas meilleur que le taux mesuré avant lancement `[proposed]` | baisse d'un tiers `[proposed]` | le kiné, sur sa mesure de référence | 3 mois après le lancement |
| E11 | Part des rendez-vous pris en ligne | moins d'un quart des nouveaux rendez-vous `[proposed]` | plus de la moitié `[proposed]` | le kiné | 3 mois après le lancement |
| E11 | Appels de prise ou de déplacement de rendez-vous | pas de baisse | baisse nette ressentie par le kiné et le secrétariat | le kiné | 1 mois après le lancement |

## Critères vérifiables / Checks
| # | Élément ou situation | Vérification | Résultat attendu | Preuve | Qui vérifie |
|---|---|---|---|---|---|
| 1 | E1 : réservation nominale | Parcours de bout en bout : choisir un créneau, saisir les informations, valider | Écran de confirmation, et le rendez-vous apparaît dans le planning du kiné | mécanique | développeur ; données synthétiques |
| 2 | E1/E4 : créneaux proposés | Demander les créneaux d'une semaine contenant horaires fermés, absences, jours fériés et rendez-vous existants | Aucun créneau hors horaires, en absence ou déjà pris n'est proposé | mécanique | développeur |
| 3 | E4 : double réservation | 20 requêtes simultanées sur le même créneau | Exactement 1 réussit, les 19 autres reçoivent un refus explicite, 1 seul rendez-vous en base | mécanique | développeur |
| 4 | E4 : règles côté serveur | Appel direct de l'API pour un créneau pris, passé, fermé ou inexistant | Refus à chaque fois, sans création de rendez-vous (un bouton grisé ne prouve rien) | mécanique | développeur |
| 5 | E7 : annulation et déplacement par le patient | Annuler, puis déplacer un rendez-vous | Le créneau est libéré, le nouveau est pris, le planning est à jour en moins d'1 minute `[proposed]` | mécanique | développeur |
| 6 | E1 : contenu de la confirmation | Lire l'écran et le message de confirmation | Date, heure, adresse du cabinet et lien d'annulation présents, aucun champ vide | mécanique | développeur |
| 7 | E1 : changement d'heure | Réserver des créneaux la veille et le lendemain du passage heure d'été/hiver | Heure affichée, planning et heure d'envoi du SMS corrects en Europe/Paris | mécanique | développeur |
| 8 | E6 : téléphones réels | Réserver sur un vieil Android, iOS Safari, petit écran, texte agrandi | Réservation menée à terme en 3 min ou moins `[proposed]` par quelqu'un qui n'a jamais utilisé l'application | terrain | le cabinet, avant ouverture, avec 5 patients volontaires |
| 9 | E6 : accessibilité | Audit automatique, puis réservation au clavier seul | Aucune erreur bloquante de niveau WCAG 2.1 AA `[proposed]` et réservation possible sans souris | relecture | auditeur accessibilité |
| 10 | E4/E1 : créneau pris pendant la saisie | Deux patients visent le même créneau, le second valide en retard | Le second voit un message clair et les prochains créneaux libres, pas d'erreur technique | mécanique | développeur |
| 11 | E2 : planning exact | Après 30 réservations, annulations et déplacements, comparer le planning affiché à la base | Le planning contient exactement les rendez-vous actifs, ni plus ni moins | mécanique | développeur |
| 12 | E2/E5 : accès au planning | Requêtes sans session, avec une session patient, puis avec l'identifiant d'un autre patient | Refus (401/403) sans fuite de contenu, et un patient ne lit jamais le rendez-vous d'un autre | mécanique | développeur |
| 13 | E10 : absences | Le kiné pose une absence sur une plage contenant déjà des rendez-vous | Les créneaux disparaissent de la réservation, et les rendez-vous existants sont signalés au kiné au lieu d'être supprimés en silence | mécanique | développeur |
| 14 | E10 : rendez-vous saisi par le kiné | Le kiné ajoute puis annule un rendez-vous pris par téléphone | Le créneau est occupé ou libéré côté réservation, et le patient saisi reçoit le rappel | mécanique | développeur |
| 15 | E2 : fraîcheur | Une réservation est faite pendant que le planning est ouvert | La réservation apparaît en 60 s ou moins `[proposed]` sans recharger à la main | mécanique | développeur |
| 16 | E2 : usage réel du planning | Le kiné utilise le planning pendant une semaine sur son appareil habituel | Il lit sa journée sans aide ni papier parallèle, et note ses gênes | terrain | le kiné, première semaine |
| 17 | E3 : un rappel par rendez-vous | Semer 50 rendez-vous actifs le lendemain, lancer la tâche d'envoi, interroger le bac à sable du fournisseur | 50 SMS envoyés, un par rendez-vous, chacun au bon numéro | mécanique | développeur |
| 18 | E3 : heure d'envoi | Horloge simulée pour la veille d'un rendez-vous | Envoi entre 17 h et 19 h Europe/Paris la veille `[proposed]` | mécanique | développeur |
| 19 | E3 : rendez-vous annulé ou déplacé | Annuler un rendez-vous, en déplacer un autre, lancer la tâche | Aucun SMS pour l'annulé, un SMS à la nouvelle date pour le déplacé, aucun pour l'ancienne | mécanique | développeur |
| 20 | E3 : une seule fois | Relancer la tâche, la redémarrer en cours d'envoi, la lancer sur deux instances | Toujours un seul SMS par rendez-vous | mécanique | développeur |
| 21 | E3 : réservation tardive | Réserver à 20 h pour 9 h le lendemain | Le patient reçoit son SMS dans les 5 min `[proposed]` après la réservation, sans doublon avec le rappel de la veille | mécanique | développeur |
| 22 | E3/E5 : contenu du SMS | Générer les SMS de tous les cas et les analyser | Date, heure, nom du cabinet et moyen d'annuler présents ; aucun motif, pathologie ni nom de patient autre que le sien ; 2 segments ou moins `[proposed]`, accents compris | mécanique | développeur |
| 23 | E3 : lisibilité du SMS | Lire le texte comme un patient de 75 ans | Compris sans explication, ton neutre, pas de jargon | relecture | une personne extérieure au projet |
| 24 | E8 : fournisseur SMS indisponible | Couper le fournisseur, réserver, lancer la tâche | La réservation aboutit, les envois sont retentés, et après épuisement des tentatives le kiné voit la liste des patients non prévenus | mécanique | développeur |
| 25 | E3 : numéro invalide ou fixe | Saisir un numéro invalide, un fixe, un numéro étranger | Refus ou signalement au moment de la réservation, et aucun SMS vers un numéro invalide | mécanique | développeur |
| 26 | E3/E5 : consentement et refus du SMS | Réserver avec refus du SMS, puis répondre STOP après un premier rappel | La réservation reste possible, aucun rappel ensuite, et l'information sur le SMS est affichée avant validation | mécanique | développeur |
| 27 | E3 : réception réelle | Envoyer de vrais SMS sur 3 opérateurs | Reçus en 5 min ou moins `[proposed]`, expéditeur lisible, accents corrects | terrain | développeur, avant ouverture |
| 28 | E5 : hébergement des données de santé | Lire le contrat d'hébergement et le registre de traitements | Le statut de l'hébergeur par rapport aux données de santé est établi et écrit (certification HDS si les données la requièrent) | relecture | délégué à la protection des données ou juriste |
| 29 | E5 : pas de donnée dans les journaux | Réserver avec un nom et un téléphone « canaris » uniques, puis chercher dans journaux, suivi d'erreurs, statistiques, URL | Valeur absente de tous ces endroits | mécanique | développeur ; données synthétiques |
| 30 | E5 : suppression | Supprimer le patient canari, puis chercher en octets bruts dans la base, ses fichiers annexes (`-wal`, `-journal`), les journaux, exports, sauvegardes | Canari introuvable, ou durée de conservation écrite pour chaque endroit où il reste | mécanique | développeur sur copie |
| 31 | E9 : liens et énumération | Deviner des liens d'annulation, essayer 10 mauvais jetons, interroger un numéro connu puis inconnu | Verrouillage après les essais, jeton expiré refusé, réponse identique pour numéro connu et inconnu | mécanique | développeur |
| 32 | E9 : réservation en masse | Un même numéro ou une même adresse IP tente 20 réservations | Plafond de rendez-vous actifs par patient (3 `[proposed]`), limitation de débit, planning non saturé | mécanique | développeur |
| 33 | E1 : charge de réservation | 50 réservations simultanées à l'ouverture de nouveaux créneaux `[proposed]`, sur environnement de même taille que la production | p95 sous 2 s, 0 % d'erreur, aucun double rendez-vous | mécanique | développeur |
| 34 | E3 : charge d'envoi | 500 rappels dans la même tâche | Tous envoyés en moins de 10 min, sans doublon ni perte | mécanique | développeur |
| 35 | Contenu : trous | Récupérer chaque écran, e-mail et SMS rendus (toutes variantes) et chercher `[à compléter]`, TODO, lorem, `{{ }}` vides | Aucune occurrence, aucun bloc requis vide | mécanique | développeur |
| 36 | Contenu : cohérence | Comparer adresse, téléphone et conditions d'annulation entre page de réservation, confirmation et SMS | Mêmes valeurs partout, égales à la configuration du cabinet | mécanique | développeur |
| 37 | E8 : restauration | Restaurer une sauvegarde sur une copie | Planning et rendez-vous identiques à la source | mécanique | développeur |
| 38 | E8 : application hors service | Couper l'application la veille d'une journée de consultation | Le kiné retrouve les rendez-vous du lendemain, par export, impression ou équivalent préparé à l'avance | terrain | le kiné et le développeur, répétition à blanc |
| 39 | E7 : états après coup | Ouvrir le lien d'un rendez-vous passé, annulé, ou après le délai d'annulation | Message correct, pas de modification possible, aucune erreur technique | mécanique | développeur |
| 40 | Test des tests | Retirer le contrôle anti-doublon, puis la suppression de la ligne 30 | Les lignes 3 et 30 échouent | mécanique | développeur |
| 41 | E11 : rendez-vous non honorés | Comparer le taux à la mesure de référence faite avant lancement | Au-dessus du plancher, vers la cible | terrain | le kiné, 3 mois après |
| 42 | E11 : adoption | Compter la part des rendez-vous pris en ligne et les appels restants | Au-dessus du plancher, vers la cible | terrain | le kiné, 1 puis 3 mois après |
| 43 | E3 : rendez-vous du lundi | Rendez-vous un lundi, tâche lancée le week-end | Rappel envoyé le jour défini par la règle du cabinet (voir question 1), jamais « perdu » | mécanique | développeur, après réponse à la question 1 |

## Ce qui passerait et serait faux / What could pass and still be wrong
- Le test de double réservation passe séquentiellement mais deux requêtes simultanées réservent le même créneau → lignes 3, 33, H1.
- Le planning est correct à l'écran mais l'API renvoie les rendez-vous d'autres patients, ou un lien d'annulation est accessible avec un autre identifiant → lignes 12, 31, H5.
- Le test d'envoi passe parce que le faux fournisseur répond toujours « OK », alors qu'un vrai échec serait marqué « envoyé » → lignes 24, H7.
- La tâche déduplique par numéro, donc une famille qui partage un téléphone perd des rappels → lignes 17, H3.
- Le SMS affiche un nom de service ou un motif lisible sur l'écran verrouillé → lignes 22, H8.
- La suppression retire le patient de l'écran mais son nom reste dans la base, les journaux ou une sauvegarde → lignes 29, 30, H4.
- Un rappel est correct à 17 h en été et décalé d'une heure après le changement d'heure → lignes 7, 18, H2.
- Seul le chemin heureux est testé : pas de page d'erreur, d'e-mail d'annulation ni de journée vide → lignes 35, H6.
- Toute la suite est verte mais teste des fonctions mortes → ligne 40.
- Tout fonctionne et les patients ne viennent pas plus qu'avant → lignes 41, 42.

## Non testable en l'état / Not testable as stated
- E3, « la veille » : l'heure d'envoi et la règle du lundi ne sont pas définies. Je propose 17-19 h (ligne 18). Question : quelle heure, et un rendez-vous du lundi est-il rappelé le dimanche ou le vendredi ?
- E7, le délai d'annulation n'est pas défini. Question : jusqu'à quand le patient peut-il annuler en ligne ?
- E1, « facile » : écarté, remplacé par les lignes 8 et 9.

## Couverture / Coverage
| Kind | Visible | Hidden | Who |
|---|---|---|---|
| mécanique | 34 | 7 | script, rejoué par le juge hors de l'espace de l'auteur |
| relecture | 3 | 1 | auditeur accessibilité, juriste ou DPO, relecteur extérieur |
| terrain | 6 | 0 | le kiné, des patients volontaires, le développeur, avant ouverture puis à 1 et 3 mois |

Une boucle peut fermer environ 80 % des lignes (41 sur 51), soit les lignes mécaniques. Elle ne dit rien de la qualité du texte du SMS, de l'accessibilité réelle, de la réception sur de vrais téléphones, de la conformité de l'hébergement, ni du résultat clé : les patients viennent-ils davantage ?

## Questions ouvertes / Open questions
1. Heure d'envoi du rappel et règle du lundi (lignes 18 et 43).
2. Un seul kiné ou plusieurs ? Le brief dit « le kiné ». Plusieurs praticiens imposeraient des plannings séparés et une règle de choix.
3. Le patient doit-il créer un compte ou réserve-t-il avec son nom et son téléphone ? Cela change les lignes 12 et 31.
4. Le motif ou l'ordonnance est-il demandé à la réservation ? Si oui, c'est une donnée de santé de plus (lignes 28 et 29).
5. Durées et types de séance (bilan ou séance) : combien de types, quelles durées ?
6. Fournisseur de SMS et nom d'expéditeur (lignes 24 et 27).
7. Durée de conservation des données après le dernier rendez-vous et obligations légales éventuelles (ligne 30).
8. Qui développe : une équipe ou un agent qui itère jusqu'au vert ? Dans le second cas, j'ajoute le critère d'arrêt de la boucle (tests figés par somme de contrôle, aucun test sauté).

✂ ----- PART CACHÉE — pour le juge seul, ne pas transmettre à l'auteur / HIDDEN PART — judge only -----

## Part cachée / Hidden part
| # | Élément ou situation | Vérification | Résultat attendu | Preuve | Qui vérifie |
|---|---|---|---|---|---|
| H1 | E4 : chevauchement | Réserver en ligne un créneau pendant que le kiné ajoute à la main un rendez-vous qui le chevauche partiellement (durées différentes), en simultané | Un seul des deux aboutit, aucun chevauchement en base | mécanique | juge, hors espace de l'auteur |
| H2 | E3 : changement d'heure | Rendez-vous le lundi qui suit le passage à l'heure d'été et celui qui suit le passage à l'heure d'hiver | Le rappel part à la bonne heure locale, la bonne veille, une fois | mécanique | juge |
| H3 | E3 : numéro partagé | Deux patients (parent et enfant) avec le même numéro, rendez-vous le même jour | Deux SMS distincts, chacun identifiant son rendez-vous, aucun perdu par déduplication | mécanique | juge |
| H4 | E5 : suppression, autres identifiants | Canaris sur nom avec accent, e-mail et numéro au format +33, puis suppression et recherche en octets bruts, journaux du bac à sable SMS compris | Introuvables, ou rétention écrite par endroit | mécanique | juge |
| H5 | E5/E9 : accès croisés | Annuler le rendez-vous d'un autre patient par jeton ou identifiant, appeler des routes du kiné avec une session patient, varier les méthodes HTTP | Refus à chaque fois, sans création, modification ni fuite | mécanique | juge |
| H6 | Contenu : états rares | Récupérer pages d'erreur, 404, e-mail d'annulation, journée vide du planning, nom très long, et chercher placeholders et blocs vides | Aucun trou, aucun champ vide | mécanique | juge |
| H7 | E8 : faux succès du fournisseur | Fournisseur simulé qui répond 200 mais signale « échec de livraison », ou qui expire, ou renvoie un échec partiel | Le rappel n'est jamais marqué « envoyé » sur un échec, il est retenté, et le kiné voit les non-prévenus | mécanique | juge |
| H8 | E5 : écran verrouillé | Lire un SMS réel tel qu'affiché sur un écran verrouillé, en se mettant à la place d'un tiers qui le voit | On y lit date et lieu seulement, sans motif, pathologie ni nom de soin | relecture | juge |

Gardes : H1 → ligne 3, exposée à un test séquentiel ; H2 → lignes 7 et 18 ; H3 → ligne 17, exposée à une déduplication par numéro ; H4 → lignes 29 et 30, exposées à un canari testé sous une seule forme ; H5 → lignes 12 et 31 ; H6 → ligne 35, qui ne couvre que les pages principales ; H7 → ligne 24, exposée à un faux fournisseur qui dit toujours OK ; H8 → ligne 22.

Aucune de ces lignes n'ajoute une exigence inconnue de l'auteur.