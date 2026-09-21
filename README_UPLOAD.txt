# HELI FPL — BETA 0.14 PWA MOBILE
App sviluppata da Antonio Armentano

PACCHETTO PRONTO PER GITHUB PAGES / iPHONE
Caricare NELLA ROOT del repository Heli-fpl:
- index.html
- manifest.webmanifest
- sw.js
- .nojekyll
- cartella icons

Poi GitHub: Settings → Pages → Build and deployment → Deploy from a branch → main → /(root) → Save.

PWA
- percorsi relativi compatibili con un project site GitHub Pages;
- manifest installabile;
- service worker per cache dell'app shell;
- icone 180/192/512;
- meta tag Apple;
- layout mobile e safe-area iPhone;
- suggerimento per Aggiungi alla schermata Home.

NOTA CONNETTIVITÀ
L'interfaccia base può essere memorizzata dal service worker dopo il primo caricamento.
Mappe, meteo, DEM 3D, ricerca e ostacoli dipendono da servizi online e richiedono connettività; la PWA non trasforma queste sorgenti in dati aeronautici offline certificati.

SICUREZZA
HELI FPL è un supporto sperimentale alla pianificazione. Non sostituisce avionica certificata, AIP/NOTAM, METAR/TAF/SIGMET, briefing ufficiali, RFM/AFM, database ostacoli/terreno certificati o valutazione dell'equipaggio.
