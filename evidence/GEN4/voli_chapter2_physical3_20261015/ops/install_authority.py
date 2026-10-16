"""Install completed scoped results in history first, then current pointers.

Preserves unrelated scopes and checks source preimages immediately before each
write. No science, native runtime change, commit, publication or sync occurs.
"""
from pathlib import Path
import hashlib,json,re
BASE=Path(__file__).resolve().parents[1];ROOT=BASE.parents[1]
REL=BASE.relative_to(ROOT).as_posix();RUNREL='GEN4/duck_gen6_local/runs/chapter2-physical-protocols-20261015-01'
def read(p):return json.loads(Path(p).read_text())
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def save(p,d):Path(p).write_text(json.dumps(d,indent=2,sort_keys=True)+'\n')
def replace_front(text,entry):return re.sub(r'^history_entry: H\d+$','history_entry: '+entry,text,count=1,flags=re.M)
def main():
 assert read(ROOT/RUNREL/'COMPLETE.json')['status']=='COMPLETE'
 assert read(BASE/'REPRODUCTION.json')['status']=='PASS'
 assert read(BASE/'chapter/PDF_VERIFICATION.json')['status']=='PASS'
 assert not (BASE/'HISTORY_INSTALLATION.json').exists(),'Authority already installed; inspect receipt instead of repeating'
 live_names=['SAM_LIVE/00_CURRENT.md','SAM_LIVE/15_VOLI_EXPANSION_CURRENT.md','SAM_LIVE/03_STARBREAKER_GW_CURRENT.md']
 misc=['SAM_PROJECT/CONTINUITY.json','GEN4/DUCK_CURRENT.json','SAM_HISTORY/HISTORY_INDEX.md']
 before={name:(ROOT/name).read_bytes() for name in live_names+misc}
 entries=ROOT/'SAM_HISTORY/entries';number=max(int(p.name[1:7]) for p in entries.glob('H[0-9]*') if re.match(r'H\d{6}_',p.name))+1
 entry='H'+str(number).zfill(6);name=entry+'_2026-10-15_CHAPTER_II_PHYSICAL_PROTOCOLS_AND_ACTUAL_CLOSURE.md';history=entries/name
 previous_live=[]
 for key in live_names:
  text=before[key].decode();hits=[x for x in text.splitlines() if ('H002635' in x or x.startswith('[ChII]') or x.startswith('[Retained memory]'))]
  previous_live.append(dict(path=key,sha256=hashlib.sha256(before[key]).hexdigest(),replaced_relevant_lines=hits))
 note=f'''---
entry_id: {entry}
entry_date: 2026-10-15
entry_type: RESULT
status: IMMUTABLE_HISTORY
supersedes: NONE
affects_live:
  - SAM_LIVE/00_CURRENT.md
  - SAM_LIVE/15_VOLI_EXPANSION_CURRENT.md
  - SAM_LIVE/03_STARBREAKER_GW_CURRENT.md
---

# Chapter II actual closure and paid receiving protocols

H002635's15-page development and all original source results are preserved.
User authorized actual spin closure, one complete paid-reference program,
measurement/error/shot specification, compact proofs and an endpoint table.
New source: {REL}/REPORT.md. Duck run: {RUNREL}.

All54 actual finite-N profiles have paired Krylov rank at least10 through
power4. The original V7 residual has exact rank2, V9 dimension9 and nonclosure.
V001_BASE reaches rank14 through power6: V5,V7,V9,V11 enlarge by exactly2;
V13 has at least one outgoing direction. No computed rank stabilizes and no
smallest invariant dimension is assigned. Explicit residual functions and
strict positive full-Gibbs norm bounds accompany the exact finite lumped
invariant upper space. New global higher residual moments remain unintegrated.
The finite-time K7 memory kernel has rank2 for every finite source time;
the propagator difference is not assigned that rank.

The forward/reverse/wait protocol uses the original positive durations and
actual conserved continuum energy. Wait retains h_R=-2E P_R. Entry/release
are external intervals. Actual and reference phases, all continuous/ramp/quench
work, midpoint energy calibration and phase unwrapping are explicit. Gross
positive and withdrawn reference work each approximate20.59066144 hbar/t_u;
their signed cancellation does not assign zero apparatus cost. The reference
prefix protocol requires at most23,482,368 fresh copies under its stated
systematic/calibration bounds; actual-clock readout has an additional account.

The source-selected fixed measurement cadence supports eta0.01 with four
separate0.001 apparatus allocations and0.006 statistical allowance. Its
99percent joint sampling guarantee uses819751 shots at each of8 times,
6558008 fresh copies total, conditional on independently established bounds.
The null is closed autonomous TLS/fixed linear receiver; generic multilevel,
open/driven two-state controls and an achieved apparatus remain separate.

Short memory/Gram/error, minimum-counter, ABBA/BAAB and full endpoint
certificates are now in the20-page40-section chapter. Source/session/native
and artifact checks have independent replay. Duck Connections completed
two180-second windows,11 native and4 local-index retrieval outcomes,0 failed
mathematical returns, all4 selected targets and parent retained. Scientific
readback passes2719checks/1452matrixentries; PDF133checks include a byte-identical
relocated rebuild. Native source preparation separately retains58 full-source
evaluation returns and6 installed inverse checks. Bounded failures stay explicit.

The closing spin review preserves completed J21/F11/T5 and the separate next
lower Dirichlet scalar. Current pointers change only after this entry exists.
No runtime installation, commit, sync, I9 access or automatic third round.

The test result suggests strong contact with the concept.

Sean Brady: originator/conceptual director. OpenAI ChatGPT and Codex:
research collaborators. New mathematics and receiving constructions: Codex.

## Preserved prior current lines and source identities

```json
{json.dumps(previous_live,indent=2)}
```
'''
 with history.open('x') as stream:stream.write(note)
 changed={}
 for key in live_names:
  text=replace_front(before[key].decode(),entry)
  if key.endswith('00_CURRENT.md'):
   text=text.replace('[I](15_VOLI_EXPANSION_CURRENT.md)(H002635)','[I](15_VOLI_EXPANSION_CURRENT.md)('+entry+')')
   text=text.replace('(H002627/H002635):J21/F11complete','(H002627/'+entry+'):J21/F11complete')
  elif key.endswith('15_VOLI_EXPANSION_CURRENT.md'):
   old='[ChII](../GEN4/voli_chapter2_continuation2_20261015/REPORT.md)(H002635):15pp;rank2.'
   new='[ChII](../'+REL+'/REPORT.md)('+entry+'):20pp;10/14.'
   assert old in text,'Current chapter pointer changed; inspect live source'
   text=text.replace(old,new,1)
  else:
   text=text.replace('scientific spin state:H002627/H002635.','scientific spin state:H002627/'+entry+'.')
   old=next(x for x in text.splitlines() if x.startswith('[Retained memory]'))
   new='[Actual closure](../'+REL+'/closure/DERIVATION.md)('+entry+'):V7 residual rank2 in54/54;rank>=10 all54,>=14 V001_BASE;V9/V13 nonclosed;smallest invariant rank open. Global higher norms and next lower Dirichlet scalar remain separate.'
   text=text.replace(old,new,1)
  cap=49152 if key.endswith('03_STARBREAKER_GW_CURRENT.md') else 16384 if key.endswith('00_CURRENT.md') else 32768
  assert len(text.encode())<=cap,(key,len(text.encode()),cap)
  changed[key]=text.encode()
 cursor=json.loads(before['GEN4/DUCK_CURRENT.json']);scope='latest_chapter2_physical_cycle'
 cursor[scope]=dict(campaign=REL,history=entry,status='COMPLETE',run=RUNREL,completion=RUNREL+'/COMPLETE.json',
  target=REL+'/TARGET.md',policy=REL+'/RUN_POLICY.json',guide=REL+'/README.md',report=REL+'/REPORT.md',follow_up=REL+'/FOLLOW_UP.md',
  round_seconds=[180,180],round_two_selector='CODEX_CURRENT_SESSION',research_mode='connections',native_returns=11,research_returns=4,failed_returns=0,
  resource_release='PASS',helper_readback='PASS',parent_retained=True,selected_targets=['ACTUAL_CLOSURE','PAID_REFERENCE','MEASUREMENT','COMPACT_CERTIFICATES'],
  automatic_repeat=False,automatic_third_round=False,storage='T500_ONLY',archive_status='NOT_REQUESTED_NO_COMMIT',
  next='Read20-page physical draft and explicit invariant-rank/physical-apparatus limits; completed cycle is recovery only.')
 changed['GEN4/DUCK_CURRENT.json']=(json.dumps(cursor,indent=2,sort_keys=True)+'\n').encode()
 routes=json.loads(before['SAM_PROJECT/CONTINUITY.json']);routes['history_entry']=entry
 if routes.get('duck_default_scope') in ['latest_chapter2_continuation_cycle',scope]:
  routes['duck_default_scope']=scope;routes['duck_default_scope_note']='Completed Chapter II physical protocols and actual closure boundary; two180-second Connections windows; this scoped cycle has exited.'
 routes['chapter_ii_physical_development']=dict(history_entry=entry,status='COMPLETE_DEVELOPMENT_PASS_MINIMAL_CLOSURE_OPEN',report=REL+'/REPORT.md',pdf=REL+'/output/pdf/SAM_Volume_I_Chapter_II_Physical_Development_Draft_20261015.pdf',reproduce=REL+'/reproduce.py',next=REL+'/FOLLOW_UP.md',prior='H002635')
 changed['SAM_PROJECT/CONTINUITY.json']=(json.dumps(routes,indent=2)+'\n').encode()
 index=before['SAM_HISTORY/HISTORY_INDEX.md'].decode()
 index+='\n| [`'+entry+'`](entries/'+name+') | 2026-10-15 | `RESULT` | ChapterII20pp;actualV7rank2all54/rank10–14;paidreference/fullshotprotocols/proofs;Duck2x18011native/4retrieval | H002635 preserved;minimal invariant closure/material apparatus open;custody/releasePASS |\n'
 changed['SAM_HISTORY/HISTORY_INDEX.md']=index.encode()
 for key,data in changed.items():
  p=ROOT/key;assert p.read_bytes()==before[key],'Concurrent authority change: '+key
  p.write_bytes(data)
 save(BASE/'HISTORY_INSTALLATION.json',dict(status='INSTALLED',history=entry,history_entries=[str(history.relative_to(ROOT))],history_sha256=sha(history),
  live_files=[dict(path=key,bytes=len(data),before_sha256=hashlib.sha256(before[key]).hexdigest(),after_sha256=sha(ROOT/key)) for key,data in changed.items()],
  unrelated_scopes_preserved=True,scientific_execution=False))
 print(json.dumps(dict(status='INSTALLED',history=entry,path=str(history.relative_to(ROOT)))))
if __name__=='__main__':main()
