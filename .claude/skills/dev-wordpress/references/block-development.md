# Block Development — schoolsWP Dev Skills

Guide complet pour le développement de blocs WordPress (Gutenberg) selon les standards modernes.

## Prérequis

- Node.js 18+
- WordPress 6.9+
- `@wordpress/scripts` installé

## Création d'un nouveau bloc

### Option 1 : Scaffolding avec create-block

```bash
npx @wordpress/create-block my-block --namespace=schoolswp
```

Structure générée :
```
my-block/
├── block.json          # Métadonnées du bloc
├── edit.js             # Composant éditeur
├── save.js             # Composant sauvegarde (ou null)
├── render.php          # Rendu dynamique (optionnel)
├── index.js            # Point d'entrée
├── style.scss          # Styles frontend
└── editor.scss         # Styles éditeur uniquement
```

### Option 2 : Création manuelle

1. Créer `block.json` :

```json
{
  "$schema": "https://schemas.wp.org/trunk/block.json",
  "apiVersion": 3,
  "name": "schoolswp/my-block",
  "version": "1.0.0",
  "title": "Mon Bloc",
  "category": "widgets",
  "icon": "star-filled",
  "description": "Description du bloc",
  "supports": {
    "html": false,
    "color": {
      "background": true,
      "text": true
    },
    "spacing": {
      "margin": true,
      "padding": true
    },
    "typography": {
      "fontSize": true
    }
  },
  "attributes": {},
  "textdomain": "schoolswp",
  "editorScript": "file:./index.js",
  "editorStyle": "file:./editor.css",
  "style": "file:./style.css",
  "viewScript": "file:./view.js"
}
```

## Modèles de blocs

### Bloc statique (sauvegarde dans le contenu)

```jsx
// edit.js
import { useBlockProps } from '@wordpress/block-editor';

export default function Edit({ attributes, setAttributes }) {
  const blockProps = useBlockProps();
  return (
    <div {...blockProps}>
      <p>Contenu dans l'éditeur</p>
    </div>
  );
}

// save.js
import { useBlockProps } from '@wordpress/block-editor';

export default function Save({ attributes }) {
  const blockProps = useBlockProps.save();
  return (
    <div {...blockProps}>
      <p>Contenu sauvegardé</p>
    </div>
  );
}
```

### Bloc dynamique (rendu serveur)

```jsx
// edit.js
import { useBlockProps } from '@wordpress/block-editor';

export default function Edit({ attributes, setAttributes }) {
  const blockProps = useBlockProps();
  return (
    <div {...blockProps}>
      <p>Prévisualisation éditeur</p>
    </div>
  );
}

// save.js — retourne null
export default function Save() {
  return null;
}
```

```php
// render.php
<?php
/**
 * Rendu dynamique du bloc.
 *
 * @var array    $attributes Les attributs du bloc.
 * @var string   $content    Le contenu du bloc.
 * @var WP_Block $block      L'instance du bloc.
 */

$wrapper_attributes = get_block_wrapper_attributes();
?>

<div <?php echo $wrapper_attributes; ?>>
  <p><?php echo esc_html( $attributes['message'] ?? 'Default' ); ?></p>
</div>
```

### Bloc interactif (Interactivity API)

```json
// block.json (extrait)
{
  "supports": {
    "interactivity": true
  },
  "viewScriptModule": "file:./view.js"
}
```

```jsx
// view.js
import { store, getContext } from '@wordpress/interactivity';

store( 'schoolswp/my-block', {
  state: {
    get isOpen() {
      const context = getContext();
      return context.isOpen;
    }
  },
  actions: {
    toggle() {
      const context = getContext();
      context.isOpen = ! context.isOpen;
    }
  }
} );
```

## Attributs

### Définition dans block.json

```json
{
  "attributes": {
    "message": {
      "type": "string",
      "default": "Hello"
    },
    "count": {
      "type": "number",
      "default": 0
    },
    "isActive": {
      "type": "boolean",
      "default": false
    },
    "items": {
      "type": "array",
      "default": [],
      "items": {
        "type": "object"
      }
    },
    "mediaId": {
      "type": "number"
    },
    "mediaUrl": {
      "type": "string",
      "source": "attribute",
      "selector": "img",
      "attribute": "src"
    }
  }
}
```

### Sources d'attributs

| Source | Description | Exemple |
|--------|-------------|---------|
| (aucune) | Stocké dans le commentaire | `type: "string"` |
| `attribute` | Extrait d'un attribut HTML | `selector: "img", attribute: "src"` |
| `text` | Contenu texte d'un élément | `selector: "p"` |
| `html` | HTML interne | `selector: "div"` |
| `query` | Liste d'éléments | `selector: "li"` |

## InnerBlocks (composition)

```jsx
import { useBlockProps, InnerBlocks } from '@wordpress/block-editor';

const ALLOWED_BLOCKS = ['core/paragraph', 'core/heading', 'core/image'];
const TEMPLATE = [
  ['core/heading', { placeholder: 'Titre...' }],
  ['core/paragraph', { placeholder: 'Contenu...' }],
];

export default function Edit() {
  const blockProps = useBlockProps();
  return (
    <div {...blockProps}>
      <InnerBlocks
        allowedBlocks={ALLOWED_BLOCKS}
        template={TEMPLATE}
        templateLock="all" // ou "insert" ou false
      />
    </div>
  );
}

export function Save() {
  const blockProps = useBlockProps.save();
  return (
    <div {...blockProps}>
      <InnerBlocks.Content />
    </div>
  );
}
```

## Enregistrement côté serveur

```php
// Dans le fichier principal du plugin ou functions.php
add_action( 'init', 'schoolswp_register_blocks' );

function schoolswp_register_blocks() {
  register_block_type( __DIR__ . '/blocks/my-block' );
}
```

## Migrations et dépréciations

Quand la structure du bloc change :

```jsx
// deprecations.js
const v1 = {
  attributes: {
    // Anciens attributs
    text: { type: 'string' }
  },
  migrate( attributes ) {
    return {
      // Nouveaux attributs
      message: attributes.text
    };
  },
  save( { attributes } ) {
    // Ancien save
    return <p>{attributes.text}</p>;
  }
};

export default [v1];
```

```jsx
// index.js
import deprecated from './deprecations';

registerBlockType( 'schoolswp/my-block', {
  // ...
  deprecated
} );
```

## Checklist de vérification

- [ ] `apiVersion: 3` dans block.json
- [ ] Namespace cohérent (`schoolswp/block-name`)
- [ ] `useBlockProps()` utilisé dans edit et save
- [ ] Supports configurés (color, spacing, typography)
- [ ] Attributs typés correctement
- [ ] Textes internationalisés (`__()`, `_e()`)
- [ ] Styles scopés au bloc (`.wp-block-schoolswp-*`)
- [ ] Pas de jQuery, utiliser Interactivity API

## Ressources

- [Block Editor Handbook](https://developer.wordpress.org/block-editor/)
- [Interactivity API](https://developer.wordpress.org/block-editor/reference-guides/interactivity-api/)
- [Block API Reference](https://developer.wordpress.org/block-editor/reference-guides/block-api/)
