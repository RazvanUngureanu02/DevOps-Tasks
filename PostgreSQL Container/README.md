# PostgreSQL Container – Task III

Acest folder conține toate fișierele necesare pentru rularea completă a Task-ului III din proiectul DevOps Internship 2025.

## Conținut

- `init_company.sql` – Script SQL pentru creare și populare baze de date
- `queries.sql` – Interogări SQL cerute în task
- `setup.sh` – Script Bash pentru automatizarea întregului proces
- `output.log` – Fișier de log cu rezultatele interogărilor SQL
- `dump_company.sql` – Exportul bazei de date PostgreSQL
- `README.md` – Acest fișier de documentație

## Ce face proiectul

Acest task configurează un container PostgreSQL, importă datele în baza de date și rulează interogări relevante.

## Pași principali

1. Creează un container Docker PostgreSQL:
   - Bază de date: `company_db`
   - Utilizator personalizat: `ituser`
   - Port expus: `5432`

2. Rulează scriptul SQL `init_company.sql`:
   - Creează tabelele: `departments`, `employees`, `salaries`
   - Inserează date în toate cele trei tabele
   - Se inserează 76 de angajați și salariile aferente

3. Rulează interogările din `queries.sql`:
   - Afișează numărul total de angajați
   - Selectează numele angajaților dintr-un anumit departament
   - Calculează salariul maxim și minim pe fiecare departament
   - Rezultatele se salvează în `output.log`

4. Exportă baza de date în `dump_company.sql` folosind `pg_dump`

5. Automatizează toți pașii de mai sus cu scriptul `setup.sh`:
   - Creează userul `admin_cee`
   - Rulează `init_company.sql`
   - Rulează `queries.sql` și salvează rezultatele

## Cum se folosește

> Toate comenzile se execută dintr-un container deja pornit și configurat (cu Docker și PostgreSQL instalat)

### 1. Deschide containerul:
```bash
docker exec -it pg-container bash
```

### 2. Rulează scriptul setup:
```bash
chmod +x setup.sh
./setup.sh
```

### 3. Verifică rezultatele:
```bash
cat output.log
```

## Output

Dacă totul este configurat corect, în fișierul `output.log` vei regăsi:
- Numărul total de angajați (76)
- Numele angajaților din departamentul selectat
- Cel mai mare și cel mai mic salariu pe fiecare departament




