import os
import re
import shutil
import subprocess
from documentcloud.addon import AddOn

class ExtractBetween(AddOn):
    """Add-On that extracts text between a start and end string"""

    def main(self):
        os.makedirs(os.path.dirname("./out/"), exist_ok=True)
        os.chdir('out')
        self.set_message("Extracting text from documents...")
        start = self.data.get('start')
        end = self.data.get('end')
        for document in self.get_documents():
            text_to_parse = document.full_text
            extracted_text = re.search('%s(.*)%s' % (start, end), text_to_parse).group(1)
            with open(f"{document.title}.txt",  'w') as file:
                file.write(extracted_text)
        os.chdir('..')
        subprocess.call("zip -q -r extract.zip out", shell=True)
        self.upload_file(open("extract.zip"))
        self.set_message("Add-On run complete.")
        shutil.rmtree("./out", ignore_errors=False, onerror=None)

if __name__ == "__main__":
    ExtractBetween().main()
