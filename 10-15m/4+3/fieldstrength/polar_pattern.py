#!/usr/bin/env python3
"""
polar_pattern.py

Usage:
  python3 polar_pattern.py data.dat
  python3 polar_pattern.py data.dat --out pattern.png
  python3 polar_pattern.py data.dat --dbmin -36 --normalize
  python3 polar_pattern.py data.dat --no-normalize  # (default)
"""

import argparse
import numpy as np
import matplotlib.pyplot as plt
import os
import sys

def read_data(filename, angcol, valcol):
    try:
        raw = np.loadtxt(filename, comments='#')
    except Exception as e:
        raise SystemExit(f"Failed to read '{filename}': {e}")

    if raw.ndim == 1:
        raw = raw.reshape(-1, 1)

    ncols = raw.shape[1]
    if ncols == 1:
        vals = raw[:, 0]
        angles = np.linspace(0, 360, len(vals), endpoint=False)
    else:
        if angcol >= ncols or valcol >= ncols:
            raise SystemExit(f"Requested column(s) ({angcol},{valcol}) out of range for {ncols} columns")
        angles = raw[:, angcol]
        vals = raw[:, valcol]
    return np.asarray(angles, float), np.asarray(vals, float)

def rmap(db, dbmin, dbmax):
    return (db - dbmin) / (dbmax - dbmin) if dbmax != dbmin else np.zeros_like(db)

def main():
    p = argparse.ArgumentParser(description="Plot polar pattern (0° up, clockwise, center=DB_MIN, outer=0 dB).")
    p.add_argument("datafile", help="Input .dat file (angle_deg value_dB or single-column values).")
    p.add_argument("--angcol", type=int, default=0, help="0-based angle column (default 0)")
    p.add_argument("--valcol", type=int, default=1, help="0-based value column (default 1)")
    p.add_argument("--dbmin", type=float, default=-36.0, help="dB mapped to center (default -36)")
    p.add_argument("--dbmax", type=float, default=0.0, help="dB mapped to outer circle (default 0)")
    p.add_argument("--gridstep", type=float, default=6.0, help="radial grid every N dB (default 6)")
    p.add_argument("--spokestep", type=float, default=30.0, help="spokes every N degrees (default 30)")
    p.add_argument("--normalize", dest="normalize", action="store_true", help="Normalize so max value = 0 dB")
    p.add_argument("--no-normalize", dest="normalize", action="store_false", help="Disable normalization (default)")
    p.set_defaults(normalize=False)
    p.add_argument("--out", default=None, help="Output filename (png/svg); show interactively if omitted.")
    p.add_argument("--dpi", type=int, default=150)
    p.add_argument("--close-loop", action="store_true", help="Close the plotted loop")
    args = p.parse_args()

    angles, vals = read_data(args.datafile, args.angcol, args.valcol)

    # Normalize so that max = 0 dB if requested
    if args.normalize:
        vmax = np.nanmax(vals)
        vals = vals - vmax
        print(f"Normalized: max={vmax:.2f} dB → shifted so max=0 dB")

    # Clip to [dbmin, dbmax] range
    vals_clip = np.clip(vals, args.dbmin, args.dbmax)
    r = rmap(vals_clip, args.dbmin, args.dbmax)

    if args.close_loop:
        angles = np.concatenate([angles, angles[:1]])
        r = np.concatenate([r, r[:1]])

    theta = np.deg2rad(angles)

    # --- plot ---
    fig, ax = plt.subplots(figsize=(6,6), subplot_kw=dict(projection="polar"))
    ax.set_theta_zero_location("N")   # 0° up
    ax.set_theta_direction(-1)        # clockwise

    ax.set_ylim(0, 1.0)

    db_ticks = np.arange(args.dbmin + args.gridstep, args.dbmax + 1e-6, args.gridstep)
    if db_ticks.size == 0:
        db_ticks = np.array([args.dbmax])
    ax.set_rticks(rmap(db_ticks, args.dbmin, args.dbmax))
    ax.set_yticklabels([f"{int(d)} dB" if float(d).is_integer() else f"{d:.1f} dB" for d in db_ticks])

    spoke_angles = np.arange(0, 360, args.spokestep)
    ax.set_thetagrids(spoke_angles, labels=[f"{int(a)}°" for a in spoke_angles])
    ax.grid(True)

    ax.plot(theta, r, lw=2)
    ax.fill_between(theta, r, 0, alpha=0.12)

    ax.set_title(f"{os.path.basename(args.datafile)}\n(center={args.dbmin} dB, outer={args.dbmax} dB"
                 + (", normalized" if args.normalize else "") + ")")

    if args.out:
        fig.savefig(args.out, dpi=args.dpi, bbox_inches="tight")
        print(f"Wrote {args.out}")
    else:
        plt.show()

if __name__ == "__main__":
    main()
