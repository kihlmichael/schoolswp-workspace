# Mapper des données imbriquées vers Google Sheets dans n8n

## Le problème

Ton JSON est imbriqué sur deux niveaux (`data.contact` et `data.booking`). Le nœud Google Sheets ne peut pas accéder directement aux champs imbriqués en mode `autoMapInputData` — il faut aplatir les données d'abord.

## Solution : nœud Set avant Google Sheets

Insère un nœud **Edit Fields (Set)** entre ton HTTP Request et ton Google Sheets.

### Configuration du nœud Set

Mode : **Manual Mapping**

Crée 6 champs :

| Nom du champ       | Expression                               |
| ------------------ | ---------------------------------------- |
| `Nom complet`      | `{{ $json.data.contact.full_name }}`     |
| `Email`            | `{{ $json.data.contact.email_address }}` |
| `Téléphone`        | `{{ $json.data.contact.phone }}`         |
| `Activité`         | `{{ $json.data.booking.activity }}`      |
| `Date`             | `{{ $json.data.booking.date }}`          |
| `Nombre de places` | `{{ $json.data.booking.slots }}`         |

### Configuration du nœud Set

- **Operation** : `Append`
- **Mapping Mode** : `autoMapInputData` (les noms de champs correspondent aux colonnes)
- Sélectionne ton spreadsheet et ton onglet

Le nœud Set aplatit les données — Google Sheets reçoit un objet plat avec des clés qui correspondent exactement aux en-têtes de ta feuille.

## Résultat attendu

La nouvelle ligne contiendra :

| Nom complet  | Email           | Téléphone    | Activité       | Date       | Nombre de places |
| ------------ | --------------- | ------------ | -------------- | ---------- | ---------------- |
| Marie Dupont | marie@dupont.fr | +33612345678 | Pilates avancé | 2025-04-15 | 2                |
