from poppler import load_from_data


class Pdf2TextConverter:

    @staticmethod
    def to_text(pdf_content):
        try:
            pdf_document = load_from_data(pdf_content)
            pages = []
        except Exception as ex:
            raise PdfConversionError("Error occurred while loading pdf document (%s)" % str(ex.__class__.__name__))

        for page_number in range(0, pdf_document.pages):
            page = pdf_document.create_page(page_number)
            pages.append(page.text())

        return PdfResult("\n\n".join(pages).strip(),
                             author=pdf_document.author.strip(),
                             creation_date=pdf_document.creation_date,
                             title=pdf_document.title.strip())


class PdfResult:

    def __init__(self, text, author=None, creation_date=None, title=None):
        self.text = text
        self.author = author
        self.creation_date = creation_date
        self.title = title


class PdfConversionError(Exception):
    pass
