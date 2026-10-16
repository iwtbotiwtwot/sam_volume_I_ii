#!/usr/bin/env python3
"""Freeze retained exact Si29 operands and proposed source-bound native words.

This is source recovery and task construction, not native execution.
"""
from pathlib import Path
from fractions import Fraction as F
import hashlib
import json

HERE = Path(__file__).resolve().parent
ROOT = next(p for p in HERE.parents if (p / 'AGENTS.md').exists())
OLD = ROOT / 'GEN4/volii_duck_expansion1/Q01_RESULT.json'
OBS = ROOT / 'GEN4/volii_duck_expansion2/OBSERVABLE_CLOSURE.json'

def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

def save(name, data):
    (HERE / name).write_text(json.dumps(data, indent=2, sort_keys=True) + '\n')

def block(matrices):
    n = sum(len(m) for m in matrices)
    ans = [['0'] * n for _ in range(n)]
    offset = 0
    for m in matrices:
        for i, row in enumerate(m):
            for j, v in enumerate(row):
                ans[offset+i][offset+j] = str(v)
        offset += len(m)
    return ans

def diag(v):
    return [[str(v[i]) if i == j else '0' for j in range(len(v))] for i in range(len(v))]

def main():
    d = json.loads(OLD.read_text())
    data = {k:d[k] for k in ['source','species','inventory','Q','incoming_number',
             'coherent_number_gram','gram_denominator','assumptions']}
    data['schema'] = 'SAM_CH3_RETAINED_SI29_EXACT_V1'
    data['source_sha256'] = sha(OLD)
    save('EXACT_INPUTS.json', data)
    bindings = {
        'schema':'SAM_CH3_SOURCE_BINDINGS_V1',
        'campaign':'voli_chapter3_source_field1_20261015',
        'files':{str(p.relative_to(ROOT)):sha(p) for p in [OLD,OBS,HERE/'EXACT_INPUTS.json',HERE/'prepare.py']},
        'scope':'Exact retained Si29 bright-source number effects and Gram forms; no new coupling, mass or SI identification.',
        'missing_archival_files':[
            'GEN4/volii_duck_expansion2/inputs/SOURCE.npz',
            'GEN4/volii_duck_expansion2/inputs/SPATIAL_GRAMS.npz',
            'GEN4/volii_duck_expansion2/CROSS_Si29.npz'],
        'recovery':'Exact JSON retains every needed Q, Nin and spatial Gram; no absent binary is reconstructed as an original file.'}
    save('SOURCE_BINDINGS.json', bindings)
    tasks=[]
    Q=d['Q']; den=d['gram_denominator']
    for label, operands, purpose in [
        ('outgoing', {**{'G'+str(t):block([d['coherent_number_gram'][t][x] for x in range(8)]) for t in range(3)},
                      'negative_denQ':block([[[-den*v for v in row] for row in Q] for _ in range(8)])},
         'Check all eight exact source outgoing Gram identities sum_species G_tx=240Q; congruence then gives each outgoing energy share h/8.'),
        ('incoming', {**{'N'+str(t):block([diag(d['incoming_number'][t][x]) for x in range(8)]) for t in range(3)},
                      'negative_I':block([diag([-1]*4) for _ in range(8)])},
         'Check all eight exact incoming occupation identities sum_species N_tx=I; the full bright energy effect is H0/8 at each site.')]:
        key='r1_si29_'+label+'_flatness'
        binding={'campaign':'voli_chapter3_source_field1_20261015','source_files':bindings['files'],
                 'question':purpose,'basis':'Eight actual cube sites, each in the retained four-component collective source basis',
                 'physical_scope':'Retained exact source identity; no microscopic gravity/cube-to-shell/SI assignment.'}
        payload={'name':key,'context':{'basis':['site%d:component%d'%(x,j) for x in range(8) for j in range(4)],
                    'field':{'radicand':0},'spectral_coordinate':'retained source Gram and occupation coordinates',
                    'units':{'entries':'exact source relative integer forms'},
                    'history':{'source_clock':'theta; physical coupling rate unassigned','source':'Si29 retained bright construction'}},
                 'data':{'operators':operands,'program':[{'name':'residual','op':'add','inputs':list(operands)}], 'output':'residual'},
                 'source_binding':binding}
        tasks.append({'key':key,'operation':'GEN3_SOURCE_OPERATOR_WORD','payload':payload,
                      'source_binding':binding,'purpose':purpose})
    save('DUCK_R1_TASKS.json',tasks)
    print(json.dumps({'status':'PREPARED_NOT_EXECUTED','native_task_count':len(tasks),'exact_input_sha256':sha(HERE/'EXACT_INPUTS.json')}))

if __name__=='__main__':
    main()
