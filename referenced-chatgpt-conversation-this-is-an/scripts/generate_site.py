from pathlib import Path
from html import escape

ROOT = Path(__file__).resolve().parents[1]

def shell(title, description, prefix, active, body):
    routes = [
        ("Home", f"{prefix}index.html", "home"),
        ("About", f"{prefix}about.html", "about"),
        ("AI & Automation", f"{prefix}work/ai-automation/index.html", "automation"),
        ("Product", f"{prefix}work/product-management/index.html", "product"),
        ("Projects", f"{prefix}work/project-management/index.html", "projects"),
        ("Insights", f"{prefix}insights.html", "insights"),
        ("Contact", f"{prefix}contact.html", "contact"),
    ]
    nav = "\n".join(f'<a href="{href}" data-nav="{key}"' + (' aria-current="page"' if key == active else '') + f'>{label}</a>' for label, href, key in routes)
    return f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="theme-color" content="#09090b">
  <meta name="description" content="{escape(description)}">
  <meta property="og:type" content="website">
  <meta property="og:title" content="{escape(title)}">
  <meta property="og:description" content="{escape(description)}">
  <meta property="og:image" content="{prefix}assets/images/social-preview.svg">
  <meta name="twitter:card" content="summary_large_image">
  <title>{escape(title)}</title>
  <link rel="icon" type="image/svg+xml" href="{prefix}assets/images/favicon.svg">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=DM+Mono:wght@400;500&family=Inter:wght@400;500;600;700&family=Space+Grotesk:wght@400;500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="{prefix}assets/css/style.css">
  <script src="{prefix}assets/js/main.js" defer></script>
</head>
<body>
  <a class="skip-link" href="#main">Skip to content</a>
  <header class="site-header"><div class="nav-shell">
    <a class="wordmark" href="{prefix}index.html" aria-label="Favour, home"><span class="wordmark-icon">F<span>.</span></span><span>FAVOUR<span class="wordmark-sub"> / AI &amp; TECHNOLOGY</span></span></a>
    <button class="menu-toggle" type="button" aria-expanded="false" aria-controls="primary-nav"><span class="menu-lines" aria-hidden="true"></span><span class="sr-only">Open navigation</span></button>
    <nav class="nav-links" id="primary-nav" aria-label="Main navigation">{nav}</nav>
  </div></header>
  <main id="main">{body}</main>
  <footer class="site-footer"><div class="footer-inner"><a class="wordmark footer-brand" href="{prefix}index.html"><span class="wordmark-icon">F<span>.</span></span><span>FAVOUR<span class="wordmark-sub"> / AI &amp; TECHNOLOGY</span></span></a><span class="footer-note">BUILT WITH CURIOSITY &amp; INTENTION</span><span class="copyright">© <span id="year">2026</span> FAVOUR ADEWUMI</span></div></footer>
</body></html>'''

def page(path, title, description, prefix, active, body):
    target = ROOT / path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(shell(title, description, prefix, active, body), encoding="utf-8")

def button(href, label, secondary=False):
    klass = "text-link" if secondary else "button button-primary"
    return f'<a class="{klass}" href="{href}">{label} <span aria-hidden="true">↗</span></a>'

def page_hero(kicker, title, copy, prefix, actions=""):
    return f'''<section class="page-hero section-wrap"><div class="hero-grid" aria-hidden="true"></div><div class="page-hero-copy reveal"><p class="eyebrow"><span class="status-dot"></span>{kicker}</p><h1>{title}</h1><p class="hero-copy">{copy}</p>{actions}</div><div class="page-hero-orbit" aria-hidden="true"><span class="orbit orbit-one"></span><span class="orbit orbit-two"></span><span class="orbit orbit-three"></span><span class="orbit-core">✳</span></div></section>'''

def section_head(number, label, title, aside=""):
    extra = f'<p class="section-aside">{aside}</p>' if aside else ""
    return f'<div class="section-heading section-heading-row reveal"><div><p class="eyebrow">{number} / {label}</p><h2>{title}</h2></div>{extra}</div>'

def category_card(prefix, category, title, copy, visual, route):
    return f'''<a class="category-card reveal" href="{prefix}work/{route}/"><div class="category-visual {visual}" aria-hidden="true"><span class="visual-stamp">{category}</span><span class="category-symbol">✳</span><span class="visual-foot">EXPLORE THE CATEGORY <span aria-hidden="true">↗</span></span></div><div class="category-info"><div><h3>{title}</h3><p>{copy}</p></div><span class="project-arrow" aria-hidden="true">↗</span></div></a>'''

def placeholder_card(prefix, slug, title, category, copy, visual="visual-automation"):
    href = f'{prefix}work/{category}/projects/{slug}/'
    return f'''<a class="project-card project-card-link reveal" href="{href}"><div class="project-visual {visual}"><span class="visual-stamp">DETAILS TO BE DOCUMENTED</span><div class="placeholder-graphic" aria-hidden="true"><span></span><span></span><span></span></div><span class="visual-foot">PERSONAL WORK / CASE STUDY IN PREPARATION</span></div><div class="project-info"><div><span class="project-type">{category.replace('-', ' ').upper()}</span><h3>{title}</h3><p>{copy}</p></div><span class="project-arrow" aria-hidden="true">↗</span></div></a>'''

# Home: retain the existing visual language and overview content, now linking into the site.
prefix = ""
home = page_hero("AI AUTOMATION / PRODUCT / PROJECT DELIVERY", "Building smarter<br>businesses with <span class=\"accent-text\">technology.</span>", "I explore how AI and thoughtful automation can make everyday work simpler — backed by experience coordinating products, projects and clinical research.", prefix, f'<div class="hero-actions">{button("work/ai-automation/", "Explore my work")} {button("about.html", "A little about me", True)}</div>')
home += '<div class="ticker" aria-label="Areas of focus"><div class="ticker-track" aria-hidden="true">' + ''.join(f'<span>{x} <i>✳</i></span>' for x in ['AI & AUTOMATION','PRODUCT THINKING','PROJECT DELIVERY','BETTER OPERATIONS']*2) + '</div></div>'
home += f'''<section class="section-wrap section-pad home-intro">{section_head('01','OVERVIEW','Curious about what<br><span class="muted-text">technology can make possible.</span>','A technology and delivery professional drawn to the space where people, processes and useful tools meet.')}
<div class="home-intro-bottom"><p>My experience spans product and project coordination and clinical research coordination. Alongside that work, I build and explore AI-enabled workflows that can reduce repetitive tasks and help teams work with more clarity.</p>{button('about.html','More about me',True)}</div></section>
<section class="services section-pad"><div class="section-wrap">{section_head('02','CAPABILITIES','Ideas, systems<br><span class="muted-text">and delivery.</span>','Primary focus: AI and workflow automation. Product and project management support a broader technology delivery practice.')}
<div class="category-grid">{category_card('', '01 / PRIMARY FOCUS','AI & Workflow Automation','Practical automations for everyday business processes.','visual-automation','ai-automation')}{category_card('', '02 / PRODUCT','Product Management','Connecting user needs, requirements and priorities.','visual-product','product-management')}{category_card('', '03 / DELIVERY','Project Management','Supporting coordinated delivery and clear follow-through.','visual-project','project-management')}</div></div></section>
<section class="section-wrap section-pad"><div class="section-heading section-heading-row reveal"><div><p class="eyebrow">03 / SELECTED WORK</p><h2>Work in progress.<br><span class="muted-text">Stories coming soon.</span></h2></div><a class="text-link" href="work/ai-automation/">Browse categories <span aria-hidden="true">↗</span></a></div><p class="work-intro reveal">Project details are being verified and documented. Browse a category to see what is being prepared.</p><div class="category-grid category-grid-compact">{category_card('', 'AUTOMATION BUILDS','Workflow builds & explorations','Personal workflow builds; detailed notes and demos are being prepared.','visual-automation','ai-automation')}{category_card('', 'PRODUCT MANAGEMENT','Product case studies','Verified examples will be added when ready to share.','visual-product','product-management')}{category_card('', 'PROJECT COORDINATION','Delivery & coordination','Selected experience will be presented with confirmed details.','visual-project','project-management')}</div></section>
<section class="contact section-pad"><div class="section-wrap contact-inner reveal"><p class="eyebrow">04 / CONTACT</p><h2>Have a thoughtful<br><span class="accent-text">problem to solve?</span></h2><p class="contact-copy">I’m open to conversations about AI automation, product work, project coordination and new opportunities.</p><a class="contact-email" href="mailto:favouradewumi0@gmail.com">favouradewumi0@gmail.com <span aria-hidden="true">↗</span></a><div class="contact-links"><a href="insights.html">INSIGHTS <span aria-hidden="true">↗</span></a><a href="https://www.linkedin.com/in/techsavvynurse" target="_blank" rel="noopener noreferrer">LINKEDIN <span aria-hidden="true">↗</span></a><span>LAGOS, NIGERIA</span></div></div></section>'''
page('index.html','Favour | AI & Technology','Favour Adewumi works across AI and workflow automation, product management, project coordination and clinical research coordination.','', 'home', home)

about = page_hero('ABOUT FAVOUR','People, processes<br>and <span class="accent-text">useful technology.</span>','I’m Favour — a technology and delivery professional interested in making complex work easier to understand, coordinate and improve.','')
about += '''<section class="section-wrap section-pad about-page"><div class="about-layout"><div class="about-intro reveal"><p class="large-copy">My work spans product and project coordination and clinical research coordination.</p><p>Alongside that experience, I build and explore AI-enabled workflows using tools including n8n, Make, Google Sheets, Telegram, ChatGPT and Claude.</p><p>I’m interested in practical technology: understanding the real need first, then making the path from idea to execution easier to navigate.</p><a class="text-link underlined" href="https://www.linkedin.com/in/techsavvynurse" target="_blank" rel="noopener noreferrer">Connect on LinkedIn <span aria-hidden="true">↗</span></a></div><div class="about-side reveal"><div class="principle-card"><span class="principle-index">01</span><div><h3>Start with the real problem.</h3><p>Listen, understand context and make the work visible.</p></div><span class="principle-mark">⌕</span></div><div class="principle-card"><span class="principle-index">02</span><div><h3>Make complexity manageable.</h3><p>Bring structure to moving parts and keep people aligned.</p></div><span class="principle-mark">↗</span></div><div class="principle-card"><span class="principle-index">03</span><div><h3>Use technology with intent.</h3><p>Choose tools that support people and useful operations.</p></div><span class="principle-mark">✳</span></div><div class="experience-note"><span class="note-mark">+</span><span>PRODUCT &amp; PROJECT COORDINATION</span><span class="note-divider">·</span><span>CLINICAL RESEARCH COORDINATION</span></div></div></div><div class="confirmation-note"><span class="note-mark">✳</span>Professional dates and titles will be added after the CV details are reconciled.</div></section>'''
page('about.html','About | Favour — AI & Technology','About Favour Adewumi and his work across AI automation, product and project coordination, and clinical research coordination.','', 'about', about)

# Capability category pages at the requested static directory routes.
categories = [
    ('work/ai-automation/index.html','AI & Workflow Automation | Favour','AI and workflow automation capability and personal workflow build placeholders.','../../','automation','AI & WORKFLOW AUTOMATION','Make routine work flow better.','I explore practical AI-enabled workflows that can make everyday business processes easier to manage. Current portfolio work includes personal builds across lead capture, tasks, content, reporting, email, appointments and customer support. Detailed notes and demos are being prepared.','01 / PRIMARY FOCUS','n8n · Make · Google Sheets · Telegram · ChatGPT · Claude','ai-automation',[
        ('lead-capture','Lead capture bot','Personal workflow build; implementation details and demo to be documented.','visual-automation'),('daily-task-assistant','Personal daily task bot','Personal workflow build; implementation details and demo to be documented.','visual-product'),('content-automation','Content automation','Personal workflow build; implementation details and demo to be documented.','visual-project'),('business-reporting','Business reporting automation','Personal workflow build; implementation details and demo to be documented.','visual-automation'),('email-automation','Email automation','Personal workflow build; implementation details and demo to be documented.','visual-product'),('appointment-booking','Appointment booking automation','Personal workflow build; implementation details and demo to be documented.','visual-project'),('ai-customer-support','AI customer support bot','Personal workflow build; implementation details and demo to be documented.','visual-automation')]),
    ('work/product-management/index.html','Product Management | Favour — AI & Technology','Product management capability and future case study placeholders.','../../','product','PRODUCT MANAGEMENT','From user needs<br>to <span class="accent-text">useful products.</span>','I’m interested in the work of clarifying problems, shaping requirements and helping teams prioritise and deliver digital products. Verified case studies are being prepared.','02 / SUPPORTING CAPABILITY','Discovery · Requirements · Prioritisation · Delivery','product-management',[
        ('case-study-placeholder','Product case studies','Verified product examples and your contribution will be added after review.','visual-product')]),
    ('work/project-management/index.html','Project Management | Favour — AI & Technology','Project management capability and future case study placeholders.','../../','projects','PROJECT & PROJECT COORDINATION','Clear plans.<br><span class="accent-text">Thoughtful delivery.</span>','I support coordinated delivery through stakeholder communication, documentation, timelines and follow-through, with experience spanning product/project coordination and clinical research coordination.','03 / SUPPORTING CAPABILITY','Coordination · Documentation · Stakeholders · Clinical research','project-management',[
        ('case-study-placeholder','Project delivery case studies','Selected NTI, Bomcel and clinical research experience will be presented with confirmed details.','visual-project')]),
]

def structure_block(items):
    return ''.join(f'<div class="case-field"><h3>{title}</h3><p>{copy}</p></div>' for title, copy in items)

case_fields = [
    ('Project overview','Project context and scope will be documented here.'),
    ('Problem or challenge','The problem and its context will be confirmed and described here.'),
    ('Objectives','Confirmed objectives will be added here.'),
    ('My role and responsibilities','Your role, responsibilities and contribution will be clearly distinguished here.'),
    ('Approach and execution','The verified approach, key decisions and execution steps will be documented here.'),
    ('Deliverables','Confirmed deliverables and supporting evidence will be listed here.'),
    ('Tools used','Tools used on this specific project will be confirmed here.'),
    ('Results or outcomes','Verified outcomes will be added when evidence is available. No metrics or client results are assumed.'),
    ('Lessons learned','Reflections and lessons learned will be added after the case study is reviewed.'),
]

for route, title, description, prefix, active, kicker, hero_title, copy, label, tools_text, category, projects in categories:
    body = page_hero(kicker, hero_title, copy, prefix, f'<div class="hero-actions"><a class="button button-primary" href="#projects">Explore projects <span aria-hidden="true">↓</span></a><a class="text-link" href="{prefix}contact.html">Discuss an opportunity <span aria-hidden="true">↗</span></a></div>')
    body += f'''<section class="section-wrap section-pad category-intro"><div class="category-summary reveal"><span class="project-type">{label}</span><p class="large-copy">This page is a starting point for documented, evidence-based case studies. It will expand as project details, outputs and learning notes are ready to share.</p><div class="tag-row">{''.join(f'<span>{escape(tool.strip())}</span>' for tool in tools_text.split('·'))}</div></div></section>
<section class="section-wrap section-pad category-projects" id="projects">{section_head('01','PROJECTS','Work to document.','Each project card opens a structured case study draft. Project specific details remain placeholders until confirmed.')}
<div class="project-grid">{''.join(placeholder_card(prefix,slug,ptitle,category,pcopy,pvisual) for slug,ptitle,pcopy,pvisual in projects)}</div><p class="disclosure-note"><span aria-hidden="true">✳</span> These are placeholders for portfolio documentation, not claims of client engagements or measured outcomes.</p></section>'''
    for slug, project_title, project_copy, project_visual in projects:
        detail_path = f'work/{category}/projects/{slug}/index.html'
        detail_prefix = '../../../../'
        detail_title = f'{project_title} — Case Study | Favour'
        detail = page_hero(f'{label} / CASE STUDY IN PREPARATION', escape(project_title), project_copy, detail_prefix)
        detail += f'''<section class="section-wrap section-pad case-study"><div class="case-status"><span class="status-dot"></span><span>PLACEHOLDER — REPLACE WITH VERIFIED CASE STUDY DETAILS BEFORE PUBLISHING</span></div><div class="case-grid">{structure_block(case_fields)}</div><p class="disclosure-note"><span aria-hidden="true">✳</span> This page is a reusable case study draft. No project specifics, client results or metrics have been added.</p><a class="text-link underlined" href="{detail_prefix}work/{category}/">← Back to {label.title()} projects</a></section>'''
        page(detail_path, detail_title, f'Case study placeholder for {project_title}. Verified details will be added later.', detail_prefix, active, detail)
    page(route,title,description,prefix,active,body)

insights = page_hero('INSIGHTS','Notes from<br><span class="accent-text">the learning curve.</span>','Short reflections on automation, product thinking and getting work done. Articles will appear here when published.','')
insights += '<section class="section-wrap section-pad"><div class="insight-placeholder reveal"><span class="insight-icon">✳</span><div><span class="project-type">THE NOTEBOOK IS OPEN</span><h2>First articles are in progress.</h2><p>Ideas are taking shape. Check back for practical notes and lessons learned.</p></div><span class="insight-index">COMING<br>SOON</span></div></section>'
page('insights.html','Insights | Favour — AI & Technology','Future writing on AI automation, product thinking and technology delivery.','', 'insights', insights)

contact = page_hero('CONTACT','Have a thoughtful<br><span class="accent-text">problem to solve?</span>','I’m open to conversations about AI automation, product work, project coordination and new opportunities.','')
contact += '<section class="section-wrap section-pad contact-page"><p class="eyebrow">LET’S CONNECT</p><a class="contact-email" href="mailto:favouradewumi0@gmail.com">favouradewumi0@gmail.com <span aria-hidden="true">↗</span></a><div class="contact-links"><a href="https://www.linkedin.com/in/techsavvynurse" target="_blank" rel="noopener noreferrer">LINKEDIN <span aria-hidden="true">↗</span></a><span>LAGOS, NIGERIA</span></div></section>'
page('contact.html','Contact | Favour — AI & Technology','Contact Favour Adewumi about AI automation, product work, project coordination and opportunities.','', 'contact', contact)

print('Generated portfolio pages and project case study drafts.')
