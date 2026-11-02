"""Check the public publication boundary without reading local-only files."""
from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parents[1]
PAGES = ('literature-map.html', 'literature-map-en.html',
         'knowledge-network.html', 'knowledge-network-en.html')
PUBLIC_DIRS = ('assets', 'literature', 'knowledge', 'papers', 'scripts', 'docs', '.github')
DATA = re.compile(r'<script id="data" type="application/json">(.*?)</script>', re.S)
LOCAL_PATH = re.compile(r'(?:^|[\s"\'(=/])(?:private|research|misc)/|review-policy\.md')

def public_files():
    yield ROOT / 'README.md'
    yield ROOT / '.gitignore'
    for name in PAGES:
        yield ROOT / name
    for folder in PUBLIC_DIRS:
        yield from (p for p in (ROOT / folder).rglob('*') if p.is_file()
                    and '__pycache__' not in p.parts)

def audit():
    errors = []
    assert '/private/' in (ROOT / '.gitignore').read_text(encoding='utf-8').splitlines()
    for path in public_files():
        if path.suffix not in {'.html', '.md', '.css', '.js', '.json'}:
            continue
        text = path.read_text(encoding='utf-8')
        if LOCAL_PATH.search(text):
            errors.append(f'{path.relative_to(ROOT)} contains a local-only reference')
        if path.suffix == '.md':
            for href in re.findall(r'\[[^\]]*\]\(([^)]+)\)', text):
                href = href.split('#')[0]
                # Deployment uses sparse checkout and serves original PDF URLs.
                target = (path.parent / href).resolve()
                if not (ROOT / 'papers').exists() and target.is_relative_to(ROOT / 'papers'):
                    continue
                if href and not re.match(r'\w+:', href) and not (path.parent / href).exists():
                    errors.append(f'{path.relative_to(ROOT)}: missing link {href}')
    for name in PAGES:
        data = json.loads(DATA.search((ROOT / name).read_text(encoding='utf-8'))[1])
        assert len(data['papers']) == 114, name
        assert all('importance' not in p and 'featured' not in p for p in data['papers']), name
        if 'concepts' in data:
            ids = {c['id'] for c in data['concepts']}
            assert len(ids) == 44, name
            assert all('experiment' not in r for r in data['routes']), name
            for c in data['concepts']:
                assert set(c['prerequisites'] + c['related']) <= ids, (name, c['id'])
            for route in data['routes']:
                assert set(route['steps']) <= ids, (name, route['id'])
            for paper in data['papers']:
                assert set(paper['concepts'] + paper['mechanismConcepts']) <= ids, (name, paper['id'])
    if errors:
        raise SystemExit('\n'.join(errors))
    print('Public audit passed: 114 papers, 44 concepts; no local-only links.')

if __name__ == '__main__':
    audit()
