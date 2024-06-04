#!/usr/bin/env python3
import os, pytest, subprocess

from utils import compare_hashes

_output_file_path = "../output"
_input_file_path = "../annotationsTest.csv"
_fm_input_file_path = "fm-test-data.csv"

def test_preprocessing_outputs_match_base():
    """
    Tests whether files produced by the script are identical (via sha256) to a known "correct" hash.
    """

    hashes = {
        "annotationsTest_base_cell_type_labels.csv" : "b0b859c60bdd9de3fb3d9417ac4e5aeaa4d83cf0ec621b64b1e77aa6665808d7",
        "annotationsTest_base_images.csv" : "51fc38a630ddca6becde6557f7b1086680e164878a42d2f84504deb8ef2f48d9",
        "annotationsTest_base_preprocessed_input_data.csv" : "f8326dc227f17d6bc35b84205704ce8bb315581546391968c4da3afcd88a23f5",
        "annotationsTest_base_decoder.json": "c53755ba55d4dba46c2c173febc9229f9d90c26f6a8350e8e94355373c4257b9"
    }

    subprocess.run(["quarto", "render", "../assets/report-template.qmd",
        "-P", "batch_name:annotationsTest_base",
        "-P", f"output_folder:{_output_file_path}",
        "-P", f"qupath_data:{_input_file_path}",
        "-P", "unwanted_celltypes:Unknown",
        "-P", "change_unwanted_celltypes_to:Other",
        "-P", "unwanted_markers:dsDNA,Beta-Tubulin,CD39,CD49a,Tantalum"
    ])

    assert compare_hashes(_output_file_path, hashes)

def test_preprocessing_outputs_match_allmarkers():
    """
    Tests whether the marker removal functionality of the script produces identical files as the notebook.
    Deviates from the base case by keeping all markers instead of removing a handful.
    """

    hashes = {
        "annotationsTest_allMarkers_cell_type_labels.csv" : "b0b859c60bdd9de3fb3d9417ac4e5aeaa4d83cf0ec621b64b1e77aa6665808d7",
        "annotationsTest_allMarkers_images.csv" : "51fc38a630ddca6becde6557f7b1086680e164878a42d2f84504deb8ef2f48d9",
        "annotationsTest_allMarkers_preprocessed_input_data.csv" : "916b12ba51a75673a326c4078170a18c0162b1c47da9427c493076d843227c40",
        "annotationsTest_allMarkers_decoder.json": "c53755ba55d4dba46c2c173febc9229f9d90c26f6a8350e8e94355373c4257b9",
    }

    subprocess.run(["quarto", "render", "../assets/report-template.qmd",
        "-P", "batch_name:annotationsTest_allMarkers",
        "-P", f"output_folder:{_output_file_path}",
        "-P", f"qupath_data:{_input_file_path}",
        "-P", "unwanted_celltypes:Unknown",
        "-P", "change_unwanted_celltypes_to:Other"
    ])

    assert compare_hashes(_output_file_path, hashes)

def test_preprocessing_outputs_match_nobcells():
    """
    Tests whether the cell type removal functional produces identical files as the notebook.
    Deviates from the base case by changing the "B cells" celltype to Other.
    """

    hashes = {
        "annotationsTest_noBCells_cell_type_labels.csv" : "ad2896ff3aea8d764d31f7ee87de5fa878bbb9ca96f55206f7208d9ff0a8764c",
        "annotationsTest_noBCells_images.csv" : "51fc38a630ddca6becde6557f7b1086680e164878a42d2f84504deb8ef2f48d9",
        "annotationsTest_noBCells_preprocessed_input_data.csv" : "f8326dc227f17d6bc35b84205704ce8bb315581546391968c4da3afcd88a23f5",
        "annotationsTest_noBCells_decoder.json": "4818c1cde68d57d023a5bb1bfe39c1a6a783b9cbbcdc92354f7ffd6b5cfb56d5",
    }

    subprocess.run(["quarto", "render", "../assets/report-template.qmd",
        "-P", "batch_name:annotationsTest_noBCells",
        "-P", f"output_folder:{_output_file_path}",
        "-P", f"qupath_data:{_input_file_path}",
        "-P", "unwanted_celltypes:Unknown,B cells",
        "-P", "change_unwanted_celltypes_to:Other",
        "-P", "unwanted_markers:dsDNA,Beta-Tubulin,CD39,CD49a,Tantalum"
    ])

    assert compare_hashes(_output_file_path, hashes)

def test_preprocessing_outputs_match_nonucleus999percentile():
    """
    Tests whether the statistics removal functional produces identical files as the notebook.
    Deviates from the base case by removing " Nucleus: Percentile: 99.9" from the default list.
    """

    hashes = {
        "annotationsTest_noNucleus99.9Percentile_cell_type_labels.csv" : "b0b859c60bdd9de3fb3d9417ac4e5aeaa4d83cf0ec621b64b1e77aa6665808d7",
        "annotationsTest_noNucleus99.9Percentile_images.csv" : "51fc38a630ddca6becde6557f7b1086680e164878a42d2f84504deb8ef2f48d9",
        "annotationsTest_noNucleus99.9Percentile_preprocessed_input_data.csv" : "65f727363319a6dc4e7688f84e9b7180c8854210dd68b14203b5f3dfe0387530",
        "annotationsTest_noNucleus99.9Percentile_decoder.json": "c53755ba55d4dba46c2c173febc9229f9d90c26f6a8350e8e94355373c4257b9",
    }

    subprocess.run(["quarto", "render", "../assets/report-template.qmd",
        "-P", "batch_name:annotationsTest_noNucleus99.9Percentile",
        "-P", f"output_folder:{_output_file_path}",
        "-P", f"qupath_data:{_input_file_path}",
        "-P", "unwanted_celltypes:Unknown",
        "-P", "change_unwanted_celltypes_to:Other",
        "-P", "unwanted_markers:dsDNA,Beta-Tubulin,CD39,CD49a,Tantalum",
        "-P", "unwanted_statistics:\" Nucleus: Mean, Nucleus: Median, Nucleus: Min, Nucleus: Max, Nucleus: Std.Dev, Nucleus: Percentile: 91.0, Nucleus: Percentile: 92.0, Nucleus: Percentile: 93.0, Nucleus: Percentile: 94.0, Nucleus: Percentile: 96.0,Nucleus: Percentile: 97.0, Nucleus: Percentile: 98.0, Nucleus: Percentile: 99.0, Nucleus: Percentile: 99.5, Nucleus: Percentile: 95.0, Nucleus: Percentile: 90.0, Nucleus: Percentile: 80.0, Nucleus: Percentile: 70.0\""
    ])

    assert compare_hashes(_output_file_path, hashes)


def test_preprocessing_outputs_match_withnucleuslengthmetadata():
    """
    Tests whether the keep additional metadata functional produces identical files as the notebook.
    Deviates from the base case by requesting to keep the "Nucleus: Length µm" column.
    """
    
    hashes = {
        "annotationsTest_withNucleusLengthMetadata_cell_type_labels.csv" : "b0b859c60bdd9de3fb3d9417ac4e5aeaa4d83cf0ec621b64b1e77aa6665808d7",
        "annotationsTest_withNucleusLengthMetadata_images.csv" : "b7c6620f42057208ca69e53713373e5a6cf5af8df3c8ca38e454ece3800a7bbb",
        "annotationsTest_withNucleusLengthMetadata_preprocessed_input_data.csv" : "f8326dc227f17d6bc35b84205704ce8bb315581546391968c4da3afcd88a23f5",
        "annotationsTest_withNucleusLengthMetadata_decoder.json": "c53755ba55d4dba46c2c173febc9229f9d90c26f6a8350e8e94355373c4257b9"
    }

    subprocess.run(["quarto", "render", "../assets/report-template.qmd",
        "-P", "batch_name:annotationsTest_withNucleusLengthMetadata",
        "-P", f"output_folder:{_output_file_path}",
        "-P", f"qupath_data:{_input_file_path}",
        "-P", "unwanted_celltypes:Unknown",
        "-P", "change_unwanted_celltypes_to:Other",
        "-P", "unwanted_markers:dsDNA,Beta-Tubulin,CD39,CD49a,Tantalum",
        "-P", "additional_metadata_to_keep:\"Nucleus: Length µm\""
    ])

    assert compare_hashes(_output_file_path, hashes)

def test_preprocessing_outputs_match_base_spaces():
    """
    Same as the base case test, but supplies cmd args with spaces.
    """

    hashes = {
        "annotationsTest_base_spaces_cell_type_labels.csv" : "b0b859c60bdd9de3fb3d9417ac4e5aeaa4d83cf0ec621b64b1e77aa6665808d7",
        "annotationsTest_base_spaces_images.csv" : "51fc38a630ddca6becde6557f7b1086680e164878a42d2f84504deb8ef2f48d9",
        "annotationsTest_base_spaces_preprocessed_input_data.csv" : "f8326dc227f17d6bc35b84205704ce8bb315581546391968c4da3afcd88a23f5",
        "annotationsTest_base_spaces_decoder.json": "c53755ba55d4dba46c2c173febc9229f9d90c26f6a8350e8e94355373c4257b9"
    }

    subprocess.run(["quarto", "render", "../assets/report-template.qmd",
        "-P", "batch_name:annotationsTest_base_spaces",
        "-P", f"output_folder:{_output_file_path}",
        "-P", f"qupath_data:{_input_file_path}",
        "-P", "unwanted_celltypes:Unknown",
        "-P", "change_unwanted_celltypes_to:Other",
        "-P", "unwanted_markers:dsDNA, Beta-Tubulin, CD39, CD49a, Tantalum"
    ])

    assert compare_hashes(_output_file_path, hashes)

def test_preprocessing_outputs_match_base_fm_withcelltype():
    """
    Tests the fm-with-celltype target with minimal args.
    """

    hashes = {
        "fm_with_celltype_base_binarized_labels.csv": "813af5273ba0390680ca9d36af382e4f386b4064e0aa3162a72b8fddefd03f3d",
        "fm_with_celltype_base_preprocessed_input_data.csv": "1ac48beec55fb07035e84318f4dd1cef144bc217592a7233d8425b1485005561",
        "fm_with_celltype_base_images.csv": "f82d90e476d3ad104d24998470270841b4366aa76a3447e8cf81918723338c98",
        "fm_with_celltype_base_decoder.json": "075ecdf0b3024954218891a3c444d92a7024496a6c42b14a3d72af6fc5824353"
    }

    subprocess.run(["quarto", "render", "../assets/report-template.qmd",
        "--execute-dir", ".",
        "-P", "batch_name:fm_with_celltype_base",
        "-P", f"output_folder:{_output_file_path}",
        "-P", f"qupath_data:{_fm_input_file_path}",
        "-P", "target:fm-with-celltype"
    ])

    assert compare_hashes(_output_file_path, hashes)

def test_preprocessing_outputs_match_base_fm_markersonly():
    """
    Tests the fm-markers-only target with minimal args.
    """

    hashes = {
        "fm_markers_only_base_binarized_labels.csv": "813af5273ba0390680ca9d36af382e4f386b4064e0aa3162a72b8fddefd03f3d",
        "fm_markers_only_base_preprocessed_input_data.csv": "83357cadfb45d9e3e532f4c08c5dcfb2c54ba0aa215e31fd081355add09cca3d",
        "fm_markers_only_base_images.csv": "f82d90e476d3ad104d24998470270841b4366aa76a3447e8cf81918723338c98",
        "fm_markers_only_base_decoder.json": "075ecdf0b3024954218891a3c444d92a7024496a6c42b14a3d72af6fc5824353"
    }

    subprocess.run(["quarto", "render", "../assets/report-template.qmd",
        "--execute-dir", ".",
        "-P", "batch_name:fm_markers_only_base",
        "-P", f"output_folder:{_output_file_path}",
        "-P", f"qupath_data:{_fm_input_file_path}",
        "-P", "target:fm-markers-only"
    ])

    assert compare_hashes(_output_file_path, hashes)