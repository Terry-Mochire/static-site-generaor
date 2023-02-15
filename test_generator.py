from unittest import TestCase
import os
import tempfile

from generator import markdown_to_html


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
