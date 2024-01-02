from googlesearch import search

def google_search(query, num_results=5):
    try:
        results = search(query, num_results=num_results, stop=num_results)
        print(f"Top {num_results} results for '{query}':")
        for i, result in enumerate(results, 1):
            print(f"{i}. {result}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    search_query = "Python programming"
    number_of_results = 5
    google_search(search_query, num_results=number_of_results)
