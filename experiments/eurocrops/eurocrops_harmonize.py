"""
Harmonize EuroCrops to have these classes:
- 33010106**: corn  -> 0000000001
- 330116****: soy   -> 0000000002
- 33010107**: rice  -> 0000000003
- 33010101**: wheat -> 0000000004
- 33010102**: wheat -> 0000000004
Everything else becomes 0000000005 (other).
And stuff not covered by a label would be nodata.
"""
import glob
import multiprocessing
import os

import fiona
import tqdm

in_dir = "/data/favyenb/eurocrops/eurocrops_orig/"
out_dir = "/data/favyenb/eurocrops/eurocrops_harmonized/"

def get_out_code(in_code):
    if not in_code:
        return "0000000000"
    if in_code.startswith("33010106"):
        return "0000000001"
    if in_code.startswith("330116"):
        return "0000000002"
    if in_code.startswith("33010107"):
        return "0000000003"
    if in_code.startswith("33010101"):
        return "0000000004"
    if in_code.startswith("33010102"):
        return "0000000004"
    return "0000000005"

in_fnames = glob.glob(os.path.join(in_dir, "**/*.shp"), recursive=True)

def harmonize(in_fname):
    out_fname = os.path.join(out_dir, os.path.basename(in_fname))
    assert not os.path.exists(os.path.join(out_dir, out_fname))
    with fiona.open(in_fname) as src:
        with fiona.open(out_fname, "w", crs=src.crs, driver=src.driver, schema=src.schema) as dst:
            for feat in src:
                feat["properties"]["EC_hcat_c"] = get_out_code(feat["properties"]["EC_hcat_c"])
                dst.write(feat)

p = multiprocessing.Pool(64)
outputs = p.imap_unordered(harmonize, in_fnames)
for _ in tqdm.tqdm(outputs, total=len(in_fnames)):
    pass
p.close()
