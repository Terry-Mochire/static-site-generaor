from unittest import TestCase
import os
import tempfile

from generator import markdown_to_html, render_template, generate_site


class Test(TestCase):
    def test_markdown_to_html(self):
        # Create a temporary input file with some markdown content
        with tempfile.NamedTemporaryFile(mode='w', delete=False) as input_file:
            input_file.write('# Hello World')
            input_file.flush()

            # Create a temporary output file
            with tempfile.NamedTemporaryFile(mode='w', delete=False) as output_file:
                output_file.flush()
                # Call the function
                markdown_to_html(input_file.name, output_file.name)

                # Check the output file
                with open(output_file.name, 'r') as f:
                    self.assertEqual(f.read(), '<h1>Hello World</h1>')

        # Delete the temporary files
        os.remove(input_file.name)
        os.remove(output_file.name)

    def test_render_template(self):
        # Create a temporary input file with .html extension in the templates Folder with some markdown content
        with tempfile.NamedTemporaryFile(mode='w', delete=False, dir='templates/', suffix='.html') as template_file:
            template_file.write('<h1>{{ title }}</h1>\n<p>{{ content}}</p>')

            template_file_name = template_file.name.split('/')[-1]
            template_file.flush()

            # Create a temporary output file
            with tempfile.NamedTemporaryFile(mode='w', delete=False) as output_file:
                output_file.flush()

                # Define context
                context = {'title': 'Hello World', 'content': 'This is test content'}

                # Call the function
                render_template(template_file_name, output_file.name, context)

                # Check the output file
                expected_html = '<h1>Hello World</h1>\n<p>This is test content</p>'
                with open(output_file.name, 'r') as f:
                    self.assertEqual(f.read(), expected_html)

        # Delete the temporary files
        os.remove(template_file.name)
        os.remove(output_file.name)

    def test_generate_site(self):
        # Create a temporary input directory with some markdown files
        with tempfile.TemporaryDirectory() as input_directory:
            with tempfile.NamedTemporaryFile(mode='w', delete=False, dir=input_directory, suffix='.md') as input_file:
                input_file.write('# Hello World')
                input_file.flush()

        # Create a temporary output directory
        with tempfile.TemporaryDirectory() as output_directory:
            # Call the function
            generate_site(input_directory, output_directory)

            # Check the output directory
            self.assertTrue(os.path.exists(output_directory + '/static/'))
            self.assertTrue(os.path.exists(output_directory + '/hello-world.html'))

            # Check the output file
            with open(output_directory + '/hello-world.html', 'r') as f:
                self.assertEqual(f.read(), '<h1>Hello World</h1>')

        # Delete the temporary files
        os.remove(input_file.name)
        os.remove(output_directory + '/hello-world.html')
        os.remove(output_directory + '/static/')
