import os
from documentcloud.addon import AddOn
from documentcloud.exceptions import APIError
from requests.exceptions import RequestException

class ExtractAndTag(AddOn):
    """Add-On that extracts text between a start and end string"""
    def main(self):
        os.makedirs(os.path.dirname("./out/"), exist_ok=True)
        os.chdir('out')
        self.set_message("Extracting text from documents...")
        start = self.data.get('start')
        end = self.data.get('end')
        for document in self.get_documents():
            text_to_parse = document.full_text
            text_to_parse = text_to_parse.replace("\n", " ")
            start_char = text_to_parse.find(start) + len(start)
            end_char = text_to_parse.find(end)
            extracted_text = text_to_parse[start_char:end_char]
            name_key = self.data.get("key_name")
            try:
                document.data[name_key] = extracted_text
                document.put()
            except (APIError, RequestException) as exc:
                print("Tagging Error on Document", str(exc))
                print(document.title)
        self.set_message("Add-On run complete.")
if __name__ == "__main__":
    ExtractAndTag().main()
