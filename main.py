from documentcloud.addon import AddOn

class ExtractBetween(AddOn):
    """Add-On that extracts text between a start and end string"""

    def main(self):
        self.set_message("Extracting text from documents...")
        start_string = self.data.get('start')
        end_string = self.data.get('end')
        for document in self.get_documents():
            text_to_parse = document.full_text
            extracted_text = text_to_parse.partition(start_string)[2].partition(end_string)[0]
            print(extracted_text)
        self.set_message("Add-On run complete.")

if __name__ == "__main__":
    ExtractBetween().main()
