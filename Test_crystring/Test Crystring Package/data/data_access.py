from mp_api.client import MPRester
from monty.serialization import dumpfn

mpr = MPRester("mhhJDAaMvh8a2OGGxEcK5zKqxlGeu2DB", mute_progress_bars = True)
def get_data_from_MP(ini: int, end: int):
    entries = {}
    vals = [f"mp-{i}" for i in range(ini, end)]
    query = mpr.materials.summary.search(material_ids=vals, fields=["material_id",  "formula_pretty", "symmetry", "structure", "band_gap"])

    for i, entry in enumerate(query):
        try:
            if entry:
                data = {}
                data["material_id"] = entry.material_id
                data["formula_pretty"] = entry.formula_pretty
                data["structure"] = entry.structure
                data["symmetry"] = entry.symmetry
                data["band_gap"] = entry.band_gap
                entries[entry.material_id] = data

        except:
            continue

    dumpfn(entries, f"MP_data-{ini}-{end}.json.gz")
    return

if __name__ == '__main__':
    get_data_from_MP(0,1000)