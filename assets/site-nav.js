/* Add future top-level pages here; all readers use this navigation. */
(() => {
  const pages = [
    ['literature-map', '论文关系', 'Paper relationships'],
    ['knowledge-network', '知识网络', 'Knowledge network'],
  ];
  const file = location.pathname.split('/').pop() || 'index.html';
  const english = file.includes('-en.');
  const current = file.startsWith('knowledge-network') ? 'knowledge-network' : 'literature-map';
  const nav = document.querySelector('[data-site-nav]');
  nav.className = 'site-nav';
  nav.setAttribute('aria-label', english ? 'Main navigation' : '主导航');
  for (const [slug, zh, en] of pages) {
    const a = document.createElement('a');
    a.href = slug + (english ? '-en' : '') + '.html';
    a.textContent = english ? en : zh;
    if (slug === current) { a.className = 'current'; a.setAttribute('aria-current', 'page'); }
    nav.append(a);
  }
  const language = document.createElement('a');
  language.id = 'english-link';
  language.className = 'site-language';
  language.textContent = english ? '中文' : 'English';
  const update = () => { language.href = current + (english ? '' : '-en') + '.html' + location.hash; };
  update(); language.addEventListener('click', update);
  nav.append(language);
})();
