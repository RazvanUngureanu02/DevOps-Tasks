
# Linux Essentials – Task I

Acest folder conține un script complet care automatizează toți pașii ceruți în Task-ul I din proiectul DevOps Internship 2025.
## Conținut

- `linux_essentials.sh` – Scriptul Bash care rulează toate comenzile cerute
- `README.md` – Documentul de față, cu explicații
## Ce face scriptul

Scriptul acoperă toate cerințele din task, inclusiv cele bonus:

1. Actualizează sistemul și instalează pachetele necesare: `dnsutils`, `net-tools`, `nano`, `curl`, `netcat`, `nginx`
2. Face lookup la `cloudflare.com` folosind `dig`
3. Adaugă în `/etc/hosts` linia `8.8.8.8 google-dns`
4. Verifică dacă portul DNS 53 este deschis pentru `google-dns` cu `netcat`
5. Modifică nameserver-ul la `8.8.8.8` în `/etc/resolv.conf`
6. Face din nou lookup la `cloudflare.com` pentru a verifica dacă DNS-ul funcționează
7. Instalează și pornește serviciul `nginx`
8. Afișează porturile active pe care ascultă `nginx` (`ss -tuln | grep LISTEN`)

### Bonusuri implementate:

9. Schimbă portul Nginx din 80 în 8080 în fișierul de config
10. Repornește Nginx și verifică ascultarea pe portul 8080
11. Schimbă titlul HTML din pagina default nginx
12. Verifică modificarea folosind `curl` și caută tag-ul `<title>`

## Cum se folosește

1. Deschide un container Ubuntu folosind Docker:

```bash
docker run -it ubuntu

2. Creează fișierul în container:

nano linux_essentials.sh

3. Dupa ce se scrie codul se salvează cu CTRL+O, Enter, apoi CTRL+X

4. Rulează comanda:
chmod +x linux_essentials.sh
./linux_essentials.sh
