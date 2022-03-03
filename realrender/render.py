import sys
import cv2
import numpy as np

from .Sim3DR import RenderPipeline


def _to_ctype(arr):
    if not arr.flags.c_contiguous:
        return arr.copy(order="C")
    return arr


_cfg = {
    "intensity_ambient": 0.3,
    "color_ambient": (1, 1, 1),
    "intensity_directional": 0.6,
    "color_directional": (1, 1, 1),
    "intensity_specular": 0.1,
    "specular_exp": 5,
    "light_pos": (0, 0, 5),
    "view_pos": (0, 0, 5),
}

_render_app = RenderPipeline(**_cfg)


def render(
    img,
    ver_lst,
    tri,
    alpha=0.6,
    color=[1, 1, 1],
    show_flag=False,
    wfp=None,
    with_bg_flag=True,
):
    """
    ver: [(3, 38365)]
    tri: (76073, 3)
    """
    # print(ver_lst)
    if with_bg_flag:
        overlap = img.copy()
    else:
        overlap = np.zeros_like(img)

    for ver_ in ver_lst:
        ver = _to_ctype(ver_)  # transpose
        overlap = _render_app.render(ver, tri, overlap, color=color)

    if with_bg_flag:
        res = cv2.addWeighted(img, 1 - alpha, overlap, alpha, 0)
    else:
        res = overlap

    if wfp is not None:
        cv2.imwrite(wfp, res)
        print(f"Save visualization result to {wfp}")

    return res


"""
predefined config to render human mesh
"""

_cfg2 = {
    "intensity_ambient": 0.3,
    "intensity_directional": 0.6,
    "color_directional": (1, 1, 1),
    "intensity_specular": 0.1,
    "specular_exp": 5,
    "light_pos": (0, 0, -5),
    "view_pos": (0, 0, 5),
}

_render_app2 = RenderPipeline(**_cfg2)


def render_human_mesh(
    img,
    ver_lst,
    tri,
    alpha=0.6,
    color=[0.56, 0.37, 0.96],
    show_flag=False,
    wfp=None,
    with_bg_flag=True,
):
    """
    ver: [(38365, 3)]
    tri: (76073, 3)
    """
    # print(ver_lst)
    if with_bg_flag:
        overlap = img.copy()
    else:
        overlap = np.zeros_like(img)

    for ver_ in ver_lst:
        ver = _to_ctype(ver_)  # transpose
        overlap = _render_app2.render(ver, tri, overlap, color)

    if with_bg_flag:
        res = cv2.addWeighted(img, 1 - alpha, overlap, alpha, 0)
    else:
        res = overlap

    if wfp is not None:
        cv2.imwrite(wfp, res)
        print(f"Save visualization result to {wfp}")
    return res
