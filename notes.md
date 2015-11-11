# Detection of design pattern

---

# Recherche

## Requête Scopus

```
       ( ( TITLE-ABS-KEY ( "design pattern" )  OR  TITLE-ABS-KEY ( "design motif" ) )
  AND  ( TITLE-ABS-KEY ( detect* )  OR  TITLE-ABS-KEY ( identif* )  OR  TITLE-ABS-KEY ( recogni* ) ) )
  AND  PUBYEAR  >  1998  
  AND  ( LIMIT-TO ( SUBJAREA ,  "COMP" )  OR  LIMIT-TO ( SUBJAREA ,  "ENGI" ) )
  AND  ( LIMIT-TO ( DOCTYPE ,  "cp" )  OR  LIMIT-TO ( DOCTYPE ,  "ar" ) ) 
  AND  ( LIMIT-TO ( EXACTKEYWORD ,  "Design Patterns" )  OR  LIMIT-TO ( EXACTKEYWORD ,  "Design patterns" ) ) 
  AND  ( LIMIT-TO ( LANGUAGE ,  "English" ) ) 
  AND  ( EXCLUDE ( SUBJAREA ,  "SOCI" )  OR  EXCLUDE ( SUBJAREA ,  "BIOC" ) ) 
  AND  ( EXCLUDE ( SUBJAREA ,  "MATH" )  OR  EXCLUDE ( SUBJAREA ,  "DECI" ) 
     OR  EXCLUDE ( SUBJAREA ,  "MATE" )  OR  EXCLUDE ( SUBJAREA ,  "PHYS" ) 
     OR  EXCLUDE ( SUBJAREA ,  "BUSI" )  OR  EXCLUDE ( SUBJAREA ,  "EART" ) 
     OR  EXCLUDE ( SUBJAREA ,  "ENVI" )  OR  EXCLUDE ( SUBJAREA ,  "MEDI" ) ) 
  AND  ( EXCLUDE ( SUBJAREA ,  "AGRI" )  OR  EXCLUDE ( SUBJAREA ,  "NEUR" )  OR  EXCLUDE ( SUBJAREA ,  "PSYC" ) ) 
  AND  ( EXCLUDE ( SRCTYPE ,  "k" )  OR  EXCLUDE ( SRCTYPE ,  "d" ) ) 
```

## Résultats

403 Articles

---

# Répartition

* [2;135]   pierre, alex
    - 6 Désaccords
    - 2 3e avis
* [136;269] pierre, badr
    - 22 Désaccords
    - 5 3e avis
* [270;404] alex, badr
    - 4 désaccords
    - 1 3e avis

---

# Critère d'exclusion

1. not a contribution in software engineering (more than a use case of soft. eng.) 

2. not a full reference or research paper

3. not about software design pattern. (including architectural and interaction pattern)
  (https://en.wikipedia.org/wiki/Software_design_pattern)
  (https://en.wikipedia.org/wiki/Design_pattern)

4. the main contribution of the paper is not about detection of design pattern.

## Résultat du screening

1. 100 articles sur la détection de DP 
2. 91 article sur les méthodes de détection de DP

---

# Schéma de classification

##Detection strategy based on
 * AI based
 * Machine learning based
     - Supervised
     - Unsupervised
 * Graph based
 * Logic based (inference on rules)
 * Metric based
 * Automata based
 * Data mining based
 * Instrumentation based (trace included)
 * Pattern matching
 * Web semantic approach
 * Other

---

# Schéma de classification

##Language generality
 * Language dependant
 * Language independant

---

# Schéma de classification

##Analysis type
 * Static
 * Dynamic
 * Hybrid

---

# Schéma de classification

##Detection Approach
 * Semantic
 * Structural
 * Other

---

# Schéma de classification

##Detection Level
 * Source code
     - Token
     - AST
     - Other
 * Model
     - UML
     - Other
 * Multi-level (?)
 * Other

---

# Schéma de classification

##Pattern detection generality
 * Specific (method for a specific pattern)
 * Generic (general approach to pattern detection)
