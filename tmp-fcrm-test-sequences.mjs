import fs from 'node:fs';

const settings = JSON.parse(fs.readFileSync('.claude/settings.local.json', 'utf8')).env;
const base = 'https://schoolswp.com/wp-json/fluent-crm/v2';
const auth = 'Basic ' + Buffer.from(settings.FLUENTCRM_API_USERNAME + ':' + settings.FLUENTCRM_API_PASSWORD).toString('base64');
const headers = { 'Authorization': auth, 'Content-Type': 'application/json', 'User-Agent': 'Mozilla/5.0' };

// 1. Récupérer le contenu du template E1 (id 2866640)
const tplResp = await fetch(base + '/templates/2866640', { headers });
const tplData = await tplResp.json();
const tpl = tplData.template;
if (!tpl) {
  console.error('Template not found, response:', JSON.stringify(tplData).slice(0, 400));
  process.exit(1);
}
console.log('Template loaded:');
console.log('  title:', tpl.post_title);
console.log('  excerpt:', tpl.post_excerpt);
console.log('  design_template:', tpl.design_template);
console.log('  body length:', (tpl.post_content || '').length);

// 2. Construire un Send Email block avec ce contenu
const sendEmail = {
  action_name: 'send_custom_email',
  type: 'action',
  settings: {
    reference_campaign: '',
    send_email_to_type: 'contact',
    send_email_custom: '',
    campaign: {
      id: '',
      parent_id: '',
      title: 'Funnel Campaign Holder',
      status: 'published',
      template_id: tpl.ID,
      email_subject: tpl.post_excerpt || '',
      email_pre_header: '',
      email_body: tpl.post_content || '',
      utm_status: 0,
      utm_source: '',
      utm_medium: '',
      utm_campaign: '',
      utm_term: '',
      utm_content: '',
      design_template: tpl.design_template || 'raw_html',
      settings: { template_config: {} },
    },
    is_scheduled: 'no',
    scheduled_at: '',
    skip_if_overdue: 'no',
    mailer_settings: {
      from_name: '',
      from_email: '',
      reply_to_name: '',
      reply_to_email: '',
      is_custom: 'no',
    },
  },
};

const payload = {
  funnel_title: 'TEST API : SEQ LM Welcome',
  status: 'draft',
  funnel_settings: JSON.stringify({ tags: ['746'], select_type: 'any', subscription_status: 'subscribed' }),
  conditions: JSON.stringify({ run_multiple: 'no' }),
  sequences: JSON.stringify([sendEmail]),
};

const r = await fetch(base + '/funnels/31/sequences', {
  method: 'POST',
  headers,
  body: JSON.stringify(payload),
});
const t = await r.text();
console.log('\nstatus', r.status);
console.log(t.slice(0, 2000));
