"""

mkinit ~/code/kwarray/kwarray/__init__.py --relative --nomods -w
mkinit ~/code/kwimage/kwimage/__init__.py --relative --nomods -w
mkinit ~/code/kwplot/kwplot/__init__.py --relative --nomods -w
mkinit netharn.util --relative --nomods -w
"""
from __future__ import absolute_import, division, print_function, unicode_literals

__extra_all__ = [
    'profiler',
    'util_dataframe',
    'dataframe_light',
]

__private__ = ['util_dataframe']


__external__ = [
    'kwarray', 'kwimage', 'kwplot'
]


# <AUTOGEN_INIT>
from .imutil import (adjust_gamma, ensure_grayscale, get_num_channels,
                     image_slices, load_image_paths, overlay_colorized,
                     wide_strides_1d,)
from .mplutil import (adjust_subplots, aggensure, axes_extent, colorbar,
                      colorbar_image, copy_figure_to_clipboard, draw_border,
                      extract_axes_extents, interpolated_colormap,
                      make_legend_img, pandas_plot_matrix, qtensure,
                      render_figure_to_image, reverse_colormap, save_parts,
                      savefig2, scores_to_cmap, scores_to_color,)
from .profiler import (IS_PROFILING, profile, profile_now,)
from .util_averages import (CumMovingAve, ExpMovingAve, InternalRunningStats,
                            MovingAve, RunningStats, WindowedMovingAve,
                            absdev,)
from .util_cachestamp import (CacheStamp,)
from .util_filesys import (get_file_info,)
from .util_fname import (align_paths, check_aligned, dumpsafe,
                         shortest_unique_prefixes, shortest_unique_suffixes,)
from .util_idstr import (compact_idstr, make_idstr, make_short_idstr,)
from .util_inspect import (default_kwargs,)
from .util_io import (read_arr, read_h5arr, write_arr, write_h5arr,)
from .util_iter import (roundrobin,)
from .util_json import (LossyJSONEncoder, NumpyEncoder,
                        ensure_json_serializable, read_json, walk_json,
                        write_json,)
from .util_misc import (FlatIndexer, SupressPrint, align, align_lines,
                        strip_ansi,)
from .util_resources import (ensure_ulimit,)
from .util_slider import (SlidingWindow, Stitcher,)
from .util_slider_dep import (SlidingIndexDataset, SlidingSlices,)
from .util_subextreme import (argsubmax, argsubmaxima,)
from .util_tensorboard import (read_tensorboard_scalars,)
from .util_torch import (BatchNormContext, DisableBatchNorm,
                         IgnoreLayerContext, ModuleMixin, freeze_params,
                         grad_context, number_of_parameters, one_hot_embedding,
                         one_hot_lookup, torch_ravel_multi_index,
                         trainable_layers,)
from .util_zip import (split_archive, zopen,)


try:
    # external modules in netharn.util are DEPRECATED
    # Don't depend on these external utilities at import time
    # In the future these will become optional, and these will no longer be
    # exposed via netharn.util
    from kwarray import (ArrayAPI, DataFrameArray, DataFrameLight, LocLight,
                         apply_grouping, arglexmax, argmaxima, argminima,
                         atleast_nd, boolmask, ensure_rng, group_consecutive,
                         group_consecutive_indices, group_indices, group_items,
                         isect_flags, iter_reduce_ufunc, maxvalue_assignment,
                         mincost_assignment, mindist_assignment, one_hot_embedding,
                         one_hot_lookup, random_combinations, random_product,
                         seed_global, shuffle, standard_normal, standard_normal32,
                         standard_normal64, stats_dict, uniform, uniform32,)
    from kwimage import (BASE_COLORS, Boxes, CSS4_COLORS, Color, Coords,
                         Detections, Heatmap, Mask, MaskList, MultiPolygon, Points,
                         PointsList, Polygon, PolygonList, Segmentation,
                         SegmentationList, TABLEAU_COLORS,
                         TORCH_GRID_SAMPLE_HAS_ALIGN, XKCD_COLORS,
                         atleast_3channels, available_nms_impls,
                         convert_colorspace, daq_spatial_nms, decode_run_length,
                         draw_boxes_on_image, draw_clf_on_image,
                         draw_text_on_image, draw_vector_field, encode_run_length,
                         ensure_alpha_channel, ensure_float01, ensure_uint255,
                         fourier_mask, gaussian_patch, grab_test_image,
                         grab_test_image_fpath, imread, imresize, imscale, imwrite,
                         load_image_shape, make_channels_comparable, make_heatmask,
                         make_orimask, make_vector_field, non_max_supression,
                         num_channels, overlay_alpha_images, overlay_alpha_layers,
                         radial_fourier_mask, rle_translate, smooth_prob,
                         stack_images, stack_images_grid, subpixel_accum,
                         subpixel_align, subpixel_getvalue, subpixel_maximum,
                         subpixel_minimum, subpixel_set, subpixel_setvalue,
                         subpixel_slice, subpixel_translate, warp_points,
                         warp_tensor,)
    from kwplot import (PlotNums, autompl, autoplt, distinct_colors,
                        distinct_markers, draw_boxes, draw_boxes_on_image,
                        draw_clf_on_image, draw_line_segments, draw_text_on_image,
                        ensure_fnum, figure, imshow, legend, make_conv_images,
                        make_heatmask, make_orimask, make_vector_field, multi_plot,
                        next_fnum, plot_convolutional_features, plot_matrix,
                        plot_surface3d, set_figtitle, set_mpl_backend,
                        show_if_requested,)
except Exception:
    pass

__all__ = ['ArrayAPI', 'BASE_COLORS', 'BatchNormContext', 'Boxes',
           'CSS4_COLORS', 'CacheStamp', 'Color', 'Coords',
           'CumMovingAve', 'DataFrameArray', 'DataFrameLight', 'Detections',
           'DisableBatchNorm', 'ExpMovingAve', 'FlatIndexer', 'Heatmap',
           'IS_PROFILING', 'IgnoreLayerContext', 'InternalRunningStats',
           'LocLight', 'LossyJSONEncoder', 'Mask', 'MaskList',
           'ModuleMixin', 'MovingAve', 'MultiPolygon', 'NumpyEncoder',
           'PlotNums', 'Points', 'PointsList', 'Polygon', 'PolygonList',
           'RunningStats', 'Segmentation', 'SegmentationList',
           'SlidingIndexDataset', 'SlidingSlices', 'SlidingWindow', 'Stitcher',
           'SupressPrint', 'TABLEAU_COLORS', 'TORCH_GRID_SAMPLE_HAS_ALIGN',
           'WindowedMovingAve', 'XKCD_COLORS', 'absdev', 'adjust_gamma',
           'adjust_subplots', 'aggensure', 'align', 'align_lines',
           'align_paths', 'apply_grouping', 'arglexmax', 'argmaxima',
           'argminima', 'argsubmax', 'argsubmaxima', 'atleast_3channels',
           'atleast_nd', 'autompl', 'autoplt', 'available_nms_impls',
           'axes_extent', 'boolmask', 'check_aligned', 'colorbar',
           'colorbar_image', 'compact_idstr', 'convert_colorspace',
           'copy_figure_to_clipboard', 'daq_spatial_nms', 'dataframe_light',
           'decode_run_length', 'default_kwargs', 'distinct_colors',
           'distinct_markers', 'draw_border', 'draw_boxes',
           'draw_boxes_on_image', 'draw_boxes_on_image', 'draw_clf_on_image',
           'draw_clf_on_image', 'draw_line_segments', 'draw_text_on_image',
           'draw_text_on_image', 'draw_vector_field', 'dumpsafe',
           'encode_run_length', 'ensure_alpha_channel', 'ensure_float01',
           'ensure_fnum', 'ensure_grayscale', 'ensure_json_serializable',
           'ensure_rng', 'ensure_uint255', 'ensure_ulimit',
           'extract_axes_extents', 'figure', 'fourier_mask', 'freeze_params',
           'gaussian_patch', 'get_file_info', 'get_num_channels',
           'grab_test_image', 'grab_test_image_fpath', 'grad_context',
           'group_consecutive', 'group_consecutive_indices', 'group_indices',
           'group_items', 'image_slices', 'imread', 'imresize', 'imscale',
           'imshow', 'imwrite', 'interpolated_colormap', 'isect_flags',
           'iter_reduce_ufunc', 'legend', 'load_image_paths',
           'load_image_shape', 'make_channels_comparable', 'make_conv_images',
           'make_heatmask', 'make_heatmask', 'make_idstr', 'make_legend_img',
           'make_orimask', 'make_orimask', 'make_short_idstr',
           'make_vector_field', 'make_vector_field', 'maxvalue_assignment',
           'mincost_assignment', 'mindist_assignment', 'multi_plot',
           'next_fnum', 'non_max_supression', 'num_channels',
           'number_of_parameters', 'one_hot_embedding', 'one_hot_embedding',
           'one_hot_lookup', 'one_hot_lookup', 'overlay_alpha_images',
           'overlay_alpha_layers', 'overlay_colorized', 'pandas_plot_matrix',
           'plot_convolutional_features', 'plot_matrix', 'plot_surface3d',
           'profile', 'profile_now', 'profiler', 'qtensure',
           'radial_fourier_mask', 'random_combinations', 'random_product',
           'read_arr', 'read_h5arr', 'read_json', 'read_tensorboard_scalars',
           'render_figure_to_image', 'reverse_colormap', 'rle_translate',
           'roundrobin', 'save_parts', 'savefig2', 'scores_to_cmap',
           'scores_to_color', 'seed_global', 'set_figtitle', 'set_mpl_backend',
           'shortest_unique_prefixes', 'shortest_unique_suffixes',
           'show_if_requested', 'shuffle', 'smooth_prob', 'split_archive',
           'stack_images', 'stack_images_grid', 'standard_normal',
           'standard_normal32', 'standard_normal64', 'stats_dict',
           'strip_ansi', 'subpixel_accum', 'subpixel_align',
           'subpixel_getvalue', 'subpixel_maximum', 'subpixel_minimum',
           'subpixel_set', 'subpixel_setvalue', 'subpixel_slice',
           'subpixel_translate', 'torch_ravel_multi_index', 'trainable_layers',
           'uniform', 'uniform32', 'util_dataframe', 'walk_json',
           'warp_points', 'warp_tensor', 'wide_strides_1d', 'write_arr',
           'write_h5arr', 'write_json', 'zopen']
# </AUTOGEN_INIT>


# Backwards compatibility patch
try:
    # external modules in netharn.util are DEPRECATED
    # Don't depend on these external utilities at import time
    # In the future these will become optional, and these will no longer be
    # exposed via netharn.util
    from . import util_dataframe
    from kwarray import dataframe_light
except Exception:
    pass
