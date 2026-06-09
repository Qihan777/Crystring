from mp_api.client import MPRester
from monty.serialization import dumpfn

mpr = MPRester("mhhJDAaMvh8a2OGGxEcK5zKqxlGeu2DB", mute_progress_bars=True)

def get_data_from_MP() -> None:
    entries = {}
    query = mpr.materials.summary.search(fields=["material_id", "formula_pretty", "symmetry", "structure", "band_gap"])

    for entry in query:
        if entry:
            try:
                data = {
                    "material_id": entry.material_id,
                    "formula_pretty": entry.formula_pretty,
                    "structure": entry.structure,
                    "symmetry": entry.symmetry,
                    "band_gap": entry.band_gap,
                }
                entries[entry.material_id] = data
            except AttributeError:
                continue
    dumpfn(entries, "MP_data.json.gz")

if __name__ == '__main__':
    get_data_from_MP()
