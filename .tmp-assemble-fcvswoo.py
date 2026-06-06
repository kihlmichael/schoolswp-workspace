import re

src = open("content/articles/fluentcart-vs-woocommerce/publish-ready.md", encoding="utf-8").read()
body = src.split("---", 2)[2].strip()
faq_block = open(".tmp-faq-kadence.html", encoding="utf-8").read()

NINJA_SETTINGS = '{"perPage":"20","show_all":"0","library":"footable","css_lib":"semantic_ui","enable_ajax":"0","css_classes":["striped","vertical_centered"],"enable_search":"0","column_sorting":"0","default_sorting":"old_first","sorting_type":"by_created_at","table_color":"ninja_no_color_table","render_type":"legacy_table","frontend_loader":"yes","table_color_type":"custom_color","expand_type":"default","stackable":"no","stacks_devices":[],"stacks_appearances":[],"table_font_family":"inherit","table_font_size":"14","pagination_position":"center","search_position":"right","formula_support":"no","show_title":"0","show_description":"0","hide_header_row":"0","show_row_data_modal":"no","hide_on_empty":"0","hide_responsive_labels":"0","alternate_color_status":"yes","table_header_color_primary":"#00d400ff","table_color_header_secondary":"#f6f5f4ff","table_color_header_border":"#f6f5f4ff","table_alt_2_color_primary":"#00d4000d","paginate_to_top":"","show_pager":"","paze_sizes":"10,20,50,100","nt_search_full_width":"","sorting_column":"","sorting_column_by":"ASC","togglePosition":"first","extra_css_class":"","sticky_first_column":"no","sticky_header":"no","sticky_header_offset":"0","disable_sticky_on_mobile":"no"}'

NINJA_IDS = ["2967688", "2967689"]

def ninja_embed(tid):
    return ('<!-- wp:ninja-tables/guten-block {"tableId":"%s","dataSource":"default","activeDesign":"other","tableSettings":%s} -->\n'
            '[ninja_tables id="%s"]\n'
            '<!-- /wp:ninja-tables/guten-block -->') % (tid, NINJA_SETTINGS, tid)

def inline(s):
    def link(m):
        t, u = m.group(1), m.group(2)
        if "fluentcart.com" in u:
            rel = "sponsored nofollow noopener"
        elif "schoolswp.com" in u:
            rel = "noopener"
        else:
            rel = "nofollow noopener"
        return '<a href="%s" target="_blank" rel="%s">%s</a>' % (u, rel, t)
    s = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", link, s)
    s = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<em>\1</em>", s)
    return s

lines = body.splitlines()
blocks = []
i, n = 0, len(lines)
table_idx = 0
while i < n:
    l = lines[i]
    if not l.strip():
        i += 1; continue
    if l.startswith("# "):
        i += 1; continue
    # stop at FAQ -> replace whole tail with Kadence FAQ
    if l.startswith("## ") and "Questions fréquentes" in l:
        break
    if l.startswith("### "):
        blocks.append('<!-- wp:heading {"level":3} -->\n<h3 class="wp-block-heading">%s</h3>\n<!-- /wp:heading -->' % inline(l[4:].strip()))
        i += 1; continue
    if l.startswith("## "):
        blocks.append('<!-- wp:heading -->\n<h2 class="wp-block-heading">%s</h2>\n<!-- /wp:heading -->' % inline(l[3:].strip()))
        i += 1; continue
    if l.lstrip().startswith("|"):
        # consume table, replace with ninja embed
        while i < n and lines[i].lstrip().startswith("|"):
            i += 1
        blocks.append(ninja_embed(NINJA_IDS[table_idx]))
        table_idx += 1
        continue
    if l.lstrip().startswith("- "):
        items = []
        while i < n and lines[i].lstrip().startswith("- "):
            items.append(inline(lines[i].lstrip()[2:].strip())); i += 1
        li = "".join('<!-- wp:list-item -->\n<li>%s</li>\n<!-- /wp:list-item -->\n' % x for x in items)
        blocks.append('<!-- wp:list -->\n<ul class="wp-block-list">\n%s</ul>\n<!-- /wp:list -->' % li)
        continue
    blocks.append('<!-- wp:paragraph -->\n<p>%s</p>\n<!-- /wp:paragraph -->' % inline(l.strip()))
    i += 1

blocks.append(faq_block)
html = "\n\n".join(blocks)
open(".tmp-fcvswoo-gutenberg-v2.html", "w", encoding="utf-8").write(html)
print("tables replaced:", table_idx, "| chars:", len(html))
print("ninja embeds:", html.count("ninja-tables/guten-block") // 2, "| core tables left:", html.count("wp:table"))
print("wp open/close:", html.count("<!-- wp:"), html.count("<!-- /wp:"))
print("emdash:", html.count("—"), "| FAQ panes:", html.count("wp:kadence/pane") // 2)
