"""Small editorial spacing pass; never reads or writes source evidence."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent
selected = [0, 1, 2, 3, 4, 5, 8, 9, 10, 11]
replacements = {
    'Data_QualityC': 'Data_Quality C', 'ConfigC': 'Config C', 'ConfigB': 'Config B',
    'Orders_MasterL': 'Orders_Master L', 'Orders_MasterG': 'Orders_Master G',
    'Orders_MasterJ': 'Orders_Master J', 'Orders_MasterT': 'Orders_Master T',
    'Orders_MasterA': 'Orders_Master A', 'DATA_MasterAA': 'DATA_Master AA',
    'DATA_MasterAI': 'DATA_Master AI', 'Pickup_ChannelH': 'Pickup_Channel H',
    'SupportT': 'Support T', 'OwnerT': 'Owner T', 'OpsT': 'Ops T', 'OpsP': 'Ops P',
    'reportT': 'report T', 'weeklySKILL': 'weekly SKILL ',
    'architecture184': 'architecture 184', 'architecture281': 'architecture 281',
    'startingA3': 'starting A3', 'flagS': 'flag S', 'typeJ': 'type J',
    'validationM': 'validation M', 'confirmed20': 'confirmed 20',
    'New20orders': 'New 20 orders', 'Breakeven1/margin': 'Breakeven = 1 / margin',
    'baseline2.8': 'baseline 2.8', 'scaling3.8': 'scaling 3.8',
    'trailing4fullweeks': 'trailing 4 full weeks', '+20%scaling': '+20% scaling',
    'notYES': 'not YES', 'ratio.15': 'ratio .15', 'confirmation.60': 'confirmation .60',
    'intervention.15': 'intervention .15', 'pickup-no-show.30': 'pickup no-show .30',
    'cause capture.90': 'cause capture .90', 'reach.70': 'reach .70',
    'recovery.25': 'recovery .25', 'cycle6': 'cycle 6',
    '3.8breakeven': '3.8 breakeven', '20order': '20 order',
    'NoAnswer': 'NoAnswer', 'last7days': 'last 7 days', 'last30days': 'last 30 days',
    'netROAS': 'net ROAS', 'daysstock': 'days of stock', 'min1June': 'minimum 1 June',
    'on13October2026': 'on 13 October 2026',
    'wallet90%gate': 'wallet 90% gate', '25RTO+2exchange': '25 RTO + 2 exchange',
    'orders14:21': 'orders 14:21', 'products18:53': 'products 18:53',
    'cleanup11': 'cleanup 11', 'units175': 'units 175', 'rebuild13:24': 'rebuild 13:24',
}
prefixes = 'All|all|current|since|within|for|of|has|exact|total|versus|New|minimum|attempts|coverage|Baseline|baseline|stage|CSV|additions|top-up|intake|Wallet|Bosta|every|recent|max|cover|including|plotted|from|with'
units = 'orders|order|rows|legs|days|day|weeks|week|minutes|units|products|variants|lines|columns|refs|checkboxes|assigned|cards|Sep|Oct|Apr|May|Jun|July|October|June|wallet'

def edit(text):
    for old, new in replacements.items():
        text = text.replace(old, new)
    text = re.sub(r'\b(' + prefixes + r')(?=\d)', r'\1 ', text)
    text = re.sub(r'(?<=\d)(?=(' + units + r')\b)', ' ', text)
    text = re.sub(r'(?<=[,:;])(?=[A-Za-z0-9])', ' ', text)
    text = re.sub(r'(?<=\d), (?=\d{3}\b)', ',', text)
    text = re.sub(r'(?<=\d): (?=\d{2}\b)', ':', text)
    text = re.sub(r'([A-Z]{1,3}\d+): ([A-Z]{1,3}\d+)', r'\1:\2', text)
    return text

for path in (ROOT / 'docs/reconstruction').glob('*.md'):
    if int(path.name[:2]) not in selected:
        continue
    text = path.read_text(encoding='utf-8-sig')
    # Protect inline code, URLs, link destinations and fenced diagrams.
    sections = re.split(r'(```[\s\S]*?```|`[^`]*`|\]\([^)]*\)|https?://\S+)', text)
    text = ''.join(part if i % 2 else edit(part) for i, part in enumerate(sections))
    path.write_text(text, encoding='utf-8')
