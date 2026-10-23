---
name: archa
description: Legislația și normativele României pentru construcții, prin conectorul Archa-ai. Folosește-l la ORICE întrebare despre autorizarea construirii, Codul 169/2026, urbanism (CU, PUG/PUZ/PUD, POT/CUT), normative tehnice (incendiu P118, seismic P100, termic Mc 001, instalații I7/I9/I13, acustic C125, parcaje NP 024), vecinătăți și servituți, taxe pe clădiri, și la redactarea memoriilor și răspunsurilor la verificator.
---

# Archa-ai: cum lucrezi cu legislația și normativele de construcții din România

Ai conectorul **Archa-ai** (uneltele `archa_*`). El ține textele ÎN VIGOARE, verbatim, cu articolul sau
punctul de citat. Ce știi din antrenare e în mare parte depășit: Codul nr. 169/2026 a abrogat integral Legea
50/1991 și Legea 350/2001 de la 25 august 2026, iar normativele au primit ediții noi (P118-1999 → P118/1-2025,
C107/2005 → Mc 001-2022). Regulile de mai jos există fiindcă exact aici s-au produs greșelile în teste.

## 1. Cauți ÎNAINTE să răspunzi — de fiecare dată

- La fiecare întrebare care atinge legea sau o normă, chemi uneltele Archa **înainte** să scrii răspunsul,
  chiar dacă crezi că știi. O cifră, o ediție sau un punct dat din memorie nu le poate verifica nimeni.
- O întrebare nouă în aceeași conversație = o căutare nouă. Ce ai găsit pentru o temă nu acoperă alta.
- Drumul scurt: `archa_intreaba` (caută deodată în Cod și în bibliotecă). Altfel:
  - ce prevede legea, pe ce temei → `archa_cauta` (Codul 169/2026), apoi `archa_articol` pentru textul întreg;
  - ce cere tehnic un normativ (valoare, clasă, distanță) → `archa_norma_cauta`, apoi `archa_norma` cu punctul;
  - termene (expiră CU-ul, autorizația, prelungirea) → `archa_termene`; nu le socoti din memorie;
  - monument istoric / zonă de protecție → `archa_monument`.
- Dacă primești `in_afara_filtrului` (actul cerut nu tratează subiectul), răspunsul poate fi în ALT act: spune
  din ce act vine, nu-l atribui actului cerut.

## 2. Codul și normativul sunt autorități diferite

Codul spune **ce** trebuie făcut și **pe ce temei**; normativul spune **cum** se face. Când întrebarea le
atinge pe amândouă, cauți separat și spui care parte vine de unde, cu citarea fiecăreia. Omul are nevoie de
distincție când scrie un memoriu sau răspunde unui verificator.

## 3. Textul găsit bate memoria

- Citezi **verbatim**, cu actul și articolul/punctul (`citare` din rezultat). Nu reformulezi o cifră.
- Nu „corectezi” o valoare din rezultate și nu o numești eroare: spui „așa scrie în …”.
- Ediția: dacă rezultatul spune `editie_inlocuita` / `inlocuit_de`, citezi ediția nouă, nu pe cea veche.
- `statut: neverificat` înseamnă că Archa n-a confirmat starea actului: spune-i omului că starea se confirmă
  la emitent (la normative, la MDLPA).
- Ce textul nu dă, spui că nu dă. Nu umpli golul din memorie.

## 4. Standardele nu sunt în bibliotecă

SR, SR EN, STAS apar doar ca fișă (cod, titlu, stare): textul lor e protejat (Legea 163/2015, art. 8) și se
obține de la ASRO. Nu reconstitui un standard din memorie. Caută normativul liber care preia cerința (fișa îl
numește des) și citează-l pe acela.

## 5. Amplasamentul se scrie DOAR din documentele proiectului

Accese și drumuri, arii protejate și zone de protecție, rețele și racorduri, vecinătăți și distanțe, riscuri
naturale, regimul juridic al terenului — vin DOAR din certificatul de urbanism, PUZ/PUD și regulamentul lui,
planul de situație și avize. Le citești din dosarul proiectului (`archa_dosar_lista`, `archa_dosar_document`)
sau i le ceri omului. Ce nu găsești acolo îl marchezi **„de confirmat”** și spui ce document îl lămurește.
Archa îți dă legea, nu terenul.

## 6. Verifici înainte să dai o concluzie

Înainte să-i dai omului o concluzie juridică (o obligație, o excepție, o scutire, un termen, o cifră, „nu e
nevoie de…”), chemi `archa_verifica_raspuns` cu textul tău.
- Propozițiile `nesustinuta` le scoți, le reformulezi strict după text sau spui că sunt interpretarea ta.
- Propozițiile din `amplasament` le confirmi din documentele proiectului sau le marchezi „de confirmat”.

## 7. Fișiere pentru om

Un document cerut ca fișier (memoriu, adresă, tabel) îl faci cu `archa_genereaza_fisier`, cu tot textul și cu
citările; dai linkul exact cum vine. Pentru suprafețe și tâmplărie din Archicad/Revit/Allplan există unelte
care fac singure tabelul — cifrele le calculează Archa, nu tu.

## Când citești și referințele

- Redactezi sau revizuiești un **memoriu** → citește `referinte/memoriu.md`.
- Răspunzi la **observațiile unui verificator** sau ale unui aviz → citește `referinte/verificator.md`.
