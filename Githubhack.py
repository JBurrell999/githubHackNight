with open("../../state_of_the_union.txt") as f:
    state_of_the_union = f.read()
from langchain_text_splitters import RecursiveCharacterTextSplitter
text_splitter = RecursiveCharacterTextSplitter(
    # Set a really small chunk size, just to show.
    chunk_size=100,
    chunk_overlap=20,
    length_function=len,
    is_separator_regex=False,
)
texts = text_splitter.create_documents([state_of_the_union])
print(texts[0])
print(texts[1])
page_content='Madam Speaker, Madam Vice President, our First Lady and Second Gentleman. Members of Congress and'
page_content='of Congress and the Cabinet. Justices of the Supreme Court. My fellow Americans.'
text_splitter.split_text(state_of_the_union)[:2]
text_splitter.split_text(state_of_the_union)[:2]
['Madam Speaker, Madam Vice President, our First Lady and Second Gentleman. Members of Congress and',
 'of Congress and the Cabinet. Justices of the Supreme Court. My fellow Americans.']
text_splitter = RecursiveCharacterTextSplitter(
    separators=[
        "\n\n",
        "\n",
        " ",
        ".",
        ",",
        "\u200b",  # Zero-width space
        "\uff0c",  # Fullwidth comma
        "\u3001",  # Ideographic comma
        "\uff0e",  # Fullwidth full stop
        "\u3002",  # Ideographic full stop
        "",
    ],
    # Existing args
)