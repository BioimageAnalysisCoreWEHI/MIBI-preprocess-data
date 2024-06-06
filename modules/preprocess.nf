#!/bin/env nextflow 

// Enable DSL-2 syntax
nextflow.enable.dsl=2

process PREPROCESS {	
	cpus "${params.cpus}"
	publishDir "${params.output_folder}", mode: 'copy'
	conda "${projectDir}/envs/environment.yml"
	memory "${params.memory}"
	beforeScript "${params.before_script}"
	container "oras://ghcr.io/wehi-researchcomputing/mibi:0.2"

	input:
	val batch_name
	path qupath_data
	val additional_meta_data
	val cell_types_to_remove
	val change_to
	val unwanted_markers
	val unwanted_compartments
	val unwanted_statistics
	path report_template

	output:
	path ("${batch_name}_report.html")
	path ("${batch_name}_*_labels.csv") // can either be celltype_labels or binarized_labels
	path ("${batch_name}_images.csv")
	path ("${batch_name}_preprocessed_input_data.csv")
	path ("${batch_name}_decoder.json", optional: true)
	
	shell:
	'''
	quarto render "!{report_template}" \\
		-o !{batch_name}_report.html \\
		-P target:!{params.target} \\
		-P qupath_data:"$(realpath !{qupath_data})" \\
		-P output_folder:"$(realpath .)" \\
		-P batch_name:"!{batch_name}" \\
		-P additional_metadata_to_keep:"!{additional_meta_data}" \\
		-P unwanted_celltypes:"!{cell_types_to_remove}" \\
		-P change_unwanted_celltypes_to:"!{change_to}" \\
		-P unwanted_markers:"\\"!{unwanted_markers}\\"" \\
		-P unwanted_compartments:"\\"!{unwanted_compartments}\\"" \\
		-P unwanted_statistics:"\\"!{unwanted_statistics}\\""
	'''
}