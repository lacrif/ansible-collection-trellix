# Collection Ansible lacrif.trellix

Cette collection fournit des rôles et du contenu Ansible pour déployer et gérer les composants Trellix Endpoint Security (anciennement McAfee) fournis par Lacrif. Elle facilite l'installation et la configuration automatisée des agents Trellix et des modules de sécurité sur les systèmes Linux.

## Contenu inclus

La collection comprend les rôles suivants :

### Rôles

- **`trellix_agent`** : Installation et gestion de l'agent Trellix (ePO Agent). Cet agent est nécessaire pour la communication avec le serveur ePolicy Orchestrator (ePO).

- **`trellix_ens_fw`** : Installation et configuration du module Firewall de Trellix Endpoint Security (ENS Firewall). Ce module fournit des fonctionnalités de pare-feu avancé.

- **`trellix_ens_tp`** : Installation et configuration du module Threat Prevention de Trellix Endpoint Security (ENS Threat Prevention). Ce module offre une protection contre les menaces incluant antivirus, anti-malware et prévention des intrusions.

- **`trellix_esp_kernelmodule`** : Installation du module noyau Trellix Endpoint Security Platform (ESP Kernel Module). Ce module est requis pour certains composants ENS et améliore les performances de sécurité au niveau du noyau.

## Installation

Créez un fichier `collections/requirements.yml` avec le contenu suivant :

```yaml
collections:
  - name: lacrif.trellix
```

Installez la collection via la ligne de commande :

```bash
ansible-galaxy collection install -r requirements.yml
```

## Utilisation

### Prérequis

- Ansible 2.7 ou supérieur
- Accès aux packages d'installation Trellix (généralement stockés sur un partage réseau monté)
- Droits d'administration (sudo/become) sur les cibles

### Variables communes

Chaque rôle utilise des variables pour configurer les versions et les chemins sources. Les chemins par défaut pointent vers `/mnt/sources_ansible/mcafee/`, mais peuvent être personnalisés.

### Exemples d'utilisation

#### Installation complète d'un agent avec ENS

```yaml
- hosts: endpoints
  become: true
  vars:
    trellix_agent_version: "5.8.5"
    trellix_ens_fw_version: "10.7.21"
    trellix_ens_tp_version: "10.7.21"
    trellix_esp_kernelmodule_version: "10.7.21"
  roles:
    - role: lacrif.trellix.trellix_agent
    - role: lacrif.trellix.trellix_esp_kernelmodule
    - role: lacrif.trellix.trellix_ens_fw
    - role: lacrif.trellix.trellix_ens_tp
```

#### Installation de l'agent uniquement

```yaml
- hosts: agents
  become: true
  roles:
    - role: lacrif.trellix.trellix_agent
      vars:
        trellix_agent_version: "5.8.5"
```

#### Installation d'ENS Threat Prevention avec options personnalisées

```yaml
- hosts: servers
  become: true
  roles:
    - role: lacrif.trellix.trellix_ens_tp
      vars:
        trellix_ens_tp_version: "10.7.21"
        trellix_ens_tp_install_options: "oasoff nocontentupdate"
```

### Variables par rôle

#### trellix_agent

- `trellix_agent_version` : Version de l'agent à installer (défaut : "5.8.5")
- `trellix_agent_src_path` : Chemin vers les packages d'installation (défaut : "/mnt/sources_ansible/mcafee/agent")

#### trellix_ens_fw

- `trellix_ens_fw_version` : Version du firewall ENS (défaut : "10.7.21")
- `trellix_ens_fw_src_path` : Chemin vers les packages (défaut : "/mnt/sources_ansible/mcafee/ens")

#### trellix_ens_tp

- `trellix_ens_tp_version` : Version de Threat Prevention (défaut : "10.7.21")
- `trellix_ens_tp_src_path` : Chemin vers les packages (défaut : "/mnt/sources_ansible/mcafee/ens")
- `trellix_ens_tp_install_options` : Options d'installation supplémentaires (défaut : "")

#### trellix_esp_kernelmodule

- `trellix_esp_kernelmodule_version` : Version du module noyau (défaut : "10.7.21")
- `trellix_esp_kernelmodule_src_path` : Chemin vers les packages (défaut : "/mnt/sources_ansible/mcafee/ens")

### Ordre d'exécution recommandé

Pour une installation complète, exécutez les rôles dans cet ordre :

1. `trellix_agent` (requis pour tous les autres)
2. `trellix_esp_kernelmodule` (si nécessaire pour ENS)
3. `trellix_ens_fw` et/ou `trellix_ens_tp`

### Systèmes d'exploitation supportés

- Debian/Ubuntu
- Red Hat Enterprise Linux/CentOS/Fedora

Les rôles détectent automatiquement la famille d'OS et appliquent les configurations appropriées.

## Tests

La collection inclut des tests Molecule pour valider le fonctionnement sur différents environnements :

```bash
# Depuis le répertoire de la collection
molecule test
```

Tests disponibles :
- `default` : Test de base
- `docker_debian` : Tests sur Debian
- `docker_rockylinux` : Tests sur Rocky Linux

## Dépannage

- Vérifiez que les packages d'installation sont accessibles via les chemins configurés
- Assurez-vous que les dépendances système sont installées
- Consultez les logs Ansible pour les erreurs d'installation
- Pour les mises à jour, les rôles vérifient automatiquement les versions actuelles

## License

GPL-2.0-or-later

## Informations sur l'auteur

Lacrif
