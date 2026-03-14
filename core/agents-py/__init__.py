# agents/ — Agents de génération de contenu schoolsWP
#
# Distinct du multi-agent-system/ (analyse technique, output JSON).
# Ces agents produisent du contenu éditorial (articles, newsletters, etc.)
#
# Agent stratégique central :
#   schoolswp_brain        → SchoolswpBrainAgent        : agent stratégique central — analyse business + 4 modes (SEO, comparatif, architecture, automation)
#
# Agents de contenu :
#   seo_writer        → SeoWriterAgent       : articles SEO WordPress long terme
#   plugin_comparator → PluginComparatorAgent : comparatifs objectifs 2-4 plugins
#   lms_trainer            → LmsTrainerAgent            : tutoriels LMS pas à pas (Tutor LMS, FluentCRM…)
#   automation_consultant  → AutomationConsultantAgent  : architecture systèmes automatisés WordPress
#   wp_teacher             → WpTeacherAgent             : leçons pédagogiques WordPress pour débutants
#   wp_business_teacher    → WpBusinessTeacherAgent     : leçons WordPress orientées business (crédibilité, conversion, SEO)
#   wp_freelance_teacher   → WpFreelanceTeacherAgent    : leçons WordPress pour freelances (brief, livraison, client, maintenance)
#   wp_profit_architect    → WpProfitArchitectAgent     : leçons site WordPress rentable (leads, ventes, conversion, ROI)
#   wp_premium_freelance   → WpPremiumFreelanceAgent    : leçons WordPress haut de gamme (positionnement, qualité, valeur perçue)
#   wp_digital_sales       → WpDigitalSalesAgent        : leçons vente digitale (page de vente, tunnel, WooCommerce, LMS, conversion)
#
# Agents d'analyse :
#   seo_competitor_analyst → SeoCompetitorAnalystAgent  : gap analysis SEO vs concurrent (tableau gaps, top 10, clusters, plan)
#
# Pipeline multi-agents :
#   article_pipeline/      → ArticlePipeline            : Writer→Auditor→Editor→Meta (4 agents séquentiels)
