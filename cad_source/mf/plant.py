"""Builds every machine and the complete plant assembly."""
from .core import *
from . import layout as LY
from . import m_prep, m_mix, m_press, m_site

MACHINES = []     # ordered list of (Asm, plant position)
INFO = {}


def build():
    if 'PLANT' in ASMS:
        return ASMS['PLANT']
    INFO['tile_kg'] = m_press.register_tooling()
    m_press.build_carrier()
    wb = m_mix.wb_geometry()
    INFO['wb'] = wb
    seq = [
        (m_site.build_CT(), (0, 0, 0)),
        (m_prep.build_ST(), (*LY.ST, 0)),
        (m_prep.build_SH(), (*LY.SH, 0)),
        (m_prep.build_SF(), (0, 0, 0)),
        (m_prep.build_DR(), (*LY.DR, 0)),
        (m_prep.build_VS(), (*LY.VS, 0)),
        (m_prep.build_DC(), (*LY.DC, 0)),
        (m_mix.build_WB(), (*wb['origin'], 0)),
        (m_mix.build_MX(), (*LY.MX, 0)),
        (m_press.build_RC(), (0, 0, 0)),
        (m_press.build_HP(), (*LY.HP, 0)),
        (m_press.build_CR(), (*LY.CR, 0)),
        (m_press.build_TR(), (*LY.TR, 0)),
        (m_site.build_FG(), (11380, 1830, 0)),
        (m_site.build_EL(), (0, 0, 0)),
        (m_site.build_SC(), (0, 0, 0)),
        (m_press.build_TT(), (9000, 4000, LY.G)),
    ]
    # tooling shown as its own "machine" for the documentation (not placed twice in the plant)
    TLA = Asm('TL', 'Mould tooling and product', desc='The tile, the cast-aluminium cavity insert (10 off), the steel punch (2 off) and the mould carrier (2 off).')
    TLA.add('TL-001', (-165, -700, 60))
    TLA.add('TL-101', (0, 0, 10 + 0)); TLA.add(ASMS['TL-110'], (0, 200, 0)); TLA.add('TL-101', (0, 400, 10))
    TLA.add('TL-102', (0, 0, 260)); TLA.add('TL-102', (0, 400, 260))
    plant = Asm('PLANT', 'Solar plastic-sand roof tile microfactory')
    for a, pos in seq:
        plant.add(a, pos)
        MACHINES.append((a, pos))
    MACHINES.append((TLA, None))
    # spare tooling quantities for the BOM (beyond what is drawn in the plant)
    INFO['extra_qty'] = {'TL-101': 2, 'TL-110': 1}
    return plant
