import cv2
import pytesseract


class TextExtractorApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', spacing=10, padding=10)

        self.image_path_input = TextInput(multiline=False, hint_text='Image path...')
        self.extract_button = Button(text='Extract Text', on_press=self.extract_text)
        self.result_label = Label(text='', halign='center')
        self.image_display = Image()

        self.layout.add_widget(self.image_path_input)
        self.layout.add_widget(self.extract_button)
        self.layout.add_widget(self.result_label)
        self.layout.add_widget(self.image_display)

        return self.layout

    def extract_text(self, instance):
        image_path = self.image_path_input.text
        if image_path:
            try:
                # Baca gambar menggunakan OpenCV
                image = cv2.imread(image_path)

                # Ekstrak teks menggunakan Tesseract OCR
                extracted_text = pytesseract.image_to_string(image)

                # Tampilkan teks hasil ekstraksi
                self.result_label.text = f'Extracted Text:\n{extracted_text}'
                self.image_display.source = image_path
            except Exception as e:
                self.result_label.text = f'Error: {str(e)}'
        else:
            self.result_label.text = 'Error: Image path is empty.'

if __name__ == '__main__':
    TextExtractorApp().run()
