# Static Site Generator

Python script for converting a directory of markdown files into a static site.

## Usage

1. Create a directory with markdown and html template files. 

Example directory structure:

```
input_directory
└── content
    ├── Assignments
    │   ├── Assignment-1-Agents.md
    │   ├── Assignment-2-Search.md
    ├── Labs
    │   ├── Lab-1-Intro-to-Python.md
    │   ├── Lab-2-Search.md
    ├── Projects
    │   ├── Final-Project.md
└── templates
    ├── base.html
    ├── assignments_template.html
    ├── labs_template.html
    ├── projects_template.html
```

I have included a sample content folder and sample templates folder.

2. Run the script

```
python3 hap.py <input_directory>
```

3. Output will be in `output` directory

```
output
├── Assignments
│   ├── Assignment-1-Agents.html
│   ├── Assignment-2-Search.html
├── Labs
│   ├── Lab-1-Intro-to-Python.html
│   ├── Lab-2-Search.html
├── Projects
│   ├── Final-Project.html
├── index.html
├── assignments.html
├── labs.html
├── projects.html
```

4. Define styles in output folder. I have include a sample styles.css

## TODO

- Specify output directory
- Custom templates and CSS
- Simplify template syntax
