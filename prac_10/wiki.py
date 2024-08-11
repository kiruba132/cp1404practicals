import wikipedia


def main():
    query = input("Enter page title: ").strip()

    while query:
        try:
            # Attempt to fetch the page with the given query
            page = wikipedia.page(query)
            print(f"\n{page.title}\n{page.summary[:500]}...\n{page.url}\n")

        except wikipedia.exceptions.DisambiguationError as e:
            print("We need a more specific title. Try one of the following, or a new search:")
            print(e.options)

        except wikipedia.exceptions.PageError:
            print(f'Page id "{query}" does not match any pages. Try another id!')

        except Exception as e:
            print(f"An unexpected error occurred: {e}")

        query = input("Enter page title: ").strip()

    print("Thank you.")


if __name__ == "__main__":
    main()
