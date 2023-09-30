import os
import shutil
import argparse
import markdown2
from collections import defaultdict
from jinja2 import Environment, FileSystemLoader

def save_html(html, filepath):
    with open(filepath, 'w', encoding='utf-8') as file:
        file.write(html)

def copytree(src, dst, symlinks=False, ignore=None):
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            shutil.copytree(s, d, symlinks, ignore)
        else:
            shutil.copy2(s, d)

def generate_site(directory):
    env = Environment(loader=FileSystemLoader(os.path.join(directory, 'templates')))
    template = env.get_template('base.html')
    
    content_directory = os.path.join(directory, 'content')
    
    # Dictionary to hold the links for the homepage
    homepage_links = defaultdict(list)

    # Iterate over subdirectories in the content directory
    for foldername, subdirectories, _ in os.walk(content_directory):
        for subdirectory in subdirectories:
            subdirectory_path = os.path.join(foldername, subdirectory)
    
            # Iterate over markdown files in each subdirectory
            for _, _, filenames in os.walk(subdirectory_path):
                for filename in filenames:
                    if filename.endswith('.md'):
                        filepath = os.path.join(subdirectory_path, filename)

                        # Define the directory where images related to the markdown file are stored
                        image_directory = filepath.replace('.md', '_files')
                        
                        
                        with open(filepath, 'r', encoding='utf-8') as file:
                            content_md = file.read()
                            
                            # get html from md
                            content_html = markdown2.markdown(content_md, extras=["tables", "fenced-code-blocks"])
                            
                            # Define where the generated HTML file will be saved
                            relative_path = os.path.relpath(subdirectory_path, content_directory)
                            output_filepath = os.path.join(directory, 'output', relative_path, filename.replace('.md', '.html'))
                            os.makedirs(os.path.dirname(output_filepath), exist_ok=True)

                            if os.path.exists(image_directory):
                                # Define the output directory for images and copy images
                                output_image_directory = output_filepath.replace('.html', '_files')
                                copytree(image_directory, output_image_directory)

                            # Render individual markdown files using the appropriate template
                            template_name = f"{subdirectory.lower()}_template.html"
                            individual_template = env.get_template(template_name)
                            output_content = individual_template.render(title=filename[:-3], content=content_html)
                            with open(output_filepath, 'w', encoding='utf-8') as file:
                                file.write(output_content)
                                
                            # Add the generated file link to homepage_links
                            relative_link = os.path.relpath(output_filepath, os.path.join(directory, 'output'))
                            homepage_links[subdirectory].append((filename[:-3], relative_link))
                            
    # Ensure the output directory exists
    output_directory = os.path.join(directory, 'output')
    os.makedirs(output_directory, exist_ok=True)
    
    # Generate the homepage with links to each content type
    home_template = env.get_template('home.html')
    homepage_content = home_template.render(title='Home', nav_links=homepage_links)
    with open(os.path.join(output_directory, 'index.html'), 'w', encoding='utf-8') as file:
        file.write(homepage_content)
        
    print("Site has been generated!")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Static Site Generator')
    parser.add_argument('directory', type=str, help='The directory of the course to render')
    
    args = parser.parse_args()
    generate_site(args.directory)
