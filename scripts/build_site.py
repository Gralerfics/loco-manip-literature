"""Package only public readers; PDF buttons use the original publisher sources."""
from pathlib import Path
import json
import re
import shutil
import argparse
from audit_public import audit

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'dist'

def build(repository='Gralerfics/loco-manip-literature', ref='main'):
    audit()
    if OUT.exists():
        # This fixed, resolved directory is the only disposable build output.
        assert OUT.resolve() == ROOT.resolve() / 'dist'
        shutil.rmtree(OUT)
    OUT.mkdir(exist_ok=True)
    # Read the canonical paper index before packaging either language.
    raw = (ROOT / 'literature-map.html').read_text(encoding='utf-8')
    data = json.loads(re.search(r'<script id="data" type="application/json">(.*?)</script>', raw, re.S)[1])
    pdfs = {p['pdf']: p['url'] for p in data['papers'] if p.get('pdf') and p.get('url')}
    for name in ('literature-map.html', 'literature-map-en.html', 'knowledge-network.html', 'knowledge-network-en.html'):
        text = (ROOT / name).read_text(encoding='utf-8')
        for pdf, source in pdfs.items():
            text = text.replace(pdf, source)
        text = re.sub(r'(?<![\w/])((?:literature|knowledge)/[\w/-]+\.md|README\.md)',
                      lambda m: f'https://github.com/{repository}/blob/{ref}/{m[1]}', text)
        text = text.replace('本地 PDF', 'PDF').replace('Local PDF', 'PDF')
        (OUT / name).write_text(text, encoding='utf-8')
    shutil.copytree(ROOT / 'assets', OUT / 'assets', dirs_exist_ok=True)
    (OUT / '.nojekyll').touch()
    (OUT / 'index.html').write_text('''<!doctype html><html lang="zh-CN"><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>论文关系</title><script>location.replace('literature-map.html'+location.search+location.hash)</script>
<a href="literature-map.html">论文关系</a></html>''', encoding='utf-8')
    print(f'Built {OUT} (PDF links point to original sources)')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repository', default='Gralerfics/loco-manip-literature')
    parser.add_argument('--ref', default='main')
    args = parser.parse_args()
    build(args.repository, args.ref)
