# -*- coding: utf-8 -*-
import sys

# _DEFAULT_COLOR_DICT = {
#         'b':'#377eb8',
#         'g':'#4daf4a',
#         'r':'#e41a1c',
#         'c':'#984ea3',
#         'm':'#a65628',
#         'y':'#ffff33'}
        
_DEFAULT_COLOR_DICT = {
    'b': (0.21568627450980393, 0.49411764705882355, 0.7215686274509804),
    'c': (0.596078431372549, 0.3058823529411765, 0.6392156862745098),
    'g': (0.30196078431372547, 0.6862745098039216, 0.2901960784313726),
    'm': (0.6509803921568628, 0.33725490196078434, 0.1568627450980392),
    'r': (0.8941176470588236, 0.10196078431372549, 0.10980392156862745),
    'y': (1.0, 1.0, 0.2)}

def improve_abbreviations(color_dict=None, mpl_module=None):
    try:
        mpl = sys.modules['matplotlib']
    except KeyError:
        raise ImportError('Matplotlib must be imported before using MICA')
    if color_dict is None:
        color_dict = _DEFAULT_COLOR_DICT
    for abbrev, color in color_dict.items():
        mpl.colors.colorConverter.colors[abbrev] = color
    mpl.colors.colorConverter.cache = {}

