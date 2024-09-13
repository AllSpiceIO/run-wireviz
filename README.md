# Run WireViz

Generate wiring diagrams using [WireViz](https://github.com/wireviz/WireViz/)
in your CI workflows.

## Usage

Add the following step to your workflow:

```yaml
- name: Run WireViz
  uses: AllSpiceIO/run-wireviz@v0.4
  with:
    # The input file(s) to process
    files: "path/to/your/input/file.yml"
```

### Notes

Your input file must be present in the workspace. If it's not already there,
you can use the [`actions/checkout`](https://github.com/actions/checkout)
action to clone your repository.

This action's versions will match the version of WireViz it is running. For
example, the tag 0.4.1 will match WireViz 0.4.1. Tags with only a major or
minor version will match all versions with that major or minor version of this
action.

### Customizing WireViz Output

You can customize the WireViz output using various input parameters:

```yaml
- name: Run WireViz with Custom Options
  uses: AllSpiceIO/run-wireviz@v0.4
  with:
    files: "path/to/your/input/file.yml"
    format: "hps"
    prepend: "path/to/prepend.yml"
    output_dir: "output"
    output_name: "my_wireviz_output"
```

These options correspond roughly to the same as the WireViz CLI. You can see the options exposed by WireViz by running:

```sh
wireviz --help
```

with the same version of WireViz as this action. To run a specific version of
WireViz in an isolated environment, consider
[uvx.](https://docs.astral.sh/uv/guides/tools/)

As of the current version, the following options are available:

- `files`: (Required) Input file(s) to process.
- `format`: Output formats (g: GV, h: HTML, p: PNG, s: SVG, t: TSV). Default: 'hpst'
- `prepend`: YAML file to prepend to the input file.
- `output_dir`: Directory to use for output files.
- `output_name`: File name (without extension) to use for output files.

#### Output Formats

The `format` input accepts a string containing one or more of the following characters to specify which file types to output:

- `g`: GraphViz (GV)
- `h`: HTML
- `p`: PNG
- `s`: SVG
- `t`: TSV (Tab-Separated Values, used for BOM.)

For example, to generate HTML, PNG, and SVG outputs, use `format: 'hps'`.

#### Working with Multiple Input Files

You can process multiple input files by providing a space-separated list:

```yaml
- name: Run WireViz on Multiple Files
  uses: AllSpiceIO/run-wireviz@v0.4
  with:
    files: "file1.yml file2.yml file3.yml"
```
