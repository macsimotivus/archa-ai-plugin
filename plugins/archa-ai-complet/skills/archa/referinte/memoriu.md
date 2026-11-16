# Memoriul: cum îl redactezi sau îl revizuiești

1. **Structura o iei din normă, nu din memorie.** Caută cu `archa_norma_cauta` / `archa_cauta` conținutul-cadru
   cerut pentru faza respectivă (DTAC, PT, documentația de urbanism, notificarea de mediu etc.) și urmează
   capitolele în ordinea cerută. La PAC din Archicad, `archa_dosar_pac` și piesa `memoriu` dau scheletul și
   cifrele din model.
2. **Datele proiectului vin din documentele lui.** Beneficiar, amplasament, suprafețe, indicatori (POT, CUT),
   regim de înălțime, accese, rețele: din CU, PUZ/PUD, planul de situație, avize, modelul din Archicad. Citește-le
   din dosar. Ce nu găsești, marchezi „de confirmat” și spui ce document îl lămurește.
3. **Fiecare trimitere legală se caută.** Pentru fiecare act citat în memoriu: e în vigoare? e ediția nouă?
   punctul există și spune ce afirmi? Folosește rezultatele Archa (`statut`, `inlocuit_de`, `citare`).
   Un memoriu copiat de anul trecut trimite des la Legea 50/1991 sau la P118-1999 — acum înlocuite.
4. **Marchează vizibil ce e nesigur.** La revizuire, separă: contradicții, date lipsă/de confirmat, note
   redacționale. Nu le amesteca în text ca fapte.
5. **Verifică înainte de a da fișierul.** `archa_verifica_raspuns` pe concluziile juridice; apoi
   `archa_genereaza_fisier`. Răspunsul uneltei îți întoarce în `amplasament` propozițiile de confirmat.
