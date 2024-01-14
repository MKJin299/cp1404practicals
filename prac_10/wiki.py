import wikipedia

while True:
    user_input = input("Enter a page title or search phrase (blank to exit): ")

    if not user_input:
        print("Exiting the program. Goodbye!")
        break

    try:
        page = wikipedia.page(user_input, autosuggest=False)
        print(f"\nTitle: {page.title}")
        print(f"Summary: {page.summary}")
        print(f"URL: {page.url}")

    except wikipedia.exceptions.DisambiguationError as e:
        print(f"\nDisambiguation Page! Choose a specific option:")
        for option in e.options:
            print(option)

    except wikipedia.exceptions.PageError:
        print(f"\nPage not found for '{user_input}'. Please try again.")

    except Exception as e:
        print(f"\nAn error occurred: {e}")
