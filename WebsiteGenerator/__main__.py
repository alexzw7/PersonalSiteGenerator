"""Build Personal HTML site from directory of HTML templates and plain files."""

import sys
import json
import os
import shutil
import click
import jinja2


@click.command()
@click.option('-v', '--verbose', is_flag=True, help="Print more output.")
@click.argument("INPUT_DIR")
def main(input_dir, verbose):
    """Templated personal website generator."""
    try:
        with open(input_dir + "/config.json") as json_file:
            data = json.load(json_file)
            html_directory = input_dir + "/html/"
            static_directory = input_dir + "/static/"
            if not os.path.exists(html_directory):
                if os.path.exists(static_directory):
                    shutil.copytree(static_directory, html_directory)
                    if verbose:
                        print("Copied " + static_directory
                              + " -> " + html_directory)
                else:
                    os.makedirs(html_directory)
            else:
                print("Error: Output file already exists")
                sys.exit(1)
            for page in data:
                page_url = page["url"]
                page_context = page["context"]
                template_env = jinja2.Environment(
                    loader=jinja2.FileSystemLoader(input_dir + "/templates"),
                    autoescape=jinja2.select_autoescape(['html', 'xml']),
                )
                template = template_env.get_template(page["template"])
                rendered_template = template.render(page_context)
                new_path = os.path.join(input_dir, "html",
                                        page_url.lstrip("/"), "index.html")
                new_direct = os.path.join(input_dir,
                                          "html", page_url.lstrip("/"))
                if not os.path.exists(new_direct):
                    os.makedirs(new_direct)
                with open(new_path, 'w') as f_new:
                    f_new.write(rendered_template)
                if verbose:
                    print("Rendered " + page["template"] + " -> " + new_path)
    except OSError:
        print("Error: Directory or file not found")
        sys.exit(1)
    except json.JSONDecodeError:
        print("Error: Invalid JSON file")
        sys.exit(1)
    except jinja2.TemplateError:
        print("Error: Problem with Jinja2 Templates")
        sys.exit(1)


if __name__ == "__main__":
    main()
