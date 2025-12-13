<!-- README en français pour la collection lacrif.trellix -->

# Collection Ansible lacrif.trellix

Cette collection fournit des rôles et du contenu Ansible pour déployer et gérer l'agent Trellix fourni par Lacrif.

## Contenu inclus

Rôles :

- `trellix_agent` : installation et configuration de l'agent.
- `trellix_ens` : installation et configuration de Endpoint Security.

## Installation

Créer un fichier `collections/requirements.yml`

```yaml
collections:
  - name: lacrif.trellix
```

Puis l'installer la ligne de commande

```bash
ansible-galaxy collection install -r requirements.yml
```

## Utilisation rapide

Exemple de playbook minimal pour déployer l'agent :

```yaml
- hosts: agents
  become: true
  roles:
    - role: lacrif.trellix.trellix_agent
      vars:
        trellix_agent_version: 5.8.5
    - role: lacrif.trellix.trellix_ens
      vars:
        trellix_trellix_ens: 10.7.21
```

Variables importantes  :

- [roles/trellix_agent/defaults/main.yml](roles/trellix_agent/defaults/main.yml)
- [roles/trellix_ens/defaults/main.yml](roles/trellix_ens/defaults/main.yml)

## Tests

Exécutez :

```bash
molecule test
```

## License

MIT / BSD

## Author Information

Lacrif
