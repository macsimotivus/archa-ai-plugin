# Archa-ai

Pluginul Archa-ai îl învață pe Claude cum să lucreze cu legislația și normativele de construcții în vigoare
în România: Codul nr. 169/2026 (care a abrogat Legea 50/1991 și Legea 350/2001), normativele de securitate la
incendiu, seismic, termic, instalații, parcaje și celelalte acte din biblioteca Archa-ai.

## Ce face

- Claude caută în Archa-ai **înainte** să răspundă, la fiecare întrebare nouă, și nu dă cifre din memorie.
- Citează **verbatim**, cu actul și articolul sau punctul, și ține separat ce cere Codul de ce cere normativul.
- Își **verifică** concluziile juridice cu `archa_verifica_raspuns` înainte să ți le dea.
- Într-un memoriu sau într-un răspuns despre proiect, nu scrie ca fapt nimic despre **amplasament** (accese,
  arii protejate, rețele, vecinătăți) fără documentele proiectului: marchează „de confirmat”.

## Cum îl instalezi

- **claude.ai (Team / Enterprise):** Admin settings › Plugins & skills › Add › Add marketplace, cu
  `macsimotivus/archa-ai-plugin`; apoi pluginul „Archa-ai” din listă.
- **claude.ai (Pro / Max):** Customize › Plugins › Add › Add marketplace, cu `macsimotivus/archa-ai-plugin`.
- **Claude Code:**

```
/plugin install archa-ai --marketplace macsimotivus/archa-ai-plugin
```

## Cum îl folosești

Ai nevoie de un cont Archa-ai și de conectorul Archa-ai adăugat în Claude (vezi https://archa-ai.ro/integrare).
Apoi pui întrebarea obișnuit, de exemplu „Care e lățimea minimă a unei scări de evacuare într-o clădire de
birouri?”; pluginul se încarcă singur când întrebarea privește construcțiile din România.

## Date

Pluginul conține doar instrucțiuni. Nu trimite și nu păstrează nimic singur: întrebările ajung la Archa-ai
numai prin conectorul pe care îl adaugi și îl conectezi tu, cu contul tău.
