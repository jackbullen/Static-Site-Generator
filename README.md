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

4. Define styles in output folder

**Sample base.html:**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{{ title }}</title>
    <link rel="stylesheet" href="../styles.css">
</head>
<body>
    {% if nav_links is defined %}
        <nav>
            {% for content_type, links in nav_links.items() %}
                <h1>{{ content_type }}</h1>
                {% for name, link in links %}
                    <a href="{{ link }}">{{ ' '.join(name.split('-')) }}</a><br>
                {% endfor %}
            {% endfor %}
        </nav>
    {% endif %}
    <div>{{ content|safe }}</div>
</body>
</html>
```

**Sample assignments_template.html:**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{{ title }}</title>
    <link rel="stylesheet" href="../styles.css">
</head>
<body>
    {% if nav_links is defined %}
        <nav>
            {% for content_type, links in nav_links.items() %}
                <h1>{{ content_type }}</h1>
                {% for name, link in links %}
                    <a href="{{ link }}">{{ ' '.join(name.split('-')) }}</a><br>
                {% endfor %}
            {% endfor %}
        </nav>
    {% endif %}
    <div>{{ content|safe }}</div>
</body>
</html>
```

**Sample styles:**

```css
body {
    font-family: 'Arial', sans-serif;
    line-height: 1.6;
    margin: 0;
    padding: 0;
    background-color: #f4f4f4;
}

nav {
    display: flex;
    justify-content: space-around;
    background: #333;
    padding: 10px;
}

nav a {
    color: white;
    text-decoration: none;
    text-transform: uppercase;
}

div {
    width: 80%;
    margin: 0 auto;
    background: #fff;
    padding: 10px;
}

h1, h2, h3 {
    line-height: 1.2;
}

```

## TODO

- Specify output directory
- Custom templates and CSS
- Simplify template syntax