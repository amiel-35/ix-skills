<p align="center">
  <img src="docs/assets/banner.svg" alt="ix-skills : des skills de knowledge-work atomiques" width="100%">
</p>

<p align="center">
  <a href="LICENSE"><img alt="Licence" src="https://img.shields.io/github/license/amiel-35/ix-skills?color=7f9a96"></a>
  <img alt="Version du plugin" src="https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fraw.githubusercontent.com%2Famiel-35%2Fix-skills%2Fmain%2Fdist%2F.claude-plugin%2Fplugin.json&query=%24.version&label=plugin&color=7fc8bd">
  <img alt="Claude Code" src="https://img.shields.io/badge/Claude%20Code-plugin-D97757">
  <img alt="Skills" src="https://img.shields.io/badge/skills-36-3d6b73">
  <img alt="Platforms" src="https://img.shields.io/badge/also-Codex%20%C2%B7%20GPT%20%C2%B7%20Gemini%20%C2%B7%20mystaffy-56707a">
</p>

<p align="center">
  <a href="#démarrage-rapide"><b>Démarrage rapide</b></a> ·
  <a href="#skills-disponibles"><b>Catalogue</b></a> ·
  <a href="#pipelines-typiques"><b>Pipelines</b></a> ·
  <a href="#contribuer"><b>Contribuer</b></a> ·
  <a href="README.md"><b>English</b></a>
</p>

---

<details>
<summary><b>Sommaire</b></summary>

- [À propos](#à-propos)
- [Démarrage rapide](#démarrage-rapide)
- [Convention de corpus — la sortie nulle](#convention-de-corpus--la-sortie-nulle)
- [Skills disponibles](#skills-disponibles)
- [Pipelines typiques](#pipelines-typiques)
- [Installation](#installation)
- [Structure](#structure)
- [Packager](#packager)
- [Projets frères](#projets-frères)
- [Contribuer](#contribuer)
- [Crédits](#crédits)
- [Licence](#licence)

</details>

## À propos

Skills de knowledge-work atomiques — portables sur Claude, GPT, Gemini, mystaffy.

37 skills en 4 catégories (2 en draft). Chaque skill encode un **processus cognitif**, pas une expertise métier. Les skills métier (RH, juridique, finance, achats, produit, tech) sont dans [ix-recipes](https://github.com/amiel-35/ix-recipes), qui s'appuie sur ces atomes.

---

## Démarrage rapide

Installer le plugin dans Claude Code :

```bash
claude plugin marketplace add amiel-35/ix-skills
claude plugin install ix-skills@ix-skills
```

Redémarrer Claude Code. Les skills sont préfixés (`critique` devient `/ix-skills:critique`), et Claude les reconnaît aussi dans une demande ordinaire :

- *« Critique ce brief : qu'est-ce qui ne va pas ? »*
- *« Avant de décider, explore les options. »*
- *« Vérifie cette note contre la source. »*

Autres plateformes (Cowork, Codex CLI, Antigravity CLI, mystaffy, GPT, Gemini) : voir [Installation](#installation).

---

## Convention de corpus — la sortie nulle

Un skill qui n'a rien à produire ouvre sa réponse par « RAS — » suivi du
motif, et s'arrête. Le jeton est littéral et identique dans tout le corpus :
c'est ce qui le rend greppable et testable.

---

## Skills disponibles

Cliquer sur une catégorie pour la déplier.

<details>
<summary><b>🧠 Cognitif — atomes de processus</b> — 18 skills</summary>


Opérations primitives sur un contenu, un problème ou une décision. Chaque skill encode un seul geste cognitif — ils sont conçus pour se chaîner, pas se substituer.

| id | Rôle | Contrainte clé |
|---|---|---|
| `critique` | Identifier les failles d'un contenu sans proposer de solution | Analyse seulement — **ne corrige pas** |
| `correction` | Transformer une critique en directives actionnables | Transforme une critique — **ne ré-analyse pas** |
| `simplify` | Repérer ce qui peut être retiré sans changer le fond | Identifie les retraits — **ne les applique pas** (voir `correction`) |
| `rephrase` | Restituer le sens réel d'un contenu dense ou ambigu | Réinterprète — le sens peut évoluer, pas seulement la forme |
| `explorer` | Générer un espace d'options — écrit d'abord la réponse par défaut puis l'écarte ; `breadth` décide si le véhicule nommé dans la demande reste une contrainte (`standard`) ou est écarté lui aussi (`broad`) | Largeur — **ne choisit pas** |
| `decision` | Arbitrer avec trade-offs visibles et recommandation nette | Choisit parmi des options existantes — **n'en génère pas** |
| `deliver` | Transformer un artifact en livrable partageable | Mise en forme et calibrage audience |
| `research` | Construire un socle factuel sourcé avant toute décision | Sources obligatoires en mode standard et approfondi — le mode `flash` répond sur la seule mémoire du modèle |
| `synthese` | Condenser un long contenu en synthèse actionnable | Compression avec perte — le détail est sacrifié intentionnellement |
| `decomposer` | Structurer un problème complexe en sous-problèmes actionnables | Les dépendances entre sous-problèmes sont identifiées, pas masquées |
| `revue-feedback` | Évaluer un feedback avant de l'accepter ou le refuser | Évalue une critique reçue — pas votre propre artifact |
| `fact-check` | Vérifier un texte contre des preuves de référence, affirmation par affirmation — confirmée, contredite, absente de la source, non vérifiable | Un verdict par affirmation, chacun appuyé sur une citation exacte de la source — **la source est une entrée**, le mode `closed` ignore ce que le modèle sait |
| `calc-check` | Recalculer chaque chiffre dérivé d'un texte — écart, taux, ratio, total, NRR, ROI — à partir des valeurs de la source, opérations écrites pas à pas — exact, écart, non recalculable, incohérent | **Une valeur absente de la source n'est jamais devinée** — le chiffre est `non recalculable` ; signale, **ne corrige pas** |
| `controle-qualite` | Vérifier un livrable contre un référentiel de règles fourni — gabarit, charte, orthographe, vocabulaire interdit — en mode `sweep` (trouver chaque manquement) ou `verdict` (trancher une liste suspectée) | Un verdict par constat, avec la règle et le passage exact — **une règle absente du référentiel n'est pas une règle** |
| `prioritize` | Ordonner une liste d'éléments par ordre d'attaque avec critères explicites — 8 méthodes (ICE, RICE, WSJF, MoSCoW, Kano, Eisenhower, valeur/effort, notation pondérée), chacune détaillée dans une fiche lue seulement si elle est choisie | Séquence des items — **ne tranche pas entre options exclusives** (utiliser `decision`) |
| `problem-framing` *(draft)* | Reformuler un sujet flou en problème actionnable | Formule la question centrale — **ne la résout pas** |
| `questioning` | Générer les bonnes questions à poser — signale chaque solution nommée (terme-parapluie d'abord, puis paramètres de taille, puis sous-artefacts) et demande si elle a été choisie ou si c'est la première idée venue | Questions seulement — **ne répond pas et n'explore pas**, ne retire jamais un terme nommé (utiliser `explorer`) |
| `argumentation` *(draft)* | Construire une argumentation structurée pour défendre ou attaquer une position | Construit le plaidoyer — **ne l'évalue pas** (utiliser `critique`) |

#### Distinctions clés

**`critique` vs `revue-feedback`**
`critique` analyse *votre propre artifact* (un document, un plan, une proposition) pour en trouver les failles. `revue-feedback` traite *un feedback que quelqu'un d'autre vous a donné* — il évalue si vous devez l'accepter, le nuancer ou le refuser avant de répondre. L'un est éditorial, l'autre est diplomatique.

**`critique` vs `fact-check` vs `calc-check` vs `controle-qualite` vs `quality-check`**
`critique` juge le fond — ce qui est faible, flou, manquant — et n'a besoin d'aucun référentiel. `fact-check` vérifie un texte contre des *preuves* : un verdict par affirmation (confirmée, contredite, absente de la source, non vérifiable), chacun appuyé sur une citation exacte de la source. `calc-check` prend le relais là où `fact-check` s'arrête sur les chiffres : un écart de 12,4 % calculé à partir de deux montants n'est pas *dans* la source, donc `fact-check` ne peut que le dire « absent de la source », juste ou faux ; `calc-check` refait le calcul à partir des valeurs de la source et dit s'il tient. `controle-qualite` vérifie un livrable contre des *règles* données en entrée — gabarit, charte, orthographe, vocabulaire interdit : un verdict par constat, avec la règle et le passage exact. Ces vérificateurs citent un texte qu'un script peut retrouver, ce qui permet de les confier à un modèle moins cher et de les vérifier à leur tour. `quality-check` pose encore une autre question : non pas si un texte est fidèle à sa source, mais si les sources elles-mêmes sont fiables.

**`simplify` vs `rephrase` vs `synthese`**
- `simplify` nomme le bruit qui pourrait sauter en conservant toute l'information — il identifie les retraits, `correction` les applique.
- `rephrase` réécrit un contenu dense ou ambigu pour rendre le sens réel lisible — il réinterprète, ne coupe pas seulement.
- `synthese` sacrifie délibérément le détail pour extraire l'essentiel — compression avec perte qui produit une synthèse actionnable.

**`explorer` vs `decision`**
Conçus pour fonctionner en séquence. `explorer` cartographie l'espace des options sans s'engager (d'abord en largeur). `decision` arbitre parmi des options existantes avec des trade-offs explicites et une recommandation (en profondeur). Lancer `decision` sans `explorer` risque de figer le choix trop tôt sur un espace incomplet.

**`critique` vs archétypes Advisory (ex. `dixieme-homme`, `contrarian`)**
`critique` est un contrôle qualité sur *votre propre artifact* — éditorial, il trouve les failles dans ce que vous avez produit. Les archétypes Advisory challengent *une croyance, un plan ou une décision* depuis une perspective spécifique — ils opèrent au niveau du raisonnement et des convictions, pas de la qualité textuelle. Utilisez `critique` pour améliorer un document ; utilisez un archétype Advisory pour stress-tester une conclusion.

</details>

<details>
<summary><b>⚔️ Conseil — archétypes de perspective</b> — 10 skills</summary>


Chaque skill impose une posture cognitive spécifique. Ils ne sont pas interchangeables — choisir en fonction de ce qu'on veut stress-tester. Lancer `chairman` après plusieurs pour synthétiser.

`contrarian`, `firstprinciples`, `expansionist`, `outsider`, `executor` et `chairman` reprennent les rôles du « LLM Council » d'Ole Lehmann, construit sur la méthode d'Andrej Karpathy ; voir [Crédits](#crédits).

---

#### `contrarian` — Points de défaillance et hypothèses non vérifiées

**Origine :** L'*advocatus diaboli* (avocat du diable), formalisé dans le droit canon catholique. L'Église exigeait un critique désigné pour plaider contre toute canonisation proposée, pour garantir la rigueur. Adopté dans la gestion de la décision et l'analyse de renseignement pour institutionnaliser la dissidence. En tant que *demande*, en revanche, « joue l'avocat du diable » va vers `dixieme-homme`, qui plaide la thèse adverse complète — `contrarian` creuse le seul point de rupture.

**Objectif :** Forcer la confrontation avec la façon la plus probable dont votre plan échoue — avant de vous engager.

**Fonctionnement :** Identifie le seul argument le plus solide contre votre décision, fait surface les hypothèses non validées, et nomme la condition dans laquelle tout s'effondre. Délibérément à sens unique vers l'échec, pas une revue équilibrée.

**Quand l'utiliser :** Vous avez un plan auquel vous croyez et voulez en trouver la vulnérabilité principale avant de le présenter ou l'exécuter. Différent de `dixieme-homme` (qui construit une thèse adverse complète) ou de `red-team` (qui raisonne comme un adversaire externe).

---

#### `executor` — Est-ce que ça tient dans la réalité ?

**Origine :** La technique du *pré-mortem*, développée par Gary Klein (1989). Plutôt que demander "qu'est-ce qui pourrait mal tourner ?", on imagine que le plan a déjà échoué et on remonte pour expliquer pourquoi.

**Objectif :** Ancrer les plans abstraits dans la réalité opérationnelle avant le lancement.

**Fonctionnement :** Teste si le plan est réellement exécutable — ressources manquantes, délais irréalistes, dépendances cachées, facteurs humains ignorés par la réflexion stratégique. La perspective est celle de quelqu'un qui doit livrer, pas concevoir.

**Quand l'utiliser :** Après qu'un plan est formé, avant que l'exécution commence. Particulièrement utile pour les plans construits par des personnes qui ne seront pas celles qui les exécutent.

---

#### `expansionist` — L'upside manquant

**Origine :** Le concept de *possible adjacent* du théoricien de la complexité Stuart Kauffman — à tout moment, les possibilités adjacentes sont déterminées par ce qui existe déjà. Appliqué à la stratégie pour révéler les options qu'on n'a pas considérées parce qu'elles n'étaient pas évidentes depuis la position de départ.

**Objectif :** Éviter le rétrécissement de scope et les leviers manqués en cartographiant ce qui est adjacent à la position actuelle.

**Fonctionnement :** Cartographie les marchés adjacents, partenariats possibles, angles inexploités et leviers non nommés. Délibérément optimiste et génératif — pas une analyse de risques.

**Quand l'utiliser :** Vous avez défini une stratégie ou une offre et voulez vérifier si vous avez laissé de l'upside évident sur la table.

---

#### `firstprinciples` — La vraie question sous la question

**Origine :** Raisonnement par premiers principes aristotélicien et méthode socratique. Popularisé en technologie par Elon Musk — plutôt que demander "comment acheter des fusées moins cher ?", SpaceX a demandé "quels sont les coûts réels des matières premières d'une fusée ?" et a construit à partir de là.

**Objectif :** Dissoudre les fausses contraintes en revenant aux vérités fondamentales. Séparer ce qui est réellement vrai de ce qui est simplement conventionnel.

**Fonctionnement :** Supprime la pensée analogique ("on fait comme ça parce que tout le monde fait comme ça") pour trouver la vraie question à laquelle répondre, et les vraies contraintes par opposition aux contraintes héritées.

**Quand l'utiliser :** Un problème semble insoluble, les réponses conventionnelles semblent insuffisantes, ou vous suspectez de résoudre le mauvais problème.

---

#### `outsider` — Lu à froid, sans contexte implicite

**Origine :** La technique du "regard de l'étranger" issue de la communication et du renseignement — vérifier si un document ou un plan est lisible par quelqu'un sans aucun background, exposant tout le savoir partagé implicite.

**Objectif :** Faire surface le contexte implicite que les experts oublient n'être pas évident pour quiconque est extérieur à la pièce.

**Fonctionnement :** Lit votre contenu comme quelqu'un qui vient d'entrer — aucun contexte, aucun historique partagé, aucun jargon. Signale tout ce qui nécessite un savoir implicite pour être compris, et identifie ce qu'un lecteur naïf mal interpréterait.

**Quand l'utiliser :** Avant de partager avec un nouveau stakeholder, une audience externe, ou quiconque hors de votre équipe immédiate.

---

#### `outside-in` — Forces externes avant les solutions internes

**Origine :** Les Cinq Forces de Porter et l'analyse de l'environnement stratégique. L'insight central : les forces externes à l'organisation (marché, concurrence, réglementation, technologie, comportement client) contraignent ce qui est possible *avant* que les choix internes deviennent pertinents.

**Objectif :** Éviter la pensée de l'intérieur vers l'extérieur — arrêter de partir de "qu'est-ce qu'on veut faire" pour partir de "qu'est-ce que l'environnement impose."

**Fonctionnement :** Cartographie les forces externes qui façonnent l'espace de décision avant de générer toute option interne. L'environnement est traité comme une contrainte, pas comme un décor.

**Quand l'utiliser :** Au début d'une analyse stratégique, à l'entrée sur un nouveau marché, ou quand les plans internes semblent déconnectés de la réalité externe.

---

#### `dixieme-homme` — Thèse adverse complète contre le consensus

**Origine :** La *doctrine du 10e homme*, institutionnalisée par l'AMAN — la Direction du renseignement militaire israélien — après l'échec catastrophique du renseignement lors de la guerre du Kippour (1973). L'échec fut attribué à la *conceptzia* : un modèle mental partagé si dominant que les signaux le contredisant étaient systématiquement ignorés. Le protocole : si 9 analystes sont d'accord, le 10e doit construire le cas le plus solide possible pour la conclusion opposée — pas trouver des failles, mais construire une contre-thèse complète. Popularisé internationalement par le film *World War Z* (2013), où Israël avait institutionnalisé la règle de "croire l'incroyable."

**Objectif :** Briser le groupthink à la racine en rendant la dissidence obligatoire, pas optionnelle.

**Fonctionnement :** Produit une thèse complète et rigoureuse argumentant le contraire du consensus actuel — avec ses propres preuves, sa logique et ses implications. Ce n'est pas l'avocat du diable (pointer les failles) ni le red-team (perspective adverse) : c'est une interprétation alternative complète des mêmes faits.

**Différences clés :**
- vs `contrarian` : contrarian trouve la faiblesse principale de votre plan. `dixieme-homme` argumente une conclusion totalement différente à partir des mêmes faits.
- vs `red-team` : red-team adopte la perspective d'un adversaire externe. `dixieme-homme` argumente contre le consensus de votre propre équipe depuis l'intérieur.
- vs `critique` : critique analyse un artifact pour ses failles. `dixieme-homme` construit un contre-récit face à une croyance partagée.

**Quand l'utiliser :** Fort alignement sur une conclusion avec suspicion de groupthink. Décisions à fort enjeu où un consensus erroné est catastrophique.

---

#### `chairman` — Arbitrer des perspectives contradictoires

**Origine :** Synthèse structurée — conçu comme le meta-skill qui intègre les outputs de plusieurs lentilles Advisory en un verdict unique.

**Objectif :** Passer de perspectives concurrentes à une décision actionnable unique avec des trade-offs explicites.

**Fonctionnement :** Prend les outputs d'autres analyses Advisory (contrarian, expansionist, red-team, etc.) et produit une synthèse : quels arguments tiennent, lesquels s'annulent, quelle est la voie recommandée, quels sont les risques résiduels.

**Quand l'utiliser :** Après avoir lancé deux skills Advisory ou plus sur le même problème et avoir besoin d'une décision unique. Utile aussi quand des stakeholders réels ont des positions genuinement contradictoires.

---

#### `red-team` — Raisonnement depuis la perspective adverse

**Origine :** Méthodologie Red Team CIA et NSA. Une équipe dédiée est chargée de raisonner et d'agir *en tant qu'adversaire* — non pas pour trouver des vulnérabilités, mais pour planifier l'attaque exactement comme l'adversaire la planifierait. Formalisée dans la communauté du renseignement américain dans les années 1970 après que les échecs de la Guerre Froide aient révélé des angles morts persistants causés par le mirror-imaging (supposer que l'adversaire pense comme vous).

**Objectif :** Exposer les angles morts que les défenseurs ne peuvent pas voir parce qu'ils raisonnent du mauvais côté du problème.

**Fonctionnement :** Habite pleinement la position de l'adversaire — ses objectifs, contraintes, ressources et raisonnement. Produit la stratégie que l'adversaire utiliserait réellement, pas celle qu'on craint qu'il utilise.

**Différences clés :**
- vs `contrarian` : contrarian trouve les failles dans votre plan depuis le point de vue d'un critique neutre. `red-team` les trouve depuis la perspective de quelqu'un qui cherche activement à vous battre.
- vs `dixieme-homme` : `dixieme-homme` argumente contre le consensus interne. `red-team` adopte les objectifs et le raisonnement d'un adversaire externe.

**Quand l'utiliser :** Stratégie concurrentielle, analyse de sécurité, préparation à une négociation, tout scénario avec un adversaire actif qui a ses propres objectifs.

---

#### `futurs-alternatifs` — Trois futurs plausibles avec signaux avancés

**Origine :** Planification par scénarios, développée par Herman Kahn à la RAND Corporation dans les années 1950 pour la stratégie nucléaire. Raffinée par la Group Planning de Shell sous Pierre Wack dans les années 1970 — Shell était la seule grande compagnie pétrolière à avoir anticipé le choc pétrolier de 1973 parce qu'elle avait construit des scénarios plutôt que des prévisions. Adoptée ensuite par la CIA pour le renseignement géopolitique et par les stratèges d'entreprise du monde entier.

**Objectif :** Se préparer à l'incertitude réelle plutôt qu'optimiser pour une seule prévision qui pourrait être fausse.

**Fonctionnement :** Produit trois futurs distincts et plausibles — pas meilleur/pire/base (c'est de l'analyse de sensibilité), mais des trajectoires genuinement différentes qui partent d'hypothèses différentes sur l'évolution du monde. Chaque futur est accompagné de signaux avancés : les indicateurs précoces qui diront *lequel* se matérialise, pour ajuster avant que ce soit évident.

**Quand l'utiliser :** Décisions à long horizon où la prédiction est impossible. Stratégie sous incertitude profonde. Planification devant rester robuste face à de multiples futurs possibles.

</details>

<details>
<summary><b>🗺️ Stratégie & Intelligence</b> — 4 skills</summary>


Outils de renseignement structuré — chacun audite une dimension différente d'un raisonnement ou d'un plan avant de s'engager.

---

#### `ach` — Matrice d'hypothèses concurrentes

**Ce qu'il fait :** Met 3–4 hypothèses concurrentes à l'épreuve des preuves disponibles. Pour chaque information, marque si elle soutient, contredit ou est neutre vis-à-vis de chaque hypothèse. Retient celle que les preuves éliminent le moins — pas celle avec laquelle on a commencé.

**Ce qu'il ne fait pas :** Ne valide pas une conclusion. Ne confirme pas ce qu'on croit déjà.

**Quand l'utiliser :** Vous avez une explication pour quelque chose et voulez vérifier que vous n'en êtes pas amoureux. Se combine naturellement avec `key-assumptions` (hypothèses cachées de chaque thèse) et `indicateurs` (signaux qui diront laquelle se réalise).

---

#### `key-assumptions` — Faire surface les hypothèses cachées

**Ce qu'il fait :** Extrait les prémisses implicites d'un raisonnement, d'une décision ou d'un plan — ce qui est tenu pour acquis sans être dit. Qualifie chaque hypothèse (solide / fragile / inconnue) et identifie les critiques dont l'effondrement ferait tout tomber.

**Ce qu'il ne fait pas :** Ne valide pas le raisonnement. Ne vérifie pas les faits. Il rend la fondation visible — c'est à vous d'en tirer les conséquences.

**Quand l'utiliser :** Avant de s'engager sur un plan, avant de présenter une analyse à un décideur, ou quand vous suspectez que ce que vous appelez "faits" sont en réalité des hypothèses non testées.

> Se combine avec `ach` (qui teste les hypothèses contre les preuves) et `quality-check` (qui audite les sources elles-mêmes).

---

#### `indicateurs` — Définir ce qu'on va surveiller

**Ce qu'il fait :** Définit à l'avance les signaux observables qui diront si un plan tient, si une hypothèse se réalise, ou si un pivot s'annonce. Produit des signaux de confirmation (le plan fonctionne) et des signaux d'alerte (quelque chose cloche), plus les signaux faibles à surveiller.

**Ce qu'il ne fait pas :** Ne suit pas les KPIs en temps réel (c'est le rôle d'un tableau de bord KPI, voir [ix-recipes](https://github.com/amiel-35/ix-recipes)). N'évalue pas la performance actuelle. Il définit le dispositif de surveillance avant le lancement.

**Quand l'utiliser :** Après qu'une décision ou un plan est formé, avant le début de l'exécution. Particulièrement puissant après `futurs-alternatifs` (indicateurs avancés par scénario) ou `ach` (signaux qui confirmeraient ou invalideraient l'hypothèse retenue).

---

#### `quality-check` — Auditer la solidité des preuves brutes

**Ce qu'il fait :** Évalue la solidité structurelle des informations sur lesquelles un raisonnement, une décision ou une analyse repose — avant qu'elles deviennent une fondation. Vérifie le type de source, la corroboration, la fraîcheur, les biais potentiels, et signale les lacunes informationnelles.

**Ce qu'il ne fait pas :** N'évalue pas les conclusions. N'évalue pas le raisonnement lui-même. Uniquement la qualité de la matière première. Ne vérifie pas un texte affirmation par affirmation contre une source donnée — c'est `fact-check`.

**Quand l'utiliser :** Avant de prendre une décision qui repose sur des données externes, des chiffres de marché ou des sources citées. Triage essentiel avant `decision` ou une note de recommandation quand on n'est pas sûr de la solidité des sources.

> `quality-check` audite les sources d'information. `key-assumptions` audite les prémisses cachées d'un raisonnement. Les deux sont de l'hygiène pré-décision, à deux niveaux différents.

</details>

<details>
<summary><b>🧩 Cadrage & production</b> — 5 skills</summary>


Du besoin flou au matériau prêt à produire : clarifier, structurer, découper, consigner. Les livrables métier qui suivent (PRD, specs, offres, fiches de poste…) sont dans [ix-recipes](https://github.com/amiel-35/ix-recipes).

---

#### `cadrage` — Clarifier avant de produire

**Ce qu'il fait :** Explore et clarifie un besoin vague ou incomplet — surface l'intention, les contraintes, les hypothèses et les points de décision avant tout lancement de production. Le besoin reformulé dit le but, jamais l'artefact que la demande nomme : cet artefact est une contrainte s'il est justifié, une hypothèse avec sa question ouverte sinon, et les attendus imposés par une consultation sont listés à part comme contraintes sur la réponse. Produit un rapport de clarification et des prochaines étapes recommandées.

**Ce qu'il ne fait pas :** Ne produit pas de brief ou de spec directement. C'est l'étape qui rend `brief` possible quand l'input est trop flou.

**Quand l'utiliser :** La demande est trop ambiguë pour être briefée directement. Quand il faut s'aligner sur ce qui est vraiment demandé avant de s'engager.

> `cadrage` pose les bonnes questions. `brief` écrit la réponse structurée. À enchaîner quand le besoin est flou.

---

#### `brief` — Besoin vague → brief structuré

**Ce qu'il fait :** Transforme un besoin, une demande ou une idée vague en brief structuré et actionnable — objectif, contraintes, critères de succès et exclusions. Sépare le besoin des solutions que la demande nomme : l'intention dit le but ; une solution nommée devient contrainte quand la demande dit pourquoi ce moyen plutôt qu'un autre, hypothèse « à valider » sinon ; ce qu'une consultation impose à la réponse (livrables, pièces) est listé à part. Le livrable est utilisable comme input pour tout skill de production en aval.

**Ce qu'il ne fait pas :** Ne clarifie pas un brief incomplet quand on ne sait pas encore ce qu'on veut (utilisez `cadrage` pour ça). Ne produit pas de spec.

**Quand l'utiliser :** Vous savez ce que vous voulez construire mais devez le structurer avant de le transmettre.

---

#### `analysis` — Décomposer avant de spécifier

**Ce qu'il fait :** Décompose un besoin complexe en lots indépendants et priorisés avant la spec ou la livraison. Produit une décomposition structurée qui alimente un PRD, un sprint ou un plan projet.

**Quand l'utiliser :** Le sujet est dense ou multi-dimensionnel et doit être découpé avant que quiconque puisse le spécifier ou l'estimer. En amont d'un PRD ou d'une spec fonctionnelle (voir [ix-recipes](https://github.com/amiel-35/ix-recipes)) pour les initiatives complexes.

---

#### `criteres-reussite` — Brief → critères de réussite vérifiables

**Ce qu'il fait :** Écrit les critères de réussite d'un livrable avant qu'il existe (son cahier de recette, sa définition de « fini ») — code, réponse ou cahier des charges de n'importe quel appel d'offres, campagne publicitaire, dissertation, travaux, grille de salaires, négociation, texte de loi, mariage — sous forme d'un tableau de tests : élément ou situation, vérification, résultat attendu, type de preuve (`mécanique` : un script ou une recherche suffit ; `relecture` : un juge autre que l'auteur ; `terrain` : seulement en vrai), qui vérifie (compétence et confidentialité). Il sépare le livrable, que l'auteur maîtrise, de l'issue, qui dépend d'autres acteurs et se vise par une zone entre un plancher et un objectif ; pose la question « qu'est-ce qui passerait tous ces tests en restant faux ? » et en fait des tests ; ajoute des tests de contenu (aucun « [à compléter] » dans le livrable rendu, une source pour chaque chiffre) ; garde une part cachée pour le juge, parade contre un auteur ou un agent qui optimise les tests visibles ; et dit quelle part du cahier une boucle automatique peut couvrir. La méthode tient seule pour n'importe quel sujet ; quatre annexes l'approfondissent selon le cas : logiciel, négociation, écrits (offre, dissertation, cahier des charges), travaux. Sans juge séparé (un couple, des associés), la part cachée devient des critères que chacun écrit seul, comparés plus tard.

**Ce qu'il ne fait pas :** Ne produit pas le livrable, et ne le juge pas — `controle-qualite` ou `quality-check` peuvent ensuite s'en servir comme grille.

**Quand l'utiliser :** Avant de commencer, pour s'accorder sur ce que « fini » veut dire ; comme critère d'arrêt d'un agent qui code en boucle jusqu'au vert ; avant une négociation, pour fixer à l'avance ce qu'est un bon accord pour chaque partie.

---

#### `compte-rendu` — Notes brutes → compte-rendu structuré

**Ce qu'il fait :** Transforme des notes brutes de réunion en compte-rendu structuré — décisions prises, actions assignées (owner + date), questions ouvertes et prochaines étapes. Distingue ce qui a été décidé de ce qui a été discuté.

**Quand l'utiliser :** Après toute réunion ayant produit des décisions ou des actions. Le livrable est directement partageable et maintient la responsabilisation claire.

</details>

---

## Pipelines typiques

```
critique → correction → deliver
explorer → decision   → deliver
cadrage  → questioning → explorer → decision
          (solutions nommées : hypothèses → questions → défaut écarté ;
           explorer breadth `standard` reste dans le véhicule nommé,
           `broad` en sort avec une contrainte positive par exécution)
critique → fact-check → correction → fact-check → deliver → controle-qualite
          (fact-check d'abord sur ce que la critique dit avoir observé, puis
           sur les faits que les corrections ajoutent ; controle-qualite sur le
           livrable contre le gabarit et les règles du client avant envoi)
controle-qualite sweep → controle-qualite verdict
          (détecteur, puis juge, sur le même référentiel)
          simplify  (standalone)
          rephrase  (standalone)
```

Les enchaînements qui passent par des skills métier (`research` → `analyse-concurrentielle` → `decision`, `brief` → `prd` → `feature-spec`, achats, recrutement) sont dans [ix-recipes](https://github.com/amiel-35/ix-recipes#workflows).

---

## Installation

### Claude Code (plugin — recommandé)

Le repo est une marketplace de plugins Claude Code (`.claude-plugin/marketplace.json` pointe sur la racine de plugin `dist/`). Installation en une fois, macOS comme Linux :

```bash
claude plugin marketplace add amiel-35/ix-skills
claude plugin install ix-skills@ix-skills
```

Les skills sont namespacés : `critique` devient `/ix-skills:critique`. Pour récupérer les mises à jour ensuite :

```bash
claude plugin marketplace update ix-skills
claude plugin update ix-skills
```

Puis redémarrer Claude Code. Les releases sont résolues par la version du manifeste (`dist/.claude-plugin/plugin.json`), voir `CHANGELOG.md`.

Dans l'app desktop Claude Code, les deux mêmes étapes passent par la commande `/plugin`.

Les skills métier (RH, juridique, finance, achats, produit, tech) forment un plugin à part, qui s'appuie sur celui-ci : `claude plugin marketplace add amiel-35/ix-recipes`, puis `claude plugin install ix-recipes@ix-recipes` (voir [ix-recipes](https://github.com/amiel-35/ix-recipes)).

**Fallback manuel** (pas de mécanisme plugin disponible) : symlinker ou copier `dist/skills` dans `~/.claude/skills/`, dossiers entiers, pour que les sous-dossiers `references/` suivent (voir [Références](#références-annexes-lues-à-la-demande)). Bien utiliser `dist/skills` — pas `skills/` : les fichiers source portent le frontmatter canonique (`id`, `label`, `description_fr`…), pas le frontmatter `name`/`description` attendu par le format Agent Skills, donc un `skills/<id>.md` brut n'est **pas** un `SKILL.md` valide.

### Un catalogue pour tous les plugins (`amiel-35`)

[amiel-35/plugins](https://github.com/amiel-35/plugins) est une marketplace (nommée `amiel-35`) qui liste ensemble ix-skills, ix-recipes et [ghost-council](https://github.com/amiel-35/ghost-council). Chaque entrée pointe sur le dossier `dist/` du repo du plugin : rien ne change ici quand un plugin est mis à jour. Dans Claude Code :

```bash
claude plugin marketplace add amiel-35/plugins
claude plugin install ix-skills@amiel-35
claude plugin install ix-recipes@amiel-35      # optionnel, s'appuie sur ix-skills
claude plugin marketplace update amiel-35      # plus tard : rafraîchir, puis claude plugin update ix-skills@amiel-35
```

Installer un plugin donné depuis **une seule** marketplace (ce catalogue *ou* celle du repo) : installé depuis les deux, il apparaît en double. Le catalogue fonctionne dans la CLI ; que le « Ajouter depuis un dépôt » de Cowork l'accepte n'est **pas encore testé**, donc pour Cowork le chemin par repo, décrit plus bas, reste celui qui fait foi.

### Claude Cowork / claude.ai

**Option A — installer comme plugin (par lot, recommandé)**

Ajouter le repo comme source de plugins : **« Ajouter depuis un dépôt »** avec `amiel-35/ix-skills`. Le manifeste marketplace fait le reste. L'installation en plugin emporte les sous-dossiers `references/`.

**Option B — uploader un seul skill**

Les dossiers `dist/skills/<id>/` sont des Agent Skills valides : en uploader un tel quel dans **Cowork → Customize** (ou l'éditeur ChatGPT Skills), ou zipper le dossier soi-même si une archive `.skill` est requise. Uploader ou zipper le dossier entier, sous-dossier `references/` compris, pour les skills qui en ont un (`prioritize`, `deliver`, `critique`) : sans lui ils se rabattent comme décrit dans [Références](#références-annexes-lues-à-la-demande). Pour régénérer les dossiers :

```bash
pip install -r requirements.txt
python3 build.py --target agentskills
```

### Codex CLI

Codex lit la même marketplace que Claude Code (testé avec codex-cli 0.155.1) :

```bash
codex plugin marketplace add amiel-35/ix-skills
codex plugin add ix-skills@ix-skills
```

Le plugin atterrit dans `~/.codex/plugins/cache/ix-skills/ix-skills/<version>/skills/<id>/`, avec les sous-dossiers `references/`. Pour mettre à jour, lancer `codex plugin marketplace upgrade` puis ré-ajouter le plugin au besoin (voir `codex plugin --help`). Pour retirer :

```bash
codex plugin remove ix-skills@ix-skills
codex plugin marketplace remove ix-skills
```

**Nommer le skill dans la demande** (« utilise le skill prioritize du plugin ix-skills pour… »). Codex lit alors `SKILL.md` puis seulement le fichier de référence utile. Sur une demande simple qui ne nomme pas le skill, Codex ne l'a pas utilisé lors de nos essais.

Le catalogue `amiel-35/plugins` utilise des sources `git-subdir` et n'est **pas testé avec Codex** : pour Codex, passer par la marketplace du repo ci-dessus.

**Installateur historique** (copie dans `~/.codex/skills/`, non retesté sur Codex 0.155) :

```bash
git clone https://github.com/amiel-35/ix-skills /tmp/ix-skills
cd /tmp/ix-skills
pip install -r requirements.txt
bash scripts/install-codex.sh          # tous les skills
bash scripts/install-codex.sh critique # un seul skill
bash scripts/install-codex.sh --dry-run
```

L'installateur construit `codex-dist/` avec `build.py` (donc `python3` doit disposer des paquets de `requirements.txt`), puis copie chaque skill dans `~/.codex/skills/<id>/SKILL.md`, avec son sous-dossier `references/` s'il en a un. `--dry-run` n'écrit rien dans `~/.codex` mais reconstruit quand même `codex-dist/` en local. Sans id, tout ce qui se trouve dans `codex-dist/` est installé. Redémarrer Codex pour activer.

### Antigravity CLI (agy, Gemini)

`agy` importe un dossier de plugin au format Claude (testé avec agy 1.3.3) :

```bash
git clone https://github.com/amiel-35/ix-skills
agy plugin import ix-skills/dist
```

Tous les skills sont importés avec leurs `references/` dans `~/.gemini/config/plugins/<plugin>/`. Utiliser `import` : `agy plugin validate` et `agy plugin install` attendent un `plugin.json` à la racine et n'acceptent pas ce format. Pour importer à la place les plugins déjà installés dans Claude Code (tous) : `agy plugin import claude`. Pour retirer : `agy plugin uninstall ix-skills`.

Comme pour Codex, **nommer le skill dans la demande** : agy lit alors `SKILL.md` puis seulement le fichier de référence utile.

### mystaffy

```bash
python3 build.py --target mystaffy
# ou pour re-générer le format ix-memory natif :
python3 build.py --target ix-memory
```

Les deux écrivent `mystaffy-dist/<id>/` (`manifest.json` + `skill.md`). Les annexes `references/` n'y sont pas copiées.

### GPT / Gemini / autre LLM (interfaces de chat)

Pour les interfaces de chat simples, sans CLI : copier-coller le contenu de `skills/<id>.md` comme system prompt. Le frontmatter YAML est ignoré sans effet de bord. Cette voie n'a pas de dossier `references/` : pour `prioritize`, `deliver` et `critique`, coller après le skill les annexes dont on a besoin (voir [Références](#références-annexes-lues-à-la-demande)).

### Références (annexes lues à la demande)

Quatre skills livrent des annexes dans un sous-dossier `references/` à côté de leur `SKILL.md`, et ne lisent que celle dont une demande a besoin : `prioritize` (un fichier par méthode : ICE, RICE, WSJF, MoSCoW, Kano, Eisenhower, valeur/effort, notation pondérée), `deliver` (gabarits HTML, profils de destinataires) `critique` (angles d'examen par type de contenu) et `criteres-reussite` (logiciel, négociation, écrits, travaux). Les sources sont dans `partials/` ; `build.py` les copie dans `dist/skills/<id>/references/` (et `codex-dist/<id>/references/`).

| Installation | Références |
|---|---|
| Plugin Claude Code / Cowork (l'une ou l'autre marketplace) | incluses |
| Copie manuelle de `dist/skills` dans `~/.claude/skills/` | incluses si les dossiers sont copiés entiers |
| Codex (`codex plugin add`, ou installateur historique `install-codex.sh`) | incluses / copiées |
| Antigravity (`agy plugin import ix-skills/dist`) | incluses |
| Upload d'un seul dossier `dist/skills/<id>/` (Cowork Customize, ChatGPT Skills) | incluses seulement si le sous-dossier `references/` est uploadé ou zippé avec |
| mystaffy / ix-memory | non emportées |
| GPT / Gemini (coller `skills/<id>.md`) | non emportées |

Sans le dossier : `prioritize` applique ses critères génériques et dit que la méthode détaillée n'était pas disponible, et `critique` choisit ses angles dans sa liste canonique. `deliver` perd les consignes HTML et les profils de destinataires : coller après lui `partials/deliver_html.md` (cible HTML) et `partials/deliver_recipient_profiles.md` (destinataire donné). Pour `prioritize`, coller le fichier de la méthode voulue, par exemple `partials/framework_rice.md` ; pour `critique`, `partials/critique_lenses.md`. `criteres-reussite` applique sa méthode de base et dit que l'annexe manquait ; coller après lui le `partials/criteres_*.md` qui correspond.

---

## Structure

```
ix-skills/
├── skills/                 ← source canonique (un .md + .mystaffy.json par skill)
├── partials/               ← annexes de référence, copiées dans references/ des skills qui les déclarent
├── docs/                   ← bannière et notes de conception
├── scripts/
│   ├── install-codex.sh    ← installateur Codex CLI
│   └── migrate_from_ix_memory.py
├── dist/                   ← racine du plugin, commité
│   ├── .claude-plugin/plugin.json   ← manifeste du plugin (à la main, bump à chaque release)
│   └── skills/<id>/SKILL.md         ← artefacts Agent Skills, générés par build.py
│       └── references/              ← annexes copiées depuis partials/ (3 skills)
├── .claude-plugin/
│   └── marketplace.json    ← manifeste marketplace, pointe sur ./dist
├── mystaffy-dist/          ← artefacts mystaffy (gitignore)
├── codex-dist/             ← artefacts Codex CLI (gitignore)
├── tests/                  ← tests du script de migration
├── build.py                ← packager multi-cibles
├── requirements.txt
├── CHANGELOG.md            ← releases, par date
├── THIRD_PARTY.md          ← sources et licences de ce que les skills reprennent de projets publics
├── TODO.md                 ← chantiers suivants (enchaînements design thinking)
└── CLAUDE.md               ← guide de contribution
```

---

## Packager

```bash
pip install -r requirements.txt         # jsonschema, pyyaml
python3 build.py --validate
python3 build.py
python3 build.py critique
python3 build.py --target agentskills   # dist/skills/<id>/SKILL.md + references/ — à commiter
python3 build.py --target cowork        # valide dist/.claude-plugin/plugin.json
python3 build.py --target mystaffy --domain cognitif
python3 build.py --target ix-memory
python3 build.py --target codex         # codex-dist/<id>/SKILL.md + references/
claude plugin validate dist             # valide le plugin (CLI Claude Code)
```

---

## Projets frères

[ix-recipes](https://github.com/amiel-35/ix-recipes) contient les recettes construites sur ces atomes : les skills métier (RH, juridique, finance, achats, produit, tech), déplacés d'ix-skills en version 4.0.0 avec leur historique, et des workflows qui enchaînent les atomes. ix-recipes dépend d'ix-skills, jamais l'inverse.

[ghost-council](https://github.com/amiel-35/ghost-council) est l'autre collection du même auteur : des méthodes de raisonnement de philosophes encodées comme skills (Popper, Kant, Pascal, Wittgenstein…), et `/council`, qui fait délibérer plusieurs angles indépendants sur une décision et rend la carte des désaccords. Les deux se complètent : ix-skills encode des gestes de travail, ghost-council des méthodes de pensée. Les postures de conseil d'ix-skills (`dixieme-homme`, `contrarian`, `red-team`, `key-assumptions`, `expansionist`…) peuvent siéger au conseil sous la forme `ix:<id>`, à côté de `ghost:popper`.

---

## Contribuer

Fork, modifie, PR. Lire `CLAUDE.md` pour les conventions.

Lire [`CLAUDE.md`](CLAUDE.md) pour le format canonique d'un skill, les règles de nommage et les checklists, et [`CHANGELOG.md`](CHANGELOG.md) pour les versions.

---

## Crédits

Plusieurs skills reprennent des rôles ou des idées de projets publics : le « LLM Council » d'Ole Lehmann et d'Andrej Karpathy pour les postures de conseil, obra/superpowers de Jesse Vincent pour `cadrage` et `revue-feedback`, Anthropic knowledge-work-plugins pour `prioritize`. Le détail, avec licences et ce qui est repris, est dans [`THIRD_PARTY.md`](THIRD_PARTY.md).

---

## Licence

MIT, voir [LICENSE](LICENSE).
