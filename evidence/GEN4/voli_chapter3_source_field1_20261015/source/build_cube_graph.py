"""Exact closed graph consequence of the explicitly declared cube embedding.
This graph has no exterior; it is not a replacement for the Poisson receiver.
"""
from pathlib import Path
from fractions import Fraction as F
import json,hashlib,itertools
BASE=Path(__file__).resolve().parent
coords=list(itertools.product([-1,1],repeat=3));n=8
L=[[F(0) for j in range(n)] for i in range(n)]
for i,x in enumerate(coords):
 for j,y in enumerate(coords):
  if sum(a!=b for a,b in zip(x,y))==1:L[i][j]=-1;L[i][i]+=1
P=[[F(1,8) for j in range(n)] for i in range(n)]
minor=[row[:7] for row in L[:7]];a=[row+[F(i==j) for j in range(7)] for i,row in enumerate(minor)]
for k in range(7):
 i=next(i for i in range(k,7) if a[i][k]);a[k],a[i]=a[i],a[k];v=a[k][k];a[k]=[x/v for x in a[k]]
 for i in range(7):
  if i!=k:v=a[i][k];a[i]=[x-v*y for x,y in zip(a[i],a[k])]
inv=[row[7:] for row in a]
assert all(sum(row)==0 for row in L)
assert all(sum(L[i][k]*P[k][j] for k in range(8))==0 for i in range(8) for j in range(8))
assert all(sum(minor[i][k]*inv[k][j] for k in range(7))==int(i==j) for i in range(7) for j in range(7))
assert sum(F(1,8) for i in range(8))==1
wire=lambda M:[[str(x) for x in row] for row in M]
d=dict(schema='SAM_DECLARED_CUBE_CLOSED_GRAPH_V1',coordinates=coords,L=wire(L),P=wire(P),minor=wire(minor),minor_inverse=wire(inv),rank=7,uniform_source_total=1,uniform_source_compatible=False,scope='Declared orthogonal cube nearest-neighbor graph; positive total source cannot solve closed conservative graph. Physical bulk and source-to-field coupling remain supplied.',builder_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
(BASE/'CUBE_GRAPH.json').write_text(json.dumps(d,indent=2)+'\n');print('Cube closed-graph exact rank7 and positive-source incompatibility')
