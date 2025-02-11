# Auto-Add users to Telegram Channel

## Descriere
Acest script permite **adăugarea automată a utilizatorilor** într-un canal Telegram folosind biblioteca **Telethon**.

## Funcționalități
- **Autentificare prin API ID și API Hash**.
- **Citirea unei liste de utilizatori** dintr-un fișier (`users.txt`).
- **Adăugarea utilizatorilor într-un canal/grup** specificat.
- **Gestionarea erorilor și a limitărilor Telegram**.

## Cerințe
- **Python 3.x**
- **Biblioteca Telethon**, instalată cu:
  ```sh
  pip install telethon

## Configurare API Telegram
- Pentru date suplimentare despre cum găsești API Hash-ul și API ID-ul [Accesează acest link](https://github.com/dariusavram/telegram_phone_scraping?tab=readme-ov-file#configurare-api-telegram) 

## Rulare

```sh
python bot.py
```
- Introdu datele cerute la rulare.

## Observații
- Scriptul necesită ca utilizatorul să fie admin al canalului, sau cel puțin să aibă permisiunea de a adăuga persoane.
- Telegram poate impune limitări asupra acestui script (după o anumită perioadă de utilizare, apare un cooldown).
