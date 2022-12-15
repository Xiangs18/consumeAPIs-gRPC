from inventory_client import Client


def print_getbook_message(response):
    print(
        "Client received a GetBook info: "
        + "ISBN: {}, title: {}".format(response.ISBN, response.title)
    )


def get_book_title(client, ISBNs, verbose=False):
    res = [0] * len(ISBNs)
    for idx, val in enumerate(ISBNs):
        response = client.getBook(val)
        if verbose:
            print_getbook_message(response)
        res[idx] = response.title
    return res


if __name__ == "__main__":
    client = Client()
    ISBNs = ["1", "2"]
    get_book_title(client, ISBNs, True)
