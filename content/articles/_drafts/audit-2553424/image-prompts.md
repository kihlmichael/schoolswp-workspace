# Images - Post 2553424

3 images a generer + placer dans le corps. Pipeline recommande : tools/generate_telegram_avatars.py ou tools/wp-media-upload/cli.py apres generation nano-banana (API Gemini directe, voir reference_nano_banana_mcp_broken).

Charte schoolsWP : vert signature 00D400 en accents only, light F4F5F7 / dark 0F1419 (voir reference_brand_colors_schoolswp). PAS de codes hex dans le prompt visuel (voir feedback_gemini_hex_color_text_rendering).

## 1. Featured image (hero)

- Emplacement : champ Featured Image WP (media en vedette)
- Format : 1600x900, ratio 16:9
- Slug fichier : wordpress-7-phase-3-gutenberg-hero.png
- Alt text : WordPress 7.0 phase 3 Gutenberg interface collaborative

Prompt nano-banana :

Wide hero illustration, modern flat editorial style, soft gradient background in light off-white and deep midnight blue, foreground showing an abstract representation of a WordPress block editor with multiple colored cursor arrows hovering over content blocks (signaling real-time collaboration), 3 small avatar circles in the top-right of the editor, single signature electric green accent stroke running diagonally as a highlight line, no readable text inside the editor, clean vector look, sharp edges, high detail, 1600x900 aspect ratio, professional tech editorial illustration.

## 2. Inline DataViews

- Emplacement : juste apres H2 "L'interface DataViews : le futur de la gestion de contenu"
- Format : 1200x750
- Slug fichier : wordpress-7-dataviews-interface.png
- Alt text : Interface DataViews WordPress 7.0 vue liste et filtres modernes

Prompt nano-banana :

Modern WordPress admin dashboard mockup, isometric perspective, showing a redesigned content list interface with rounded card rows, filter chips at the top, a grid and list view toggle button, soft drop shadows, light beige background, dark navy accents, single electric green accent on the active filter chip, no readable text (use placeholder grey rectangles for labels), Apple-design-system inspiration, clean and aerated layout, 1200x750.

## 3. Inline collaboration temps reel

- Emplacement : juste apres H3 "Collaboration en temps reel et edition multi-utilisateurs"
- Format : 1200x750
- Slug fichier : wordpress-7-collaboration-temps-reel.png
- Alt text : Edition multi-utilisateurs temps reel dans WordPress 7.0

Prompt nano-banana :

Top-down flat illustration of a WordPress Gutenberg editor screen, showing 3 colored cursor pointers (orange, blue, purple) each labeled with a small avatar circle, hovering over different paragraph blocks of an article, soft connection lines linking the avatars, light cream background, deep navy text blocks as placeholders (no readable text), single electric green highlight on the active block being co-edited, clean editorial flat style, 1200x750.

## Workflow d'upload (rappel)

1. Generer les 3 images via nano-banana (API Gemini directe, espacement 15s mini si free tier, voir reference_gemini_image_rate_limit).
2. Exporter ExifTool au PATH avant upload (voir reference_exiftool_path).
3. Preparer le manifest YAML dans tools/wp-media-upload/articles/wordpress-7-nouveautes-guide-complet.yml.
4. Lancer cli.py upload --article wordpress-7-nouveautes-guide-complet depuis .venv/Scripts/python.
5. Inserer les blocs Gutenberg image dans le post (manuel via Gutenberg ou via Novamira execute-php apres upload).
