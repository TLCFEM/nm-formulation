# Reformulation of Concentrated Plasticity Frame Element With N-M Interaction and Generalised Plasticity

This repository contains the source code and example models of paper [10.1061/JSENDH/STENG-12176](https://doi.org/10.1061/JSENDH/STENG-12176).

To cite or reproduce figures in the paper, you can find the corresponding figure and copy the source code in your work.

The numerical examples used in the paper are developed in `suanPan`. To perform the numerical analysis, one can download and install [`suanPan`](https://github.com/TLCFEM/suanPan). Then run the model via, for example, the following command in the corresponding
folders under the corresponding folders in `MODELS`.

```sh
suanpan -f SingleSection.supan
```

All mentioned models are implemented in `suanPan`:

1. Elements
    1. 2D Beam Element [NMB21](https://tlcfem.github.io/suanPan-manual/latest/Library/Element/Beam/NMB21/)
    2. 3D Beam Element [NMB31](https://tlcfem.github.io/suanPan-manual/latest/Library/Element/Beam/NMB31/)
2. Sections
    1. Linear Hardening [NM2D2](https://tlcfem.github.io/suanPan-manual/latest/Library/Section/SectionNM/NM2D2/)
    2. Nonlinear Hardening [NM2D3](https://tlcfem.github.io/suanPan-manual/latest/Library/Section/SectionNM/NM2D3/)
    3. Per-component Hardening [NM2D3K](https://tlcfem.github.io/suanPan-manual/latest/Library/Section/SectionNM/NM2D3K/)
    4. Linear Hardening [NM3D2](https://tlcfem.github.io/suanPan-manual/latest/Library/Section/SectionNM/NM3D2/)
    5. Nonlinear Hardening [NM3D3](https://tlcfem.github.io/suanPan-manual/latest/Library/Section/SectionNM/NM3D3/)
    6. Per-component Hardening [NM32D3K](https://tlcfem.github.io/suanPan-manual/latest/Library/Section/SectionNM/NM3D3K/)
