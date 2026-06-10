# DNS Baseline — michaelkihl.fr

**Date** : 10 avril 2026
**Registrar** : Netim (transfert finalisé)
**NS actuels** : ns1.o2switch.net / ns2.o2switch.net
**IP o2switch** : 109.234.164.43

---

## Enregistrements critiques (à migrer)

### A (Web)

| Nom | TTL | Valeur |
|-----|-----|--------|
| michaelkihl.fr | 1800 | 109.234.164.43 |
| ftp.michaelkihl.fr | 14400 | 109.234.164.43 |
| mail.michaelkihl.fr | 3600 | 109.234.164.43 |
| n8n.michaelkihl.fr | 14400 | 109.234.164.43 |

### CNAME (Web)

| Nom | TTL | Valeur |
|-----|-----|--------|
| www.michaelkihl.fr | 14400 | michaelkihl.fr |

### MX (Mail)

| Nom | TTL | Priorité | Valeur |
|-----|-----|----------|--------|
| michaelkihl.fr | 14400 | 0 | mail.michaelkihl.fr |

### TXT — SPF

| Nom | TTL | Valeur |
|-----|-----|--------|
| michaelkihl.fr | 14400 | v=spf1 include:mailgun.org include:spf.jabatus.fr include:spf.sendinblue.com ~all |
| michaelkihl.fr | 14400 | v=spf1 include:spf.sendinblue.com mx ~all |
| *.michaelkihl.fr | 14400 | v=spf1 include:mailgun.org ~all |
| n8n.michaelkihl.fr | 14400 | v=spf1 +a +mx +ip4:109.234.164.43 ~all |

> **ATTENTION** : il y a 2 enregistrements SPF sur la racine. C'est une anomalie (un seul SPF par domaine est valide selon la RFC).

### TXT — DKIM

| Nom | TTL | Valeur (résumée) |
|-----|-----|------------------|
| default._domainkey.michaelkihl.fr | 14400 | v=DKIM1; k=rsa; p=MIIBIjAN... (clé o2switch) |
| mail._domainkey.michaelkihl.fr | 14400 | k=rsa; p=MIGfMA0G... (clé mail) |
| email._domainkey.michaelkihl.fr | 14400 | k=rsa; p=MIGfMA0G... (clé Mailgun) |

### TXT — DMARC

| Nom | TTL | Valeur |
|-----|-----|--------|
| _dmarc.michaelkihl.fr | 14400 | v=DMARC1; p=none; rua=mailto:rua@dmarc.brevo.com |

### TXT — Vérifications

| Nom | TTL | Valeur |
|-----|-----|--------|
| michaelkihl.fr | 14400 | Sendinblue-code:d1865a0b4d5a498c059bba998ee0633e |
| michaelkihl.fr | 14400 | brevo-code:5075d95977fb4d3782e8ea1f852fe1c4 |
| _mailpoet.michaelkihl.fr | 14400 | 244420455748ae3c47e16abad3f3bc57 |

---

## Services tiers (CNAME à conserver)

| Nom | TTL | Valeur | Service |
|-----|-----|--------|---------|
| email.michaelkihl.fr | 14400 | eu.mailgun.org | Mailgun |
| lien.michaelkihl.fr | 14400 | links.switchy.io | Switchy |
| si33964.michaelkihl.fr | 14400 | inbound.systeme.io | Systeme.io |
| gcz2pirsvdnp.michaelkihl.fr | 14400 | gv-74iunozqpstnln.dv.googlehosted.com | Google (vérif) |
| mailpoet1._domainkey.michaelkihl.fr | 14400 | dkim1.sendingservice.net | MailPoet DKIM |
| mailpoet2._domainkey.michaelkihl.fr | 14400 | dkim2.sendingservice.net | MailPoet DKIM |
| systemeio1._domainkey.michaelkihl.fr | 14400 | key1.systeme.io | Systeme.io DKIM |
| systemeio2._domainkey.michaelkihl.fr | 14400 | key2.systeme.io | Systeme.io DKIM |
| brevo1._domainkey.michaelkihl.fr | 14400 | b1.michaelkihl-fr.dkim.brevo.com | Brevo DKIM |
| brevo2._domainkey.michaelkihl.fr | 14400 | b2.michaelkihl-fr.dkim.brevo.com | Brevo DKIM |

---

## Sous-domaines (enregistrements cPanel auto-générés)

Ces enregistrements sont créés automatiquement par cPanel et n'auront PAS besoin d'être recréés sur xCloud :

- cpanel.michaelkihl.fr → 109.234.164.43
- webdisk.michaelkihl.fr → 109.234.164.43
- webmail.michaelkihl.fr → 109.234.164.43
- whm.michaelkihl.fr → 109.234.164.43
- cpcalendars.michaelkihl.fr → 109.234.164.43
- cpcontacts.michaelkihl.fr → 109.234.164.43
- autodiscover.michaelkihl.fr → 109.234.164.43
- autoconfig.michaelkihl.fr → 109.234.164.43

Idem pour n8n.michaelkihl.fr et maekihlfr.michaelkihl.fr (sous-domaines avec leurs propres records cPanel).

---

## Rollback express

En cas de problème après migration :

1. **Rollback web** : remettre A `@` → 109.234.164.43
2. **Rollback mail** : remettre MX `@` → priorité 0, mail.michaelkihl.fr + A mail → 109.234.164.43
