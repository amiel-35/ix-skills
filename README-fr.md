# ix-skills

Skills de knowledge-work atomiques — portables sur Claude, GPT, Gemini, mystaffy.

78 skills en 10 catégories. Chaque skill encode un **processus cognitif**, pas une expertise métier.

[🇬🇧 English version](README.md)

---

## Skills disponibles

### 🧠 Cognitif — atomes de processus

Opérations primitives sur un contenu, un problème ou une décision. Chaque skill encode un seul geste cognitif — ils sont conçus pour se chaîner, pas se substituer.

| id | Rôle | Contrainte clé |
|---|---|---|
| `critique` | Identifier les failles d'un contenu sans proposer de solution | Analyse seulement — **ne corrige pas** |
| `correction` | Transformer une critique en directives actionnables | Transforme une critique — **ne ré-analyse pas** |
| `simplify` | Épurer un contenu sans changer le fond | Préserve toute l'information — supprime la friction |
| `rephrase` | Restituer le sens réel d'un contenu dense ou ambigu | Réinterprète — le sens peut évoluer, pas seulement la forme |
| `explorer` | Générer un espace d'options sans trancher | Largeur — **ne choisit pas** |
| `decision` | Arbitrer avec trade-offs visibles et recommandation nette | Choisit parmi des options existantes — **n'en génère pas** |
| `deliver` | Transformer un artifact en livrable partageable | Mise en forme et calibrage audience |
| `research` | Construire un socle factuel sourcé avant toute décision | Sources obligatoires — aucune affirmation non sourcée |
| `synthese` | Condenser un long contenu en synthèse actionnable | Compression avec perte — le détail est sacrifié intentionnellement |
| `decomposer` | Structurer un problème complexe en sous-problèmes indépendants | Les sous-problèmes doivent être indépendants — pas de dépendances croisées |
| `revue-feedback` | Évaluer un feedback avant de l'accepter ou le refuser | Évalue une critique reçue — pas votre propre artifact |

#### Distinctions clés

**`critique` vs `revue-feedback`**
`critique` analyse *votre propre artifact* (un document, un plan, une proposition) pour en trouver les failles. `revue-feedback` traite *un feedback que quelqu'un d'autre vous a donné* — il évalue si vous devez l'accepter, le nuancer ou le refuser avant de répondre. L'un est éditorial, l'autre est diplomatique.

**`simplify` vs `rephrase` vs `synthese`**
- `simplify` supprime le bruit en conservant toute l'information — le résultat est plus court mais complet.
- `rephrase` réécrit un contenu dense ou ambigu pour rendre le sens réel lisible — il réinterprète, ne coupe pas seulement.
- `synthese` sacrifie délibérément le détail pour extraire l'essentiel — compression avec perte qui produit une synthèse actionnable.

**`explorer` vs `decision`**
Conçus pour fonctionner en séquence. `explorer` cartographie l'espace des options sans s'engager (d'abord en largeur). `decision` arbitre parmi des options existantes avec des trade-offs explicites et une recommandation (en profondeur). Lancer `decision` sans `explorer` risque de figer le choix trop tôt sur un espace incomplet.

**`critique` vs archétypes Advisory (ex. `dixieme-homme`, `contrarian`)**
`critique` est un contrôle qualité sur *votre propre artifact* — éditorial, il trouve les failles dans ce que vous avez produit. Les archétypes Advisory challengent *une croyance, un plan ou une décision* depuis une perspective spécifique — ils opèrent au niveau du raisonnement et des convictions, pas de la qualité textuelle. Utilisez `critique` pour améliorer un document ; utilisez un archétype Advisory pour stress-tester une conclusion.

---

### ⚔️ Conseil — archétypes de perspective

Chaque skill impose une posture cognitive spécifique. Ils ne sont pas interchangeables — choisir en fonction de ce qu'on veut stress-tester. Lancer `chairman` après plusieurs pour synthétiser.

---

#### `contrarian` — Points de défaillance et hypothèses non vérifiées

**Origine :** L'*advocatus diaboli* (avocat du diable), formalisé dans le droit canon catholique. L'Église exigeait un critique désigné pour plaider contre toute canonisation proposée, pour garantir la rigueur. Adopté dans la gestion de la décision et l'analyse de renseignement pour institutionnaliser la dissidence.

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

---

### 🗺️ Stratégie & Intelligence

| id | Rôle |
|---|---|
| `ach` | Matrice d'hypothèses concurrentes — trouver celle que les preuves éliminent le moins |
| `key-assumptions` | Rendre visibles les hypothèses implicites d'un raisonnement |
| `indicateurs` | Signaux de confirmation et d'alerte pour un plan |
| `quality-check` | Évaluer la solidité structurelle d'une information |
| `note-strategique` | Produire une note stratégique structurée et argumentée |
| `strategie-prix` | Stratégie de prix avec valeur perçue, segmentation et scénarios |
| `business-case-draft` | Structurer une décision d'investissement avec coûts, bénéfices, risques |
| `tam-sam-som` | Estimer marché total, accessible et capturable |

---

### 🔍 Recherche & Analyse

| id | Rôle |
|---|---|
| `analyse-concurrentielle` | Socle factuel sur le paysage concurrentiel |
| `analyse-cdc` | Analyser un cahier des charges reçu |
| `budget-variance-analysis` | Analyser écarts budget/réel avec hypothèses correctives |
| `metriques-saas` | Diagnostic CAC, LTV, NRR, churn |
| `total-cost-analysis` | Structurer un coût total avec coûts cachés et risques |
| `financial-narrative` | Chiffres financiers bruts → narrative exécutive |
| `data-storytelling` | Transformer des données en narrative avec insight et recommandation |

---

### 📊 Métriques & Pilotage

| id | Rôle |
|---|---|
| `okr` | Transformer un objectif vague en OKR structuré |
| `tableau-de-bord-kpi` | Définir et structurer un dashboard KPI |
| `offer-comparison` | Comparer des offres fournisseurs sur grille pondérée |
| `vendor-scorecard` | Grille d'évaluation fournisseur réutilisable |
| `compliance-checklist` | Générer une checklist conformité RGPD, droit du travail, sectorielle |

---

### ⚖️ Juridique & Contrats

| id | Rôle |
|---|---|
| `contract-review` | Analyser un contrat clause par clause |
| `cgv-checker` | Identifier les clauses déséquilibrées dans des CGV/CGU |
| `conformite-rgpd` | Checklist conformité RGPD depuis un document technique |
| `legal-risk-flag` | Identifier rapidement les signaux juridiques d'alerte |
| `nda-draft` | Générer un NDA adapté au contexte |
| `contrat-fournisseur` | Analyser ou rédiger un contrat fournisseur côté acheteur |

---

### 👥 RH & People

| id | Rôle |
|---|---|
| `fiche-poste` | Produire une fiche de poste structurée et publiable |
| `entretien-professionnel` | Préparer un entretien professionnel (art. L6315-1) |
| `interview-guide-recruteur` | Guide entretien recruteur avec questions STAR |
| `interview-loop-planner` | Concevoir le processus de recrutement complet |
| `onboarding-plan` | Plan d'intégration 30-60-90 jours |
| `offboarding-structure` | Plan de départ avec passation de connaissance |
| `people-review` | Structurer une revue talent collective |
| `performance-review-helper` | Préparer l'entretien annuel avec objectifs SMART |
| `plan-developpement-competences` | Plan de développement individuel ou collectif |
| `grille-remuneration` | Structurer une grille salariale par famille et niveau |
| `contrat-emploi` | Analyser ou rédiger un contrat de travail |
| `lettre-cadrage-disciplinaire` | Rédiger une lettre de cadrage disciplinaire |
| `org-design-brief` | Formaliser une cible organisationnelle avec diagnostic |

---

### 💻 Produit & Tech

| id | Rôle |
|---|---|
| `prd` | Produire un Product Requirements Document complet |
| `feature-spec` | Spec fonctionnelle : user stories, MoSCoW, critères d'acceptance |
| `product-spec` | Spec actionnable depuis un brief ou besoin cadré |
| `brief` | Transformer un besoin flou en brief exploitable |
| `cadrage` | Clarifier un besoin avant toute production |
| `analysis` | Décomposer un besoin complexe en lots actionnables |
| `persona` | Produire des personas utilisateur structurés |
| `journey-map` | Carte du parcours utilisateur avec frictions et opportunités |
| `mockup` | Produire un mockup HTML autonome depuis un brief ou spec |
| `reformulation-us` | Réécrire des user stories mal rédigées en US testables |
| `ticket-triage` | Catégoriser, prioriser P1–P4 et router un ticket support |
| `code-review` | Revue de code : sécurité, performance, correction, maintenabilité |
| `system-design` | Concevoir une architecture système ou technique |
| `tech-debt` | Identifier, catégoriser et prioriser la dette technique |

---

### 🚀 Business & Sales

| id | Rôle |
|---|---|
| `offre-commerciale` | Produire le contenu d'une offre client structurée |
| `negotiation-brief` | Position structurée avant une négociation |
| `rfp-draft` | Générer un appel d'offres structuré |
| `stakeholder-comms` | Rédiger des communications adaptées à l'audience |
| `compte-rendu` | Notes brutes → compte-rendu structuré avec décisions et actions |
| `retrospective` | Rétrospective blameless avec faits, causes et actions |

---

## Pipelines typiques

```
critique → correction → deliver
explorer → decision   → deliver
research → analyse-concurrentielle → decision
brief    → prd → feature-spec
          simplify  (standalone)
          rephrase  (standalone)
```

---

## Installation

### Claude Code

Claude Code scanne `~/.claude/skills/` au démarrage — un sous-répertoire par skill, contenant chacun un `SKILL.md`.

```bash
git clone https://github.com/amiel-35/ix-skills /tmp/ix-skills
for f in /tmp/ix-skills/skills/*.md; do
  id=$(basename "$f" .md)
  mkdir -p ~/.claude/skills/$id
  cp "$f" ~/.claude/skills/$id/SKILL.md
done
```

Ou pour installer un seul skill :

```bash
mkdir -p ~/.claude/skills/critique
cp skills/critique.md ~/.claude/skills/critique/SKILL.md
```

### Claude.ai

**Option A — upload direct (un skill à la fois)**

Dans **Settings → Skills**, glisser-déposer `skills/<id>.md` directement.

**Option B — bundle `.skill` (par lot)**

```bash
git clone https://github.com/amiel-35/ix-skills
cd ix-skills
pip install -r requirements.txt
python3 build.py --target claude-ai
```

Glisser les fichiers `dist/*.skill` dans **Settings → Skills**.

### mystaffy

```bash
python3 build.py --target mystaffy
# ou pour re-générer le format ix-memory natif :
python3 build.py --target ix-memory
```

### GPT / Gemini / autre LLM

Copier-coller le contenu de `skills/<id>.md` comme system prompt. Le frontmatter YAML est ignoré sans effet de bord.

---

## Structure

```
ix-skills/
├── skills/                 ← source canonique (un .md + .mystaffy.json par skill)
├── scripts/
│   └── migrate_from_ix_memory.py
├── dist/                   ← .skill pour claude.ai (gitignore)
├── mystaffy-dist/          ← artefacts mystaffy (gitignore)
├── .claude-plugin/
│   └── plugin.json
├── build.py                ← packager multi-cibles
├── requirements.txt
└── CLAUDE.md               ← guide de contribution
```

---

## Packager

```bash
python3 build.py --validate
python3 build.py
python3 build.py critique
python3 build.py --target claude-ai
python3 build.py --target mystaffy --domain cognitif
python3 build.py --target ix-memory
```

---

## Contribuer

Fork, modifie, PR. Lire `CLAUDE.md` pour les conventions.

---

## Licence

MIT
