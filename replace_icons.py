import re

with open('Untitled-1.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Facebook SVG
facebook_svg = '<svg viewBox="0 0 24 24" width="24" height="24" fill="#1877F2"><path d="M24 12.073c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.99 4.388 10.954 10.125 11.854v-8.385H7.078v-3.47h3.047V9.43c0-3.007 1.792-4.669 4.533-4.669 1.312 0 2.686.235 2.686.235v2.953H15.83c-1.491 0-1.956.925-1.956 1.874v2.25h3.328l-.532 3.47h-2.796v8.385C19.612 23.027 24 18.062 24 12.073z"/></svg>'

# WhatsApp SVG
whatsapp_svg = '<svg viewBox="0 0 24 24" width="24" height="24" fill="#25D366"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.67-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.076 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421-7.403h-.004a9.87 9.87 0 00-4.869 1.171L.039 2.487l1.39 4.953a9.9 9.9 0 00-1.512 5.684c0 5.476 4.441 9.926 9.896 9.926 2.662 0 5.164-.994 7.202-2.812l4.718 1.24-1.53-4.888a9.88 9.88 0 001.414-5.466c0-5.475-4.441-9.926-9.896-9.926"/></svg>'

# Email SVG
email_svg = '<svg viewBox="0 0 24 24" width="24" height="24" fill="#FF5733"><path d="M20 4H4c-1.1 0-1.99.9-1.99 2L2 18c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z"/></svg>'

# Telegram SVG
telegram_svg = '<svg viewBox="0 0 24 24" width="24" height="24" fill="#0088cc"><path d="M12 0C5.373 0 0 5.373 0 12s5.373 12 12 12 12-5.373 12-12S18.627 0 12 0zm5.562 8.161c-.176 1.841-1.028 6.311-1.452 8.371-.188.998-.556 1.332-.912 1.365-.777.072-1.368-.509-2.119-.997-.738-.461-1.156-.748-1.873-1.197-1.049-.656-.369-1.015.229-1.603.16-.16 2.929-2.688 2.98-2.914.007-.03.013-.141-.052-.212-.064-.07-.161-.046-.23-.027-.098.02-1.65 1.048-4.66 3.143-.44.312-.839.464-1.201.456-.395-.01-1.154-.224-1.72-.409-.692-.223-1.236-.342-1.188-.722.024-.181.271-.359.747-.547 2.926-1.273 4.888-2.108 5.864-2.414 2.791-1.191 3.375-1.396 3.759-1.404.083-.001.271.019.394.119.1.083.127.194.139.271.011.068.024.15.024.23z"/></svg>'

# Replace hero section Facebook icon
content = re.sub(
    r'<a class="icon-btn" href="https://www\.facebook\.com/profile\.php\?id=61552305287329" target="_blank" rel="noopener" title="Facebook"><span>[^<]*</span></a>',
    f'<a class="icon-btn" href="https://www.facebook.com/profile.php?id=61552305287329" target="_blank" rel="noopener" title="Facebook">{facebook_svg}</a>',
    content
)

# Replace hero section WhatsApp icon
content = re.sub(
    r'<a class="icon-btn" href="https://wa\.me/8801609166109" target="_blank" rel="noopener" title="WhatsApp Message"><span>[^<]*</span></a>',
    f'<a class="icon-btn" href="https://wa.me/8801609166109" target="_blank" rel="noopener" title="WhatsApp Message">{whatsapp_svg}</a>',
    content
)

# Replace hero section Email icon
content = re.sub(
    r'<a class="icon-btn" href="mailto:redpen361@gmail\.com" title="Send Email"><span>[^<]*</span></a>',
    f'<a class="icon-btn" href="mailto:redpen361@gmail.com" title="Send Email">{email_svg}</a>',
    content
)

# Replace hero section Telegram icon
content = re.sub(
    r'<a class="icon-btn" href="https://t\.me/phycokiller420" target="_blank" rel="noopener" title="Telegram"><span>[^<]*</span></a>',
    f'<a class="icon-btn" href="https://t.me/phycokiller420" target="_blank" rel="noopener" title="Telegram">{telegram_svg}</a>',
    content
)

# Now replace contact section icons (q-items)
# Replace WhatsApp q-item icon
content = re.sub(
    r'<a class="q-item wh" href="https://wa\.me/8801609166109"[^>]*>\s*<div class="q-left"><div class="q-icon">[^<]*</div><span>WhatsApp</span></div>',
    f'<a class="q-item wh" href="https://wa.me/8801609166109" target="_blank" rel="noopener">\n          <div class="q-left"><div class="q-icon">{whatsapp_svg}</div><span>WhatsApp</span></div>',
    content
)

# Replace Email q-item icon
content = re.sub(
    r'<a class="q-item em" href="mailto:redpen361@gmail\.com">\s*<div class="q-left"><div class="q-icon">[^<]*</div><span>Email</span></div>',
    f'<a class="q-item em" href="mailto:redpen361@gmail.com">\n          <div class="q-left"><div class="q-icon">{email_svg}</div><span>Email</span></div>',
    content
)

# Replace Facebook q-item icon
content = re.sub(
    r'<a class="q-item fb" href="https://www\.facebook\.com/profile\.php\?id=61552305287329"[^>]*>\s*<div class="q-left"><div class="q-icon">[^<]*</div><span>Facebook</span></div>',
    f'<a class="q-item fb" href="https://www.facebook.com/profile.php?id=61552305287329" target="_blank" rel="noopener">\n          <div class="q-left"><div class="q-icon">{facebook_svg}</div><span>Facebook</span></div>',
    content
)

# Replace Telegram q-item icon
content = re.sub(
    r'<a class="q-item tg" href="https://t\.me/phycokiller420"[^>]*>\s*<div class="q-left"><div class="q-icon">[^<]*</div><span>Telegram</span></div>',
    f'<a class="q-item tg" href="https://t.me/phycokiller420" target="_blank" rel="noopener">\n          <div class="q-left"><div class="q-icon">{telegram_svg}</div><span>Telegram</span></div>',
    content
)

with open('Untitled-1.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("✓ All social media icons replaced with SVG logos!")
